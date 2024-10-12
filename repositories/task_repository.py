from models.task import Task, db

class TaskRepository:

    @staticmethod
    def create_task(name, description):
        task = Task(name=name, description=description)
        db.session.add(task)
        db.session.commit()
        return task
    
    def list_all_tasks():
        tasks = Task.query.all()
        return tasks

        
    @staticmethod
    def update_task(name, description, oldid):
        task = Task.query.filter_by(id=oldid).first()
        task.name = name
        task.description = description
        db.session.commit()    
    
        return task             