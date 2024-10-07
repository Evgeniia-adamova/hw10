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
