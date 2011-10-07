import logging
import datetime
import wsgiref.handlers
import pyamf

from google.appengine.ext import db
from pyamf.remoting.gateway.wsgi import WSGIGateway

class CategoriaItemCardapio(db.Model):
	nome = db.StringProperty()
	
class ItemCardapio(db.Model):
	categoria = db.ReferenceProperty(CategoriaItemCardapio)
	nome = db.StringProperty()
	
class Cardapio(db.Model):
	nome = db.StringProperty()
	itens = db.ListProperty(db.Key)
	descricao = db.StringProperty()

class Usuario(db.Model):
	email = db.ListProperty(db.Email)
	contaFacebook = db.StringProperty()
	contaTwitter = db.StringProperty()	
	
class Restaurante(db.Model):
	nomeFantasia = db.StringProperty()
	conta_facebook = db.StringProperty()
	conta_twitter = db.StringProperty()
	clientes = db.ListProperty(db.Key)
	cardapioUnico = db.ReferenceProperty(Cardapio, collection_name="restaurante_unico_set")
	cardapioSegunda = db.ReferenceProperty(Cardapio, collection_name="restaurante_segunda_set")
	cardapioTerca = db.ReferenceProperty(Cardapio, collection_name="restaurante_terca_set")
	cardapioQuarta = db.ReferenceProperty(Cardapio, collection_name="restaurante_quarta_set")
	cardapioQuinta = db.ReferenceProperty(Cardapio, collection_name="restaurante_quinta_set")
	cardapioSexta = db.ReferenceProperty(Cardapio, collection_name="restaurante_sexta_set")
	cardapioSabado = db.ReferenceProperty(Cardapio, collection_name="restaurante_sabado_set")
	cardapioDomingo = db.ReferenceProperty(Cardapio, collection_name="restaurante_domingo_set")
		
class Agendamento(db.Model):
	restaurante  = db.ReferenceProperty(Restaurante)
	usuarios  = db.ReferenceProperty(Usuario)
	
class HistoricoEnvio(db.Model):
	restaurante = db.ReferenceProperty(Restaurante)
	usuarios   = db.ReferenceProperty(Usuario)
	cardapio = db.ReferenceProperty(Cardapio)
	data = db.DateTimeProperty(auto_now_add=True)

def echo(data):
    return data

	
def saveCategoria(newCategoria):
	newCategoria.put()
	return newCategoria

def deleteCategoria(categoriaKey):
	db.delete(categoriaKey)
	
def getCategorias():
	return CategoriaItemCardapio.all().fetch(100)

def getItemsCardapio():
	itemCardapio = ItemCardapio()
	itemCardapio.nome = "teste"
	itemCardapio.categoria = CategoriaItemCardapio.get("ahJkZXZ-Y2FyZGFwaW9kaWFyaW9yGwsSFUNhdGVnb3JpYUl0ZW1DYXJkYXBpbxgGDA")
	itemCardapio.put()
	return ItemCardapio.all().fetch(100)	
	
	
def main():
    services = {
        'echo': echo,
		'getCategorias': getCategorias,
		'getItemsCardapio': getItemsCardapio,
		'saveCategoria': saveCategoria,
    }
	
    gateway = WSGIGateway(services, logger=logging, debug=True)
    wsgiref.handlers.CGIHandler().run(gateway)

pyamf.register_class( CategoriaItemCardapio, "CategoriaItemCardapio" )
	
if __name__ == '__main__':
    main()
