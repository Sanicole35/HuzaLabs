# -*- coding: utf-8 -*-
"""Assignment Review (In-class practice).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fiz-QO4giDV2PqvdnaHRzt1ITke8a65z

## **Assignment Review**

## Alexianne

HW 1 PART A - QUESTION 1.
distance(x1, y1, x2, y2):
Write the function distance(x1, y1, x2, y2) that takes four int or float values x1, y1, x2, y2 that represent the two points (x1, y1) and (x2, y2), and returns the distance between those points as a float.
"""

import math
def distance(x1, y1, x2, y2):

  return math.sqrt((x2-x1)**2 + (y2-y1)**2)

distance(1,2,3,4)

"""## Agnes

HW1
PART B - QUESTION 9.
nearestOdd(n):
Write the function nearestOdd(n) that takes an int or float n, and returns as an int value the nearest odd number to n. In the case of a tie, return the smaller odd value. Note that the result must be an int, so nearestOdd(13.0) is the int 13, and not the float 13.0. Hint: Remember that the built-in round function works in surprising ways. Instead of round(n), you should use roundHalfUp(n) from this week's notes. That said, there are good ways to solve this problem without using rounding at all, if you prefer.
"""

def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    # You do not need to understand how this function works.
    import decimal
    rounding = decimal.ROUND_HALF_UP
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))


def nearestOdd(n):
  if int (n) ==n:
    if n%2 == 0:
      return int(n)-1
    else:
      return int(n)
  if roundHalfUp(n)%2 == 0:
    if roundHalfUp(n) > n:
      return roundHalfUp(n)-1
    else:
      return roundHalfUp(n)+1
  else:
    return roundHalfUp(n)

nearestOdd(9.8)

"""## Rosine

HW2
nthSmithNumber(n)
Write the function nthSmithNumber that takes a non-negative int n and returns the nth Smith number, where a Smith number is a composite (non-prime) the sum of whose digits are the sum of the digits of its prime factors (excluding 1). Note that if a prime number divides the Smith number multiple times, its digit sum is counted that many times. For example, 4 equals 2**2, so the prime factor 2 is counted twice, thus making 4 a Smith Number.
"""



"""## Aline

HW3
Library management System
(Mandatory section)

1. Book Class
Task: Create a Book class with attributes such as title, author, isbn, and availability.
Features:
The class should include a method to display book information.
Implement encapsulation by making availability a private attribute with getter and
setter methods to access and update its value.

2. Library Class
Task: Design a Library class that manages a collection of books.
Features:
Store books in a list.
Add methods to add a book, remove a book, and list all books.
Include a method to search for a book by title or author.

3. Borrowing System
Task: Enhance the Library class with a borrowing system.
Features:
Add methods to check out a book and return a book. Checking out a book should update the book’s
availability.
Include error checking to prevent checking out a book that is not available.

4. User Interaction
Task: Implement a simple text-based user interface (UI) that allows interacting with the library system
through the console.
Features:
Users should be able to add books, list all books, borrow a book, and return a book through input
prompts.
The UI should provide clear instructions and feedback based on user actions.


5. Inheritance - Extending the System

Task: Introduce a DigitalBook class that inherits from the Book class.

Features:
Add specific attributes relevant to digital books, such as file_size or format (e.g., PDF,
ePub).

Override or extend methods as necessary to handle digital-specific features, such as a
method to download  the book, which could simulate downloading by printing a
message to the console.
"""



from inspect import isbuiltin
class Book():
  def __init__(self, title ,author, isbn):
    self.title =title
    self.author = author
    self.isbn =isbn
    self._availability = True

  def get_availability(self):
    return self._availability

  def set_availability(self,availability):
    self._availability =availability


class Library():
  def __init__ (self, ):
    self._books=[]

  def add_book(self, book):
    self._books.append(book)

  def rent_book(self, title):
    for book in self._books:
      if book.title ==title and book.get_availability() == True:
        book.set_availability(False)
        return book

    print('This book is not available!')

book1= Book('rich dad poor dad','Robert','isbn-02')
book2= Book('my name is life','carine','isbn-03')
ikirezi_library=Library()

ikirezi_library.add_book(book1)
ikirezi_library.add_book(book2)

ikirezi_library.rent_book('my name is life')

print(book1.get_availability())
print(book2.get_availability())