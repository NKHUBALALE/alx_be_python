def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item(shopping_list):
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"'{item}' has been added to the shopping list.")
    else:
        print("Invalid input. Please enter a valid item name.")

def remove_item(shopping_list):
    item = input("Enter the item to remove: ").strip()
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from the shopping list.")
    else:
        print(f"'{item}' not found in the shopping list.")

def view_list(shopping_list):
    if shopping_list:
        print("\nShopping List:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("The shopping list is empty.")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()

        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                # Prompt for and add an item
                add_item(shopping_list)
            elif choice == 2:
                # Prompt for and remove an item
                remove_item(shopping_list)
            elif choice == 3:
                # Display the shopping list
                view_list(shopping_list)
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")
        else:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
