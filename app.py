from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# Initialize an empty list to store tasks
tasks = []


@app.route('/')
def index():
    # Render the index.html template with the current tasks
    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    # Get the task from the form and append it to the tasks list
    task = request.form.get('task')
    if task:  # Ensure the task is not empty
        tasks.append(task)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
