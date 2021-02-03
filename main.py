from Book import *
from Member import *
from Borrower import *

borrow_date = datetime.datetime(2020, 11, 7).date()
return_date = datetime.datetime(2021, 1, 7).date()

b1 = Borrower("14p8195", "Ibrahim", "Cairo, Egypt", "12345", borrow_date, return_date)
print(b1)
