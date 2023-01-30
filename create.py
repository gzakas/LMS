from sqlalchemy.orm import sessionmaker
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
    while True:
        book_name = input("Name of the book: ")
        while True:
            try:
                book_isbn = input("Books ISBN code: ")
                book_isbn = int(book_isbn)
                break
            except ValueError:
                print("Error: Books ISBN must be a number!")
        while True:
            try:    
                authors = input("Authors ID: ")
                authors = int(authors)
                break
            except ValueError:
                print("Error: Authors ID must be a number!")
        while True:
            try:
                publishers = input("Publishers ID: ")
                publishers = int(publishers)
                break
            except ValueError:
                print("Error: Publishers ID must be a number!")
        add_book(book_name, book_isbn, authors, publishers)
        user_choice = input("Do you want to add another book? (yes/no): ")
        if user_choice.lower() == "no" or "":
            break
def add_author(author_name, author_surname):
    authors = Author(author_name, author_surname)
    session.add(authors)
    session.commit()
    return authors

def add_author_from_input():
    clear()
    while True:
        author_name = input("Name of the author: ")
        author_surname = input("Surname of the author: ")
        add_author(author_name, author_surname)
        user_choice = input("Do you want to add another author? (yes/no): ")
        if user_choice.lower() == "no" or "":
            break
        

def register_customer(customer_name, customer_surname, customer_address):
    customers = Customer(customer_name, customer_surname, customer_address)
    session.add(customers)
    session.commit()
    return customers

def register_customer_from_input():
    clear()
    customer_name = input("Customers name: ")
    customer_surname = input("Customers surname: ")
    customer_address = input("Customers address: ")
    return register_customer(customer_name, customer_surname, customer_address)

def new_librarian(librarian_name, librarian_surname):
    librarians = Librarian(librarian_name, librarian_surname)
    session.add(librarians)
    session.commit()
    return librarians

def new_librarian_from_input():
    clear()
    librarian_name = input("Librarians name: ")
    librarian_surname = input("Librarians surname: ")
    return new_librarian(librarian_name, librarian_surname)

def new_publisher(publisher_name):
    publishers = Publisher(publisher_name)
    session.add(publishers)
    session.commit()
    return publishers

def new_publisher_from_input():
    clear()
    publisher_name = input("Publishers name: ")
    return new_publisher(publisher_name)

def assign_loan(loan_date, loan_active, customer_id, book_id, librarian_id):
    loans = Loan(loan_date, loan_active, customer_id, book_id, librarian_id)
    session.add(loans)
    session.commit()
    return loans

def assign_loan_from_input():
    clear()
    loan_date = datetime.datetime.now().date()
    loan_active = True
    while True:
        try:
            customer_id = input("Enter customers ID: ")
            customer_id = int(customer_id)
            break
        except ValueError:
            print("Error: Customer ID must be a number")
    while True:
        try:
            book_id = input("Enter books ID: ")
            book_id = int(book_id)
            break
        except ValueError:
            print("Error: Book ID must be a number")
    while True:
        try:
            librarian_id = input("Enter librarians ID: ")
            librarian_id = int(librarian_id)
            break
        except ValueError:
            print("Error: Librarian ID must be a number")
    return assign_loan(loan_date, loan_active, customer_id, book_id, librarian_id)

def check_active_loans(query=session.query(Loan)):
    clear()
    query = session.query(Book, Loan, Customer)\
        .join(Loan, Book.book_id == Loan.book_id)\
        .join(Customer, Loan.customer_id == Customer.customer_id)\
            .filter(Loan.loan_active == True).all()
    if query:
        for x in query:
            print("Loan id: {}, Book id: {}, Book name: {}, Loaned at: {}, Customers name: {} {}".format(
                x.Loan.loan_id,
                x.Book.book_id,
                x.Book.book_name,
                x.Loan.loan_date,
                x.Customer.customer_name,
                x.Customer.customer_surname
            ))
    else:
        print("No books are currently loaned")

def customer_returns(user_input):
    current_date = datetime.datetime.now().date()
    session.query(Loan).filter_by(book_id=user_input).update({Loan.return_date: current_date, Loan.loan_active: False})
    session.commit()

