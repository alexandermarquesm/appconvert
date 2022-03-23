from flask import Blueprint

from .views import convert, cryptogames

bp = Blueprint(
    "webui",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/css/styles.css",
)


def init_app(app):
    bp.add_url_rule("/convert", view_func=convert)
    bp.add_url_rule("/cryptogames", view_func=cryptogames)

    app.register_blueprint(bp)
