class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.page = 0

    def turn_page(self, page):
        self.page = page

class Library:
    def __init__(self, *args):
        self.books = []
        self.books.append(list(args))

    def find_book(self, title):
        try:
            return [el for el in self.books if el.title == title][0]
        except IndexError:
            return "Book does not exist"

b1 = Book("Title", "author")
b2 = Book("Title2", "author2")
b3 = Book("Title3", "author3")
lib = Library(b1, b2)
print(lib)
