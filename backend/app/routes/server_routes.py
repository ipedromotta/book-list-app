from flask import Blueprint, jsonify


server_routes = Blueprint('server_routes', __name__)

@server_routes.route('/', methods=['GET'])
def index():
    return jsonify("Servidor esta rodando...")

@server_routes.route('/docs', methods=['GET'])
def docs():
    return jsonify("")
