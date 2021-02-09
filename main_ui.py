import tkinter as tk
from ui_createMainFrames import *

# create window:
window = tk.Tk()

# start window at full screen size:
window_width = window.winfo_screenwidth()
window_height = window.winfo_screenheight()
window.geometry("%dx%d" % (window_width, window_height))
window.title("Library Management System")

# create members' frame:
createMembersFrame(window)

# create books' frame:
createBooksFrame(window)

# create borrowers' frame:
createBorrowersFrame(window)

# enter main loop:
window.mainloop()
