from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'The Strain',
        'author': 'Chuck Hogan'
    },
    {
        'id': 2,
        'title': 'It',
        'author': 'Stephen King'
    }
]


@app.route('/books', methods=['GET'])
def listBooks():
    return jsonify(books)

@app.route('/booksbyid/<int:id>', methods=['GET'])
def listBookbyId(id):
    for book in books:
        if(book.get('id') == id):
            return jsonify(book)
    pass

@app.route('/editbookbyid/<int:id>', methods=['POST'])
def editBookbyId(id):
    editValue = request.get_json()
    for index, book in enumerate(books):
        if(book.get('id') == id):
            books[index].update(editValue)
            return jsonify(books[index])
    pass
        
    

app.run(port=5000, host='localhost', debug=True)