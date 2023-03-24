from bancodedados import conectar
from flask import Blueprint, render_template

listar_bp = Blueprint('listarProduto', __name__)

# app = Flask(__name__)

# @app.route('/')
@listar_bp.route('/')
def index():
    sql = "SELECT * FROM produto"
    con = conectar()
    cur = con.cursor()
    cur.execute(sql)
    produtos = cur.fetchall()

    cur.close()
    con.close()

    return render_template('index.html', produtos=produtos)