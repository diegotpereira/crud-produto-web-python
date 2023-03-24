from bancodedados import conectar
from flask import Blueprint, redirect, render_template, request, url_for

deletar_produto_bp = Blueprint('deletarProduto', __name__)

@deletar_produto_bp.route('/deletar-produto/<int:id>', methods=['GET', 'POST'])

def deletar_produto(id):

    if request.method == 'POST':
        con = conectar()
        cur = con.cursor()
        cur.execute('DELETE FROM produto WHERE id=%s', (id,))
        con.commit()

        cur.close()
        con.close()

        return redirect(url_for('listarProduto.index'))

    else:
        con = conectar()
        cur = con.cursor()
        cur.execute('SELECT * FROM produto WHERE id=%s', (id,))
        produto = cur.fetchone()

        cur.close()
        con.close()
        return render_template('deletar_produto.html', produto=produto)
