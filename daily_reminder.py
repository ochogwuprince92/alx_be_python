def get_user_input():
    # Prompt for a single task
    task = input("Enter your task: ")
    # Prompt for the task’s priority
    priority = input("Priority (high/medium/low): ").lower()
    # Ask if the task is time-bound
    time_bound = input("Is it time-bound? (yes/no): ").lower() == 'yes'
    return task, priority, time_bound

def generate_reminder(task, priority, time_bound):
    match priority:
        case "high":
            if time_bound:
                return f"Reminder: '{task}' is a high priority task that requires immediate attention today!"
            else:
                return f"Reminder: '{task}' is a high priority task. Consider completing it when you have free time."
        case "medium":
            if time_bound:
                return f"Reminder: '{task}' is a medium priority task that requires immediate attention today!"
            else:
                return f"Reminder: '{task}' is a medium priority task. You can complete it later."
        case "low":
            if time_bound:
                return f"Reminder: '{task}' is a low priority task that requires immediate attention today!"
            else:
                return f"Reminder: '{task}' is a low priority task. Consider completing it when you have free time."
        case _:
            return "Priority not recognized. Please enter high, medium, or low."

def main():
    task, priority, time_bound = get_user_input()
    reminder = generate_reminder(task, priority, time_bound)
    # Print the reminder message
    print(reminder)

if __name__ == "__main__":
    main()
