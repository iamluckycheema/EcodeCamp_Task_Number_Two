# To-Do List Application

A simple command-line and gui(flask) todo list application written in pyhton that allows users to manage their tasks. The application supports adding, removing, and displaying tasks, and it stores tasks is text file for presistance.

## Features

- Add new tasks
- Remove existing tasks
- View the list of tasks
- GUI and Command line interface
- Presistent storage using text file
- Unit tests using `pytest`

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

with xtra features.

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
