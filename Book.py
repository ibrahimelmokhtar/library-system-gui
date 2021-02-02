import datetime

class Book():
    def __init__(self, name, isbn, author, publication_date, publisher, pages_number, cover_type):
        """ Create a new book.

        Args:
            name (string): Name of the book.
            isbn (string): ID number of the book.
            author (string): Name of the author who wrote the book.
            publication_date (date): Date of publication.
            publisher (string): Name of the publisher who published the book.
            pages_number (integer): Number of pages of the book.
            cover_type (string): Type of cover of the book.
        """
        self.name = name
        self.isbn = isbn
        self.author = author
        self.publication_date = publication_date
        self.publisher = publisher
        self.pages_number = pages_number
        self.cover_type = cover_type

    def __str__(self):
        """ Print th Book object to terminal.
        """

        output = """
        Book's Info.
        \tName\t\t: {}
        \tISBN\t\t: {}
        \tAuthor\t\t: {}
        \tPublication Date: {}
        \tPublisher\t: {}
        \tPages' Number\t: {}
        \tCover Typr\t: {}
        """

        return output.format(self.name, self.isbn, self.author, self.publication_date,
                             self.publisher, self.pages_number, self.cover_type)

# Setter and Getter functions:
    def setName(self, name):
        self.name = name
    def setISBN(self, isbn):
        self.isbn = isbn
    def setAuthor(self, author):
        self.author = author
    def setDate(self, publication_date):
        self.publication_date = publication_date
    def setPublisher(self, publisher):
        self.publisher = publisher
    def setPagesNumber(self, pages_number):
        self.pages_number = pages_number
    def setCoverType(self, cover_type):
        self.cover_type = cover_type

    def getName(self, name):
        return self.name
    def getISBN(self, isbn):
        return self.isbn
    def getAuthor(self, author):
        return self.author
    def getDate(self, publication_date):
        return self.publication_date
    def getPublisher(self, publisher):
        return self.publisher
    def getPagesNumber(self, pages_number):
        return self.pages_number
    def getCoverType(self, cover_type):
        return self.cover_type
