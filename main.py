import logging
import wsgiref.handlers
import pyamf

from google.appengine.ext import db
from pyamf.remoting.gateway.wsgi import WSGIGateway
from aetypes import Enum


class DiaCardapio(Enum):
	domingo = "domingo"
	segunda = "segunda"
	terca = "terca"
	quarta = "quarta"
	quinta = "quinta"
	sexta = "sexta"
	sabado = "sabado"
	unico = "unico"

class TipoPrato(db.Model):
	nome = db.StringProperty()
	
class Prato(db.Model):
	tipoPrato = db.ReferenceProperty(TipoPrato)
	nome = db.StringProperty()
	
class Cardapio(db.Model):
	nome = db.StringProperty()
	descricao = db.StringProperty()
	dia_semana = db.StringProperty()
	pratos = db.ListProperty(db.Key)

class Destinario(db.Model):
	email = db.ListProperty(db.Email)
	contaFacebook = db.StringProperty()
	contaTwitter = db.StringProperty()	
	
class Restaurante(db.Model):
	nomeFantasia = db.StringProperty()
	conta_facebook = db.StringProperty()
	conta_twitter = db.StringProperty()
	tipo_cardapio = db.StringProperty()
	email_cabecalho = db.TextProperty()
	email_rodape = db.TextProperty()
	cardapios = db.ListProperty(db.Key)
	tipo_pratos = db.ListProperty(db.Key)
	pratos = db.ListProperty(db.Key)
	
class DestinatarioRestaurante(db.Model):
	destinatario = db.Reference(Destinario, collection_name = 'restaurantes')	
	restaurante = db.Reference(Restaurante, collection_name = 'destinatarios')






	
def saveCategoria(newCategoria):
	newCategoria.put()
	return newCategoria

def deleteCategoria(categoriaKey):
	db.delete(categoriaKey)
	
def getCategorias():
	return TipoPrato.all().fetch(100)

def getItemsCardapio():
	itemCardapio = ItemCardapio()
	itemCardapio.nome = "teste"
	itemCardapio.categoria = TipoPrato.get("ahJkZXZ-Y2FyZGFwaW9kaWFyaW9yGwsSFUNhdGVnb3JpYUl0ZW1DYXJkYXBpbxgGDA")
	itemCardapio.put()
	return ItemCardapio.all().fetch(100)	
	
	
def main():
	services = {
		'getCategorias': getCategorias,
		'getItemsCardapio': getItemsCardapio,
		'saveCategoria': saveCategoria,
    }
	
	gateway = WSGIGateway(services, logger=logging, debug=True)
	wsgiref.handlers.CGIHandler().run(gateway)

	pyamf.register_class( TipoPrato, "TipoPrato" )
	
if __name__ == '__main__':
	main()
