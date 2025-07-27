# Configurações do projeto

## Execução local
Para rodar o backend localmente, siga os passos abaixo:

1. Instale as dependências: Navegue até o diretório backend e execute o comando abaixo para instalar as dependências necessárias:
    ```
    pip install -r requirements.txt
    ```
2. Inicie o servidor: Após a instalação, execute o arquivo run.py para iniciar a API. Por padrão, a API estará disponível em http://localhost:5000/books.

Pronto! Agora você pode acessar a API no seu navegador ou via ferramentas como Postman ou curl. A URL de acesso será http://localhost:5000/books.

## Execução em docker
Para rodar o backend usando Docker, basta seguir os passos abaixo:

1. Construa a imagem Docker: No diretório raiz do projeto, onde o Dockerfile está localizado, execute o comando para construir a imagem:
    ```
    docker build -t backend .
    ```
2. Execute o container: Após a imagem ser criada, execute o container com o seguinte comando:
    ```
    docker run -p 5000:5000 backend
    ```

Isso iniciará o backend dentro de um container Docker, e a API ficará disponível na mesma URL: http://localhost:5000/books.

Nota: Certifique-se de ter o Docker instalado e em funcionamento antes de executar esses comandos.
