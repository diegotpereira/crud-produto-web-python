from bancodedados import conectar

from flask import Blueprint, Flask, request, redirect, url_for, render_template

alterar_produto_bp = Blueprint('alterar_produto', __name__)

@alterar_produto_bp.route('/editar-produto/<int:id>', methods=['GET','POST'])
def editar_produto(id):

    con = conectar()
    cur = con.cursor()
    
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        preco = request.form['preco']
        
        cur.execute('UPDATE produto SET nome=%s, descricao=%s, preco=%s WHERE id=%s', (nome, descricao, preco, id))
        con.commit()
        cur.close()
        con.close()

        return redirect(url_for('listarProduto.index'))

    else:

        cur.execute('SELECT * FROM produto WHERE id=%s', (id,))

        produto = cur.fetchone()

        return render_template('alterar_produto.html', produto=produto)