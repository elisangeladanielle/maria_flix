from psycopg_connection import cursor

def insere_pessoa(dados_pessoa):

    cursor.execute("INSERT INTO pessoa (nome, cpf, email,"
                   "data_nascimento)"
                   "VALUES (%s, %s, %s, %s)",
                   (
                       dados_pessoa['nome'],
                       dados_pessoa['cpf'],
                       dados_pessoa['email'],
                       dados_pessoa['data_nascimento'],
                   )
                   )

def retorna_pessoas():
    cursor.execute("SELECT * FROM pessoa")
    return cursor.fetchall()

def retorna_pessoa(id):

    #cur = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM pessoa WHERE id = %s", [id])
    pessoa = cursor.fetchone()
    return pessoa if pessoa else {}
    #pessoa['nome'] = 'Lisa 2'
    #print(pessoa)
    #opa = [dict(zip(columns, row)) for row in cursor.fetchall()]


def atualiza_pessoa(pessoa):
    query = "UPDATE pessoa SET nome = %s, cpf = %s, email = %s, data_nascimento = %s" \
            "WHERE id = %s"
    params = [pessoa['nome'], pessoa['cpf'], pessoa['email'], pessoa['data_nascimento']]

    cursor.execute(query, params)

def remove_pessoa(id):
    cursor.execute("DELETE FROM pessoa WHERE id = %s", [id])

