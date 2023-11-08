from admin import Admin
from User import User
#import Book
def main():
    admin_name = "admin"
    admin_password = "admin123"
    admin = Admin(admin_name, admin_password)

    users_file = "/home/b-121/Documents/python lsm project/users.json"
    books_file = "/home/b-121/Documents/python lsm project/books.json"
    user_manager = User("/home/b-121/Documents/python lsm project/users.json", "/home/b-121/Documents/python lsm project/books.json")
    books = user_manager.books  # Get the books data from user_manager

    print("\t\t\t\t Welcome to the Library Management System...!")
    print("1. Admin")
    print("2. User")
    user_type = input("Select user type: ")

    if user_type == "1":
        admin_name_input = input("Enter admin name: ")
        admin_password_input = input("Enter admin password: ")
        if admin.authenticate(admin_name_input, admin_password_input):
            print("Admin authenticated successfully.")
            while True:
                print("1. Add Book")
                print("2. View Books")
                print("3. Update Book Information")
                print("4. Remove Book")
                print("5. Create User Account")
                print("6. View User Information")
                # print("7. Handle Fine")
                # print("8. Generate Overdue Report")
                print("9. Exit")
                admin_choice = input("Select option: ")
                if admin_choice == "1":
                    title = input("Enter book title: ")
                    author = input("Enter book author: ")
                    copies = int(input("Enter number of copies: "))
                    genre=input("Please enter the genre of the book (e.g., Fiction, Mystery, Science Fiction): ")
                    admin.add_book(title, author, copies,genre)

                elif admin_choice == "2":
                    admin.display_books()
                    
                elif admin_choice == "3":
                    admin.update_book()
                    
                elif admin_choice=='4':
                    admin.remove()
                    
                elif admin_choice=='5':
                    username = input("Enter Username: ")
                    #password = input("Enter your password: ")
                    user_manager.signup(username)
                elif admin_choice=='6':
                    #admin.view_all_users_information(admin_password) 
                    admin.view_all_users_information()
                elif admin_choice == "9":
                    print("Exiting Admin Panel.")
                    break
                else:
                    print("Invalid choice. Please try again.")

        else:
            print("Invalid admin credentials. Access denied.")

    elif user_type == "2":
        print("1. Login")
        print("2. Sign Up")
        print("3. Exit")
        user_choice = input("Select option: ")

        if user_choice == "1":
            user_id = str(input("Enter your user ID: "))
            token = input("Enter your token: ")
            if user_manager.login(user_id, token):
               
                while True:
                    print("1. Borrow Book")
                    print("2. Return Book")
                    print("3. View Borrowed Books")
                    print("4. Logout")
                    user_option = input("Select option: ")

                    if user_option == "1":
                       # book_id_or_title = input("Enter book ID or title to borrow: ")
                        user_manager.borrow_book()
                    elif user_option == "2":
                       # book_id = input("Enter book ID to return: ")
                        user_manager.return_book()
                    elif user_option == "3":
                        user_manager.display_available_books()
                        user_manager.view_borrowed_books()
                    elif user_option == "4":
                        print("Logging out...")
                        break
                    else:
                        print("Invalid option. Please try again.")

            else:
                print("Invalid user ID or password. Please try again.")

        elif user_choice == "2":
            username = input("Enter your username: ").strip()
            user_manager.signup(username)
            # Implement user functionalities (borrow books, return book\]\\6, etc.)
            while True:
                print("1. Borrow Book")
                print("2. Return Book")
                print("3. View Borrowed Books")
                print("4. Logout")
                user_option = input("Select option: ")

                if user_option == "1":
                    user_manager.borrow_book()
                elif user_option == "2":
                   # book_id = input("Enter book ID to return: ")
                    user_manager.return_book()
                elif user_option == "3":
                    user_manager.view_borrowed_books()
                elif user_option == "4":
                    print("Sign out...")
                    break
                else:
                    print("Invalid option. Please try again.")
               
        elif user_choice=="3":
            print("Existing the Library Manegement System.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
