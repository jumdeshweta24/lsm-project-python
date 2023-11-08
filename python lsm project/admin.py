import json
from User import User
class Admin:
    def __init__(self, admin_name, password,user_manager=None):
        self.admin_name = admin_name
        self.password = password
        self.user_manager = user_manager
        with open('/home/b-121/Documents/python lsm project/users.json', 'r') as file:
                self.users = json.load(file)
        with open('/home/b-121/Documents/python lsm project/books.json', 'r') as file:
                self.books = json.load(file)
       #users_file='/home/b-121/Documents/python lsm project/users.json'
               
    def save_books(self):
        try:
            with open('/home/b-121/Documents/python lsm project/books.json', 'w') as file:
                json.dump(self.books, file, indent = 4)
            print("Books successfully saved.")
        except Exception as e:
            print(f"Error saving books: {e}")
            
    def authenticate(self, admin_name, password):
        return self.admin_name == admin_name and self.password == password

    def add_book(self, title, author, copies, genre):
        book_id = str(len(self.books) + 1)
        self.books[book_id] = {
            "title": title,
            "author": author,
            "copies": copies,
            "available": copies,
            "genre": genre
        }
        print(f"Book '{title}' added successfully with ID: {book_id}")
        self.save_books()
        
        
    def update_book(self):
        #print(f"Updating book ID: {book_id}, Field: {field}, New Value: {new_value}")
        self.display_books()
        book_id = input("Enter book id you want to update: ").strip()
        if book_id in self.books:
            field_to_update = input("Enter field to update (title, author, copies, genre): ").lower()
            new_value = input("Enter new value: ")
            if field_to_update in self.books[book_id]:
                self.books[book_id][field_to_update]=new_value 
                print(f"Book ID {book_id} : {field_to_update} Update to {new_value}.")
                self.save_books()
            else:
               print("Invalid field. Allowed fields: 'title', 'author', 'copies', 'genre'")
        else:
            print("Invalid book ID. Please try again.")
        
          
    def remove(self):
        self.display_books()
        book_id=input("Enter book id you want to Remove").strip()
        if book_id in self.books:
            del self.books[book_id]
            print(f"Book ID {book_id} Remove Succesfully")
            self.save_books()
        else:
            print("Book Not Found")
    def display_books(self):
        print("Available Books:")
        for book_id, book in self.books.items():
            print(f"Book ID: {book_id}, Title: {book['title']}, Author: {book['author']},Copies :{book['copies']}, Available : {book['available']}, Genre: {book['genre']}")
     
    def  view_all_users_information(self):
        print("All User Information:")
        for user_id, user_info in self.users["users"].items():
                #print(f"User ID: {user_id}, Username: {user_info['username']}, Token: {user_info['token']}, Fines: {user_info['fines']}")
                username = user_info.get('username', 'N/A')
                token = user_info.get('token', 'N/A')
                fines = user_info.get('fines', 0)
                books_borrowed = user_info.get('books_borrowed', {})
                print(f"User ID: {user_id}, Username: {username}, Token: {token}, Fines: {fines}")
               
                                    
        # for book_id, book_info in books_borrowed.items():
        #     title = book_info.get('title', 'N/A')
        #     author = book_info.get('author', 'N/A')
        #     borrowed_date = book_info.get('borrowed_date', 'N/A')
        #     due_date = book_info.get('due_date', 'N/A')
        #     count = book_info.get('count', 0)
        #     print(f"Book ID: {book_id}, Title: {title}, Author: {author}, Borrowed Date: {borrowed_date}, Due Date: {due_date}, Count: {count}")
        # # entered_password = input("Enter admin password: ")
        # # if entered_password == admin_password:
        # #     print("All User Information:")
        # #     self.user_manager.view_all_users_information(admin_password)
        # # else:
        # #     print("Incorrect admin password. Permission denied.")




# Example usage
admin1 = Admin("admin1", "admin123")
# import json
# from datetime import datetime

# class Admin:
#     def __init__(self, admin_name, password):
#         self.admin_name = admin_name
#         self.password = password
#         self.load_books()
#         self.load_users()

#     def load_books(self):
#         try:
#             with open('books.json', 'r') as file:
#                 self.books = json.load(file)
#         except FileNotFoundError:
#             self.books = {}

#     def load_users(self):
#         try:
#             with open('users.json', 'r') as file:
#                 self.users = json.load(file)
#         except FileNotFoundError:
#             self.users = {}

#     def save_books(self):
#         with open('books.json', 'w') as file:
#             json.dump(self.books, file)

#     def save_users(self):
#         with open('users.json', 'w') as file:
#             json.dump(self.users, file)

#     def authenticate(self, admin_name, password):
#         return self.admin_name == admin_name and self.password == password
    
