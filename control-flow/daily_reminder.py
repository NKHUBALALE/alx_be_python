task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ")
time_bound = input("Is the task time-bound (yes or no): ")

match priority:
    case "high":
        reminder = f"Reminder: {task} is of high priority"
    case "medium":
        reminder = f"Reminder: {task} is of medium priority"
    case "low":
        reminder = f"Reminder: {task} is of low priority"
    case _:
        reminder = f"Reminder: {task} has an unknown priority level"

if time_bound == "yes":
    reminder += " that requires immediate attention today!"

print(reminder)
