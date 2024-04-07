import psycopg2

from supabase import create_client, Client
from settings import SUPABASE_URL, SUPABASE_KEY, SUPABASE_PASSWORD
from csv_reader import get_clientes, get_pagamentos


supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def integrar_csv_bd():
    """
        Função que integra o CSV com a base de dados
        1. integrar csv de clientes
        2. integrar csv de pagamentos
    """
    supabase.table('cliente').delete().gt('id', -1).execute()

    for cliente in get_clientes():
        supabase.table('cliente').insert(cliente).execute()

    for pagamento in get_pagamentos():
        supabase.table('pagamento').insert(pagamento).execute()

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
        cur.execute("""
            SELECT cliente_id, SUM(valor) AS total_nao_pago 
            FROM pagamento
            WHERE NOT foi_pago
            GROUP BY cliente_id
            ORDER BY total_nao_pago DESC;
        """)
        for result in cur.fetchall():
            devedores.append({
                'cliente_id': result[0],
                'valor': result[1]
            })

        cur.close()

    return devedores

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
        cur.execute("""
            SELECT cliente_id, SUM(valor) AS total_pago 
            FROM pagamento
            WHERE foi_pago
            GROUP BY cliente_id
            ORDER BY total_pago DESC;
        """)
        for result in cur.fetchall():
            pagamentos_pagos.append({
                'cliente_id': result[0],
                'valor': result[1]
            })

        cur.close()

    return pagamentos_pagos

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
        cur.execute("""
            SELECT data, 
                SUM(CASE WHEN foi_pago THEN 0 ELSE valor END) AS valor_a_receber,
                SUM(CASE WHEN foi_pago THEN valor ELSE 0 END) AS valor_recebido
            FROM pagamento
            GROUP BY data
            ORDER BY data;
        """)
        for result in cur.fetchall():
            pagamentos_por_dia.append({
                'data': result[0].strftime('%d/%m/%Y'),
                'valor_a_receber': result[1],
                'valor_recebido': result[2],
                'saldo_do_dia': result[2] - result[1]
            })
        cur.close()

    return pagamentos_por_dia

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