def customer_returns_from_input():
    clear()
    while True:
        try:
            user_input = input("Enter book ID which the customer returned: ")
            user_input = int(user_input)
            if not user_input:
                raise ValueError
            else:
                customer_returns(user_input)
                break
        except ValueError:
            print("Error: This field must be a number")

def search(user_selection):
    if user_selection == '1':
        value = input("Searching for: ")
        query1 = session.query(Author).filter(Author.author_name.ilike(f"%{value}%")).all()
        query2 = session.query(Author).filter(Author.author_surname.ilike(f"%{value}%")).all()
        query3 = session.query(Book).filter(Book.book_name.ilike(f"%{value}%")).filter(~session.query(Loan).filter(Loan.book_id == Book.book_id).exists()).all()
        query4 = session.query(Publisher).filter(Publisher.publisher_name.ilike(f"%{value}%")).all()
        query5 = session.query(Loan).filter(Loan.loan_active==True).all()
        for querys in query1:
            print("Authors name", querys)
        for querys in query2:
            print("Authors surname:", querys)
        for querys in query3:
            print("Available book:", querys)
        for querys in query4:
            print("Publisher:", querys)
        for querys in query5:
            book = session.query(Book).get(querys.book_id)
            customer = session.query(Customer).get(querys.customer_id)
            librarian = session.query(Librarian).get(querys.librarian_id)
            print(f"Loaned book: {book.book_name}, by customer: {customer.customer_name} {customer.customer_surname}, assigned by librarian: {librarian.librarian_name} {librarian.librarian_surname}")
    elif user_selection == '2':
        value = input("Searching for: ")
        query1 = session.query(Author).filter(Author.author_name.ilike(f"%{value}%")).all()
        query2 = session.query(Author).filter(Author.author_surname.ilike(f"%{value}%")).all()
        for querys in query1:
            print(f"Authors name: {querys.author_name}")
        for querys in query2:
            print(f"Authors surname: {querys.author_surname}")
    elif user_selection == '3':
        value = input("Searching for: ")
        query = session.query(Book).filter(Book.book_name.ilike(f"%{value}%")).filter(~session.query(Loan).filter(Loan.book_id == Book.book_id).exists()).all()
        if query:
            for querys in query:
                print(f"Book ID: {querys.book_id} {querys}")
        else:
            print("Found nothing")
    elif user_selection == '4':
        value = input("Searching for: ")
        query = session.query(Publisher).filter(Publisher.publisher_name.ilike(f"%{value}%")).all()
        if query:
            for querys in query:
                print(querys)
        else:
            print("Found nothing")
    elif user_selection == '5':
        query = session.query(Loan, Book, Customer).\
        join(Book, Loan.book_id == Book.book_id).\
        join(Customer, Loan.customer_id == Customer.customer_id).\
        filter(Loan.loan_active==True).all()
        if query:
            for loan, book, customer in query:
                print("Book `{}` was loaned to {} {} on {} ".format(
                    book.book_name,
                    customer.customer_name,\
                    customer.customer_surname,
                    loan.loan_date
                ))
        else:
                print("Nothing is loaned")
    elif user_selection == '6':
        while True:
            try:
                value = input("Enter librarians ID: ")
                value = int(value)
                if not value:
                    raise ValueError
                query = session.query(Loan, Book, Customer, Librarian).\
                    join(Book, Loan.book_id == Book.book_id).\
                    join(Customer, Loan.customer_id == Customer.customer_id).\
                    join(Librarian, Loan.librarian_id == Librarian.librarian_id).\
                    filter(Loan.librarian_id==value and Loan.loan_active==False).all()
                if query:
                    for loan, book, customer, librarian in query:
                        print("Librarian {} {} loaned a book named `{}` to {} {} on {}".format(
                            librarian.librarian_name,
                            librarian.librarian_surname,
                            book.book_name,
                            customer.customer_name,
                            customer.customer_surname,
                            loan.loan_date
                        ))
                    break
                else:
                    print("Nothing is loaned by this librarian")
                    break
            except ValueError:
                print("Librarian ID must be an integer!")
    
def search_from_input():
    clear()
    user_selection = input("Search by: \n1| Everything (Excluding loaned books)\n2| Author\n3| Book\n4| Publisher\n5| All loaned books\n6| Loaned books by librarians ID\nChoice: ")
    return search(user_selection)    

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