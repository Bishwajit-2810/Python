from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    @abstractmethod
    def display_info(self):
        pass


class Book(LibraryItem):
    def __init__(self, title, author, publication_year, genre):
        super().__init__(title, author, publication_year)
        self.genre = genre

    def display_info(self):
        info = f"Title: {self.title}\nAuthor: {self.author}\nPublication Year: {self.publication_year}\nGenre: {self.genre}"
        return info


class Magazine(LibraryItem):
    def __init__(self, title, author, publication_year, issue_number):
        super().__init__(title, author, publication_year)
        self.issue_number = issue_number

    def display_info(self):
        info = f"Title: {self.title}\nAuthor: {self.author}\nPublication Year: {self.publication_year}\nIssue Number: {self.issue_number}"
        return info


class DVD(LibraryItem):
    def __init__(self, title, author, publication_year, duration):
        super().__init__(title, author, publication_year)
        self.duration = duration

    def display_info(self):
        info = f"Title: {self.title}\nAuthor: {self.author}\nPublication Year: {self.publication_year}\nDuration: {self.duration} minutes"
        return info


class Library:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def display_all_items(self):
        for item in self.items:
            print(f"--- {type(item).__name__}:")
            print(item.display_info())
            print()


# Example usage:

library = Library()

book = Book("The Silent Patient", "Alex Michaelides", 2019, "Psychological Thriller")
magazine = Magazine("Nelolian: The Investigation", "Sharlok Homes", 2022, 3)
dvd = DVD("Crime Scene: The Movie", "Frank Darabont", 1994, 132)

library.add_item(book)
library.add_item(magazine)
library.add_item(dvd)

library.display_all_items()