#     def display_books(self,books):
#         print("Available Books:")
#         for book_id, book in self.books.items():
#             print(f"Book ID: {book_id}, Title: {book['title']}, Author: {book['author']}, Available Copies: {book['available']}, Rent: {book['rent']}, Genre: {book['genre']}")

#     def add_book(self, title, author, copies, rent, genre):
#         book_id = str(len(self.books) + 1)
#         self.books[book_id] = {
#             "title": title,
#             "author": author,
#             "copies": copies,
#             "available": copies,
#             "rent": rent,
#             "genre": genre
#         }
#         print(f"Book '{title}' added successfully with ID: {book_id}")
#         self.save_books()

#     def remove_book(self, book_id):
#         if book_id in self.books:
#             del self.books[book_id]
#             print(f"Book with ID {book_id} removed successfully.")
#             self.save_books()
#         else:
#             print("Book not found.")

#     def update_book(self, book_id, field, new_value):
#         if book_id in self.books:
#             if field in self.books[book_id]:
#                 self.books[book_id][field] = new_value
#                 print(f"Book ID {book_id}: {field} updated to {new_value}.")
#                 self.save_books()
#             else:
#                 print("Invalid field.")
#         else:
#             print("Book not found.")

#     def view_books(self,books):
#         print("Available Books:")
#         for book_id, book in self.books.items():
#             print(f"Book ID: {book_id}, Title: {book['title']}, Author: {book['author']}, Available Copies: {book['available']}, Rent: {book['rent']}, Genre: {book['genre']}")

#     def create_user_account(self, username, password):
#         user_id = str(len(self.users) + 1)
#         self.users[user_id] = {
#             "username": username,
#             "password": password,
#             "borrowed_books": {},
#             "fines": 0
#         }
#         print(f"User '{username}' created successfully with ID: {user_id}")
#         self.save_users()

#     def view_user_info(self, user_id):
#         if user_id in self.users:
#             user_info = self.users[user_id]
#             print(f"User ID: {user_id}, Username: {user_info['username']}, Borrowed Books: {user_info['borrowed_books']}, Fines: {user_info['fines']}")
#         else:
#             print("User not found.")

#     def handle_fine(self, user_id, fine_amount):
#         if user_id in self.users:
#             self.users[user_id]['fines'] += fine_amount
#             print(f"Fine of {fine_amount} added to User ID: {user_id}.")
#             self.save_users()
#         else:
#             print("User not found.")

#     def generate_overdue_report(self):
#         today = datetime.now()
#         print("Overdue Books:")
#         for book_id, book in self.books.items():
#             due_date = datetime.strptime(book.get("due_date", ""), "%Y-%m-%d")
#             if due_date and due_date < today:
#                 print(f"Book ID: {book_id}, Title: {book['title']}, Due Date: {due_date.strftime('%Y-%m-%d')}")

# # Example usage
# admin1 = Admin("admin1", "admin123")

# while True:
#     print("1. Add Book")
#     print("2. Remove Book")
#     print("3. Update Book Information")
#     print("4. View Books")
#     print("5. Create User Account")
#     print("6. View User Information")
#     print("7. Handle Fine")
#     print("8. Generate Overdue Report")
#     print("9. Display Books")
#     print("10. Exit")
#     choice = input("Select option: ")

#     if choice == '1':
#         title = input("Enter book title: ")
#         author = input("Enter author name: ")
#         copies = int(input("Enter number of copies: "))
#         rent = float(input("Enter rent price: "))
#         genre = input("Enter genre: ")
#         admin1.add_book(title, author, copies, rent, genre)

#     elif choice == '2':
#         book_id = input("Enter Book ID to remove: ")
#         admin1.remove_book(book_id)

#     elif choice == '3':
#         book_id = input("Enter Book ID to update: ")
#         field = input("Enter field to update (title, author, copies, rent, genre): ")
#         new_value = input("Enter new value: ")
#         admin1.update_book(book_id, field, new_value)

#     elif choice == '4':
#         admin1.view_books(books)

#     elif choice == '5':
#         username = input("Enter username: ")
#         password = input("Enter password: ")
#         admin1.create_user_account(username, password)

#     elif choice == '6':
#         user_id = input("Enter User ID to view info: ")
#         admin1.view_user_info(user_id)

#     elif choice == '7':
#         user_id = input("Enter User ID to handle fine: ")
#         fine_amount = float(input("Enter fine amount: "))
#         admin1.handle_fine(user_id, fine_amount)

#     elif choice == '8':
#         admin1.generate_overdue_report()


#     elif choice == '9':
#         admin1.save_books()  # Save books before exiting
#         admin1.save_users()  # Save users before exiting
#         print("Exiting the program.")
#         break

#     else:
#         print("Invalid choice. Please try again.")

