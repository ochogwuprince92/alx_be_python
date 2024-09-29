shopping_list = []

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item():
    item = input("Enter the item you want to add: ")
    shopping_list.append(item)
    print(f"{item} has been added to your shopping list.")

def remove_item():
    item = input("Enter the item you want to remove: ")
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from your shopping list.")
    else:
        print(f"{item} was not found in your shopping list.")

def view_list():
    if shopping_list:
        print("Here is your shopping list:")
        for i, item in enumerate(shopping_list, 1):
            print(f"{i}. {item}")
    else:
        print("Your shopping list is empty.")

while True:
    display_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '3':
        view_list()
    elif choice == '4':
        print("Exiting Shopping List Manager. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a number between 1 and 4.")
if __name__ == "__main__":
    main()