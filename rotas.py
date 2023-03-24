# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return 'Página inicial'


# if __name__ == '__main__':
#     app.run()


from flask import Blueprint

rotas_bp = Blueprint('rotas', __name__)


# @rotas_bp.route('/')
# def index():
#     return 'Página Inicial'

@rotas_bp.route('/sobre')
def sobre():
    return 'Página Sobre'