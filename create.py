from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_, and_
from model import Author, Publisher, Book, Customer, Librarian, Loan, engine
import datetime
import os

Session = sessionmaker(bind=engine)
session = Session()

def user_choice_menu():
    print("------ [ Library Admin Menu ] -------")
    print("1| Add a new publisher")
    print("2| Add a new author")
    print("3| Add a new book")
    print("4| Register a new customer")
    print("5| Assign a new loan")
    print("6| Customers returns")
    print("7| Check active loans")
    print("8| Search")
    print("9| Add a new librarian")
    print("0| Exit the program")

    choice = input("What's your choice?: ")
    return choice

def clear():
    os.system("cls")

def add_book(book_name, book_isbn, authors, publishers):
    book = Book(book_name, book_isbn, authors, publishers)
    session.add(book)
    session.commit()
    return book

def add_book_from_input():
    clear()
    authors_list = [0]
    publishers_list = [0]
    while True:
        print("0 | Back to Menu")
        book_name = input("Name of the book: ")
        clear()
        if book_name == "0":
            return
        while True:
            try:
                print("0 | Back to Menu")
                book_isbn = input("Books ISBN code: ")
                book_isbn = int(book_isbn)
                clear()
                if book_isbn == 0:
                    return
                break
            except ValueError:
                clear()
                print("Error: Books ISBN must be a number!")
        while True:
            try:
                print("0 | Back to Menu")
                author_list = session.query(Author)
                for tries in author_list:
                    print(f"{tries.author_id} | {tries}") 
                    authors_list.append(tries.author_id)   
                authors = input("Authors ID: ")
                authors = int(authors)
                clear()
                if authors not in authors_list:
                    clear()
                    print("Error: Author with that ID was not found")
                    continue
                if authors == 0:
                    return
                break
            except ValueError:
                clear()
                print("Error: Authors ID must be a number!")
        while True:
            try:
                print("0 | Back to Menu")
                publisher_list = session.query(Publisher)
                for tries in publisher_list:
                    print(f"{tries.publisher_id} | {tries.publisher_name}")
                    publishers_list.append(tries.publisher_id)
                publishers = input("Publishers ID: ")
                publishers = int(publishers)
                clear()
                if publishers not in publishers_list:
                    clear()
                    print("Error: Publisher with that ID was not found")
                    continue
                if publishers == 0:
                    return
                break
            except ValueError:
                clear()
                print("Error: Publishers ID must be a number!")
        add_book(book_name, book_isbn, authors, publishers)
        user_choice = input("Do you want to add another book? (yes/no): ")
        if user_choice.lower() == "no":
            break
        elif user_choice.lower() == "yes":
            continue
        else:
            print("This input wasn't an option... I'll take it as a 'no' then")
            break
def add_author(author_name, author_surname):
    authors = Author(author_name, author_surname)
    session.add(authors)
    session.commit()
    return authors

def add_author_from_input():
    clear()
    while True:
        print("0 | Back to Menu")
        author_name = input("Name of the author: ")
        if author_name == "":
            print("This field can't be empty!")
            continue
        elif author_name == "0":
            clear()
            return
        clear()
        break
    while True:
        print("0 | Back to Menu")
        author_surname = input("Surname of the author: ")
        if author_surname == "":
            print("This field can't be empty!")
            continue
        if author_surname == "0":
            clear()
            return
        clear()
        add_author(author_name, author_surname)
        print("Author was added successfully")
        break
    while True:
        user_choice = input("Do you want to add another author? (yes/no): ")
        if user_choice.lower() == "no":
            break
        elif user_choice.lower() == "yes":
            add_author_from_input()
        else:
            print("Your input wasn't an option... I'll take it as a 'no' then")
            break
        

def register_customer(customer_name, customer_surname, customer_address):
    customers = Customer(customer_name, customer_surname, customer_address)
    session.add(customers)
    session.commit()
    return customers

def register_customer_from_input():
    clear()
    while True:
        print("0 | Back to Menu")
        customer_name = input("Customers name: ")
        if customer_name == "":
            clear()
            print("This field can't be empty!")
            continue
        if customer_name == "0":
            clear()
            return
        clear()
        break
    while True:
        print("0 | Back to Menu")
        customer_surname = input("Customers surname: ")
        if customer_surname == "":
            clear()
            print("This field can't be empty!")
            continue
        if customer_surname == "0":
            clear()
            return
        clear()
        break
    while True:
        print("0 | Back to Menu")
        customer_address = input("Customers address: ")
        if customer_address == "":
            clear()
            print("This field can't be empty!")
            continue
        if customer_address == "0":
            clear()
            return
        clear()
        print("Customer was added successfully")
        register_customer(customer_name, customer_surname, customer_address)
        user_choice = input("Do you want to add another book? (yes/no): ")
        if user_choice.lower() == "no":
            break
        elif user_choice.lower() == "yes":
            continue
        else:
            print("This input wasn't an option... I'll take it as a 'no' then")
            break

