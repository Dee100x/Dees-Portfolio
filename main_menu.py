import os

def clear():
    os.system("clear")

def menu():
    clear()
    print("=" * 30)
    print("  Dee's Portfolio")
    print("=" * 30)
    print("1) Network Scanner")
    print("2) Password Policy Analyser")
    print("3) Exit")
    print()

def main():
    while True:
        menu()
        choice = input("Select an option: ")

        if choice == "1":
            os.system("cd network_scanner_cli && sudo python3 cli_scanner.py")

        elif choice == "2":
            os.system("cd password_policy_analyser_cli && sudo python3 password_analyser.py")

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            input("Invalid option. Press Enter to try again.")

if __name__ == "__main__":
    main()
