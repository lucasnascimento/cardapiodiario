from google.appengine.ext import db
from google.appengine.ext.db import polymodel
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
	variado = "variado"

class TipoPrato(db.Model):
	nome = db.StringProperty()
	
class Prato(db.Model):
	tipoPrato = db.ReferenceProperty(TipoPrato)
	nome = db.StringProperty()
	
class Cardapio(polymodel.PolyModel):
	nome = db.StringProperty()
	descricao = db.StringProperty()
	pratos = db.ListProperty(db.Key)

class CardapioConfig(Cardapio):
	dia_semana = db.StringProperty()

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
	destinatario = db.Reference(Destinario, collection_name = 'destinatario_restaurante')	
	restaurante = db.Reference(Restaurante, collection_name = 'destinatario_restaurante')

class Mensagem(db.Model):
	data_envio = db.DateTimeProperty()
	restaurante = db.ReferenceProperty(Restaurante, collection_name = "mensagem")
	cardapio = db.ReferenceProperty(Cardapio, collection_name = "mensagem")
	destinatarios = db.ListProperty(db.Key)
	body = db.TextProperty()