import json
import uuid
from datetime import datetime, timedelta

class User:
    def __init__(self, users_file, books_file):
        self.users_file = users_file
        self.books_file = books_file
        with open('/home/b-121/Documents/python lsm project/users.json', 'r') as file:
                self.users = json.load(file)
        with open('/home/b-121/Documents/python lsm project/books.json', 'r') as file:
                self.books = json.load(file)
        # self.users = self.load_data(self.users_file)
        # self.books = self.load_data(self.books_file)
        self.current_user = None
    #Load data from JSON files
    
    def load_data(self, file_name):
        try:
            with open(file_name, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            data = {}
        return data#

    # Save data to JSON files
    def save_data(self):
        with open(self.users_file, 'w') as users_file:
            json.dump(self.users, users_file, indent=4)
        with open(self.books_file, 'w') as books_file:
            json.dump(self.books, books_file, indent=4)


    # User signup method
    def signup(self, username):
        user_id = str(len(self.users["users"]) + 1)
        token = str(uuid.uuid4())
        user_data = {
            "username": username,
            "token": token,  # Add the token to the user data
            "books_borrowed": {},
            "fines": 0
        }
        
        self.users["users"][user_id] = user_data
        self.save_data()
        print(f"User '{username}' created successfully.")
        print("Your user ID is:", user_id, "and your token is:", token)
        
   

    def login(self, user_id, token):
        if user_id in self.users["users"] and self.users["users"][user_id]["token"] == token:
            self.current_user = user_id
            print("Login successful. Welcome,", self.users["users"][user_id]["username"])
            return True
        else:
            print("Invalid user ID or token. Please try again.")
            return False
        
    def borrow_book(self):
        view_books = input("Do you want to view available books first? (yes/no): ").lower()
        if view_books == 'yes':
            self.display_available_books()
        book_id_or_title = input("Enter book ID or title to borrow:").strip()
        if self.current_user:
            if book_id_or_title.isdigit():
                book_id = book_id_or_title
                if book_id in self.books and self.books[book_id]["available"] > 0:
                    current_date = datetime.now().strftime('%Y-%m-%d')
                    due_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
                    borrowed_book_info = {
                        "title": self.books[book_id]["title"],
                        "author": self.books[book_id]["author"],
                        "borrowed_date": current_date,
                        "due_date": due_date
                    }
                    # Update count of the same book in the user's borrowed books
                    if book_id in self.users["users"][self.current_user]["books_borrowed"]:
                        self.users["users"][self.current_user]["books_borrowed"][book_id]["count"] += 1
                    else:
                        borrowed_book_info["count"] = 1
                        self.users["users"][self.current_user]["books_borrowed"][str(book_id)] = borrowed_book_info

                    self.books[book_id]["available"] -= 1
                    print("Book borrowed successfully. Due date:", due_date)
                    self.save_data()
                else:
                    print("Book not available for borrowing.")
            else:
                found_books = []
                for book_id, book_info in self.books.items():
                    if book_info["title"].lower() == book_id_or_title.lower() and book_info["available"] > 0:
                        found_books.append(book_id)

                if found_books:
                    book_id = found_books[0]
                    current_date = datetime.now().strftime('%Y-%m-%d')
                    due_date = (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d')
                    borrowed_book_info = {
                        "title": self.books[book_id]["title"],
                        "author": self.books[book_id]["author"],
                        "borrowed_date": current_date,
                        "due_date": due_date,
                        "count": 1
                    }
                    self.users["users"][self.current_user]["books_borrowed"][str(book_id)] = borrowed_book_info
                    self.books[book_id]["available"] -= 1
                    print("Book borrowed successfully. Due date:", due_date)
                    self.save_data()
                else:
                    print("Book not available for borrowing or not found.")
        else:
            print("Please login to borrow a book.")

    def display_available_books(self):
        print("Available Books:")
        for book_id, book_info in self.books.items():
            if book_info["available"] > 0:
                print(f"Book ID: {book_id}, Title: {book_info['title']}, Author: {book_info['author']}")


    def return_book(self):
        view_borrowed_books = input("Do you want to view borrowed books first? (yes/no): ").lower()
        if view_borrowed_books== 'yes':
            self.view_borrowed_books()  # Display borrowed books
        book_id = input("Enter book ID to return: ")
        if book_id in self.users["users"][self.current_user]["books_borrowed"]:
            due_date = datetime.strptime(self.users["users"][self.current_user]["books_borrowed"][book_id]["due_date"], '%Y-%m-%d')
            current_date = datetime.now()
            num_copies = int(input("Enter the number of copies to return: "))
            if num_copies > self.users["users"][self.current_user]["books_borrowed"][book_id]["count"]:
                print("Invalid number of copies. Please try again.")
                return
            self.users["users"][self.current_user]["books_borrowed"][book_id]["count"] -= num_copies
            self.books[book_id]["available"] += num_copies

            if self.users["users"][self.current_user]["books_borrowed"][book_id]["count"] == 0:
                del self.users["users"][self.current_user]["books_borrowed"][book_id]
            
            # Calculate fine for overdue book
            if current_date > due_date:
                days_overdue = (current_date - due_date).days
                fine = days_overdue * 5  # Assuming a fine of 5 units per day overdue
                self.users["users"][self.current_user]["fines"] += fine
                print(f"Book returned successfully with a fine of {fine} units.")
            else:
                print("Book returned successfully.")
            
            self.save_data()
        else:
            print("Invalid book ID or book not borrowed by the current user.")

    # def view_all_users_information(self, admin_password):
    #     entered_password = input("Enter admin password: ")
    #     if entered_password == admin_password:
    #         print("All User Information:")
    #         for user_id, user_info in self.users["users"].items():
    #             self._print_user_info(user_id, user_info)
    #     else:
    #         print("Incorrect admin password. Permission denied.")

    # def _print_user_info(self, user_id, user_info):
    #     username = user_info.get('username', 'N/A')
    #     token = user_info.get('token', 'N/A')
    #     fines = user_info.get('fines', 0)
    #     books_borrowed = user_info.get('books_borrowed', {})
    #     print(f"User ID: {user_id}, Username: {username}, Token: {token}, Fines: {fines}")
    #     print("Books Borrowed:")
    #     for book_id, book_info in books_borrowed.items():
    #         title = book_info.get('title', 'N/A')
    #         author = book_info.get('author', 'N/A')
    #         borrowed_date = book_info.get('borrowed_date', 'N/A')
    #         due_date = book_info.get('due_date', 'N/A')
    #         count = book_info.get('count', 0)
    #         print(f"Book ID: {book_id}, Title: {title}, Author: {author}, Borrowed Date: {borrowed_date}, Due Date: {due_date}, Count: {count}")


    def view_borrowed_books(self):
        if self.current_user:
            borrowed_books = self.users["users"][self.current_user]["books_borrowed"]
            if borrowed_books:
                print("Borrowed Books:")
                for book_id, book_info in borrowed_books.items():
                    title = book_info.get('title', 'N/A')
                    author = book_info.get('author', 'N/A')
                    borrowed_date = book_info.get('borrowed_date', 'N/A')
                    due_date = book_info.get('due_date', 'N/A')
                    count = book_info.get('count', 0)
                    print(f"Book ID: {book_id}, Title: {title}, Author: {author}, Borrowed Date: {borrowed_date}, Due Date: {due_date}, Count: {count}")
            else:
                print("No books currently borrowed.")
        else:
            print("Please login to view borrowed books.")


            
    