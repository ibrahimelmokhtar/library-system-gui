import tkinter as tk
from manageJsonFile import *
from functools import partial   # to pass function parameters within "command" in tkinter.Entry()

# used constant variables:
ENTRY_WIDTH = 50
PADDING_Y = 10
PADDING_X = 10

# *********************************************************************
def createButtons(masterFrame, objectData, itemClass, buttonText, lastInnerRow, messageRow):
    """Create specific bundle of buttons.

    Args:
        masterFrame (): main window to display buttons on it.
        objectData (): user input handler.
        itemClass (class type): type of the item.
        buttonText (string): text to be displayed on each button.
        lastInnerRow (int): the starting place at which buttons will be displayed.
        messageRow (int): the place to display the output message.
    """
    itemType = type(itemClass)
    clearAllBtn = tk.Button(master=masterFrame, text="Clear Fields", width=15,
                                command=partial(clearFields, objectData))
    clearAllBtn.grid(row=lastInnerRow, column=0, pady=(PADDING_Y, 0))

    functionText = "Add " + buttonText
    addItemBtn = tk.Button(master=masterFrame, text=functionText, width=15,
                                command=partial(addItem, itemClass, objectData, masterFrame, messageRow))
    addItemBtn.grid(row=lastInnerRow, column=1, pady=(PADDING_Y, 0))

    functionText = "Delete " + buttonText
    deleteItemBtn = tk.Button(master=masterFrame, text=functionText, width=15,
                                command=partial(deleteItem, itemType, objectData, masterFrame, messageRow))
    deleteItemBtn.grid(row=lastInnerRow, column=2, pady=(PADDING_Y, 0))

    lastInnerRow += 1
    displayFullListBtn = tk.Button(master=masterFrame, text="Display Full List", width=15,
                                command=partial(displayFullList, itemType, masterFrame, messageRow))
    displayFullListBtn.grid(row=lastInnerRow, column=0, pady=(PADDING_Y, PADDING_Y))

    functionText = "Update " + buttonText
    updateItemBtn = tk.Button(master=masterFrame, text=functionText, width=15,
                                command=partial(updateItem, itemType, objectData, masterFrame, messageRow))
    updateItemBtn.grid(row=lastInnerRow, column=1, pady=(PADDING_Y, PADDING_Y))

    functionText = "Display " + buttonText
    displayItemBtn = tk.Button(master=masterFrame, text=functionText, width=15,
                                command=partial(displayItem, itemType, objectData, masterFrame, messageRow))
    displayItemBtn.grid(row=lastInnerRow, column=2, pady=(PADDING_Y, PADDING_Y))

def createMembersFrame(masterWindow):
    """Create members' frame into main window.

    Args:
        masterWindow (): main window to display frames on it.
    """
    # add members' frame:
    memberFrame = tk.Frame(master=masterWindow, relief=tk.RIDGE, borderwidth=5)
    memberFrame.grid(row=0, column=0, pady=(2*PADDING_Y, 0))

    innerRow = 0
    tk.Label(master=memberFrame, text="Members' Section",
            font="Verdana 15 underline bold").grid(row=innerRow, column=1)

    # add members' data fields:
    innerRow += 1
    tk.Label(master=memberFrame, text="ID: ").grid(row=innerRow, column=0)
    memberIDEntry = tk.Entry(master=memberFrame, width=ENTRY_WIDTH)
    memberIDEntry.grid(row=innerRow, column=1, pady= (PADDING_Y, 0))

    innerRow += 1
    tk.Label(master=memberFrame, text="Name: ").grid(row=innerRow, column=0)
    memberNameEntry = tk.Entry(master=memberFrame, width=ENTRY_WIDTH)
    memberNameEntry.grid(row=innerRow, column=1, pady= (PADDING_Y, 0))

    innerRow += 1
    tk.Label(master=memberFrame, text="Address: ").grid(row=innerRow, column=0)
    memberAddressEntry = tk.Entry(master=memberFrame, width=ENTRY_WIDTH)
    memberAddressEntry.grid(row=innerRow, column=1, pady= (PADDING_Y, 0))

    memberData = [memberIDEntry, memberNameEntry, memberAddressEntry]

    innerRow += 1
    messageRow = innerRow
    tk.Label(master=memberFrame, text="", font="bold").grid(row=innerRow, column=1)

    innerRow += 1
    buttonText = "Member"
    itemClass = Member()
    createButtons(memberFrame, memberData, itemClass, buttonText, innerRow, messageRow)

