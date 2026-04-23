from utils import load_books, save_books

def return_book():
    books = load_books()

    book_id = input("Enter Book ID to return: ")

    if book_id in books:
        if books[book_id]["status"] == "issued":
            books[book_id]["status"] = "available"
            save_books(books)
            print("Book returned successfully!")
        else:
            print("Book was not issued!")
    else:
        print("Book not found!")