## Book Reading List

Basic python book reading list application. For practicing teamwork and GitHub collaboration. 

Uses SQLite3 database to store data. 

Requires at least Python 3.7.

This program stores a list of books, with a unique ID, an author, and a title.
Each book can be marked as "read" or "unread."

Main Menu:

1: Add Book
Enter the book's title, followed by the book's author. This will add a book to the reading list. The book will be marked as "unread" by default.

2: Search For Book
Search for a book that is already in the reading list by author or title. The program will also look for partial matches.

3: Show Unread Books
List all books that have been marked as "unread."

4: Show Read Books
List all books that have been marked as "read."

5: Show All Books
List all books, regardless of read/unread status.

6: Change Book Read Status
Change the read/unread status of a single book. Look up the book by ID, then type "read" or "unread" when prompted.

7: Delete Book
Delete a book from the reading list by ID.

Q: Quit
Exit the program.