task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

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

print(f"Reminder: {reminder}")
