
from flask import request


def index(nome=None):
	if request.method == 'GET':
		if not nome:
			return {'Hello':'World'}
		return {'ola ':nome}
			
			
	elif request.method == 'POST':
		if nome:
			return {'Hello':nome}
		return {'Hello':'Post'}