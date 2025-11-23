from peewee import *

db = SqliteDatabase('database.db')

class Book(Model):
    name = CharField()
    author = CharField()

    class Meta:
        database = db