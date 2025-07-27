from flask import Blueprint, request, jsonify
from models.book import Book


book_routes = Blueprint('book_routes', __name__)

conn = None

@book_routes.route('/books', methods=['GET'])
def get_books():
    return jsonify(Book.get_all_books(conn))

@book_routes.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    return jsonify(Book.get_book(book_id, conn))

@book_routes.route('/books', methods=['GET', 'POST'])
def create_book():
    post_data = request.get_json()
    return Book.insert_book(post_data, conn)

@book_routes.route('/books/<book_id>', methods=['PUT'])
def update_book(book_id):
    post_data = request.get_json()
    return Book.update_book(post_data, conn)

@book_routes.route('/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    return Book.delete_book(book_id, conn)
