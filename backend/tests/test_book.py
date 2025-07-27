import pytest
from http import HTTPStatus
from app import create_app
from app.database import db
from app.models.book import Book


@pytest.fixture(scope='module') # para controlar o tempo de vida de uma fixture no contexto de execução dos testes
def test_client():
    # Cria a aplicação para testes
    app = create_app(config='config.TestingConfig')
    
    # Cria um cliente de teste (para simular requisições HTTP)
    testing_client = app.test_client()

    # Cria as tabelas no banco de dados (em memória)
    with app.app_context():
        db.create_all()  # Cria as tabelas antes de rodar os testes
    yield testing_client  # Isso vai ser utilizado nos testes

    # Após os testes, destrói as tabelas
    with app.app_context():
        db.drop_all()

@pytest.fixture
def new_book(test_client):
    with test_client.application.app_context():
        book = Book(title='Test Book', author='Test Author')
        db.session.add(book)
        db.session.commit()
        yield book
        # Limpa o livro após o teste, só se existir
        book_in_db = db.session.get(Book, book.id)
        if book_in_db:
            db.session.delete(book_in_db)
            db.session.commit()
        
# Testando a criação de um novo livro (POST)
def test_create_book(test_client):
    data = {'title': 'New Book', 'author': 'New Author'}
    response = test_client.post('/books', json=data)
    assert response.status_code == HTTPStatus.CREATED  # Status 201 - Criado
    assert 'New Book' in response.json['title']

# Testando a obtenção de todos os livros (GET)
def test_get_books(test_client, new_book):
    response = test_client.get('/books')
    assert response.status_code == HTTPStatus.OK
    assert len(response.json) > 0
    assert any(book['title'] == new_book.title for book in response.json)

# Testando a obtenção de um livro específico (GET)
def test_get_book(test_client, new_book):
    response = test_client.get(f'/books/{new_book.id}')
    assert response.status_code == HTTPStatus.OK
    assert response.json['title'] == new_book.title

# Testando a atualização de um livro (PUT)
def test_update_book(test_client, new_book):
    updated_data = {'title': 'Updated Book', 'author': 'Updated Author'}
    response = test_client.put(f'/books/{new_book.id}', json=updated_data)
    assert response.status_code == HTTPStatus.OK
    assert response.json['title'] == 'Updated Book'
    
    # Verificando se o livro foi atualizado
    updated_book = db.session.get(Book, new_book.id)
    assert updated_book.title == 'Updated Book'

# Testando a exclusão de um livro (DELETE)
def test_delete_book(test_client, new_book):
    response = test_client.delete(f'/books/{new_book.id}')
    assert response.status_code == HTTPStatus.OK
    json_data = response.get_json()
    assert json_data['message'] == 'Livro deletado com sucesso.'

    # Confirma que o livro foi deletado no banco, usando o app_context do teste
    with test_client.application.app_context():
        deleted_book = db.session.get(Book, new_book.id)
        assert deleted_book is None

