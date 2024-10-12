from flask import Blueprint, render_template, request, jsonify, redirect, url_for
from services.task_service import TaskService

task_blueprint = Blueprint('tasks', __name__)

@task_blueprint.route('/tasks', methods=['POST'])
def create_task():

    data = request.form
    name = data.get('name')
    description = data.get('description')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    TaskService.create_task(name, description)
    return redirect(url_for('tasks.index'))

@task_blueprint.route('/')
def index():
    tasks =  TaskService.list_all_tasks()
    return render_template('index.html', tasks=tasks)
    
@task_blueprint.route('/update', methods=['POST'])
def update_task():

    data = request.form
    id = data.get('id')    
    name = data.get('newname')
    description = data.get('newdescription')

    if not name:
        return jsonify({'error': 'Name is required'}), 400

    TaskService.update_task(name, description, id)
    return redirect(url_for('tasks.index'))  