from utils import load_books, save_books

def add_book():
    books = load_books()

    book_id = input("Enter Book ID: ")
    if book_id in books:
        print("Book already exists!")
        return

    name = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    books[book_id] = {
        "name": name,
        "author": author,
        "status": "available"
    }

    save_books(books)
    print("Book added successfully!")