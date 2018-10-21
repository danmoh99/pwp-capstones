class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print('This user\'s email has been updated to {address}'.format(address = self.address))

    def __repr__(self):
        return 'User: {name}, email: {email}, books read: {books}'.format(name = self.name, email = self.email, books = len(self.books))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        average = 0
        for value in self.books.values():
            if value == None: continue
            average += value
        return average/len(self.books)

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print('This book\'s ISBN has been updated to {isbn}'.format(isbn = self.isbn))

    def add_rating(self, rating):
        if rating == None or 0 > rating or rating > 4:
            print('Invalid Rating')
        else:
            self.ratings.append(rating)

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def get_average_rating(self):
        average = 0
        for rating in self.ratings:
            if rating == None: continue
            average += rating
        return average/len(self.ratings)

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return '{title}'.format(title = self.title)

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return '{title} by {author}'.format(title = self.title, author = self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return '{title}, a {level} manual on {subject}'.format(title = self.title, level = self.level, subject = self.subject)

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating = None):
        if not email in self.users:
            print('No user with email {}!'.format(email))
        else:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if not book in self.books:
                self.books[book] = 1
            else:
                self.books[book] = self.books[book] + 1

    def add_user(self, name, email, user_books = None):
        self.users[email] = User(name, email)
        if not user_books == None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for key in self.books.keys():
            print(key)

    def print_users(self):
        for value in self.users.values():
            print(value)

    def most_read_book(self):
        maxval = list(self.books.values())[0]
        maxkey = list(self.books.keys())[0]
        for key, value in self.books.items():
            if maxval < value:
                maxval = value
                maxkey = key
        return maxkey

    def highest_rated_book(self):
        maxrating = 0
        maxbook = list(self.books.keys())[0]
        for book in self.books.keys():
            if maxrating < book.get_average_rating():
                maxrating = book.get_average_rating()
                maxbook = book
        return maxbook

    def most_positive_user(self):
        maxrating = 0
        maxuser = self.users[list(self.users.keys())[0]]
        for user in self.users.values():
            if maxrating < user.get_average_rating():
                maxrating = user.get_average_rating()
                maxuser = user
        return user

    def get_n_most_read_books(self, n):
        temp = self.books
        books = []
        for i in range(n):
            maxval = 0
            maxkey = list(temp.keys())[0]
            for key, value in temp.items():
                if maxval < value:
                    maxval = value
                    maxkey = key
            books.append(maxkey)
            temp.pop(maxkey)
        return books

    def get_n_most_prolific_readers(self, n):
        temp = self.users
        print(temp)
        users = []
        for i in range(n):
            maxval = list(temp.values())[0]
            maxkey = list(temp.keys())[0]
            for key, value in temp.items():
                if len(maxval.books) < len(value.books):
                    maxval = value
                    maxkey = key
            users.append(maxval)
            temp.pop(maxkey)
        return users
