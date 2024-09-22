# Get the task details from the user
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match case statement to handle the priority level
match priority:
    case 'high':
        priority_message = f"'{task}' is a high priority task"
    case 'medium':
        priority_message = f"'{task}' is a medium priority task"
    case 'low':
        priority_message = f"'{task}' is a low priority task"
    case _:
        print("Invalid priority. Please enter 'high', 'medium', or 'low'.")
        exit()

# If statement to modify the reminder based on time sensitivity
if time_bound == 'yes':
    time_message = "and requires immediate attention today!"
elif time_bound == 'no':
    time_message = "but is not time-bound."
else:
    print("Invalid time-bound response. Please enter 'yes' or 'no'.")
    exit()

# Print the final customized reminder
print(f"Reminder: {priority_message} {time_message}")
