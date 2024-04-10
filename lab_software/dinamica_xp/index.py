import pandas as pd

from front import rich_pagamentos_por_dia, rich_pagamentos_pagos, rich_devedores
import db_manager

CLIENTES_CSV = 'assets/clientes.csv'
PAGAMENTOS_CSV = 'assets/pagamentos.csv'

CLIENTES_FRAME = pd.read_csv(
    CLIENTES_CSV, index_col=False, sep=';', encoding='utf-8', header=0)

PAGAMENTOS_FRAME = pd.read_csv(
    PAGAMENTOS_CSV, index_col=False, sep=';', encoding='utf-8', header=0)


def listar_devedores():
    """
        Lista os devedores
    """
    devedores = db_manager.get_devedores()
    rich_devedores(devedores)


def listar_pagamentos_pagos():
    """
        Lista os pagamentos pagos
    """
    pagamentos_pagos = db_manager.get_pagamentos_pagos()
    rich_pagamentos_pagos(pagamentos_pagos)


def listar_pagamentos_por_dia():
    """
        Lista os pagamentos por dia
    """
    pagamentos_por_dia = db_manager.get_pagamentos_por_dia()
    rich_pagamentos_por_dia(pagamentos_por_dia)


if __name__ == '__main__':
    print('Sistema de cobrança!')
    print('===================')

    map_opcoes = {
        '1': listar_devedores,
        '2': listar_pagamentos_pagos,
        '3': listar_pagamentos_por_dia,
        '4': db_manager.integrar_csv_bd,
    }

    on_menu = True
    while on_menu:
        print('AÇÕES:')
        print('1 - Listar devedores')
        print('2 - Listar pagamentos pagos')
        print('3 - Listar pagamentos por dia')
        print('4 - Importar CSV para base de dados')
        print('5 - Sair')
        opcao = input('Escolha uma ação: ')
        action = map_opcoes.get(opcao, None)
        if action:
            action()
            input('Pressione ENTER para continuar...')
        else:
            on_menu = False
            print('Saindo...')
