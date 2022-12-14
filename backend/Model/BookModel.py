from datetime import datetime
from uuid import uuid4
from Controller.ResponseController import ResponseController
from Model.Enum.RequestEnum import RequestEnum


class BookModel:
    
    @staticmethod
    def get_book(id_book, conn):
        try:
            query = f"SELECT * FROM BOOKS WHERE ID_BOOK = '{id_book}'"
            cursor = conn.cursor()
            cursor.execute(query)
            row = cursor.fetchone()
            cursor.close()
            if row:
                return ResponseController.get_response(RequestEnum.OK.value, row, "Sucesso")
            else:
                return ResponseController.get_response(RequestEnum.NOT_FOUND.value, list(), "Nenhum registro encontrado")
        except Exception as ex:
            return ResponseController.get_response(RequestEnum.BAD_REQUEST.value, list(), f"Erro ao obter registro: {ex}")
        
    @staticmethod
    def get_all_books(conn):
        try:
            query = 'SELECT * FROM BOOKS'
            cursor = conn.cursor()
            cursor.execute(query)
            rows = cursor.fetchall()
            cursor.close()
            
            if rows:
                return ResponseController.get_response(RequestEnum.OK.value, rows, "Sucesso")
            else:
                return ResponseController.get_response(RequestEnum.NOT_FOUND.value, list(), "Nenhum registro encontrado")
        except Exception as ex:
            return ResponseController.get_response(RequestEnum.INTERNAL_ERROR.value, list(), f"Erro ao obter registro: {ex}")
        
    @staticmethod
    def insert_book(book, conn):
        try:
            id_book = uuid4().hex
            created = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            query = f"INSERT INTO BOOKS (ID_BOOK, TITLE, AUTHOR, READ, CREATED_AT) VALUES ('{id_book}', '{book['title']}', '{book['author']}', {book['read']}, '{created}')"
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.execute("SELECT ID_BOOK FROM BOOKS ORDER BY CREATED_AT DESC LIMIT 1")
            last_insert = cursor.fetchone()
            last_insert = BookModel.get_book(last_insert["ID_BOOK"], conn)
            cursor.close()
            
            return ResponseController.get_response(RequestEnum.CREATED.value, last_insert["payload"], "Livro adicionado!")
        except Exception as ex:
            return ResponseController.get_response(RequestEnum.INTERNAL_ERROR.value, list(), f"Erro ao cadastrar livro: {ex}")
        
    @staticmethod
    def update_book(book, conn):
        try:
            query = f"UPDATE BOOKS SET TITLE = '{book['title']}', AUTHOR = '{book['author']}', READ = {book['read']} WHERE ID_BOOK = '{book['id']}'"
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.close()
            book_updated = BookModel.get_book(book['id'], conn)
            
            return ResponseController.get_response(RequestEnum.OK.value, book_updated["payload"], "Livro atualizado!")
        except Exception as ex:
            return ResponseController.get_response(RequestEnum.INTERNAL_ERROR.value, list(), f"Erro ao atualizar: {ex}")
        
    @staticmethod
    def delete_book(id_book, conn):
        try:
            book_for_delete = BookModel.get_book(id_book, conn)
            if book_for_delete["status"] == RequestEnum.NOT_FOUND.value:
                return ResponseController.get_response(RequestEnum.NOT_FOUND.value, list(), "Nenhum registro encontrado")
            
            query = f"DELETE FROM BOOKS WHERE ID_BOOK = '{id_book}'"
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            cursor.close()

            return ResponseController.get_response(RequestEnum.OK.value, book_for_delete["payload"], "Livro deletado!")
        except Exception as ex:
            return ResponseController.get_response(RequestEnum.INTERNAL_ERROR.value, list(), f"Erro ao deletar livro: {ex}")
        
        