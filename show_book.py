from utils import load_books

def show_books():
    books = load_books()

    if not books:
        print("No books available.")
        return

    print("\n Book List ")
    for book_id in books:
        b = books[book_id]
        print("ID:", book_id)
        print("Name:", b["name"])
        print("Author:", b["author"])
        print("Status:", b["status"])