from manageJsonFile import *

"""
# add objects:

addObject(Member("14p8195", "Ibrahim El-Mokhtar", "Cairo, Egypt"))
addObject(Member("14p9090", "Mohamed Adel", "Cairo, Egypt"))
addObject(Member("14p9702", "Amir Eid", "Cairo, Egypt"))

addObject(Book("The Hunger Games", "0439023483",
               "Suzanne Collins", datetime.datetime(2008, 9, 14).date(),
               "Scholastic Press", 374, "Hardcover"))

addObject(Borrower("14p9090", "Mohamed Adel", "Cairo, Egypt", "0439023483",
                   datetime.datetime(2020, 10, 14).date(),
                   datetime.datetime(2020, 11, 7).date()))

addObject(Book("Harry Potter and the Order of the Phoenix", "0439358078",
               "J.K. Rowling", datetime.datetime(2003, 6, 21).date(),
               "Scholastic Inc.", 870, "Paperback"))

addObject(Book("Animal Farm", "0451526341",
               "George Orwell", datetime.datetime(1945, 8, 17).date(),
               "Signet Classics", 141, "Mass Market Paperback"))

addObject(Book("The Da Vinci Code", "None",
               "Dan Brown", datetime.datetime(2003, 3, 18).date(),
               "Anchor", 489, "Paperback"))

addObject(Borrower("14p8195", "Ibrahim El-Mokhtar", "Cairo, Egypt", "0439358078",
                   datetime.datetime(2021, 1, 10).date(),
                   datetime.datetime(2021, 2, 12).date()))
"""

"""
# search objects:

# search member by ID:  (exists)
person = searchPerson("14p8195")
# search member by ID:  (does NOT exist)
person = searchPerson("14p0000")

# search borrower by ID:    (exists)
person = searchPerson("14p9090")
# search borrower by ID:    (does NOT exist)
person = searchPerson("14p9702")

# search member by name:    (exists)
person = searchPerson("Ibrahim El-Mokhtar", isName=True)
# search borrower by name:  (does NOT exist)
person = searchPerson("Amir Eid", isName=True)

# search book by name:  (exists)
searchBook("The Hunger Games", isName=True)
# search book by name:  (does NOT exist)
searchBook("Harry Potter", isName=True)
# search book by ISBN   (exists)
searchBook("0451526341")
# search book by ISBN   (does NOT exist)
searchBook("1400096898")
"""

# display full lists:
print("Members' list:")
count = displayFullList(type(Member()))
print("Total: {} items\n\n".format(count))

print("Books' list:")
count = displayFullList(type(Book()))
print("Total: {} items\n\n".format(count))

print("Borrowers' list:")
count = displayFullList(type(Borrower()))
print("Total: {} items\n\n".format(count))
