# shopping_list_manager.py

def display_shopping_list(shopping_list):
    """Display the shopping list."""
    print("Your shopping list:")
    for item in shopping_list:
        print(f"- {item}")

def add_item(shopping_list):
    """Add an item to the shopping list."""
    item = input("Enter the item to add: ")  # Required input prompt
    shopping_list.append(item)
    print(f"'{item}' has been added to your shopping list.")

def main():
    shopping_list = []
    
    while True:
        print("\n1. Add item")
        print("2. View shopping list")
        print("3. Exit")
        
        choice = input("Choose an option (1, 2, or 3): ")

        if choice == '1':
            add_item(shopping_list)
        elif choice == '2':
            display_shopping_list(shopping_list)
        elif choice == '3':
            print("Exiting the shopping list manager.")
            break
        else:
            print("Invalid choice. Please select again.")

if __name__ == "__main__":
    main()
