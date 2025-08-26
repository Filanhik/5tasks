class Library:
    def __init__(self):
        self.books = []
        self.next_id = 1

    def add_book(self, title, author):
        book = {"id": self.next_id, "Название": title, "Автор": author}
        self.books.append(book)
        self.next_id += 1
        return book

    def get_all_books(self):
        return self.books

    def get_book_by_id(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                return book
        return None

    def delete_book(self, book_id):
        for book in self.books:
            if book["id"] == book_id:
                self.books.remove(book)
                return True
        return False