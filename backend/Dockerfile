# Use a imagem oficial do Python
FROM python:3.11-slim

# Define o diretório de trabalho no container
WORKDIR /app

# Copia os arquivos do projeto para dentro do container
COPY . .

# Instala as dependências do projeto
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Define variável de ambiente para produção (pode mudar depois)
ENV FLASK_APP=app
ENV FLASK_ENV=production
ENV DATABASE_URL=sqlite:///database.db
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Expõe a porta usada pelo Flask
EXPOSE 5000

# Comando para rodar o app
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app"]
