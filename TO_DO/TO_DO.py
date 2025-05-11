import json
import os
from typing import List, Dict

class TodoList:
    def __init__(self):
        self.tasks: List[Dict] = []
        self.data_file = "todo_data.json"
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from JSON file if it exists"""
        if os.path.exists(self.data_file):
            with open(self.data_file, 'r') as f:
                self.tasks = json.load(f)

    def save_tasks(self):
        """Save tasks to JSON file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def add_task(self, description: str):
        """Add a new task to the list"""
        self.tasks.append({
            "description": description,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })
        self.save_tasks()
        print(f"\n✅ Task added: '{description}'")

    def display_tasks(self):
        """Show all tasks with pretty formatting"""
        if not self.tasks:
            print("\nYour to-do list is empty!")
            return

        print("\nYour To-Do List:")
        for i, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else "✗"
            desc = task["description"]
            print(f"{i}. [{status}] {desc}")

    def mark_complete(self, task_num: int):
        """Mark a task as completed"""
        if 1 <= task_num <= len(self.tasks):
            self.tasks[task_num-1]["completed"] = True
            self.save_tasks()
            print(f"\n Task {task_num} marked as complete!")
        else:
            print("\n Invalid task number!")

    def delete_task(self, task_num: int):
        """Remove a task from the list"""
        if 1 <= task_num <= len(self.tasks):
            removed = self.tasks.pop(task_num-1)
            self.save_tasks()
            print(f"\nRemoved task: '{removed['description']}'")
        else:
            print("\nInvalid task number!")

    def clear_all(self):
        """Remove all tasks"""
        if self.tasks:
            self.tasks.clear()
            self.save_tasks()
            print("\n🧹 All tasks cleared!")
        else:
            print("\nList is already empty!")

def get_int_input(prompt: str, min_val=None, max_val=None) -> int:
    """Safely get integer input with validation"""
    while True:
        try:
            num = int(input(prompt))
            if (min_val is not None and num < min_val) or (max_val is not None and num > max_val):
                print(f"Please enter a number between {min_val} and {max_val}")
                continue
            return num
        except ValueError:
            print("Please enter a valid number!")

def main():
    todo = TodoList()
    
    while True:
        print("\n" + "="*30)
        print("To-Do List Manager")
        print("="*30)
        print("1. Add New Task")
        print("2. View All Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Clear All Tasks")
        print("6. Exit")
        print("="*30)

        choice = get_int_input("Enter your choice (1-6): ", 1, 6)

        if choice == 1:
            task = input("\nEnter task description: ").strip()
            if task:
                todo.add_task(task)
            else:
                print("\n❌ Task description cannot be empty!")

        elif choice == 2:
            todo.display_tasks()

        elif choice == 3:
            todo.display_tasks()
            if todo.tasks:
                task_num = get_int_input("\nEnter task number to mark complete: ", 1, len(todo.tasks))
                todo.mark_complete(task_num)

        elif choice == 4:
            todo.display_tasks()
            if todo.tasks:
                task_num = get_int_input("\nEnter task number to delete: ", 1, len(todo.tasks))
                todo.delete_task(task_num)

        elif choice == 5:
            confirm = input("\nAre you sure you want to clear ALL tasks? (y/n): ").lower()
            if confirm == 'y':
                todo.clear_all()

        elif choice == 6:
            print("\n👋 Goodbye! Your tasks are saved for next time.")
            break

if __name__ == "__main__":
    from datetime import datetime
    main()