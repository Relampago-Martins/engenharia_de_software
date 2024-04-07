import pandas as pd
from utils import converter_formato_data_usa


def get_clientes():
    """
    Retorna uma lista de dicionários com os clientes
    clientes_list = [
        { 'id': 1, 'nome': 'Fulano'},
    ]
    """
    clientes_frame = pd.read_csv(
    'assets/clientes.csv', index_col=False, sep=';', encoding='utf-8', header=0)
    return clientes_frame[['id', 'nome']].to_dict('records')

def get_pagamentos():
    """
    Retorna uma lista de dicionários com os pagamentos e seus respectivos valores
    devedores_list = [
        { 'cliente_id': 1, 'data': 17/12/1997, 'valor': 100.0, 'foi_pago': True},
    ]
    """
    pagamentos_frame: pd.DataFrame = pd.read_csv(
    'assets/pagamentos.csv', index_col=False, sep=';', encoding='utf-8', header=0)

    pagamentos_frame['data'] = pagamentos_frame['data'].apply(converter_formato_data_usa)
    pagamentos_frame['foi_pago'] = pagamentos_frame['foi_pago'].apply(lambda x: x == 't')

    return pagamentos_frame[['cliente_id', 'data', 'valor', 'foi_pago']].to_dict('records')
