from flask import Blueprint

from .index import index


bp = Blueprint('views',__name__)

bp.add_url_rule(
   '/',methods=['GET','POST'],
   view_func=index,endpoint='index'
)

bp.add_url_rule(
	'/<string:nome>/',
	methods=['GET','POST'],
	view_func=index,
	endpoint='hhh'
)

def config_vw(app):
    app.register_blueprint(bp)
