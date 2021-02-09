import json
from Book import *
from Member import *
from Borrower import *
import tkinter as tk

# used constant variables:
dataJsonFile = "data.json"
TIMEOUT = 2000
DONE_MESSAGE = "Done Successfully!"
ERROR_MESSAGE = "Invalid Item!"

# *********************************************************************
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
    # read full json data from file:
    with open(dataJsonFile, 'r') as inputFile:
            data = inputFile.read()
            data = json.loads(data)
    return data

def saveIntoFile(data, objectData, masterFrame, messageRow):
    """Save JSON data into .json file.

    Args:
        data (dict): json data required to be saved.
        objectData (): user input handler.
        masterFrame (): the frame that the message will be displayed on it.
        messageRow (int): the place to display the output message.
    """
    # write json data after formatting:
    with open(dataJsonFile, 'w') as outputFile:
        data = json.dumps(data, indent=2)
        outputFile.write(data)

    # display appropriate message then clear user input fields:
    displayMessage(masterFrame, messageRow, DONE_MESSAGE, "green")
    clearFields(objectData)

def displayMessage(masterFrame, messageRow, messageText, messageColor):
    """Display message for the user.

    Args:
        masterFrame (): the frame that the message will be displayed on it.
        messageRow (int): the place to display the output message.
        messageText (string): the message text.
        messageColor (string): the message color.
    """
    # set appropriate message:
    message = tk.Label(master=masterFrame, text=messageText, fg=messageColor, font="bold")
    message.grid(row=messageRow, column=1)

    # message displayed will disappear:
    message.after(TIMEOUT, lambda: message.config(text="", font="bold"))

def clearFields(objectData):
    """Clear input fields.

    Args:
        objectData (): user input handler.
    """
    # delete each user input field:
    for dataEntry in objectData:
        dataEntry.delete(0, 'end')

def insertFields(objectData, foundObject):
    """Insert specific text into user input fields.

    Args:
        objectData (): user input handler.
        foundObject (object): object to be displayed on user input fields.
    """
    # clear all user input fields:
    clearFields(objectData)

    # set item's data depending on object's type:
    if type(foundObject) is Member:
        foundObjectData = [foundObject.getID(), foundObject.getName(), foundObject.getAddress()]
    elif type(foundObject) is Book:
        foundObjectData = [foundObject.getName(), foundObject.getISBN(), foundObject.getAuthor(),
                           foundObject.getDate(), foundObject.getPublisher(),
                           foundObject.getPagesNumber(), foundObject.getCoverType()]
    elif type(foundObject) is Borrower:
        foundObjectData = [foundObject.getID(), foundObject.getName(), foundObject.getAddress(),
                           foundObject.getISBN(), foundObject.getBorrowDate(), foundObject.getReturnDate()]

    # display item's data on user input fields:
    for i in range(len(foundObjectData)):
        objectData[i].insert(0, foundObjectData[i])

