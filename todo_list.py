todo_list = []

try:
    with open("todo_list.txt", "r") as file:
        todo_list = [line.strip() for line in file.readlines()]
except FileNotFoundError:
    pass  # No saved list yet; start fresh
while True:
  print("\nTo-Do List:")
  for i, task in enumerate(todo_list, 1):
    print(f"{i}, {task}")
  print("\nOptions: add, remove, quit")
  choice = input("What do you want to do?").lower()

  if choice == "add:
    task = input("Enter a new task:")
    todo_list.append(task)
    print(f'"{task}" added!')
  elif choice == "remove":
    num = int(input("Enter the number of the task to remove:"))
    if i <= num <= len(todo_list):
      removed = todo_list.pop(num - 1)
      print(f'"{removed}" removed!')
    else:
      print("Invalid task number.")
  elif choice == "quit":
    print("Goodbye!")
    with open("todo_list.txt", "w") as file:
    for task in todo_list:
        file.write(task + "\n")
print("Your to-do list has been saved!")
    break
  else:
    print("Invalid option. Please try again.")