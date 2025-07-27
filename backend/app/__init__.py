from flask import Flask
from flask_cors import CORS


from app.database import db
from app.routes.book_routes import book_routes
from app.routes.server_routes import server_routes


def create_app(config='config.DevelopmentConfig'):
    app = Flask(__name__)

    CORS(app, resources={r'/*': {'origins': '*'}})

    app.config.from_object(config)
    db.init_app(app)
    
    with app.app_context():
        db.create_all()

    app.register_blueprint(book_routes)
    app.register_blueprint(server_routes)

    return app
