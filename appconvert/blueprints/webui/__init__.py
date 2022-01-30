from flask import Blueprint
from .views import home, convert, cryptogames, defi

bp = Blueprint(
    "webui",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/css/styles.css",
)


def init_app(app):
    bp.add_url_rule("/", view_func=home)
    bp.add_url_rule("/convert", view_func=convert)
    bp.add_url_rule("/cryptogames", view_func=cryptogames)
    bp.add_url_rule("/defi", view_func=defi)

    app.register_blueprint(bp)
