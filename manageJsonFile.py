import json
from Book import *
from Member import *
from Borrower import *
import tkinter as tk

dataJsonFile = "data.json"
TIMEOUT = 2000
DONE_MESSAGE = "Done Successfully!"
ERROR_MESSAGE = "Invalid Item!"

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

def saveIntoFile(data, objectData, masterFrame, messageRow):
    """Save JSON data into .json file.

    Args:
        data (dict): JSON object
    """
    with open(dataJsonFile, 'w') as outputFile:
        data = json.dumps(data, indent=2)
        outputFile.write(data)
    displayMessage(masterFrame, messageRow, DONE_MESSAGE, "green")
    clearFields(objectData)

# display label message for the user:
def displayMessage(masterFrame, messageRow, messageText, messageColor):
    message = tk.Label(master=masterFrame, text=messageText, fg=messageColor, font="bold")
    message.grid(row=messageRow, column=1)
    message.after(TIMEOUT, lambda: message.config(text="", font="bold"))

# clear input fields:
def clearFields(objectData):
    for dataEntry in objectData:
        dataEntry.delete(0, 'end')

def insertFields(objectData, foundObject):
    clearFields(objectData)
    if type(foundObject) is Member:
        foundObjectData = [foundObject.getID(), foundObject.getName(), foundObject.getAddress()]
    elif type(foundObject) is Book:
        foundObjectData = [foundObject.getName(), foundObject.getISBN(), foundObject.getAuthor(),
                           foundObject.getDate(), foundObject.getPublisher(),
                           foundObject.getPagesNumber(), foundObject.getCoverType()]
    elif type(foundObject) is Borrower:
        foundObjectData = [foundObject.getID(), foundObject.getName(), foundObject.getAddress(),
                           foundObject.getISBN(), foundObject.getBorrowDate(), foundObject.getReturnDate()]

    for i in range(len(foundObjectData)):
        objectData[i].insert(0, foundObjectData[i])

def addItem(newObject, objectData, masterFrame, messageRow, isDeleting=False):
    """Add new Member, Book, or Borrower.

    Args:
        newObject (object): the new object to be added.
    """
    # check JSON file existence:
    data = checkFileExistence()

    # append a (dict) object to specific list:
    if isDeleting:
        insertFields(objectData, newObject)

    if type(newObject) is Member:
        data["members"].append(
            {
                "id": objectData[0].get(),
                "name": objectData[1].get(),
                "address": objectData[2].get()
            }
        )
    elif type(newObject) is Book:
        data["books"].append(
            {
                "name": objectData[0].get(),
                "isbn": objectData[1].get(),
                "author": objectData[2].get(),
                "publication_date": objectData[3].get(),
                "publisher": objectData[4].get(),
                "pages_number": objectData[5].get(),
                "cover_type": objectData[6].get()
            }
        )
    elif type(newObject) is Borrower:
        data["borrowers"].append(
            {
                "id": objectData[0].get(),
                "name": objectData[1].get(),
                "address": objectData[2].get(),
                "isbn": objectData[3].get(),
                "borrow_date": objectData[4].get(),
                "return_date": objectData[5].get()
            }
        )
    else:
        print("Invalid Object!\n")
        displayMessage(masterFrame, messageRow, ERROR_MESSAGE, "red")

    # save into JSON file:
    saveIntoFile(data, objectData, masterFrame, messageRow)

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
    return False

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
    return False

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

def displayFullList(listType, masterFrame, messageRow):
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
        displayMessage(masterFrame, messageRow, ERROR_MESSAGE, "red")

    # create new window to display data:
    displayWindow = tk.Tk()
    window_width = displayWindow.winfo_screenwidth()
    window_height = displayWindow.winfo_screenheight()
    displayWindow.geometry("%dx%d" % (window_width/2, window_height/2))
    displayWindow.title("Members' Full List")

    frameRow = 0
    for item in data[objectType]:
        itemFrame = tk.Frame(master=displayWindow, relief=tk.RIDGE, borderwidth=5)
        itemFrame.grid(row=frameRow, column=0, padx=(10, 10), pady=(10, 0))

        tk.Label(master=itemFrame, text="Member's Data",
                 font="Verdana 10 underline bold").grid(row=0, column=1)
        tk.Label(master=itemFrame, text="ID: ").grid(row=1, column=0)
        tk.Label(master=itemFrame, text=item["id"]).grid(row=1, column=1)

        tk.Label(master=itemFrame, text="Name: ").grid(row=2, column=0)
        tk.Label(master=itemFrame, text=item["name"]).grid(row=2, column=1)

        tk.Label(master=itemFrame, text="Address: ").grid(row=3, column=0)
        tk.Label(master=itemFrame, text=item["address"]).grid(row=3, column=1)

        objectReturned = convertDictIntoObject(item, convertTo)
        print(objectReturned)
        count += 1
        frameRow += 1
    displayMessage(masterFrame, messageRow, DONE_MESSAGE, "green")
    return count

