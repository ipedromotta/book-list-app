import pytest
from app import create_app, db
from models.book import Book


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

@pytest.fixture(scope='module')
def new_book():
    book = Book(title='Test Book', author='Test Author')
    db.session.add(book)
    db.session.commit()
    return book

# Testando a criação de um novo livro (POST)
def test_create_book(test_client):
    data = {'title': 'New Book', 'author': 'New Author'}
    response = test_client.post('/api/books', json=data)
    assert response.status_code == 201  # Status 201 - Criado
    assert 'Book created' in response.json['message']

# Testando a obtenção de todos os livros (GET)
def test_get_books(test_client, new_book):
    response = test_client.get('/api/books')
    assert response.status_code == 200
    assert len(response.json) > 0
    assert response.json[0]['title'] == new_book.title

# Testando a obtenção de um livro específico (GET)
def test_get_book(test_client, new_book):
    response = test_client.get(f'/api/books/{new_book.id}')
    assert response.status_code == 200
    assert response.json['title'] == new_book.title

# Testando a atualização de um livro (PUT)
def test_update_book(test_client, new_book):
    updated_data = {'title': 'Updated Book', 'author': 'Updated Author'}
    response = test_client.put(f'/api/books/{new_book.id}', json=updated_data)
    assert response.status_code == 200
    assert response.json['message'] == 'Book updated'
    
    # Verificando se o livro foi atualizado
    updated_book = Book.query.get(new_book.id)
    assert updated_book.title == 'Updated Book'

# Testando a exclusão de um livro (DELETE)
def test_delete_book(test_client, new_book):
    response = test_client.delete(f'/api/books/{new_book.id}')
    assert response.status_code == 200
    assert response.json['message'] == 'Book deleted'
    
    # Verificando se o livro foi excluído
    deleted_book = Book.query.get(new_book.id)
    assert deleted_book is None
