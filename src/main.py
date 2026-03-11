import sys


class DataManager:
    def __init__(self):
        self.data = []

    def add_item(self):
        value = input("Enter a value: ").strip()

        # Edge Case 1: Empty input
        if value == "":
            print("Error: Input cannot be empty.")
            return

        # Edge Case 2: Duplicate input
        if value in self.data:
            print("Error: Duplicate value not allowed.")
            return

        self.data.append(value)
        print("Value added successfully.")

    def remove_item(self):
        value = input("Enter value to remove: ").strip()

        if value not in self.data:
            print("Error: Value not found.")
            return

        self.data.remove(value)
        print("Value removed successfully.")

    def view_items(self):
        if not self.data:
            print("No data available.")
            return

        print("\nStored Values:")
        for i, item in enumerate(self.data, start=1):
            print(f"{i}. {item}")

    def clear_items(self):
        confirm = input("Are you sure you want to clear all data? (y/n): ").lower()

        if confirm == "y":
            self.data.clear()
            print("All data cleared.")
        else:
            print("Operation cancelled.")


class Application:
    def __init__(self):
        self.manager = DataManager()

    def display_menu(self):
        print("\n==== Mini Project Menu ====")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. View Items")
        print("4. Clear All Items")
        print("5. Exit")

    def run(self):
        while True:
            self.display_menu()

            choice = input("Enter your choice: ").strip()

            if choice == "1":
                self.manager.add_item()

            elif choice == "2":
                self.manager.remove_item()

            elif choice == "3":
                self.manager.view_items()

            elif choice == "4":
                self.manager.clear_items()

            elif choice == "5":
                print("Exiting application.")
                sys.exit()

            else:
                print("Invalid choice. Please select a valid option.")


def main():
    app = Application()
    app.run()


if __name__ == "__main__":
    main()