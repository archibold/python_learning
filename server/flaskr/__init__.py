"""Fabryka aplikacji Flask."""

from flask import Flask

from flaskr.config import Config
from flaskr.extensions import db
from flaskr.routes.items import items_bp
from flaskr.routes.files import files_bp


def create_app(config_object=Config):
    """Tworzy skonfigurowaną instancję aplikacji.

    Argument ``config_object`` umożliwia w przyszłości łatwe podmiennej
    konfiguracji w testach lub dla różnych środowisk.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)
    app.config['UPLOAD_FOLDER'] = Config.UPLOAD_FOLDER

    db.init_app(app)
    app.register_blueprint(items_bp)
    app.register_blueprint(files_bp)

    with app.app_context():
        db.create_all()

    return app
