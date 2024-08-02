from flask import Flask


def create_app():
    app = Flask(__name__)

    # Configurations
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///calorie_tracker.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize extensions
    migrate.init_app(app, db)

    # Register blueprints
    from .routes import bp as main_bp

    app.register_blueprint(main_bp)

    return app
