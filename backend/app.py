from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from routes.book_routes import book_routes
from routes.server_routes import server_routes


db = SQLAlchemy()

def create_app(config='config.DevelopmentConfig'):
    app = Flask(__name__)
    app.config.from_object(__name__)

    CORS(app, resources={r'/*': {'origins': '*'}})

    app.config.from_object(config)
    db.init_app(app)

    app.register_blueprint(book_routes)
    app.register_blueprint(server_routes)

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True,
    )
