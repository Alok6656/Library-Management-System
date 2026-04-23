from add_book import add_book
from issue_book import issue_book
from return_book import return_book
from show_book import show_books

def main():
    while True:
        print("\n LIBRARY MENU ")
        print("1. Add Book")
        print("2. Issue Book")
        print("3. Return Book")
        print("4. Show Books")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            issue_book()
        elif choice == "3":
            return_book()
        elif choice == "4":
            show_books()
        elif choice == "5":
            print("Goodbye")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()