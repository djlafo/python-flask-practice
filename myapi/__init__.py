# pylint: disable=unused-variable

from flask import Flask
import os

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="dev",
        DATABASE=os.path.join(app.instance_path, "myapi.sqlite")
    )

    @app.route("/health")
    def health():
        return "Healthy"

    return app