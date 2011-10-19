import logging
import wsgiref.handlers
import pyamf

from google.appengine.ext import db
from pyamf.remoting.gateway.wsgi import WSGIGateway
from model import TipoPrato
from model import Cardapio
from model import Prato
from model import Destinario
from model import Restaurante
from model import DestinatarioRestaurante

	
def salvarRestaurante(restaurante):
	restaurante.put()
	return restaurante

def recuperarRestaurantePorNome(nome):
	return Restaurante.all().filter(" nome = ", nome).get()

def recuperarRestaurantePorKey(key):
	return db.get(key)

def recuperarRestaurantes():
	return Restaurante.all().fetch(100) 
	
def main():
	services = {
		'salvarRestaurante': salvarRestaurante,
		'recuperarRestaurantePorNome': recuperarRestaurantePorNome,
		'recuperarRestaurantePorKey': recuperarRestaurantePorKey,
		'recuperarRestaurantes': recuperarRestaurantes,

    }
	
	gateway = WSGIGateway(services, logger=logging, debug=True)
	wsgiref.handlers.CGIHandler().run(gateway)

	pyamf.register_class( TipoPrato, "TipoPrato" )
	pyamf.register_class( Prato, "Prato" )
	pyamf.register_class( Cardapio, "Cardapio" )
	pyamf.register_class( Destinario, "Destinario" )
	pyamf.register_class( Restaurante, "Restaurante" )
	pyamf.register_class( DestinatarioRestaurante, "DestinatarioRestaurante" )
	
if __name__ == '__main__':
	main()
