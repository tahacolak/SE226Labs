#author:tahacolak
from datetime import datetime

class ArchiveItem:
    def __init__(self, uid, title, year):
        self.uid = uid
        self.title = title
        self.year = int(year)

    def __str__(self):
        return f"UID: {self.uid}, Title: {self.title}, Year: {self.year}"

    def __eq__(self, other):
        return isinstance(other, ArchiveItem) and self.uid == other.uid

    def is_recent(self, n):
        return self.year >= (2025 - n)

class Book(ArchiveItem):
    def __init__(self, uid, title, year, author, pages):
        super().__init__(uid, title, year)
        self.author = author
        self.pages = int(pages)

    def __str__(self):
        return f"Book | UID: {self.uid}, Title: {self.title}, Year: {self.year}, Author: {self.author}, Pages: {self.pages}"

class Article(ArchiveItem):
    def __init__(self, uid, title, year, journal, doi):
        super().__init__(uid, title, year)
        self.journal = journal
        self.doi = doi

    def __str__(self):
        return f"Article | UID: {self.uid}, Title: {self.title}, Year: {self.year}, Journal: {self.journal}, DOI: {self.doi}"

class Podcast(ArchiveItem):
    def __init__(self, uid, title, year, host, duration):
        super().__init__(uid, title, year)
        self.host = host
        self.duration = int(duration)

    def __str__(self):
        return f"Podcast | UID: {self.uid}, Title: {self.title}, Year: {self.year}, Host: {self.host}, Duration: {self.duration} min"

def save_to_file(items, filename):
    with open(filename, 'w') as f:
        for item in items:
            if isinstance(item, Book):
                f.write(f"Book,{item.uid},{item.title},{item.year},{item.author},{item.pages}\n")
            elif isinstance(item, Article):
                f.write(f"Article,{item.uid},{item.title},{item.year},{item.journal},{item.doi}\n")
            elif isinstance(item, Podcast):
                f.write(f"Podcast,{item.uid},{item.title},{item.year},{item.host},{item.duration}\n")

def load_from_file(filename):
    items = []
    with open(filename, 'r') as f:
        for line in f:
            parts = line.strip().split(',')
            type_ = parts[0]
            if type_ == "Book":
                items.append(Book(*parts[1:]))
            elif type_ == "Article":
                items.append(Article(*parts[1:]))
            elif type_ == "Podcast":
                items.append(Podcast(*parts[1:]))
    return items

# Create sample items
items = [
    Book("B001", "Deep Learning", 2018, "Ian Goodfellow", 775),
    Book("B002", "Clean Code", 2008, "Robert C. Martin", 464),
    Article("A001", "AI in Medicine", 2021, "Nature Medicine", "10.1038/nm.1234"),
    Article("A002", "Quantum Computing", 2020, "Science Advances", "10.1126/sciadv.abc123"),
    Podcast("P001", "The AI Podcast", 2023, "NVIDIA", 45),
    Podcast("P002", "Lex Fridman Podcast", 2022, "Lex Fridman", 90)
]

# Save and load
save_to_file(items, "archive.txt")
loaded_items = load_from_file("archive.txt")

# Print loaded items
for item in loaded_items:
    print(item)
