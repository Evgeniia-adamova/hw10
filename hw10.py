class Books:
    """This class is about books"""

    def __init__(self, title, author, year, price, stoplist):
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.stoplist = stoplist

    def get_info(self):
        print("Title:", self.title)
        print("Author:", self.author)
        print("Year:", self.year)
        print("Price:", self.price)
        print("Stoplist:", self.stoplist)

    def find_most_expensive(books):
        most_expensive_book = books[0]
        for book in books:
            if book.price > most_expensive_book.price:
                most_expensive_book = book
        return most_expensive_book

    def set_stoplist(self, boolean):
        self.stoplist = boolean
        print(f"Stoplist updated to: {self.stoplist}")

    def censor(self, author_name, boolean):
        if self.author == author_name:
            self.set_stoplist(boolean)
            print(f"Book by {self.author} has been censored.")


book1 = Books("War and Peace", "Tolstoy", 1666, 700, [True])
book2 = Books("House", "Ivanov", 2001, 678, [False])
book1.get_info()
books_list = [book1, book2]
most_expensive = Books.find_most_expensive(books_list)
most_expensive.get_info()
book1.set_stoplist(False)
book1.censor("Tolstoy", False)