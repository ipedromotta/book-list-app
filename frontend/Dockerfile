# Etapa 1: build (usa imagem leve com Node.js)
FROM node:20-slim AS build

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos de dependência e instala
COPY package*.json ./
RUN npm install

# Copia o resto do projeto e faz o build
COPY . .
RUN npm run build

# Etapa 2: serve com nginx (imagem super leve)
FROM nginx:alpine

# Remove configs dentro de conf.d, mas mantém a pasta conf.d
RUN rm -rf /etc/nginx/conf.d/*

# Copia o arquivo de configuração para a pasta correta
COPY nginx/default.conf /etc/nginx/conf.d/default.conf

# Copia os arquivos buildados do Vue
COPY --from=build /app/dist /usr/share/nginx/html

# Expõe a porta padrão
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
