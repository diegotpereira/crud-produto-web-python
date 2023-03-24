import psycopg2

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