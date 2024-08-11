import os
import pytest
from io import StringIO
from contextlib import redirect_stdout

# Import functions from todo.py
from todo import load_tasks, save_tasks, add_task, remove_task, display_tasks, TASKS_FILE, main

# A helper function to clean up the tasks file before and after tests
def cleanup():
    if os.path.exists(TASKS_FILE):
        os.remove(TASKS_FILE)

# Fixture to run the cleanup before and after each test
@pytest.fixture(autouse=True)
def run_around_tests():
    cleanup()
    yield
    cleanup()

def test_load_tasks_empty_file():
    tasks = load_tasks()
    assert tasks == []

def test_save_and_load_tasks():
    tasks = ["Task 1", "Task 2"]
    save_tasks(tasks)
    loaded_tasks = load_tasks()
    assert loaded_tasks == tasks

def test_add_task():
    add_task("New Task")
    tasks = load_tasks()
    assert len(tasks) == 1
    assert tasks[0] == "New Task"

def test_remove_task():
    tasks = ["Task 1", "Task 2", "Task 3"]
    save_tasks(tasks)
    remove_task(2)
    updated_tasks = load_tasks()
    assert len(updated_tasks) == 2
    assert updated_tasks == ["Task 1", "Task 3"]

def test_remove_task_invalid(capsys):
    tasks = ["Task 1", "Task 2"]
    save_tasks(tasks)
    remove_task(5)  # Invalid task number (out of range)
    captured = capsys.readouterr()
    assert "ERROR: Invalid task number." in captured.out

    # Ensure no tasks were removed
    updated_tasks = load_tasks()
    assert len(updated_tasks) == 2

def test_add_empty_task(capsys):
    add_task("")
    captured = capsys.readouterr()
    assert "ERROR: Task cannot be empty." in captured.out
    
    tasks = load_tasks()
    assert len(tasks) == 0

def test_display_tasks(capsys):
    tasks = ["Task 1", "Task 2"]
    save_tasks(tasks)
    display_tasks()
    captured = capsys.readouterr()
    assert "1. Task 1" in captured.out
    assert "2. Task 2" in captured.out

def test_display_tasks_empty(capsys):
    display_tasks()
    captured = capsys.readouterr()
    assert "Your to-do list is empty." in captured.out

def test_invalid_choice(capsys, monkeypatch):
    # Simulate user input for invalid choice followed by exit command
    inputs = iter(['5', '4'])  # '5' is invalid, '4' is to exit
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    main()  # Run the main function, which will process the inputs
    captured = capsys.readouterr()
    # Check the output for the invalid choice message
    assert "ERROR: Invalid option. Please try again." in captured.out
    # Check the output for the exit message
    assert "SUCCESS: Exiting the To-Do List Application." in captured.out

