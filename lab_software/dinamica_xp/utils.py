from datetime import datetime


def float_to_currency(value):
    """
    Converte um valor float para uma string no formato de moeda brasileira
    18.0 -> R$ 18,00
    """
    return f'R$ {value:,.2f}'.replace(',', '#').replace('.', ',').replace('#', '.')

def converter_formato_data(data_int):
    """
        Extrair dia, mês e ano do inteiro original
    """
    dia = data_int // 1000000
    mes = (data_int % 1000000) // 10000
    ano = data_int % 10000

    # Formatar a data e retornar como string
    data_formatada = datetime(ano, mes, dia).strftime('%d/%m/%Y')
    return data_formatada
