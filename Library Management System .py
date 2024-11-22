class Book:
    def __init__(self, title, author, genre, book_id):
        self.title = title
        self.author = author
        self.genre = genre
        self.book_id = book_id
        self.borrowed = False
        self.rating = None

    def borrow(self):
        if not self.borrowed:
            self.borrowed = True
            print(f'{self.title} has been borrowed.')
        else:
            print(f'{self.title} is already borrowed.')

    def return_book(self):
        if self.borrowed:
            self.borrowed = False
            print(f'{self.title} has been returned.')
        else:
            print(f'{self.title} was not borrowed.')

    def add_rating(self, rating):
        self.rating = rating
        print(f'Rating for {self.title} added: {self.rating}')
