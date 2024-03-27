from datetime import datetime


def float_to_currency(value):
    """
    Converte um valor float para uma string no formato de moeda brasileira
    18.0 -> R$ 18,00
    """
    return f'R$ {value:,.2f}'.replace(',', '#').replace('.', ',').replace('#', '.')

def int_to_date(date_int):
    """
    Converte um valor inteiro para uma string no formato de data
    20210101 -> 01/01/2021
    """
    date_str = str(date_int)
    
    return datetime.strptime( date_str, '%Y%m%d').strftime('%d/%m/%Y')
