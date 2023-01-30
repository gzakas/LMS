from create import *

while True:
    choice = user_choice_menu()
    if choice == "0" or choice == "":
        break
    elif choice == "1":
        new_publisher_from_input()
    elif choice == "2":
        add_author_from_input()
    elif choice == "3":
        add_book_from_input()
    elif choice == "4":
        register_customer_from_input()
    elif choice == "5":
        assign_loan_from_input()
    elif choice == "6":
        customer_returns_from_input()
    elif choice == "7":
        check_active_loans()
    elif choice == '8':
        search_from_input()
    elif choice == '9':
        new_librarian_from_input()