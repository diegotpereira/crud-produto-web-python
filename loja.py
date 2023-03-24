# from bancodedados import conectar
# from flask import Flask, render_template, request, redirect, url_for

# app = Flask(__name__)

# class Loja:

#     def __init__(self):
        
#         self.con = conectar()
#         self.cursor = self.con.cursor()

#     @app.route('/add_produto', methods=['POST'])
#     def add_produto(self, nome, descricao, preco):

#         self.cursor.execute("INSERT INTO products (name, descricao, price) VALUES (%s, %s)", (nome, descricao, preco))
#         self.con.commit()