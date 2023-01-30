from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Date, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///data/lms.db')
Base = declarative_base()


class Authors(Base):
    __tablename__ = 'authors'
    author_id = Column(Integer, primary_key=True)
    author_name = Column("Author name", String)
    author_surname = Column("Author surname", String)
    books = relationship("Books", back_populates='author')

    def __init__(self, author_name, author_surname):
        self.author_name = author_name
        self.author_surname = author_surname

    def __str__(self):
        return "{} {}".format(self.author_name, self.author_surname)

    def __repr__(self):
        return "{} {}".format(self.author_name, self.author_surname)


class Publishers(Base):
    __tablename__ = 'publishers'
    publisher_id = Column(Integer, primary_key=True)
    publisher_name = Column("Publisher", String)
    books = relationship('Books', back_populates='publisher')

    def __init__(self, publisher_name):
        self.publisher_name = publisher_name

    def __str__(self):
        return "{}".format(self.publisher_name)

    def __repr__(self):
        return "{}".format(self.publisher_name)


class Books(Base):
    __tablename__ = 'books'
    book_id = Column(Integer, primary_key=True)
    book_name = Column("Book name", String)
    book_isbn = Column("ISBN", Integer)
    author_id = Column("Author id", Integer, ForeignKey('authors.author_id'))
    author = relationship("Authors", back_populates='books')
    publisher_id = Column("Publisher id", Integer, ForeignKey('publishers.publisher_id'))
    publisher = relationship("Publishers", back_populates='books')
    loans = relationship('Loans', back_populates='books')

    def __init__(self, book_name, book_isbn, author_id, publisher_id):
        self.book_name = book_name
        self.book_isbn = book_isbn
        self.author_id = author_id
        self.publisher_id = publisher_id

    def __str__(self):
        return "{} {}".format(self.book_name, self.book_isbn)

    def __repr__(self):
        return "{} {}".format(self.book_name, self.book_isbn)

class Customers(Base):
    __tablename__ = 'customers'
    customer_id = Column(Integer, primary_key=True)
    customer_name = Column("Customer name", String)
    customer_surname = Column("Customer surname", String)
    customer_address = Column("Customer address", String)
    loans = relationship("Loans", back_populates='customers')

    def __init__(self, customer_name, customer_surname, customer_address):
        self.customer_name = customer_name
        self.customer_surname = customer_surname
        self.customer_address = customer_address

    def __str__ (self):
        return "{} {} {}".format(self.customer_name, self.customer_surname, self.customer_address)

    def __repr__ (self):
        return "{} {} {}".format(self.customer_name, self.customer_surname, self.customer_address)


class Librarians(Base):
    __tablename__ = 'librarians'
    librarian_id = Column(Integer, primary_key=True)
    librarian_name = Column("Librarian name", String)
    librarian_surname = Column("Librarian surname", String)
    loans = relationship("Loans", back_populates='librarian')

    def __init__(self, librarian_name, librarian_surname):
        self.librarian_name = librarian_name
        self.librarian_surname = librarian_surname

    def __str__(self):
        return "{} {}".format(self.librarian_name, self.librarian_surname)

    def __repr__(self):
        return "{} {}".format(self.librarian_name, self.librarian_surname)


class Loans(Base):
    __tablename__ = 'loans'
    loan_id = Column(Integer, primary_key=True, autoincrement=True)
    loan_date = Column("Loan date", Date)
    loan_active = Column("Loan status", Boolean, default=False)
    customer_id = Column("Customer id", Integer, ForeignKey('customers.customer_id'))
    customers = relationship("Customers", back_populates='loans')
    book_id = Column("Book id", Integer, ForeignKey('books.book_id'))
    books = relationship("Books", back_populates='loans')
    librarian_id = Column("Librarian id", Integer, ForeignKey('librarians.librarian_id'))
    librarian = relationship("Librarians", back_populates='loans')
    return_date = Column("Date of return", Date, default=None)

    def __init__(self, loan_date, loan_active, customer_id, book_id, librarian_id):
        self.loan_date = loan_date
        self.loan_active = loan_active
        self.customer_id = customer_id
        self.book_id = book_id
        self.librarian_id = librarian_id

    def __str__(self):
        return "{} {}".format(self.librarian_id, self.book_id)

    def __repr__(self):
        return "{} {}".format(self.librarian_id, self.book_id)


if __name__ == '__main__':
    Base.metadata.create_all(engine)