def createBooksFrame(masterWindow):
    """Create books' frame into main window.

    Args:
        masterWindow (): main window to display frames on it.
    """
    # add books' frame:
    bookFrame = tk.Frame(master=masterWindow, relief=tk.RIDGE, borderwidth=5)
    bookFrame.grid(row=1, column=0, pady=(2*PADDING_Y, 0))

    innerRow = 0
    tk.Label(master=bookFrame, text="Books' Section",
            font="Verdana 15 underline bold").grid(row=innerRow, column=1)

    # add books' data fields:
    innerRow += 1
    tk.Label(master=bookFrame, text="Name: ").grid(row=innerRow, column=0)
    bookNameEntry = tk.Entry(master=bookFrame, width=ENTRY_WIDTH)
    bookNameEntry.grid(row=innerRow, column=1, pady= (PADDING_Y, 0))

    innerRow += 1
    tk.Label(master=bookFrame, text="ISBN: ").grid(row=innerRow, column=0)
    bookISBNEntry = tk.Entry(master=bookFrame, width=ENTRY_WIDTH)
    bookISBNEntry.grid(row=innerRow, column=1, pady= (PADDING_Y, 0))

    innerRow += 1
    tk.Label(master=bookFrame, text="Author: ").grid(row=innerRow, column=0)
    bookAuthorEntry = tk.Entry(master=bookFrame, width=ENTRY_WIDTH)
    bookAuthorEntry.grid(row=innerRow, column=1, pady= (PADDING_Y, 0))

    innerRow += 1
    tk.Label(master=bookFrame, text="Publication Date: ").grid(row=innerRow, column=0)
    bookPublishDateEntry = tk.Entry(master=bookFrame, width=ENTRY_WIDTH)
    bookPublishDateEntry.grid(row=innerRow, column=1, pady= (PADDING_Y, 0))

    innerRow += 1
    tk.Label(master=bookFrame, text="Publisher: ").grid(row=innerRow, column=0)
    bookPublisherEntry = tk.Entry(master=bookFrame, width=ENTRY_WIDTH)
    bookPublisherEntry.grid(row=innerRow, column=1, pady= (PADDING_Y, 0))

    innerRow += 1
    tk.Label(master=bookFrame, text="Pages Number: ").grid(row=innerRow, column=0)
    bookPagesNumberEntry = tk.Entry(master=bookFrame, width=ENTRY_WIDTH)
    bookPagesNumberEntry.grid(row=innerRow, column=1, pady= (PADDING_Y, 0))

    innerRow += 1
    tk.Label(master=bookFrame, text="Cover Type: ").grid(row=innerRow, column=0)
    bookCoverTypeEntry = tk.Entry(master=bookFrame, width=ENTRY_WIDTH)
    bookCoverTypeEntry.grid(row=innerRow, column=1, pady= (PADDING_Y, 0))

    bookData = [bookNameEntry, bookISBNEntry, bookAuthorEntry, bookPublishDateEntry,
                bookPublisherEntry, bookPagesNumberEntry, bookCoverTypeEntry]

    innerRow += 1
    messageRow = innerRow
    tk.Label(master=bookFrame, text="", font="bold").grid(row=innerRow, column=1)

    innerRow += 1
    buttonText = "Book"
    itemClass = Book()
    createButtons(bookFrame, bookData, itemClass, buttonText, innerRow, messageRow)

def createBorrowersFrame(masterWindow):
    """Create borrowers' frame into main window.

    Args:
        masterWindow (): main window to display frames on it.
    """
    # add borrowers' frame:
    borrowerFrame = tk.Frame(master=masterWindow, relief=tk.RIDGE, borderwidth=5)
    borrowerFrame.grid(row=1, column=1,
                       pady=(2*PADDING_Y, 0), padx=(PADDING_X, PADDING_X))

    innerRow = 0
    tk.Label(master=borrowerFrame, text="Borrowers' Section",
            font="Verdana 15 underline bold").grid(row=innerRow, column=1)

    # add borrowers' data fields:
    innerRow += 1
    tk.Label(master=borrowerFrame, text="ID: ").grid(row=innerRow, column=0)
    bookIDEntry = tk.Entry(master=borrowerFrame, width=ENTRY_WIDTH)
    bookIDEntry.grid(row=innerRow, column=1, pady= (PADDING_Y, 0))

    innerRow += 1
    tk.Label(master=borrowerFrame, text="Name: ").grid(row=innerRow, column=0)
    bookNameEntry = tk.Entry(master=borrowerFrame, width=ENTRY_WIDTH)
    bookNameEntry.grid(row=innerRow, column=1, pady= (PADDING_Y, 0))

    innerRow += 1
    tk.Label(master=borrowerFrame, text="Address: ").grid(row=innerRow, column=0)
    bookAddressEntry = tk.Entry(master=borrowerFrame, width=ENTRY_WIDTH)
    bookAddressEntry.grid(row=innerRow, column=1, pady= (PADDING_Y, 0))

    innerRow += 1
    tk.Label(master=borrowerFrame, text="ISBN: ").grid(row=innerRow, column=0)
    bookISBNEntry = tk.Entry(master=borrowerFrame, width=ENTRY_WIDTH)
    bookISBNEntry.grid(row=innerRow, column=1, pady= (PADDING_Y, 0))

    innerRow += 1
    tk.Label(master=borrowerFrame, text="Borrow Date: ").grid(row=innerRow, column=0)
    bookBorrowDateEntry = tk.Entry(master=borrowerFrame, width=ENTRY_WIDTH)
    bookBorrowDateEntry.grid(row=innerRow, column=1, pady= (PADDING_Y, 0))

    innerRow += 1
    tk.Label(master=borrowerFrame, text="Return Date: ").grid(row=innerRow, column=0)
    bookReturnDateEntry = tk.Entry(master=borrowerFrame, width=ENTRY_WIDTH)
    bookReturnDateEntry.grid(row=innerRow, column=1, pady= (PADDING_Y, 0))

    borrowerData = [bookIDEntry, bookNameEntry, bookAddressEntry,
                    bookISBNEntry, bookBorrowDateEntry, bookReturnDateEntry]

    innerRow += 1
    messageRow = innerRow
    tk.Label(master=borrowerFrame, text="", font="bold").grid(row=innerRow, column=1)

    innerRow += 1
    buttonText = "Borrower"
    itemClass = Borrower()
    createButtons(borrowerFrame, borrowerData, itemClass, buttonText, innerRow, messageRow)
