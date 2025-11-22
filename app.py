from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {
        'id': 1,
        'title': 'The Strain',
        'author': 'Chuck Hogan'
    }
]


@app.route('/books')
def listBooks():
    return jsonify(books)

app.run(port=5000, host='localhost', debug=True)