def new_librarian(librarian_name, librarian_surname):
    librarians = Librarian(librarian_name, librarian_surname)
    session.add(librarians)
    session.commit()
    return librarians

def new_librarian_from_input():
    clear()
    while True:
        print("0 | Back to Menu")
        librarian_name = input("Librarians name: ")
        if librarian_name == "":
            print("This field can't be empty!")
            continue
        if librarian_name == "0":
            clear()
            return
        clear()
        break
    while True:
        print("0 | Back to Menu")
        librarian_surname = input("Librarians surname: ")
        if librarian_surname == "":
            print("This field can't be empty!")
            continue
        if librarian_surname == "0":
            clear()
            return
        clear()
        new_librarian(librarian_name, librarian_surname)
        print("Librarian was added successfully")
        break
    while True:
        user_choice = input("Do you want to add another librarian? (yes/no): ")
        if user_choice.lower() == "no":
            break
        elif user_choice.lower() == "yes":
            add_author_from_input()
        else:
            print("Your input wasn't an option... I'll take it as a 'no' then")
            break

def new_publisher(publisher_name):
    publishers = Publisher(publisher_name)
    session.add(publishers)
    session.commit()
    return publishers

def new_publisher_from_input():
    clear()
    while True:
        print("0 | Back to Menu")
        publisher_name = input("Publishers name: ")
        if publisher_name == "":
            print("This field can't be empty!")
            continue
        if publisher_name == "0":
            clear()
            return
        clear()
        new_publisher(publisher_name)
        print("Publisher was added successfully")
        break
    while True:
        user_choice = input("Do you want to add another publisher? (yes/no): ")
        if user_choice.lower() == "no":
            break
        elif user_choice.lower() == "yes":
            new_publisher_from_input()
        else:
            print("Your input wasn't an option... I'll take it as a 'no' then")
            break

def assign_loan(loan_date, loan_active, customer_id, book_id, librarian_id):
    loans = Loan(loan_date, loan_active, customer_id, book_id, librarian_id)
    session.add(loans)
    session.commit()
    return loans

def assign_loan_from_input():
    clear()
    loan_date = datetime.datetime.now().date()
    loan_active = True
    customer_ids = [0]
    while True:
        try:
            customer_list = session.query(Customer)
            for tries in customer_list:
                print(f"{tries.customer_id} | {tries.customer_name} {tries.customer_surname}")
                customer_ids.append(tries.customer_id)
            print("0 | Back to Menu")
            customer_id = input("Enter customers ID: ")
            customer_id = int(customer_id)
            clear()
            if customer_id not in customer_ids:
                clear()
                print("Error: Customer with that ID was not found")
                continue
            break
        except ValueError:
            clear()
            print("Error: Customer ID must be a number!")
    if customer_id == 0:
        return

    while True:
        books_list = [0]
        try:
            book_list = session.query(Book).filter(~session.query(Loan).filter(and_(Loan.book_id == Book.book_id, Loan.loan_active == True)).exists()).all()
            for tries in book_list:
                print(f"{tries.book_id} | {tries.book_name}")
                books_list.append(tries.book_id)
            print("0 | Back to Menu")
            book_id = input("Enter books ID: ")
            book_id = int(book_id)
            clear()
            if book_id not in books_list:
                clear()
                print("Error: Book with that ID was not found")
                continue
            break
        except ValueError:
            clear()
            print("Error: Book ID must be a number!")
    if book_id == 0:
        return

    while True:
        librarians_list = [0]
        try:
            librarian_list = session.query(Librarian)
            for tries in librarian_list:
                print(f"{tries.librarian_id} | {tries.librarian_name} {tries.librarian_surname}")
                librarians_list.append(tries.librarian_id)
            print("0 | Back to Menu")
            librarian_id = input("Enter librarians ID: ")
            librarian_id = int(librarian_id)
            clear()
            if librarian_id not in librarians_list:
                clear()
                print("Error: Librarian with that ID was not found")
                continue
            break
        except ValueError:
            clear()
            print("Error: Librarian ID must be a number!")
    if librarian_id == 0:
        return
    print("Loan was successful!")
    return assign_loan(loan_date, loan_active, customer_id, book_id, librarian_id)

