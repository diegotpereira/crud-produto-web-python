from bancodedados import conectar

from flask import Blueprint, Flask, request, redirect, url_for, render_template

adicionar_bp = Blueprint('produtos', __name__)

@adicionar_bp.route('/inserir', methods=['GET','POST'])
def inserir():
    
    nome = request.form['nome']
    preco = request.form['preco']
    descricao = request.form['descricao']

    con = conectar()
    cur = con.cursor()
    # sql = "INSERT INTO produto (nome, preco, descricao) VALUES (%s, %s, %s)", (nome, preco, descricao)

    cur.execute("INSERT INTO produto (nome, preco, descricao) VALUES (%s, %s, %s)", (nome, preco, descricao))
    con.commit()
    cur.close()
    con.close()

    return redirect(url_for('listarProduto.index'))