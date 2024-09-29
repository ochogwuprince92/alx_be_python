# shopping_list_manager.py

shopping_list = []  # Array to store shopping list items

# Define display_menu function
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. View Items")
    print("3. Remove Item")
    print("4. Exit")

# Function to add an item to the shopping list
def add_item():
    item = input("Enter the item to add: ")
    shopping_list.append(item)
    print(f"{item} has been added to the list.")

# Function to view all items in the shopping list
def view_items():
    if shopping_list:
        print("Shopping List:")
        for idx, item in enumerate(shopping_list, start=1):
            print(f"{idx}. {item}")
    else:
        print("Your shopping list is empty.")

# Function to remove an item from the shopping list
def remove_item():
    view_items()
    try:
        item_index = int(input("Enter the number of the item to remove: ")) - 1
        if 0 <= item_index < len(shopping_list):
            removed_item = shopping_list.pop(item_index)
            print(f"{removed_item} has been removed from the list.")
        else:
            print("Invalid item number.")
    except ValueError:
        print("Please enter a valid number.")

# Main loop to run the shopping list manager
def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice (1-4): "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == 1:
            add_item()
        elif choice == 2:
            view_items()
        elif choice == 3:
            remove_item()
        elif choice == 4:
            print("Exiting Shopping List Manager.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Run the program
if __name__ == "__main__":
    main()
