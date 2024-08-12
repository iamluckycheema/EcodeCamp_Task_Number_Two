import os
import pytest
from app import app
from utils import load_tasks, save_tasks

@pytest.fixture
def client():
    # Setup: Create a test client using Flask's test client
    app.config['TESTING'] = True
    client = app.test_client()

    # Backup the original tasks file and use a temporary file for testing
    if os.path.exists('tasks_backup.json'):
        os.remove('tasks_backup.json')

    if os.path.exists('tasks.json'):
        os.rename('tasks.json', 'tasks_backup.json')
    save_tasks([])  # Start with an empty task list
    yield client

    # Teardown: Restore the original tasks file after testing
    if os.path.exists('tasks_backup.json'):
        if os.path.exists('tasks.json'):
            os.remove('tasks.json')
        os.rename('tasks_backup.json', 'tasks.json')

def test_index_empty(client):
    """Test the index page with no lists or tasks"""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Your Todos' in response.data
    assert b'Create New List' in response.data


def test_add_list(client):
    """Test adding a new list"""
    response = client.post('/add_list', data={'list_name': 'Work'})
    assert response.status_code == 302  # Redirect after adding a list

    response = client.get('/')
    assert b'Work' in response.data  # Check if the list was added


def test_add_task(client):
    """Test adding a new task to a list"""
    client.post('/add_list', data={'list_name': 'Work'})
    response = client.post('/Work/add', data={'task': 'Finish report'})
    assert response.status_code == 302  # Redirect after adding a task

    response = client.get('/Work')
    assert b'Finish report' in response.data  # Check if the task was added


def test_toggle_task_completion(client):
    """Test toggling task completion status"""
    client.post('/add_list', data={'list_name': 'Work'})
    client.post('/Work/add', data={'task': 'Finish report'})
    response = client.post('/Work/toggle/2')
    assert response.status_code == 302

    response = client.get('/Work')
    assert b'<s>Finish report</s>' in response.data


def test_remove_task(client):
    """Test removing a task from a list"""
    client.post('/add_list', data={'list_name': 'Work'})
    client.post('/Work/add', data={'task': 'Finish report'})
    response = client.get('/Work/remove/2')
    assert response.status_code == 302 

    response = client.get('/Work')
    assert b'Finish report' not in response.data 


def test_remove_list(client):
    """Test removing a list by removing all its tasks"""
    client.post('/add_list', data={'list_name': 'Work'})
    #client.post('/Work/add', data={'task': 'Task 1'})
    client.get('/Work/remove/1')
    response = client.get('/')
    assert b'Work' not in response.data
