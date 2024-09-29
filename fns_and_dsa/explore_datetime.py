from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the current date and time
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    # Prompt the user for the number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    # Calculate the future date
    future_date = datetime.now() + timedelta(days=days_to_add)
    # Format the future date
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    print(f"Future date: {formatted_future_date}")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
