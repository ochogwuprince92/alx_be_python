# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Generate reminder message
reminder_message = ""

match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task"
        if time_bound == "yes":
            reminder_message += " that requires immediate attention today!"
    case "medium":
        reminder_message = f"'{task}' is a medium priority task."
        if time_bound == "yes":
            reminder_message += " Consider completing it soon."
    case "low":
        reminder_message = f"'{task}' is a low priority task."
        if time_bound == "yes":
            reminder_message += " It can wait but try to finish it when you can."
    case _:
        reminder_message = "Invalid priority level. Please enter high, medium, or low."

# Print the reminder
print(reminder_message)