def check_active_loans(query=session.query(Loan)):
    clear()
    query = session.query(Book, Loan, Customer, Librarian)\
        .join(Loan, Book.book_id == Loan.book_id)\
        .join(Customer, Loan.customer_id == Customer.customer_id)\
        .join(Librarian, Loan.librarian_id == Librarian.librarian_id)\
            .filter(Loan.loan_active == True).all()
    if query:
        for x in query:
            print("Loan id: {}, Book id: {}, Book name: {}, Loaned at: {}, Customers name: {} {}, Librarian: {} {}".format(
                x.Loan.loan_id,
                x.Book.book_id,
                x.Book.book_name,
                x.Loan.loan_date,
                x.Customer.customer_name,
                x.Customer.customer_surname,
                x.Librarian.librarian_name,
                x.Librarian.librarian_surname
            ))
        input("Press Enter to continue...")
        clear()
    else:
        print("No books are currently loaned")
        input("Press Enter to continue...")
        clear()

def customer_returns(user_input):
    current_date = datetime.datetime.now().date()
    session.query(Loan).filter_by(book_id=user_input).update({Loan.return_date: current_date, Loan.loan_active: False})
    session.commit()

def customer_returns_from_input():
    clear()
    while True:
        try:
            all_loans = session.query(Loan).filter(Loan.loan_active != 0).all()
            for tries in all_loans:
                book = session.query(Book).get(tries.book_id)
                customer = session.query(Customer).get(tries.customer_id)
                print(f"Book id: {tries.book_id} | {book.book_name} | currently loaned to: {customer.customer_name} {customer.customer_surname}")
            print("0 | Back to Menu")
            user_input = input("Enter book ID which the customer returned: ")
            user_input = int(user_input)
            if user_input == 0:
                clear()
                return
            if not user_input:
                raise ValueError
            else:
                loan = session.query(Loan).filter(Loan.book_id == user_input, Loan.loan_active == True).first()
                if loan is None:
                    clear()
                    print("Error: Book with that ID is not loaned.")
                    continue
                clear()
                customer_returns(user_input)
                print("Book was returned successfully")
                break
        except ValueError:
            clear()
            print("Error: This field must be a number!")

