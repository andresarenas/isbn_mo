from repositories.task_repository import TaskRepository

class TaskService:

    @staticmethod
    def create_task(name, description):
        return TaskRepository.create_task(name, description)
        
    @staticmethod
    def list_all_tasks():
        return TaskRepository.list_all_tasks()        
        
    @staticmethod
    def update_task(name, description, id):
        return TaskRepository.update_task(name, description, id)        