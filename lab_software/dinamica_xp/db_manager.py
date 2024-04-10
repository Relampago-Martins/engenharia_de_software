import psycopg2
import sqlite3

from supabase import create_client, Client
from settings import SUPABASE_URL, SUPABASE_KEY, SUPABASE_PASSWORD
from csv_reader import get_clientes as get_clientes_csv, get_pagamentos


supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def integrar_csv_bd():
    """
        Função que integra o CSV com a base de dados
        1. integrar csv de clientes
        2. integrar csv de pagamentos
    """
    supabase.table('cliente').delete().gt('id', -1).execute()

    for cliente in get_clientes_csv():
        supabase.table('cliente').insert(cliente).execute()

    for pagamento in get_pagamentos():
        supabase.table('pagamento').insert(pagamento).execute()

def get_clientes():
    """
    Retorna uma lista de dicionários com os clientes
    clientes_list = [
        { 'id': 1, 'nome': 'Fulano'},
    ]
    """
    response = supabase.table('cliente').select('*').execute()
    return response.data

def get_devedores():
    """
    Retorna uma lista de dicionários com os devedores e seus respectivos valores,
    a partir do banco de dados
    devedores_list = [
        { 'cliente_id': 1, 'valor': 100.0},
    ]
    """
    devedores = []
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(get_devedores_sql())
        for result in cur.fetchall():
            devedores.append({
                'cliente_nome': result[1],
                'valor': result[2]
            })

        cur.close()

    return devedores

def get_devedores_sql():
    return """
        SELECT cliente_id, nome as cliente_nome, SUM(valor) AS total_nao_pago 
        FROM pagamento, cliente
        WHERE pagamento.cliente_id = cliente.id
            AND NOT foi_pago
        GROUP BY cliente_id, cliente_nome
        ORDER BY total_nao_pago DESC;
    """


def get_pagamentos_pagos():
    """
    Retorna uma lista de dicionários com os pagamentos pagos,
    a partir do banco de dados
    pagamentos_pagos_list = [
        { 'cliente_id': 1, 'valor': 100.0},
    ]
    """
    pagamentos_pagos = []
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(get_pagamentos_pagos_sql())
        for result in cur.fetchall():
            pagamentos_pagos.append({
                'cliente_id': result[0],
                'cliente_nome': result[1],
                'valor': result[2]
            })

        cur.close()

    return pagamentos_pagos

def get_pagamentos_pagos_sql():
    return """
        SELECT cliente_id, nome as cliente_nome, SUM(valor) AS total_pago 
        FROM pagamento, cliente
        WHERE pagamento.cliente_id = cliente.id
            AND foi_pago
        GROUP BY cliente_id, cliente_nome
        ORDER BY total_pago DESC;
    """

def get_pagamentos_por_dia():
    """
    Retorna uma lista de dicionários com os pagamentos por dia,
    a partir do banco de dados

    pagamentos_por_dia_list = [
        {
            'data': 31/05/2014, 'valor_a_receber': 20.0,
            'valor_recebido': 352.0, 'saldo_do_dia': 332.0
        },
        {
            'data': 31/07/2014, 'valor_a_receber': 86.67,
            'valor_recebido': 152.0, 'saldo_do_dia': 65.33
        },
    ]
    """
    pagamentos_por_dia = []
    with get_connection() as conn:
        cur = conn.cursor()
        cur.execute(get_pagamentos_por_dia_sql())
        for result in cur.fetchall():
            pagamentos_por_dia.append({
                'data': result[0].strftime('%d/%m/%Y'),
                'valor_a_receber': result[1],
                'valor_recebido': result[2],
                'saldo_do_dia': result[2] - result[1]
            })
        cur.close()

    return pagamentos_por_dia

def get_pagamentos_por_dia_sql():
    return """
        SELECT data, 
            SUM(CASE WHEN foi_pago THEN 0 ELSE valor END) AS valor_a_receber,
            SUM(CASE WHEN foi_pago THEN valor ELSE 0 END) AS valor_recebido
        FROM pagamento
        GROUP BY data
        ORDER BY data;
    """

def get_connection():
    """
    Retorna uma conexão com o banco de dados
    """
    return psycopg2.connect(
        user='postgres.obtulqhtzsrfjhzynsod',
        password=SUPABASE_PASSWORD,
        host='aws-0-sa-east-1.pooler.supabase.com',
        port=5432,
        dbname='postgres',
    )


class InMemoryDB:
    def __init__(self):
        self.conn = sqlite3.connect(":memory:")
        self.create_tables()
        self.populate_tables()

    def create_tables(self):
        cursor = self.conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cliente (
            id INTEGER PRIMARY KEY,
            nome VARCHAR(60)
        )
        """)

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS pagamento (
            id INTEGER PRIMARY KEY,
            cliente_id INTEGER,
            valor DOUBLE PRECISION,
            foi_pago BOOLEAN,
            data DATE,
            FOREIGN KEY (cliente_id) REFERENCES cliente(id)
        )
        """)

        self.conn.commit()

    def populate_tables(self):
        """
            Popula com dados fake
        """
        cursor = self.conn.cursor()

        cursor.execute("""
        INSERT INTO cliente (id, nome) VALUES
        (1, 'João'),
        (2, 'Maria'),
        (3, 'José')
        """)

        cursor.execute("""
        INSERT INTO pagamento (id, cliente_id, valor, foi_pago, data) VALUES
        (1, 1, 100.0, 0, '2021-10-01'),
        (2, 2, 200.0, 1, '2021-10-01'),
        (3, 3, 300.0, 0, '2021-10-01')
        """)

        self.conn.commit()


    def close(self):
        self.conn.close()

    def execute_query(self, query, parameters=None):
        cursor = self.conn.cursor()
        if parameters:
            cursor.execute(query, parameters)
        else:
            cursor.execute(query)
        self.conn.commit()
        return cursor.fetchall()
