# 📚 Library Management System (Python CLI)

A simple Library Management System built using Python.
This project runs in the command line (CLI) and uses dictionaries with file handling to manage book records.

---

## 📁 Project Structure

```bash
LIBRARYMANAGEMENTSYSTEM/
│
├── add_book.py        # Add new book
├── issue_book.py      # Issue a book
├── return_book.py     # Return a book
├── show_book.py       # Display all books
├── main.py            # Main menu (entry point)
└── utils.py           # File handling functions
```

---

## ⚙️ Features

* Add new books
* Issue books
* Return books
* View all books
* Dictionary-based data storage
* File-based persistence (`books.txt`)

---

## 🧠 Technologies Used

* Python (Core)
* Dictionary (for storing book data)
* File Handling (for saving and loading data)

---

## ▶️ How to Run

1. Clone the repository:

   ```
   https://github.com/Alok6656/Library-Management-System.git
   ```

2. Navigate to the project folder:

   ```
   cd LIBRARYMANAGEMENTSYSTEM
   ```

3. Run the program:

   ```
   python main.py
   ```

---

## 📌 Sample Menu

```bash
 LIBRARY MENU 
1. Add Book
2. Issue Book
3. Return Book
4. Show Books
5. Exit
```

---

## 💾 Data Storage Format

Data is stored in `books.txt` in this format:

```
book_id,book_name,author,status
```

Example:

```
101,Python Basics,John,available
102,Data Structures,Smith,issued
```

---

## 🔍 How It Works

* Each book is stored as a dictionary:

  ```
  {
      "101": {
          "name": "Python Basics",
          "author": "John",
          "status": "available"
      }
  }
  ```
* File acts as a simple database
* No lists are used for storing records

---

## ⚠️ Limitations

* No student/user tracking
* No due date system
* No search functionality
* No database integration
* Basic validation only

---

## 🚀 Future Improvements

* Add student management system
* Add due date and fine system
* Add search by book name
* Use database (SQLite/MySQL)
* Improve CLI interface

---

## 👨‍💻 Author

Alok

---

## 📜 License

This project is for educational purposes only.
