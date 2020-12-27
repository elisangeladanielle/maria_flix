from psycopg_connection import cursor

def insere_assistidos(dados_assistidos):
    cursor.execute("INSERT INTO assistidos (id_pessoa, id_filme_serie, status,"
                   "data_inicio, data_fim)"
                   "VALUES (%s, %s, %s, %s, %s)",
                   (
                       dados_assistidos['id_pessoa'],
                       dados_assistidos['id_filme_serie'],
                       dados_assistidos['status'],
                       dados_assistidos['data_inicio'],
                       dados_assistidos['data_fim'],
                   )
                   )


def retorna_assistidoss():
    cursor.execute("SELECT * FROM assistidos")
    return cursor.fetchall()


def retorna_assistidos(id):
    # cur = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM assistidos WHERE id = %s", [id])
    assistidos = cursor.fetchone()
    return assistidos if assistidos else {}


def atualiza_assistidos(assistidos):
    query = "UPDATE assistidos SET id_pessoa = %s, id_filme_serie = %s, status = %s, data_inicio = %s, data_fim = %s" \
            "WHERE id = %s"
    params = [assistidos['id_pessoa'], assistidos['id_filme_serie'], assistidos['status'], assistidos['data_inicio'], assistidos['data_fim']]

    cursor.execute(query, params)


def remove_assistidos(id):
    cursor.execute("DELETE FROM assistidos WHERE id = %s", [id])

