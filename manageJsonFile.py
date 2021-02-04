import json
from Book import *
from Member import *
from Borrower import *

dataJsonFile = "data.json"

def checkFileExistence():
    """ Check if JSON file exists or not.
        Then create the file if it does NOT exist.

    Returns:
        dict: contains members, books, and borrowers lists.
    """
    # Try reading to see if the JSON file already exists.
    # If not, create an empty JSON file.
    try:
        data = readFromFile()
    except:
        with open(dataJsonFile, 'w') as outputFile:
            data = {}
            data["members"] = []
            data["books"] = []
            data["borrowers"] = []
            data = json.dumps(data, indent=2)
            outputFile.write(data)
        data = readFromFile()   # re-read data from the file.
    return data

def readFromFile():
    with open(dataJsonFile, 'r') as inputFile:
            data = inputFile.read()
            data = json.loads(data)
    return data
def saveIntoFile(data):
    with open(dataJsonFile, 'w') as outputFile:
        data = json.dumps(data, indent=2)
        outputFile.write(data)

def addObject(newObject):
    # check JSON file existence:
    data = checkFileExistence()

    # append a (dict) object to specific list:
    if type(newObject) is Member:
        memberObject = newObject
        data["members"].append(
            {
                "id": memberObject.getID(),
                "name": memberObject.getName(),
                "address": memberObject.getAddress()
            }
        )
    elif type(newObject) is Book:
        bookObject = newObject
        data["books"].append(
            {
                "name": bookObject.getName(),
                "isbn": bookObject.getISBN(),
                "author": bookObject.getAuthor(),
                "publication_date": str(bookObject.getDate()),
                "publisher": bookObject.getPublisher(),
                "pages_number": bookObject.getPagesNumber(),
                "cover_type": bookObject.getCoverType()
            }
        )
    elif type(newObject) is Borrower:
        borrowerObject = newObject
        data["borrowers"].append(
            {
                "id": borrowerObject.getID(),
                "name": borrowerObject.getName(),
                "address": borrowerObject.getAddress(),
                "isbn": borrowerObject.getISBN(),
                "borrow_date": str(borrowerObject.getBorrowDate()),
                "return_date": str(borrowerObject.getReturnDate())
            }
        )

    # save into JSON file:
    saveIntoFile(data)
