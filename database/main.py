from database import db, Book

db.connect()

db.create_tables([Book])

book = Book.create(name = 'Livro1', author='author1')

listbooks = Book.select()

for b in listbooks:
    print(b.name)