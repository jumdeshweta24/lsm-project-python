# class Book:
#     def __init__(self, title, author, copies):
#         self.title = title
#         self.author = author
#         self.copies = copies
#         self.available = copies

#     def borrow_book(self):
#         if self.available > 0:
#             self.available -= 1
#             print(f"Book '{self.title}' borrowed successfully.")
#             return True
#         else:
#             print(f"Sorry, '{self.title}' is currently unavailable.")
#             return False
        

#     def return_book(self):
#         if self.available < self.copies:
#             self.available += 1
#             print(f"Book '{self.title}' returned successfully.")
#             return True
#         else:
#             print(f"Invalid operation. '{self.title}' has already been returned.")
#             return False

#     def get_book_info(self):
#         return f"Title: {self.title}, Author: {self.author}, Available Copies: {self.available}/{self.copies}"

# Example usage:
# book = Book("Sample Book", "John Doe", 3)
# book.borrow_book()
# book.return_book()
# print(book.get_book_info())


