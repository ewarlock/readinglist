from bookstore import Book


def display_menu_get_choice(menu):
    """ Displays all of the menu options, checks that the user enters a valid choice and returns the choice.
     :param menu: the menu to display
     :returns: the user's choice """
    while True:
        print(menu)
        choice = input('Enter choice? ').upper()
        if menu.is_valid(choice):
            return choice
        else:
            print('Not a valid choice, try again.')


def message(msg):
    """ Prints a message for the user
     :param msg: the message to print"""
    print(msg)


def show_books(books):
    """ Display all books in a list of Books, or a 'No books' message
     :param books: the book list """

    if books:
        for book in books:
            print(f'\n{book}\n')
    else:
        print('\nNo books to display\n')


def get_book_info():
    """ Create a new Book from title and author provided by user
     :returns: a Book created from the title and author. """
    title = input('Enter book title: ')
    author = input('Enter book author: ')
    return Book(title, author)


def get_book_id():
    """ Ask for ID, validate to ensure is positive integer
    :returns: the ID value """
    while True:
        try:
            id = int(input('Enter book ID: '))
            if id > 0:
                return id
            else:
                print('Please enter a positive number.')

        except ValueError:
            print('Please enter a number.')


def get_read_value():
    """ Ask user to enter 'read' or 'not read'
     :returns: True if user enters 'read' or False if user enters 'not read' """
    while True:
        response = input('Enter \'read\' if book is read or \'not read\' if book is not read: ')
        if response.lower() in ['read', 'not read']:
            return response.lower() == 'read'
        else:
            print('Type \'read\' or \'not read\'')


def confirm_read_status(book):
    """ Displays message that tells users if they read the book or not.
     :param books: the book list """
    if book.read:
        print(f'\nYou have read {book.title} by: {book.author}\n')
    else:
        print(f'\nYou have not read {book.title} by: {book.author}\n')


def ask_question(question):
    """ Ask user question
    :param: the question to ask
    :returns: user's response """
    return input(question)

def confirm_deletion(book):
    """ Ask user to confirm deletion of book in database
    :param: the book to be deleted
    :returns: True if user enters y or Y to delete or False if user enters n or N to not delete."""
    while True:
        response = input(f'Are you sure you want to delete {book.title} by {book.author}? (Y/N)')
        if response.upper() == 'Y':
            print('Book deleted.')
            return True
        elif response.upper() == 'N':
            print('Book was not deleted.')
            return False
        else:
            print('Please enter Y for yes or N for no.')
