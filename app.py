# Import necessary modules from Flask and a custom utils module
from flask import Flask, render_template, request, redirect, url_for
from utils import load_tasks, get_lists, add_task, remove_task, toggle_task_completion

app = Flask(__name__)

#Index route
@app.route('/')
def index():
    tasks = load_tasks()
    lists = get_lists()
    
    return render_template('index.html', tasks=tasks, lists=lists)

@app.route('/<list_name>')
def show_list(list_name):
    tasks = load_tasks()
    lists = get_lists()

    return render_template('index.html', tasks=tasks, lists=lists, current_list=list_name)

# Route for adding a new task to a list
@app.route('/<list_name>/add', methods=['POST'])
def add(list_name):
    task = request.form['task']
    if task:
        add_task(task, list_name)

    return redirect(f'/{list_name}')

# Route for removing a task from a list
@app.route('/<list_name>/remove/<int:id>')
def remove(list_name, id):
    remove_task(id, list_name)

    return redirect(f'/{list_name}')

# Define a route for toggling a task's completion status
@app.route('/<list_name>/toggle/<int:id>', methods=['POST'])
def toggle(list_name, id):
    toggle_task_completion(id, list_name)
    return redirect(f'/{list_name}')

# Define a route for adding a new list
@app.route('/add_list', methods=['POST'])
def add_list():
    list_name = request.form['list_name']
    tasks = load_tasks()
    if not any(task['list'] == list_name for task in tasks):
        # Create a new list by adding a dummy task to it
        add_task('Dummy task', list_name)
        # Remove the dummy task
        remove_task(len(tasks), list_name)

    return redirect(f'/{list_name}')

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)