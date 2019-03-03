# from . import app, main, config, models, view
from app import app

db = app.db
manager = app.manager

# __all__ = [app, main, config, models, view]