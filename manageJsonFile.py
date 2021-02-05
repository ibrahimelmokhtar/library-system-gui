import json
from Book import *
from Member import *
from Borrower import *
import tkinter as tk

dataJsonFile = "data.json"
TIMEOUT = 2000

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
    """Read JSON data from .json file.

    Returns:
        dict: JSON object contains all saved data.
    """
    with open(dataJsonFile, 'r') as inputFile:
            data = inputFile.read()
            data = json.loads(data)
    return data
def saveIntoFile(data, objectData, masterFrame):
    """Save JSON data into .json file.

    Args:
        data (dict): JSON object
    """
    with open(dataJsonFile, 'w') as outputFile:
        data = json.dumps(data, indent=2)
        outputFile.write(data)
    displayMessage(masterFrame, "Done Successfully!", "green")
    clearFields(objectData)

# display label message for the user:
def displayMessage(masterFrame, messageText, messageColor):
    message = tk.Label(master=masterFrame, text=messageText, fg=messageColor, font="bold")
    message.grid(row=4, column=1)
    message.after(TIMEOUT, lambda: message.config(text=""))

# clear input fields:
def clearFields(objectData):
    for dataEntry in objectData:
        dataEntry.delete(0, 'end')

def addObject(newObject, objectData, masterFrame, isDeleting=False):
    """Add new Member, Book, or Borrower.

    Args:
        newObject (object): the new object to be added.
    """
    # check JSON file existence:
    data = checkFileExistence()

    # append a (dict) object to specific list:
    if type(newObject) is Member:
        if isDeleting:
            objectData[0].insert(0, newObject.getID())
            objectData[1].insert(0, newObject.getName())
            objectData[2].insert(0, newObject.getAddress())
        data["members"].append(
            {
                "id": objectData[0].get(),
                "name": objectData[1].get(),
                "address": objectData[2].get()
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
    else:
        print("Invalid Object!\n")

    # save into JSON file:
    saveIntoFile(data, objectData, masterFrame)

def searchPerson(name_or_id, personType, isName=False):
    """Search members or borrowers lists using name or ID to see if specific person exists or not.

    Args:
        name_or_id (string): the name or ID of the person.
        isName (bool, optional): Specify weather first argument is name or not. Defaults to False.

    Returns:
        dict: the required person if exists.
    """
    # check JSON file existence:
    data = checkFileExistence()

    if personType == "members":
        convertTo = type(Member())
    else:
        convertTo = type(Borrower())

    searchField = "id"
    if isName:
        searchField = "name"

    for person in data[personType]:
        if person[searchField] == name_or_id:
            print("{} exists.".format(personType[:-1]))
            person = convertDictIntoObject(person, convertTo)
            return person
    print("{} does NOT exist.\n".format(personType[:-1]))

def searchBook(name_or_isbn, isName=False):
    """Search books list using name or ISBN to see if specific book exists or not.

    Args:
        name_or_isbn (string): the name or ISBN of the book.
        isName (bool, optional): Specify if first argument is name or not. Defaults to False.

    Returns:
        dict: the required book if exists.
    """
    # check JSON file existence:
    data = checkFileExistence()

    searchField = "isbn"
    if isName:
        searchField = "name"

    for book in data["books"]:
        if book[searchField] == name_or_isbn:
            print("Book exists.")
            book = convertDictIntoObject(book, type(Book()))
            return book
    print("Book does NOT exist.\n")

def convertDictIntoObject(jsonDict, objectType):
    """Convert dict json format into its corresponding object type.

    Args:
        jsonDict (dict): json object to be converted.
        objectType (object): desired object type (Member, Book, or Borrower).

    Returns:
        object: the result of the conversion.
    """
    if objectType == type(Member()):
        objectReturned = Member(jsonDict["id"], jsonDict["name"], jsonDict["address"])
    elif objectType == type(Book()):
        objectReturned = Book(jsonDict["name"], jsonDict["isbn"], jsonDict["author"],
                              jsonDict["publication_date"], jsonDict["publisher"],
                              jsonDict["pages_number"], jsonDict["cover_type"])
    elif objectType == type(Borrower()):
        objectReturned = Borrower(jsonDict["id"], jsonDict["name"], jsonDict["address"],
                                  jsonDict["isbn"], jsonDict["borrow_date"], jsonDict["return_date"])
    else:
        print("Invalid Object!\n")
    return objectReturned

def displayFullList(listType):
    """Display full list.

    Args:
        listType (class type): the list's type to be displayed.

    Returns:
        int: the number of items in the displayed list.
    """
    # check JSON file existence:
    data = checkFileExistence()

    count = 0
    if listType == type(Member()):
        objectType = "members"
        convertTo = type(Member())

    elif listType == type(Borrower()):
        objectType = "borrowers"
        convertTo = type(Borrower())

    elif listType == type(Book()):
        objectType = "books"
        convertTo = type(Book())
    else:
        print("Invalid Object!\n")


    for item in data[objectType]:
        objectReturned = convertDictIntoObject(item, convertTo)
        print(objectReturned)
        count += 1
    return count

def displayItem(searchKeyword, itemType, masterFrame, isName=False):
    """Display specific item.

    Args:
        searchKeyword (string): name, id, or isbn of the item.
        itemType (class type): the item's type to be displayed.
        isName (bool, optional): Specify if first argument is name or not. Defaults to False.
    """
    item = ""
    if itemType == type(Member()):
        item = searchPerson(searchKeyword, "members", isName)
    elif itemType == type(Borrower()):
        item = searchPerson(searchKeyword, "borrowers", isName)
    elif itemType == type(Book()):
        item = searchBook(searchKeyword, isName)
    else:
        print("Invalid Object!\n")

    if item != None:
        print(item)

def deleteItem(itemType, objectData, masterFrame):
    """Delete specific item.

    Args:
        searchKeyword (string): name, id, or isbn of the item.
        itemType (class type): type of the item.
        isName (bool, optional): specify if first argument is name or not. Defaults to False.

    Returns:
        object: the deleted object.
    """
    # check JSON file existence:
    data = checkFileExistence()

    searchKeyword, isName = captureData(objectData)

    if itemType == type(Member()):
        itemType = "members"
        convertTo = type(Member())
        itemToBeDeleted = searchPerson(searchKeyword, itemType, isName)
    elif itemType == type(Borrower()):
        itemType = "borrowers"
        convertTo = type(Borrower())
        itemToBeDeleted = searchPerson(searchKeyword, itemType, isName)
    elif itemType == type(Book()):
        itemType = "books"
        convertTo = type(Book())
        itemToBeDeleted = searchBook(searchKeyword, isName)
    else:
        print("Invalid Object!\n")

    # check the type of returned item: (to validate that it exists)
    if type(itemToBeDeleted) != convertTo:
        displayMessage(masterFrame, "Invalid item!", "red")
        return False

    newData = data.copy()
    newData[itemType] = []
    saveIntoFile(newData, objectData, masterFrame)
    for item in data[itemType]:
        item = convertDictIntoObject(item, convertTo)
        if item == itemToBeDeleted:
            continue

        addObject(item, objectData, masterFrame, isDeleting=True)
    return itemToBeDeleted

def updateItem(searchKeyword, itemType, newItem, masterFrame, isName=False):
    # check JSON file existence:
    data = checkFileExistence()

    itemToBeDeleted = deleteItem(searchKeyword, itemType, isName)
    if type(itemToBeDeleted) != False:
        addObject(newItem, masterFrame)
        print("Data is up-to-date.")

def captureData(objectData):
    if len(objectData[0].get()) > 0:
        searchKeyword = objectData[0].get()
        isName = False
    else:
        searchKeyword = objectData[1].get()
        isName = True

    return searchKeyword, isName
