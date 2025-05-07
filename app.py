from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)
TASKS_FILE = 'tasks.json'


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, 'w', encoding='utf-8') as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)


@app.route('/')
def index():
    sort = request.args.get('sort')
    tasks = load_tasks()

    if sort == 'deadline':
        tasks.sort(key=lambda x: x['deadline'])
    elif sort == 'priority':
        priority_map = {'augsts': 1, 'vidējs': 2, 'zems': 3}
        tasks.sort(key=lambda x: priority_map.get(x['priority'], 4))

    return render_template('index.html', tasks=tasks)


@app.route('/add', methods=['POST'])
def add_task():
    title = request.form['title']
    deadline = request.form['deadline']
    priority = request.form['priority']

    tasks = load_tasks()
    task = {
        'id': len(tasks) + 1,
        'title': title,
        'deadline': deadline,
        'priority': priority
    }
    tasks.append(task)
    save_tasks(tasks)
    return redirect('/')


@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [t for t in tasks if t['id'] != task_id]
    for i, t in enumerate(tasks, 1):
        t['id'] = i
    save_tasks(tasks)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
