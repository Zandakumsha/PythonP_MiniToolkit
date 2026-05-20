import main as todo
import motivation
import tracker


def app_menu():
    while True:
        print("=== Project Launcher Menu ===")
        print("1. Todo List")
        print("2. Motivation Generator")
        print("3. Budget Tracker")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            print("\nOpening Todo List...\n")
            todo.menu()
            print("Returned to launcher menu.\n")
        elif choice == '2':
            print("\nOpening Motivation Generator...\n")
            motivation.main()
            print("Returned to launcher menu.\n")
        elif choice == '3':
            print("\nOpening Budget Tracker...\n")
            tracker.menu()
            print("Returned to launcher menu.\n")
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.\n")


if __name__ == "__main__":
    app_menu()
