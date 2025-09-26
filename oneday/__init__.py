from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy


import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM 적용
    db.init_app(app)
    migrate.init_app(app, db)
    from .import models

    # 블루 프린트 등록
    from oneday.views import main_views , course_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(course_views.bp)

    return app


