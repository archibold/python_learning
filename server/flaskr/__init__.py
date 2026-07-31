"""Fabryka aplikacji Flask."""

from flask import Flask

from flaskr.config import Config
from flaskr.extensions import db
from flaskr.routes.items import items_bp


def create_app(config_object=Config):
    """Tworzy skonfigurowaną instancję aplikacji.

    Argument ``config_object`` umożliwia w przyszłości łatwe podmiennej
    konfiguracji w testach lub dla różnych środowisk.
    """
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    app.register_blueprint(items_bp)

    with app.app_context():
        db.create_all()

    return app
