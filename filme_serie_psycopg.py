from psycopg_connection import cursor

def insere_filme_serie(dados_filme_serie):
    cursor.execute("INSERT INTO filme_serie (tipo, nome, temporada,"
                   "episodio)"
                   "VALUES (%s, %s, %s, %s)",
                   (
                       dados_filme_serie['tipo'],
                       dados_filme_serie['nome'],
                       dados_filme_serie['temporada'],
                       dados_filme_serie['episodio'],
                   )
                   )


def retorna_filme_series():
    cursor.execute("SELECT * FROM filme_serie")
    return cursor.fetchall()


def retorna_filme_serie(id):
    # cur = conn.cursor(cursor_factory=RealDictCursor)
    cursor.execute("SELECT * FROM filme_serie WHERE id = %s", [id])
    filme_serie = cursor.fetchone()
    return filme_serie if filme_serie else {}


def atualiza_filme_serie(filme_serie):
    query = "UPDATE filme_serie SET nome = %s, tipo = %s, temporada = %s, episodio = %s" \
            "WHERE id = %s"
    params = [filme_serie['nome'], filme_serie['tipo'], filme_serie['temporada'], filme_serie['episodio']]

    cursor.execute(query, params)


def remove_filme_serie(id):
    cursor.execute("DELETE FROM filme_serie WHERE id = %s", [id])

