from utils import load_books, save_books

def issue_book():
    books = load_books()

    book_id = input("Enter Book ID to issue: ")

    if book_id in books:
        if books[book_id]["status"] == "available":
            books[book_id]["status"] = "issued"
            save_books(books)
            print("Book issued successfully!")
        else:
            print("Book already issued!")
    else:
        print("Book not found!")