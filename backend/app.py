from flask import Flask, jsonify, request
from flask_cors import CORS

from Model.BookModel import BookModel
from Controller.ConnectionDBController import ConnectionDBController

app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

conn = ConnectionDBController.get_connection()
conn.row_factory = ConnectionDBController.dict_factory

@app.route('/', methods=['GET'])
def index():
    return jsonify("Servidor esta rodando...")

@app.route('/books', methods=['GET', 'POST'])
def all_books():
    if request.method == 'POST':
        post_data = request.get_json()
        return BookModel.insert_book(post_data, conn)
    else:
        return jsonify(BookModel.get_all_books(conn))


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    if request.method == 'PUT':
        post_data = request.get_json()
        return BookModel.update_book(post_data, conn)
    if request.method == 'DELETE':
        return BookModel.delete_book(book_id, conn)


if __name__ == '__main__':
    app.debug = True
    app.run()