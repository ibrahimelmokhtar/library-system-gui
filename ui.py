import tkinter as tk
from manageJsonFile import *
from functools import partial   # to pass function parameters within "command" in tkinter.Entry()

# create window:
window = tk.Tk()
ENTRY_WIDTH = 50
PADDING_Y = 5
PADDING_X = 5

# start window at full screen size:
window_width = window.winfo_screenwidth()
window_height = window.winfo_screenheight()
window.geometry("%dx%d" % (window_width, window_height))
window.title("Library Management System")

# add members' frame:
memberFrame = tk.Frame(master=window, relief=tk.RIDGE, borderwidth=5)
memberFrame.grid(row=0, column=0)
tk.Label(master=memberFrame, text="Members' Section",
         font="Verdana 15 underline bold").grid(row=0, column=1)

# add members' data fields:
tk.Label(master=memberFrame, text="ID: ").grid(row=1, column=0)
memberIDEntry = tk.Entry(master=memberFrame, width=ENTRY_WIDTH)
memberIDEntry.grid(row=1, column=1, pady= (PADDING_Y, 0))

tk.Label(master=memberFrame, text="Name: ").grid(row=2, column=0)
memberNameEntry = tk.Entry(master=memberFrame, width=ENTRY_WIDTH)
memberNameEntry.grid(row=2, column=1, pady= (PADDING_Y, 0))

tk.Label(master=memberFrame, text="Address: ").grid(row=3, column=0)
memberAddressEntry = tk.Entry(master=memberFrame, width=ENTRY_WIDTH)
memberAddressEntry.grid(row=3, column=1, pady= (PADDING_Y, 0))

memberData = [memberIDEntry, memberNameEntry, memberAddressEntry]

tk.Label(master=memberFrame, text="", font="bold").grid(row=4, column=1)

# members' buttons:
addMemberBtn = tk.Button(master=memberFrame, text="Add Member", width=15,
                               command=partial(addObject, Member(), memberData, memberFrame))
addMemberBtn.grid(row=5, column=1, pady=(PADDING_Y, 0))

deleteMemberBtn = tk.Button(master=memberFrame, text="Delete Member", width=15,
                               command=partial(deleteItem, type(Member()), memberData, memberFrame))
deleteMemberBtn.grid(row=5, column=2, pady=(PADDING_Y, 0))

displayFullMembersBtn = tk.Button(master=memberFrame, text="Display Full List", width=15,
                               command=partial(displayFullList, type(Member()), memberFrame))
displayFullMembersBtn.grid(row=6, column=0, pady=(PADDING_Y, PADDING_Y))

updateMemberBtn = tk.Button(master=memberFrame, text="Update Member", width=15,
                               command=partial(updateItem, type(Member()), memberData, memberFrame))
updateMemberBtn.grid(row=6, column=1, pady=(PADDING_Y, PADDING_Y))

displayMemberBtn = tk.Button(master=memberFrame, text="Display Member", width=15,
                               command=partial(displayItem, type(Member()), memberData, memberFrame))
displayMemberBtn.grid(row=6, column=2, pady=(PADDING_Y, PADDING_Y))
"""
tk.Label(text="New Book: ").pack()
tk.Label(text="Name: ").pack()
tk.Entry(width=100).pack()
tk.Label(text="ISBN: ").pack()
tk.Entry(width=100).pack()
tk.Label(text="Author: ").pack()
tk.Entry(width=100).pack()
tk.Label(text="Publication Date: ").pack()
tk.Entry(width=100).pack()
tk.Label(text="Publisher: ").pack()
tk.Entry(width=100).pack()
tk.Label(text="Pages Number: ").pack()
tk.Entry(width=100).pack()
tk.Label(text="Cover Type: ").pack()
tk.Entry(width=100).pack()
tk.Button(text="Add Book", width=15).pack()

tk.Label(text="New Borrower: ").pack()
tk.Label(text="ID: ").pack()
tk.Entry(width=100).pack()
tk.Label(text="Name: ").pack()
tk.Entry(width=100).pack()
tk.Label(text="Address: ").pack()
tk.Entry(width=100).pack()
tk.Label(text="ISBN: ").pack()
tk.Entry(width=100).pack()
tk.Label(text="Borrow Date: ").pack()
tk.Entry(width=100).pack()
tk.Label(text="Return Date: ").pack()
tk.Entry(width=100).pack()
tk.Button(text="Add Borrower", width=15).pack()
"""

window.mainloop()
