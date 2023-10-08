import os
from flask import Flask
from src.worker.init_celery import celery

config_filename = os.path.abspath(os.path.dirname(__file__)) + "/../config.py"

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)
    app.app_context().push()

    initialize_database(app)
    register_blueprints(app)
    initialize_mail(app)
    initialize_celery(app)

    return app

def register_blueprints(app):
    from src.routes import route_blueprint

    app.register_blueprint(route_blueprint)

def initialize_database(app):
    from src.models.init_db import db

    db.init_app(app)
    with app.app_context():
        db.create_all(app=app)

def initialize_mail(app):
    from src.mail.init_mail import mail
    
    mail.init_app(app)

def initialize_celery(app):

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery.Task = ContextTask
    import src.worker.task

app = create_app()