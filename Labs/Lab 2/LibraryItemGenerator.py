
import Catalogue
from DVD import DVD
from Journal import Journal
from book import Book

class LibraryItemGenerator:
    def __init__(self):
        pass

    def add(self, obj, i):
        """
        Add a brand new item to the library with a unique call number.
        """
        call_number = input("Enter Call Number: ")
        title = input("Enter title: ")
        num_copies = int(input("Enter number of copies (positive number): "))

        if i == 1:
            book_data = (call_number, title, num_copies)
            author = input("Enter Author Name: ")
            new_book = Book(book_data[0], book_data[1], book_data[2], author)

        if i == 2: # journal
            name = input("Enter Journal Name: ")
            issue_no = input("Enter Issue No.")
            publisher = input("Enter Publisher: ")
            new_book = Journal(name, issue_no, publisher, call_number, title, num_copies)

        if i == 3: # dvd
            release_date = input("Enter Release Date: ")
            region_code = input("Enter Region Code: ")
            new_book = DVD(release_date, region_code, call_number, title, num_copies)

        found_book = obj._retrieve_book_by_call_number(
            new_book.call_number)
        if found_book:
            print(f"Could not add book with call number "
                  f"{new_book.call_number}. It already exists. ")
        else:
            obj._book_list.append(new_book)
            print("Item added successfully! Details:")
            print(new_book)