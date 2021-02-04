from Member import *

class Borrower(Member):
    def __init__(self, id="", name="", address="", isbn="", borrow_date="", return_date=""):
        """Create a new borrower.

        Args:
            id (string): Member's ID.
            name (string): Member's name.
            address (string): Member's address.
            isbn (string): Book's ISBN.
            borrow_date (date): Actual borrowing date.
            return_date (date): Expected return date.
        """
        super().__init__(id, name, address)
        self.isbn = isbn
        self.borrow_date = borrow_date
        self.return_date = return_date

    def __str__(self):
        """ Print the Borrower object to the terminal.
        """

        output = """\tBorrower's Info.
        \tID\t\t: {}
        \tName\t\t: {}
        \tAddress\t\t: {}
        \tBook ISBN\t: {}
        \tBorrowing Date\t: {}
        \tReturn Date\t: {}
        """

        return output.format(self.id, self.name, self.address,
                             self.isbn, self.borrow_date, self.return_date)

    def __eq__(self, other) :
        return self.__dict__ == other.__dict__

# Setter and Getter functions:
    def setISBN(self, isbn):
        self.isbn = isbn
    def setBorrowDate(self, borrow_date):
        self.borrow_date = borrow_date
    def setReturnDate(self, return_date):
        self.return_date = return_date

    def getISBN(self):
        return self.isbn
    def getBorrowDate(self):
        return self.borrow_date
    def getReturnDate(self):
        return self.return_date
