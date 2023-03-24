from flask import Flask, render_template, request, redirect
import psycopg2
from bancodedados import conectar

app = Flask(__name__)

con = conectar()

@app.route("/")
def index():

    return render_template("login.html")

@app.route("/login", methods=["POST"])
def login():

    email = request.form["email"]
    senha = request.form["senha"]

    cursor = con.cursor()
    cursor.execute("SELECT * FROM USUARIOS WHERE email = %s AND senha = %s", (email, senha))

    usuario = cursor.fetchone()

    if usuario:

        return redirect("/painel")

    else:

        error = "Usuário ou senha inválidos!"

        return render_template("login.html", error=error)

@app.route("/painel")
def painel():

    return "Bem vindo ao painel"


@app.route('/registrar', methods=["POST"])
def registrar():
    nome = request.form["nome"]
    email = request.form["email"]
    senha = request.form["senha"]
    confirmar_senha = request.form["confirmar_senha"]
    usuarionome = request.form["usuarionome"]

    #verificar se a senha e a confirmação de senha são iguais
    if senha != confirmar_senha:

        return redirect("/painel")

    #verificar se o usuário já existe no banco de dados
    cursor = con.cursor()
    cursor.execute('SELECT * FROM usuarios WHERE usuarionome = %s', (usuarionome,))

    usuario = cursor.fetchone()

    if usuario:

        return redirect("/painel")

    # criar um novo usuário no banco de dados

    cursor.execute("INSERT INTO usuarios (nome, email, senha, usuarionome) VALUES (%s, %s, %s, %s)", (nome, email, senha, usuarionome))
    con.commit()

    return redirect("/home")


@app.route('/home')
def home():
    return 'Welcome to the home page!'
    

if __name__ == "__main__":
    app.run(debug=True)

