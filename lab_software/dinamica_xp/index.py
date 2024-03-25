import pandas as pd

CLIENTES_CSV = 'assets/clientes.csv'
PAGAMENTOS_CSV = 'assets/pagamentos.csv'

clientes_frame = pd.read_csv(
    CLIENTES_CSV, index_col=False, sep=';', encoding='utf-8', header=0)

pagamentos_frame = pd.read_csv(
    PAGAMENTOS_CSV, index_col=False, sep=';', encoding='utf-8', header=0)


def get_devedores(pagamentos_df, clientes_df):
    """
    Retorna uma lista de dicionários com os devedores e seus respectivos valores
    devedores_list = [
        { 'cliente_id': 1, 'valor': 100.0},
    ]
    clientes_list = [
        { 'id': 1, 'nome': 'Fulano'},
    ]
    """
    devedores_list = pagamentos_df[pagamentos_df['foi_pago'].str.contains('f')]
    devedores_list = devedores_list.groupby(['cliente_id'], as_index=False)['valor'].sum()
    devedores_list = devedores_list.sort_values('valor', ascending=False).to_dict('records')

    clientes_list = clientes_df[['id', 'nome']]
    clientes_list = clientes_list.to_dict('records')

    return devedores_list, clientes_list

def float_to_currency(value):
    """
    Converte um valor float para uma string no formato de moeda brasileira
    18.0 -> R$ 18,00
    """
    return f'R$ {value:,.2f}'.replace(',', '#').replace('.', ',').replace('#', '.')

if __name__ == '__main__':
    devedores, clientes = get_devedores(pagamentos_frame, clientes_frame)

    for devedor in devedores:
        for cliente in clientes:
            if devedor['cliente_id'] == cliente['id']:
                devedor['cliente_nome'] = cliente['nome']
                break

    for devedor in devedores:
        print(f"{devedor['cliente_nome']} deve " \
            f"{float_to_currency(devedor['valor'])}")
