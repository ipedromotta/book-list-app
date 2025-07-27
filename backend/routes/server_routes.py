from flask import Blueprint, jsonify


server_routes = Blueprint('server_routes', __name__)

@server_routes.route('/', methods=['GET'])
def index():
    return jsonify("Servidor esta rodando...")