def search(user_selection):
    clear()
    if user_selection == 1:
        value = input("Searching for: ")
        authors = session.query(Author).filter(or_(Author.author_name.ilike(f"%{value}%"), Author.author_surname.ilike(f"%{value}%"))).all()
        book_name_search = session.query(Book).filter(or_(and_(Book.book_name.ilike(f"%{value}%"), 
            ~session.query(Loan).filter(Loan.book_id == Book.book_id).exists()),
                and_(Book.book_name.ilike(f"%{value}%"), 
                    session.query(Loan).filter(Loan.book_id == Book.book_id, Loan.loan_active == 0).exists()))).all()
        publisher_name_search = session.query(Publisher).filter(Publisher.publisher_name.ilike(f"%{value}%")).all()
        loaned_check = session.query(Loan)\
            .filter(and_(Loan.loan_active == True,session.query(Book)\
            .filter(and_(Book.book_id == Loan.book_id, Book.book_name.ilike(f"%{value}%"))).exists()))
                
        for tries in authors:
            print(f"Author: {tries.author_name} {tries.author_surname}")
        for tries in book_name_search:
            print(f"Available book: {tries.book_id} {tries.book_name}")
        for tries in publisher_name_search:
            print(f"Publisher: {tries.publisher_name}")
        for tries in loaned_check:
            book = session.query(Book).get(tries.book_id)
            customer = session.query(Customer).get(tries.customer_id)
            librarian = session.query(Librarian).get(tries.librarian_id)
            print(f"Loaned book: ID: {book.book_id} {book.book_name}, by customer: {customer.customer_name} {customer.customer_surname}, assigned by librarian: {librarian.librarian_name} {librarian.librarian_surname}")
        input("Press Enter to continue...")
        clear()
    elif user_selection == 2:
        value = input("Searching in Authors for: ")
        authors = session.query(Author).filter(or_(Author.author_name.ilike(f"%{value}%"), Author.author_surname.ilike(f"%{value}%"))).all()
        for author in authors:
            print(f"{author.author_id}| {author.author_name} {author.author_surname}")
        input("Press Enter to continue...")
        clear()
    elif user_selection == 3:
        value = input("Searching in Books for: ")
        book_search = session.query(Book).filter(or_(and_(Book.book_name.ilike(f"%{value}%"), 
            ~session.query(Loan).filter(Loan.book_id == Book.book_id).exists()),and_(Book.book_name.ilike(f"%{value}%"), 
            session.query(Loan).filter(Loan.book_id == Book.book_id, Loan.loan_active == 0).exists()))).all()
        if book_search:
            for tries in book_search:
                print(f"Book ID: {tries.book_id} {tries.book_name}")
            input("Press Enter to continue...")
            clear()
        else:
            print("Found nothing")
            input("Press Enter to continue...")
            clear()
    elif user_selection == 4:
        value = input("Searching in Publishers for: ")
        publisher_search = session.query(Publisher).filter(Publisher.publisher_name.ilike(f"%{value}%")).all()
        if publisher_search:
            for tries in publisher_search:
                print(f"{tries.publisher_id}. {tries.publisher_name}")
            input("Press Enter to continue...")
            clear()
        else:
            print("Found nothing")
            input("Press Enter to continue...")
            clear()
    elif user_selection == 5:
        value = input("Searching in loaned books for: ")
        loan_search = session.query(Loan, Book, Customer)\
        .join(Book, Loan.book_id == Book.book_id)\
        .join(Customer, Loan.customer_id == Customer.customer_id)\
        .filter(Loan.loan_active==True)\
        .filter(Book.book_name.ilike(f"%{value}%"))\
        .all()
        if loan_search:
            for loan, book, customer in loan_search:
                print("Book `{}` was loaned to {} {} on {} ".format(
                    book.book_name,
                    customer.customer_name,\
                    customer.customer_surname,
                    loan.loan_date
                ))
            input("Press Enter to continue...")
            clear()
        else:
            print("Nothing similar to that is loaned")
            input("Press Enter to continue...")
            clear()

    elif user_selection == 6:
        librarians_list = []
        while True:
            try:
                librarian_list = session.query(Librarian)
                for tries in librarian_list:
                    print(f"{tries.librarian_id} | {tries.librarian_name} {tries.librarian_surname}")
                    librarians_list.append(tries.librarian_id)
                value = input("Enter librarians ID: ")
                value = int(value)
                if value not in librarians_list:
                    clear()
                    print("Error: Librarian with that ID was not found")
                    continue
                break
            except ValueError:
                clear()
                print("Error: ID should be a number!")
        while True:
            try:
                book_search = session.query(Loan, Book, Customer, Librarian).\
                    join(Book, Loan.book_id == Book.book_id).\
                    join(Customer, Loan.customer_id == Customer.customer_id).\
                    join(Librarian, Loan.librarian_id == Librarian.librarian_id).\
                    filter(Loan.librarian_id==value and Loan.loan_active==False).all()
                if book_search:
                    clear()
                    for loan, book, customer, librarian in book_search:
                        if loan.return_date:
                            print("Librarian {} {} loaned a book named `{}` to {} {} on {} and it was returned on {}".format(
                            librarian.librarian_name,
                            librarian.librarian_surname,
                            book.book_name,
                            customer.customer_name,
                            customer.customer_surname,
                            loan.loan_date,
                            loan.return_date
                        ))
                        else:
                            print("Librarian {} {} loaned a book named `{}` to {} {} on {} and it is still loaned".format(
                                librarian.librarian_name,
                                librarian.librarian_surname,
                                book.book_name,
                                customer.customer_name,
                                customer.customer_surname,
                                loan.loan_date
                            ))
                    input("Press Enter to continue...")
                    clear()
                    break
                else:
                    print("Nothing is loaned by this librarian")
                    input("Press Enter to continue...")
                    break
            except ValueError:
                print("Librarian ID must be an integer!")
    elif user_selection == '0':
        user_choice_menu()
    
def search_from_input():
    clear()
    user_selections = [1, 2, 3, 4, 5, 6, 0]
    
    while True:
        try:
            user_selection = int(input("Search by: \n1| Everything\n2| Author\n3| Book\n4| Publisher\n5| Loaned books\n6| Loaned books history by librarians ID \n0| Go back to menu\nChoice: "))
            if user_selection not in user_selections:
                clear()
                print("It is not an option!")
                continue
            else:
                return search(user_selection) 
        except ValueError:
            clear()
            print("Only numbers below are an option")
   

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