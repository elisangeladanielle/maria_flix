from flask import Flask, request
from flask_restful import Resource, Api

from pessoa_psycopg import retorna_pessoas, insere_pessoa, retorna_pessoa, remove_pessoa, atualiza_pessoa
from filme_serie_psycopg import retorna_filme_series, retorna_filme_serie, insere_filme_serie, remove_filme_serie, atualiza_filme_serie
from assistidos_psycopg import retorna_assistidoss, retorna_assistidos, insere_assistidos, remove_assistidos, atualiza_assistidos

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return "Uhuuuul"

class Pessoa(Resource):
    def get(self):
        pessoas = retorna_pessoas()
        return pessoas

    def post(self):
        pessoa = request.json
        insere_pessoa(pessoa)
        return "Pessoa inserida com sucesso!"

    def put(self):
        pessoa = request.json
        atualiza_pessoa(pessoa)
        return "Pessoa atualizada com sucesso!"

class PessoaDetail(Resource):
    def get(self, id):
        pessoa = retorna_pessoa(id)
        return pessoa

    def delete(self, id):
        remove_pessoa(id)
        return "Pessoa removida com sucesso!"

class Filme_serie(Resource):
    def get(self):
        filme_series = retorna_filme_series()
        return filme_series

    def post(self):
        filme_serie = request.json
        insere_filme_serie(filme_serie)
        return "Filme/série inserido com sucesso!"

    def put(self):
        filme_serie = request.json
        atualiza_filme_serie(filme_serie)
        return "Filme/série atualizado com sucesso!"

class FilmeSerieDetail(Resource):
    def get(self, id):
        filme_serie = retorna_filme_serie(id)
        return filme_serie

    def delete(self, id):
        remove_filme_serie(id)
        return "Filme/série removido com sucesso!"

class Assistidos(Resource):
    def get(self):
        assistidoss = retorna_assistidoss()
        return assistidoss

    def post(self):
        assistidos = request.json
        insere_assistidos(assistidos)
        return "Filme/série assistido inserido com sucesso!"

    def put(self):
        assistidos = request.json
        atualiza_assistidos(assistidos)
        return "Filme/série assistido atualizado com sucesso!"

class AssistidosDetail(Resource):
    def get(self, id):
        assistidos = retorna_assistidos(id)
        return assistidos

    def delete(self, id):
        remove_assistidos(id)
        return "Filme/série assistido removido com sucesso!"


#declarando endpoint (a barra) = raiz da api -- se colocar a url sem a barra do final, tem que vir o resultado tb
api.add_resource(HelloWorld, "/")
api.add_resource(Pessoa, "/pessoas")
api.add_resource(PessoaDetail, "/pessoa/<int:id>")
api.add_resource(Filme_serie, "/filme_series")
api.add_resource(FilmeSerieDetail, "/filme_serie/<int:id>")
api.add_resource(Assistidos, "/assistidoss")
api.add_resource(AssistidosDetail, "/assistidos/<int:id_pessoa>")

# __variável__ = variável privada
# todo o resto é considerada pública
if __name__ == "__main__":
    app.run(debug=True)

