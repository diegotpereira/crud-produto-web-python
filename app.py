# from flask import Flask
# # import psycopg2
# from bancodedados import conectar
# # from loja import Loja  

# from .rotas import *

# app = Flask(__name__)

# loja = Loja()


# @app.route('/')
# def index():

#     return "Bem-vindo à loja"

# @app.route('/add_produto')
# def add_produto():

#     return render_template('cadastrar_produto.html')

# @app.route('/add_produto', methods=['POST'])
# def add_produto_post():
#     nome = request.form['nome']
#     preco = request.form['preco']
#     descricao = request.form['descricao']

#     con = conectar()
#     cur = con.cursor()
#     cur.execute("INSERT INTO produto (nome, preco, descricao) VALUES (%s, %s, %s)", (nome, preco, descricao))
#     con.commit()
#     cur.close()
#     con.close()

#     return redirect(url_for('index'))
# banco_dados = 'localhost'
# banco_dados_nome = 'projetos_python'
# banco_dados_usuario = 'postgres'
# banco_dados_password = '123'

# def conectar():
#     con = psycopg2.connect(
#         host=banco_dados,
#         dbname=banco_dados_nome,
#         user=banco_dados_usuario,
#         password=banco_dados_password
#     )

#     return con

# @app.route('/')

# def index():
#     sql = "SELECT * FROM produto"
#     con = conectar()
#     cur = con.cursor()
#     cur.execute(sql)
#     produtos = cur.fetchall()

#     cur.close()
#     con.close()

#     return render_template('index.html', produtos=produtos)


# # Rota para exibir o formulário de cadastro de produto
# @app.route('/produto/novo')
# def cadastro():

#     return render_template('cadastrar_produto.html')

# @app.route('/inserir', methods=['POST'])
# def inserir():
    

#     nome = request.form['nome']
#     preco = request.form['preco']
#     descricao = request.form['descricao']

#     con = conectar()
#     cur = con.cursor()
#     # sql = "INSERT INTO produto (nome, preco, descricao) VALUES (%s, %s, %s)", (nome, preco, descricao)

#     cur.execute("INSERT INTO produto (nome, preco, descricao) VALUES (%s, %s, %s)", (nome, preco, descricao))
#     con.commit()
#     cur.close()
#     con.close()

#     return redirect(url_for('index'))

from flask import Flask
# from rotas import rotas_bp
from listaProduto import listar_bp
from adicionarProduto import adicionar_bp;
from novoProduto import novo_bp
from alterarProduto import alterar_produto_bp
from deletarProduto import deletar_produto_bp
# from alterarProduto import mostrar_formulario_bp

app = Flask(__name__)

app.register_blueprint(listar_bp)
app.register_blueprint(adicionar_bp)
app.register_blueprint(novo_bp)
# app.register_blueprint(mostrar_formulario_bp)
app.register_blueprint(alterar_produto_bp)
app.register_blueprint(deletar_produto_bp)

if __name__ == '__main__':
    app.run(debug=True)