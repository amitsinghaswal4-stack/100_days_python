class ToDoList:
  def __init__(self):
      self.tasks = []

  def add_task(self, task):
      self.tasks.append({"task": task, "done": False})
      print(f"Added: {task}")

  def remove_task(self, index):
      if 0 <= index < len(self.tasks):
          removed = self.tasks.pop(index)
          print(f"Removed: {removed['task']}")
      else:
          print("Invalid task number.")

  def complete_task(self, index):
      if 0 <= index < len(self.tasks):
          self.tasks[index]["done"] = True
          print(f"Marked as done: {self.tasks[index]['task']}")
      else:
          print("Invalid task number.")

  def show_tasks(self):
      if not self.tasks:
          print("No tasks yet!")
          return
      print("\n--- To-Do List ---")
      for i, t in enumerate(self.tasks):
          status = "✓" if t["done"] else " "
          print(f"{i + 1}. [{status}] {t['task']}")
      print()


def main():
  todo = ToDoList()

  while True:
      print("1. Add task")
      print("2. Remove task")
      print("3. Mark task as done")
      print("4. Show tasks")
      print("5. Exit")

      choice = input("Choose an option: ")

      if choice == "1":
          task = input("Enter task: ")
          todo.add_task(task)
      elif choice == "2":
          todo.show_tasks()
          index = int(input("Enter task number to remove: ")) - 1
          todo.remove_task(index)
      elif choice == "3":
          todo.show_tasks()
          index = int(input("Enter task number to mark done: ")) - 1
          todo.complete_task(index)
      elif choice == "4":
          todo.show_tasks()
      elif choice == "5":
          print("Goodbye!")
          break
      else:
          print("Invalid choice, try again.")


if __name__ == "__main__":
  main()