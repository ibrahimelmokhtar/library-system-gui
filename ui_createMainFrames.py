import tkinter as tk
from manageJsonFile import *
from functools import partial   # to pass function parameters within "command" in tkinter.Entry()

ENTRY_WIDTH = 50
PADDING_Y = 10
PADDING_X = 10


def createButtons(masterFrame, objectData, buttonText, lastInnerRow):
    functionText = "Add " + buttonText
    addMemberBtn = tk.Button(master=masterFrame, text=functionText, width=15,
                                command=partial(addObject, Member(), objectData, masterFrame))
    addMemberBtn.grid(row=lastInnerRow, column=1, pady=(PADDING_Y, 0))

    functionText = "Delete " + buttonText
    deleteMemberBtn = tk.Button(master=masterFrame, text=functionText, width=15,
                                command=partial(deleteItem, type(Member()), objectData, masterFrame))
    deleteMemberBtn.grid(row=lastInnerRow, column=2, pady=(PADDING_Y, 0))

    lastInnerRow += 1
    displayFullMembersBtn = tk.Button(master=masterFrame, text="Display Full List", width=15,
                                command=partial(displayFullList, type(Member()), masterFrame))
    displayFullMembersBtn.grid(row=lastInnerRow, column=0, pady=(PADDING_Y, PADDING_Y))

    functionText = "Update " + buttonText
    updateMemberBtn = tk.Button(master=masterFrame, text=functionText, width=15,
                                command=partial(updateItem, type(Member()), objectData, masterFrame))
    updateMemberBtn.grid(row=lastInnerRow, column=1, pady=(PADDING_Y, PADDING_Y))

    functionText = "Display " + buttonText
    displayMemberBtn = tk.Button(master=masterFrame, text=functionText, width=15,
                                command=partial(displayItem, type(Member()), objectData, masterFrame))
    displayMemberBtn.grid(row=lastInnerRow, column=2, pady=(PADDING_Y, PADDING_Y))


def createMembersFrame(masterWindow):
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
    tk.Label(master=memberFrame, text="", font="bold").grid(row=innerRow, column=1)

    innerRow += 1
    buttonText = "Member"
    createButtons(memberFrame, memberData, buttonText, innerRow)


def createBooksFrame(masterWindow):
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
    tk.Label(master=bookFrame, text="", font="bold").grid(row=innerRow, column=1)

    innerRow += 1
    buttonText = "Book"
    createButtons(bookFrame, bookData, buttonText, innerRow)


def createBorrowersFrame(masterWindow):
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
    tk.Label(master=borrowerFrame, text="", font="bold").grid(row=innerRow, column=1)

    innerRow += 1
    buttonText = "Borrower"
    createButtons(borrowerFrame, borrowerData, buttonText, innerRow)
