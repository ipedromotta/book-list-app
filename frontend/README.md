## Configurações do projeto

### Execução local
Para rodar o frontend localmente, siga os passos abaixo:
1. Instale as dependências: Navegue até o diretório frontend e execute o comando abaixo para instalar as dependências necessárias:
    ```
    npm install
    ```

2. Inicie a aplicação: Após a instalação, execute o comando abaixo:
    -  Para iniciar a aplicação em modo de desenvolvimento (Hot-Reload):
        ```
        npm run dev
        ```
    - Para compilar e minificar para produção:
        ```
        npm run build
        ```

A aplicação estará disponível em http://localhost:5173/ e você pode acessá-la pelo navegador.

### Execução em docker
Para rodar o frontend usando Docker, basta seguir os passos abaixo:

1. Construa a imagem Docker: No diretório frontend, onde o Dockerfile está localizado, execute o comando para construir a imagem:
    ```
    docker build -t frontend .
    ```

2. Execute o container: Após a imagem ser criada, execute o container com o comando abaixo. Isso irá rodar o frontend em um container e mapear a porta local para o container:
    ```
    docker run -p 5173:5173 frontend
    ```

A aplicação estará disponível na URL http://localhost:5173/.

Nota: Certifique-se de ter o Docker instalado e funcionando corretamente antes de executar esses comandos.
