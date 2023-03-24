from flask import Blueprint, render_template

novo_bp = Blueprint('novoProduto', __name__)

@novo_bp.route('/novo-produto')
def novo():

    return render_template('cadastrar_produto.html')