"""Konfiguracja odczytywana ze zmiennych środowiskowych."""

import os


class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:////data/app.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