def addItem(newObject, objectData, masterFrame, messageRow, isDeleting=False):
    """Add new Member, Book, or Borrower.

    Args:
        newObject (object): new object to be added.
        objectData (): user input handler.
        masterFrame (): the frame that the message will be displayed on it.
        messageRow (int): the place to display the output message.
        isDeleting (bool, optional): determine if any deletion is required.. Defaults to False.
    """
    # check JSON file existence:
    data = checkFileExistence()

    # used while deleting item from specific list:
    if isDeleting:
        insertFields(objectData, newObject)

    # add item to its corresponding list:
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
        personType (string): a word descripe the input object type.
        isName (bool, optional): Specify weather first argument is name or not. Defaults to False.

    Returns:
        dict: the required person if exists.
    """
    # check JSON file existence:
    data = checkFileExistence()

    # set converting type depending on person's type:
    if personType == "members":
        convertTo = type(Member())
    else:
        convertTo = type(Borrower())

    # set searching data:
    searchField = "id"
    if isName:
        searchField = "name"

    # find specific person (member or borrower):
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

    # set searching data:
    searchField = "isbn"
    if isName:
        searchField = "name"

    # find specific book:
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
    # set returned object's data from json data:
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
    """Display full list into new window.

    Args:
        listType (class type): the list's type to be displayed.
        masterFrame (): the frame that the message will be displayed on it.
        messageRow (int): the place to display the output message.

    Returns:
        int: the number of items in the displayed list.
    """
    # check JSON file existence:
    data = checkFileExistence()

    count = 0       # used to get total number of items.

    # set used variables depending on list's type:
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
    titleText = objectType.capitalize()
    displayWindow.title("{}' Full List".format(titleText))

    frameRow = 1        # used to set each frame's place.
    for item in data[objectType]:
        # create new frame:
        itemFrame = tk.Frame(master=displayWindow, relief=tk.RIDGE, borderwidth=5)
        itemFrame.grid(row=frameRow, column=0, padx=(10, 10), pady=(10, 0))

        # set frame's title:
        tk.Label(master=itemFrame, text="{}'s Data".format(titleText[:-1]),
                 font="Verdana 10 underline bold").grid(row=0, column=1)

        # display required data depending on list's type:
        if listType == type(Member()):
            tk.Label(master=itemFrame, text="ID: ").grid(row=1, column=0)
            tk.Label(master=itemFrame, text=item["id"]).grid(row=1, column=1)

            tk.Label(master=itemFrame, text="Name: ").grid(row=2, column=0)
            tk.Label(master=itemFrame, text=item["name"]).grid(row=2, column=1)

            tk.Label(master=itemFrame, text="Address: ").grid(row=3, column=0)
            tk.Label(master=itemFrame, text=item["address"]).grid(row=3, column=1)

        elif listType == type(Book()):
            tk.Label(master=itemFrame, text="Name: ").grid(row=1, column=0)
            tk.Label(master=itemFrame, text=item["name"]).grid(row=1, column=1)

            tk.Label(master=itemFrame, text="ISBN: ").grid(row=2, column=0)
            tk.Label(master=itemFrame, text=item["isbn"]).grid(row=2, column=1)

            tk.Label(master=itemFrame, text="Author: ").grid(row=3, column=0)
            tk.Label(master=itemFrame, text=item["author"]).grid(row=3, column=1)

            tk.Label(master=itemFrame, text="Publication Date: ").grid(row=4, column=0)
            tk.Label(master=itemFrame, text=item["publication_date"]).grid(row=4, column=1)

            tk.Label(master=itemFrame, text="Publisher: ").grid(row=5, column=0)
            tk.Label(master=itemFrame, text=item["publisher"]).grid(row=5, column=1)

            tk.Label(master=itemFrame, text="Pages Number: ").grid(row=6, column=0)
            tk.Label(master=itemFrame, text=item["pages_number"]).grid(row=6, column=1)

            tk.Label(master=itemFrame, text="Cover Type: ").grid(row=7, column=0)
            tk.Label(master=itemFrame, text=item["cover_type"]).grid(row=7, column=1)

        elif listType == type(Borrower()):
            tk.Label(master=itemFrame, text="ID: ").grid(row=1, column=0)
            tk.Label(master=itemFrame, text=item["id"]).grid(row=1, column=1)

            tk.Label(master=itemFrame, text="Name: ").grid(row=2, column=0)
            tk.Label(master=itemFrame, text=item["name"]).grid(row=2, column=1)

            tk.Label(master=itemFrame, text="Address: ").grid(row=3, column=0)
            tk.Label(master=itemFrame, text=item["address"]).grid(row=3, column=1)

            tk.Label(master=itemFrame, text="ISBN: ").grid(row=4, column=0)
            tk.Label(master=itemFrame, text=item["isbn"]).grid(row=4, column=1)

            tk.Label(master=itemFrame, text="Borrow Date: ").grid(row=5, column=0)
            tk.Label(master=itemFrame, text=item["borrow_date"]).grid(row=5, column=1)

            tk.Label(master=itemFrame, text="Return Date: ").grid(row=6, column=0)
            tk.Label(master=itemFrame, text=item["return_date"]).grid(row=6, column=1)

        # display item's data on console:
        objectReturned = convertDictIntoObject(item, convertTo)
        print(objectReturned)
        count += 1
        frameRow += 1

    # display total number of displayed items:
    tk.Label(master=displayWindow, text="Total: {}".format(count),
                 font="Verdana 15 underline bold").grid(row=0, column=1)

    # display appropriate message:
    displayMessage(masterFrame, messageRow, DONE_MESSAGE, "green")
    return count

def displayItem(itemType, objectData, masterFrame, messageRow):
    """Display specific item on user input fields.

    Args:
        itemType (class type): the object's type to be displayed.
        objectData (): user input handler.
        masterFrame (): the frame that the message will be displayed on it.
        messageRow (int): the place to display the output message.
    """

    # item to be displayed:
    item = None

    # capture item's data:
    searchKeyword, isName = captureData(itemType, objectData)

    # fetch specific item:
    if itemType == type(Member()):
        item = searchPerson(searchKeyword, "members", isName)
    elif itemType == type(Borrower()):
        item = searchPerson(searchKeyword, "borrowers", isName)
    elif itemType == type(Book()):
        item = searchBook(searchKeyword, isName)
    else:
        print("Invalid Object!\n")
        displayMessage(masterFrame, messageRow, ERROR_MESSAGE, "red")

    # display item's data and appropriate message:
    if item:
        insertFields(objectData, item)
        displayMessage(masterFrame, messageRow, DONE_MESSAGE, "green")
    else:
        displayMessage(masterFrame, messageRow, ERROR_MESSAGE, "red")

def deleteItem(itemType, objectData, masterFrame, messageRow):
    """Delete specific item.

    Args:
        itemType (class type): type of the item.
        objectData (): user input handler.
        masterFrame (): the frame that the message will be displayed on it.
        messageRow (int): the place to display the output message.

    Returns:
        object: the deleted object.
    """
    # check JSON file existence:
    data = checkFileExistence()

    # capture item's data:
    searchKeyword, isName = captureData(itemType, objectData)

    # search item's existence:
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

    # clear specific list from JSON file:
    newData = data.copy()
    newData[itemType] = []
    saveIntoFile(newData, objectData, masterFrame, messageRow)

    # add all items again, but skip specific one:
    for item in data[itemType]:
        item = convertDictIntoObject(item, convertTo)
        if item == itemToBeDeleted:
            continue
        addItem(item, objectData, masterFrame, messageRow, isDeleting=True)

    return itemToBeDeleted

def updateItem(itemType, objectData, masterFrame, messageRow):
    """Update specific item's data.

    Args:
        itemType (class type): type of the item.
        objectData (): user input handler.
        masterFrame (): the frame that the message will be displayed on it.
        messageRow (int): the place to display the output message.
    """
    # check JSON file existence:
    data = checkFileExistence()

    # capture item's data:
    searchKeyword, isName = captureData(itemType, objectData)
    newItem = captureFullData(itemType, objectData)

    # delete old item:
    itemToBeDeleted = deleteItem(itemType, objectData, masterFrame, messageRow)

    # add new item:
    if type(itemToBeDeleted) != False:
        addItem(newItem, objectData, masterFrame, messageRow, isDeleting=True)
        print("Data is up-to-date.")

def captureData(itemType, objectData):
    """Capture data from specific user input fields.

    Args:
        itemType (class type): type of the item.
        objectData (): user input handler.

    Returns:
        tuple: a paired output contains (searchKeyword, isName)
    """
    # check JSON file existence:
    data = checkFileExistence()

    # set used variables:
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

    # check item's existence then capture its data:
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
    """Capture data from ALL the user input fields.

    Args:
        itemType (class type): type of the item.
        objectData (): user input handler.

    Returns:
        object: the captured object.
    """
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
