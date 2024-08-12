# To-Do List Application

A simple command-line and gui(flask) todo list application written in pyhton that allows users to manage their tasks. The application supports adding, removing, and displaying tasks, and it stores tasks is text file for presistance.
GUI version also allows one to create multiple task lists and mark completed tasks. The UI is designed to be user friendly, with tab-based navigation system that makes it easy to switch between different lists.

## Features

- Add new tasks
- Remove existing tasks
- View the list of tasks
- Presistent storage using text file
- Unit tests using `pytest`
- GUI and Command line interface

## GUI Only Fetures

- Create multiple task lists
- Mark completed tasks
- Tab-based navigation system
- Loacl JSON file for presistant storage

## Getting Started

### Prerequisits

- Python 3.x installed
- `pip` (pyhton package manager)

### Installation

1. Clone the repository:

```bash
git clone https://github.com/iamluckycheema/EcodeCamp_Task_Number_Two.git
```

2. Create the virtual environment (recommended):

```bash
python -m venv venv
source venv/bin/activate #on windows use `venv\Scripts\activate`
```

3. Install the required packages:

```bash
pip install -r requirements.txt
```

### Running the application

#### Method 1: CLI Based

venv and other packages not necessary only pyhton is required.

4. Run:

```bash
python todo.py
```

##### Usage

1. Add Task: Choose option 1 and enter the task description.
2. Remove Task: Choose option 2, view the tasks, and enter the task number to remove.
3. View Tasks: Choose option 3 to display all tasks.
4. Exit: Choose option 4 to exit the application.

#### Method 2: Flask GUI

with extra features. 4. Run:

```bash
python app.py
```

5. Open your browser and go to
   `http://127.0.0.1:5000/` to use app.

##### GUI Usage

##### Navigating the Application

- **Tabs for Lists:** At the top of the page, you'll see tabs for each task list. Click on a tab to view and manage the tasks in that list. The first list is automatically selected when you load the page.
- **Creating a New List:** To create a new list, click on the `+ New List` tab. Enter the name of your new list in the form that appears and click Create List. A new tab will be created for your list.

##### Managing Tasks

- **Adding a Task:** Within any list, you can add a task by typing it into the input field and clicking the `Add Task` button.

- **Toggling Task Completion:** Each task has a checkbox that you can click to mark it as complete or incomplete. Completed tasks will appear with a strikethrough.

- **Removing a Task:** To remove a task, click the `delete icon` link next to the task. The task will be deleted from the list.

### Customization

#### Styling

The application uses a basic CSS file (`style.css`) for styling. You can customize the look and feel of the application by editing this file.

#### Modifying the Backend

The backend logic is written in Python using Flask. If you want to modify how tasks are stored, processed, or displayed, you can edit the following files:

- **app.py:** Contains the Flask routes and main application logic.
- **utils.py:** Contains utility functions for loading, saving, and manipulating tasks.

### Testing the Application

Unit tests are provided to verify the functionality of the application. To run the tests:

- Install pytest:

```bash
pip install pytest
```

- Run the tests:

```bash
pytest
```

### Contact

For any questions or concerns, please feel free to reach out to me at <iamluckycheema@gmail.com>.
