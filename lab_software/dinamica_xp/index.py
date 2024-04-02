import pandas as pd

from utils import float_to_currency, converter_formato_data
from front import rich_pagamentos_por_dia, rich_pagamentos_pagos, rich_devedores

CLIENTES_CSV = 'assets/clientes.csv'
PAGAMENTOS_CSV = 'assets/pagamentos.csv'

CLIENTES_FRAME = pd.read_csv(
    CLIENTES_CSV, index_col=False, sep=';', encoding='utf-8', header=0)

PAGAMENTOS_FRAME = pd.read_csv(
    PAGAMENTOS_CSV, index_col=False, sep=';', encoding='utf-8', header=0)


def get_clientes():
    """
    Retorna uma lista de dicionários com os clientes
    clientes_list = [
        { 'id': 1, 'nome': 'Fulano'},
    ]
    """
    return CLIENTES_FRAME[['id', 'nome']].to_dict('records')

def get_devedores(pagamentos_df):
    """
    Retorna uma lista de dicionários com os devedores e seus respectivos valores
    devedores_list = [
        { 'cliente_id': 1, 'valor': 100.0},
    ]
    """
    devedores_list = pagamentos_df[pagamentos_df['foi_pago'].str.contains('f')]
    devedores_list = devedores_list.groupby(['cliente_id'], as_index=False)['valor'].sum()
    devedores_list = devedores_list.sort_values('valor', ascending=False).to_dict('records')

    return devedores_list

def get_pagamentos_pagos(pagamentos_df):
    """
    Retorna uma lista de dicionários com os pagamentos pagos
    pagamentos_pagos_list = [
        { 'cliente_id': 1, 'valor': 100.0},
    ]
    """
    pagamentos_pagos_list = pagamentos_df[pagamentos_df['foi_pago'].str.contains('t')]
    pagamentos_pagos_list = pagamentos_pagos_list.groupby(
                                                ['cliente_id'], as_index=False)['valor'].sum()
    pagamentos_pagos_list = pagamentos_pagos_list.sort_values(
                                                'valor', ascending=False).to_dict('records')

    return pagamentos_pagos_list

def get_pagamentos_por_dia(pagamentos_df):
    """
    Retorna uma lista de dicionários com os pagamentos por dia.

    pagamentos_por_dia_list = [
        {
            'data': 31052014, 'valor_a_receber': 20.0,
            'valor_recebido': 352.0, 'saldo_do_dia': 332.0
        },
        {
            'data': 31072014, 'valor_a_receber': 86.67,
            'valor_recebido': 152.0, 'saldo_do_dia': 65.33
        },
    ]
    """
    devedores_list = pagamentos_df[pagamentos_df['foi_pago'].str.contains('f')]
    devedores_list = devedores_list.groupby(['data'], as_index=False)['valor'].sum()
    devedores_list.rename(columns={'valor': 'valor_a_receber'}, inplace=True)

    pagadores_list = pagamentos_df[pagamentos_df['foi_pago'].str.contains('t')]
    pagadores_list = pagadores_list.groupby(['data'], as_index=False)['valor'].sum()
    pagadores_list.rename(columns={'valor': 'valor_recebido'}, inplace=True)

    # une os devedores e pagadores com base na data
    pagamentos_por_dia_list = pd.merge(devedores_list, pagadores_list, on='data', how='outer')
    pagamentos_por_dia_list.fillna(0, inplace=True)

    # faz tratamento de datas e ordena
    pagamentos_por_dia_list['data'] = pagamentos_por_dia_list['data'].apply(converter_formato_data)
    pagamentos_por_dia_list['data'] = pd.to_datetime(
        pagamentos_por_dia_list['data'], format='%d/%m/%Y')
    pagamentos_por_dia_list = pagamentos_por_dia_list.sort_values(by='data')
    pagamentos_por_dia_list['data'] = pagamentos_por_dia_list['data'].dt.strftime('%d/%m/%Y')

    pagamentos_por_dia_list['saldo_do_dia'] = pagamentos_por_dia_list['valor_recebido'] - \
        pagamentos_por_dia_list['valor_a_receber']

    return pagamentos_por_dia_list.to_dict('records')

def listar_devedores():
    """
        Lista os devedores
    """
    devedores = get_devedores(PAGAMENTOS_FRAME)
    for devedor in devedores:
        for cliente in get_clientes():
            if devedor['cliente_id'] == cliente['id']:
                devedor['cliente_nome'] = cliente['nome']
                break

    rich_devedores(devedores)


def listar_pagamentos_pagos():
    """
        Lista os pagamentos pagos
    """
    pagamentos_pagos = get_pagamentos_pagos(PAGAMENTOS_FRAME)
    for pagamento_pago in pagamentos_pagos:
        for cliente in get_clientes():
            if pagamento_pago['cliente_id'] == cliente['id']:
                pagamento_pago['cliente_nome'] = cliente['nome']
                break

    rich_pagamentos_pagos(pagamentos_pagos)


def listar_pagamentos_por_dia():
    """
        Lista os pagamentos por dia
    """
    pagamentos_por_dia = get_pagamentos_por_dia(PAGAMENTOS_FRAME)
    rich_pagamentos_por_dia(pagamentos_por_dia)


if __name__ == '__main__':
    print('Sistema de cobrança!')
    print('===================')
    print('AÇÕES:')
    print('1 - Listar devedores')
    print('2 - Listar pagamentos pagos')
    print('3 - Listar pagamentos por dia')
    print('4 - Sair')
    opcao = input('Escolha uma ação: ')

    map_opcoes = {
        '1': listar_devedores,
        '2': listar_pagamentos_pagos,
        '3': listar_pagamentos_por_dia,
        '4': exit,
    }

    if opcao in map_opcoes:
        map_opcoes[opcao]()
    else:
        print('Opção inválida')
        exit(1)
