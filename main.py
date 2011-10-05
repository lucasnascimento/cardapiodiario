#!/usr/bin/env python
import cgi
import os
import datetime

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext import db
from google.appengine.ext.webapp import template

_DEBUG = True

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
	
class BaseRequestHandler(webapp.RequestHandler):
	def generate(self, template_name, template_values={}):
		values = {}
		values.update(template_values)

		path = os.path.join(os.path.dirname(__file__), template_name)
		self.response.out.write(template.render(path, values, debug=_DEBUG))
		
class MainHandler(BaseRequestHandler):
    def get(self):
        self.generate('meuRestaurante.html')
		
class ClassificationRequest(BaseRequestHandler):
	def post(self):
		classification = Classification()
		classification.position = int(self.request.get('position'))
		classification.date = datetime.datetime.strptime(self.request.get('date'), '%m/%d/%Y')
		classification.player = self.request.get('player')
		classification.put()
			
		self.generate('classification.html', getClassifications())
	def get(self):
		opt = self.request.get('opt')
		if opt == 'delete':
			key = self.request.get('key')
			db.delete(db.get(key))
			self.generate('classification.html', getClassifications())
		elif opt == 'byPlayer':
			player = self.request.get('player')
			self.generate('classification.html', getClassificationsByPlayer(player))
		else :
			self.generate('classification.html', getClassifications())

class RankinkgRequest(BaseRequestHandler):
	def post(self):
		processRanking()
		self.generate('ranking.html', getRankings())
	def get(self):
		processRanking()
		self.generate('ranking.html', getRankings())
		
def getClassifications():
	classifications_query = Classification.all().order('-date').order('position')
	classifications = classifications_query.fetch(100)
	template_values = {'classifications': classifications}
	return template_values
	
def getClassificationsByPlayer(player):
	classifications_query = Classification.all().filter(' player = ' , player)
	classifications = classifications_query.fetch(100)
	template_values = {'classifications': classifications}
	return template_values
	
def getRankings():
	rankings_query = Ranking.all().order('-points')
	rankings = rankings_query.fetch(100)
	template_values = {'rankings': rankings}
	return template_values
	
def processRanking():
	db.delete(Ranking.all())
	classifications = Classification.all().order('-player').fetch(100)
	
	for classification in classifications:
		ranking = Ranking.all().filter(' player = ' , classification.player ).get()
		
		if ranking is None:
			ranking = Ranking()
			ranking.points = 0
		
		if classification.position == 1 :
			ranking.points = ranking.points + 10
		elif classification.position == 2 :
			ranking.points = ranking.points + 5
		elif classification.position == 3 :
			ranking.points = ranking.points + 3
		else :
			ranking.points = ranking.points + 1
			
		ranking.player = classification.player
		ranking.put()
			
	
	

application = webapp.WSGIApplication([('/', MainHandler)]
							,debug=True)
def main():
	run_wsgi_app(application)

if __name__ == '__main__':
    main()
