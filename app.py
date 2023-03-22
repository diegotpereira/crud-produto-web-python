from flask import Flask, render_template, request, redirect, url_for
import psycopg2

app = Flask(__name__)

banco_dados = 'localhost'
banco_dados_nome = 'projetos_python'
banco_dados_usuario = 'postgres'
banco_dados_password = '123'

def conectar():
    con = psycopg2.connect(
        host=banco_dados,
        dbname=banco_dados_nome,
        user=banco_dados_usuario,
        password=banco_dados_password
    )

    return con

@app.route('/')

def index():
    sql = "SELECT * FROM produto"
    con = conectar()
    cur = con.cursor()
    cur.execute(sql)
    produtos = cur.fetchall()

    cur.close()
    con.close()

    return render_template('index.html', produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)