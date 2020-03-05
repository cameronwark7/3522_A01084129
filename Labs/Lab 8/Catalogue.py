import difflib
from book import Book
import LibraryItemGenerator

class Catalogue:
    def __init__(self, book_list, l):
        """
                Intialize the library with a list of books.
                :param book_list: a sequence of book objects.
                """
        self._book_list = book_list
        self._lig = l

    def add_item(self):
        user_input = None
        while user_input != 7:
            print("\nWhich item would you like to add?")
            print("-----------------------")
            print("1. Book")
            print("2. Journal")
            print("3. DVD")
            print("4. [Back]")
            string_input = input("Please enter your choice (1-4)")

            # handle user pressing only enter in menu
            if (string_input == ''):
                continue

            user_input = int(string_input)

            if user_input == 1:
                self._lig.add(self, 1)
                user_input = input("Press Enter to continue")
            elif user_input == 2:
                self._lig.add(self, 2)
                user_input = input("Press Enter to continue")
            elif user_input == 3:
                self._lig.add(self, 3)
                user_input = input("Press Enter to continue")
            elif user_input == 4:
                return
            else:
                print("Could not process the input. Please enter a"
                      " number from 1 - 4.")

        print("Thank you for visiting the Library.")
        #self._lig.add_book()

    # everything that searches, adds or removes books.
    def remove_book(self, call_number):
        """
        Remove an existing book from the library
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        found_book = self._retrieve_book_by_call_number(call_number)
        if found_book:
            self._book_list.remove(found_book)
            print(f"Successfully removed {found_book.get_title()} with "
                  f"call number: {call_number}")
        else:
            print(f"book with call number: {call_number} not found.")

    def return_book(self, call_number):
        """
        Return an book with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        status = self.increment_book_count(call_number)
        if status:
            print("book returned successfully!")
        else:
            print(f"Could not find book with call number {call_number}"
                  f". Return failed.")

    def check_out(self, call_number):
        """
        Check out an book with the given call number from the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        """
        library_book = self._retrieve_book_by_call_number(call_number)
        if library_book.check_availability():
            status = self.reduce_book_count(call_number)
            if status:
                print("Checkout complete!")
            else:
                print(f"Could not find book with call number {call_number}"
                      f". Checkout failed.")
        else:
            print(f"No copies left for call number {call_number}"
                  f". Checkout failed.")

    def _retrieve_book_by_call_number(self, call_number):
        """
        A private method that encapsulates the retrieval of an book with
        the given call number from the library.
        :param call_number: a string
        :return: book object if found, None otherwise
        """
        found_book = None
        for library_book in self._book_list:
            if library_book.call_number == call_number:
                found_book = library_book
                break
        return found_book

    def reduce_book_count(self, call_number):
        """
        Decrement the book count for an book with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the book was found and count decremented, false
        otherwise.
        """
        library_book = self._retrieve_book_by_call_number(call_number)
        if library_book:
            library_book.decrement_number_of_copies()
            return True
        else:
            return False

    def increment_book_count(self, call_number):
        """
        Increment the book count for an book with the given call number
        in the library.
        :param call_number: a string
        :precondition call_number: a unique identifier
        :return: True if the book was found and count incremented, false
        otherwise.
        """
        library_book = self._retrieve_book_by_call_number(call_number)
        if library_book:
            library_book.increment_number_of_copies()
            return True
        else:
            return False

    def find_books(self, title):
        """
        Find books with the same and similar title.
        :param title: a string
        :return: a list of titles.
        """
        title_list = []
        for library_book in self._book_list:
            title_list.append(library_book.get_title())
        results = difflib.get_close_matches(title, title_list,
                                            cutoff=0.5)
        return results

    def display_available_items(self):
        """
        Display all the books in the library.
        """
        print("Item List")
        print("--------------", end="\n\n")
        for library_book in self._book_list:
            print(library_book)