def displayItem(itemType, objectData, masterFrame, messageRow):
    """Display specific item.

    Args:
        searchKeyword (string): name, id, or isbn of the item.
        itemType (class type): the item's type to be displayed.
        isName (bool, optional): Specify if first argument is name or not. Defaults to False.
    """
    item = None
    searchKeyword, isName = captureData(itemType, objectData)
    if itemType == type(Member()):
        item = searchPerson(searchKeyword, "members", isName)
    elif itemType == type(Borrower()):
        item = searchPerson(searchKeyword, "borrowers", isName)
    elif itemType == type(Book()):
        item = searchBook(searchKeyword, isName)
    else:
        print("Invalid Object!\n")
        displayMessage(masterFrame, messageRow, ERROR_MESSAGE, "red")

    if item:
        insertFields(objectData, item)
        displayMessage(masterFrame, messageRow, DONE_MESSAGE, "green")
    else:
        displayMessage(masterFrame, messageRow, ERROR_MESSAGE, "red")


def deleteItem(itemType, objectData, masterFrame, messageRow):
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

    searchKeyword, isName = captureData(itemType, objectData)

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
        displayMessage(masterFrame, messageRow, ERROR_MESSAGE, "red")

    # check the type of returned item: (to validate that it exists)
    if type(itemToBeDeleted) != convertTo:
        displayMessage(masterFrame, messageRow, ERROR_MESSAGE, "red")
        return False

    newData = data.copy()
    newData[itemType] = []
    saveIntoFile(newData, objectData, masterFrame, messageRow)
    for item in data[itemType]:
        item = convertDictIntoObject(item, convertTo)
        if item == itemToBeDeleted:
            continue

        addItem(item, objectData, masterFrame, messageRow, isDeleting=True)
    return itemToBeDeleted

def updateItem(itemType, objectData, masterFrame, messageRow):
    # check JSON file existence:
    data = checkFileExistence()

    searchKeyword, isName = captureData(itemType, objectData)
    newItem = captureFullData(itemType, objectData)

    itemToBeDeleted = deleteItem(itemType, objectData, masterFrame, messageRow)
    if type(itemToBeDeleted) != False:
        addItem(newItem, objectData, masterFrame, messageRow, isDeleting=True)
        print("Data is up-to-date.")

def captureData(itemType, objectData):
    # check JSON file existence:
    data = checkFileExistence()

    if itemType == type(Member()):
        itemType = "members"
        fields = ["id", "name"]
        fieldPlace = [0, 1]
    elif itemType == type(Borrower()):
        itemType = "borrowers"
        fields = ["id", "name"]
        fieldPlace = [0, 1]
    elif itemType == type(Book()):
        itemType = "books"
        fields = ["isbn", "name"]
        fieldPlace = [1, 0]

    for item in data[itemType]:
        if objectData[fieldPlace[0]].get() == item[fields[0]]:
            searchKeyword = objectData[fieldPlace[0]].get()
            isName = False
            break
        elif objectData[fieldPlace[1]].get() == item[fields[1]]:
            searchKeyword = objectData[fieldPlace[1]].get()
            isName = True
            break

    return searchKeyword, isName

def captureFullData(itemType, objectData):
    if itemType == type(Member()):
        newItem = Member(objectData[0].get(), objectData[1].get(), objectData[2].get())

    elif itemType == type(Book()):
        newItem = Book(objectData[0].get(), objectData[1].get(), objectData[2].get(),
                       objectData[3].get(), objectData[4].get(), objectData[5].get(),
                       objectData[6].get())

    elif itemType == type(Borrower()):
        newItem = Borrower(objectData[0].get(), objectData[1].get(), objectData[2].get(),
                           objectData[3].get(), objectData[4].get(), objectData[5].get())


    return newItem
