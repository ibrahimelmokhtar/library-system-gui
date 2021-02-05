import tkinter as tk
from manageJsonFile import *
from functools import partial   # to pass function parameters within "command" in tkinter.Entry()

# create window:
window = tk.Tk()
ENTRY_WIDTH = 80
PADDING_Y = 10
PADDING_X = 10

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

# members' buttons:
addMemberBtn = tk.Button(master=memberFrame, text="Add Member", width=15,
                               command=partial(addObject, Member(), memberData, memberFrame))
addMemberBtn.grid(row=5, column=1, pady=(PADDING_Y, 0))

window.mainloop()
