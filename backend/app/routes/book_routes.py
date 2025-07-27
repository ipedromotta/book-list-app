from http import HTTPStatus
from sqlalchemy.exc import SQLAlchemyError
from flask import Blueprint, request, jsonify

from app.models.book import Book
from app.database import db


book_routes = Blueprint('book_routes', __name__)

@book_routes.route('/books', methods=['GET'])
def get_books():
    try:
        books = Book.query.all()
        return jsonify([book.to_dict() for book in books]), HTTPStatus.OK
    except SQLAlchemyError:
        return jsonify({"error": "Erro ao acessar o banco de dados."}), HTTPStatus.INTERNAL_SERVER_ERROR

@book_routes.route('/books/<book_id>', methods=['GET'])
def get_book(book_id):
    try:
        try:
            book_id = int(book_id)
        except ValueError:
            return jsonify({"error": "ID inválido. Deve ser um número inteiro."}), HTTPStatus.BAD_REQUEST

        book = db.session.get(Book, book_id)
        if not book:
            return jsonify({"error": "Livro não encontrado."}), HTTPStatus.NOT_FOUND

        return jsonify(book.to_dict()), HTTPStatus.OK

    except SQLAlchemyError:
        return jsonify({"error": "Erro ao acessar o banco de dados."}), HTTPStatus.INTERNAL_SERVER_ERROR

    except Exception as e:
        return jsonify({"error": f"Erro inesperado: {str(e)}"}), HTTPStatus.INTERNAL_SERVER_ERROR
    
@book_routes.route('/books', methods=['POST'])
def create_book():
    try:
        post_data = request.get_json()

        if not post_data:
            return jsonify({"error": "JSON inválido ou não enviado"}), HTTPStatus.BAD_REQUEST

        title = post_data.get('title')
        author = post_data.get('author')
        read = post_data.get('read', False)

        errors = {}
        if not title:
            errors['title'] = 'Campo obrigatório.'
        if not author:
            errors['author'] = 'Campo obrigatório.'
        if not isinstance(read, bool):
            errors['read'] = 'Deve ser um valor booleano.'

        if errors:
            return jsonify({"errors": errors}), HTTPStatus.UNPROCESSABLE_ENTITY

        book = Book(title=title, author=author, read=read)
        db.session.add(book)
        db.session.commit()

        obj = book.to_dict()
        obj['message'] = 'Livro criado com sucesso.'
        return jsonify(obj), HTTPStatus.CREATED

    except SQLAlchemyError as e:
        db.session.rollback()
        return jsonify({"error": "Erro ao salvar no banco de dados."}), HTTPStatus.INTERNAL_SERVER_ERROR

    except Exception as e:
        return jsonify({"error": str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR

@book_routes.route('/books/<book_id>', methods=['PUT'])
def update_book(book_id):
        try:
            try:
                book_id = int(book_id)
            except ValueError:
                return jsonify({"error": "ID inválido. Deve ser um número inteiro."}), HTTPStatus.BAD_REQUEST
            
            book = db.session.get(Book, book_id)

            if not book:
                return jsonify({"error": "Livro não encontrado."}), HTTPStatus.NOT_FOUND
            
            post_data = request.get_json()

            if not post_data:
                return jsonify({"error": "JSON inválido ou não enviado"}), HTTPStatus.BAD_REQUEST

            title = post_data.get('title')
            author = post_data.get('author')
            read = post_data.get('read')

            if title is None and author is None and read is None:
                return jsonify({"error": "Preencha pelo menos um campo para atualizar."}), HTTPStatus.UNPROCESSABLE_ENTITY
        
            if title is not None:
                book.title = title
            if author is not None:
                book.author = author
            if read is not None:
                if not isinstance(read, bool):
                    return jsonify({"error": "O campo 'read' deve ser booleano."}), HTTPStatus.BAD_REQUEST
                book.read = read
        
            db.session.commit()

            obj = book.to_dict()
            obj['message'] = 'Livro atualizado com sucesso.'
            return jsonify(obj), HTTPStatus.OK
        
        except SQLAlchemyError:
            db.session.rollback()
            return jsonify({"error": "Erro ao atualizar o livro no banco de dados."}), HTTPStatus.INTERNAL_SERVER_ERROR

        except Exception as e:
            return jsonify({"error": f"Erro inesperado: {str(e)}"}), HTTPStatus.INTERNAL_SERVER_ERROR

@book_routes.route('/books/<book_id>', methods=['DELETE'])
def delete_book(book_id):
    try:
        try:
            book_id = int(book_id)
        except ValueError:
            return jsonify({"error": "ID inválido. Deve ser um número inteiro."}), HTTPStatus.BAD_REQUEST

        book = db.session.get(Book, book_id)

        if not book:
            return jsonify({"error": "Livro não encontrado."}), HTTPStatus.NOT_FOUND

        db.session.delete(book)
        db.session.commit()

        return jsonify({"message": "Livro deletado com sucesso."}), HTTPStatus.OK

    except SQLAlchemyError:
        db.session.rollback()
        return jsonify({"error": "Erro ao deletar do banco de dados."}), HTTPStatus.INTERNAL_SERVER_ERROR

    except Exception as e:
        return jsonify({"error": f"Erro inesperado: {str(e)}"}), HTTPStatus.INTERNAL_SERVER_ERROR
    
