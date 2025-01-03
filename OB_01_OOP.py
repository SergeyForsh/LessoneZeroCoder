class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False
    def mark_as_completed(self):
        self.completed = True
    def __str__(self):
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.description} (Deadline: {self.deadline})"
class TaskManager:
    def __init__(self):
        self.tasks = []
    def add_task(self, description, deadline):
        new_task = Task(description, deadline)
        self.tasks.append(new_task)
    def mark_task_as_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_completed()
        else:
            print("Invalid task index.")
    def get_current_tasks(self):
        return [task for task in self.tasks if not task.completed]
    def display_tasks(self):
        for index, task in enumerate(self.tasks):
            print(f"{index}. {task}")
# Пример использования:
if __name__ == "__main__":
    task_manager = TaskManager()
    # Добавление задач
    task_manager.add_task("Купить продукты", "2024-12-10")
    task_manager.add_task("Закончить проект", "2024-12-20")
    task_manager.add_task("Сделать домашнее задание", "2024-12-18")
    # Вывод текущих задач
    print("Текущие задачи:")
    task_manager.display_tasks()
    # Отметка задачи как выполненной
    task_manager.mark_task_as_completed(1)
    # Вывод текущих задач после отметки
    print("\nПосле выполнения задачи:")
    task_manager.display_tasks()