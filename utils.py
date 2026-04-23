def load_books():
    books = {}
    try:
        with open("books.txt", "r") as file:
            for line in file:
                book_id, name, author, status = line.strip().split(",")
                books[book_id] = {
                    "name": name,
                    "author": author,
                    "status": status
                }
    except FileNotFoundError:
        pass
    return books


def save_books(books):
    with open("books.txt", "w") as file:
        for book_id in books:
            b = books[book_id]
            line = f"{book_id},{b['name']},{b['author']},{b['status']}\n"
            file.write(line)