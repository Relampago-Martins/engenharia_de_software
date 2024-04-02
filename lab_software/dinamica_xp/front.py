from rich.console import Console
from rich.table import Table


def rich_pagamentos_por_dia(pagamentos_por_dia):
    """
        Função que exibe os pagamentos por dia em uma tabela
        utilizando a biblioteca rich
    """
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Data")
    table.add_column("Valor a Receber")
    table.add_column("Valor Recebido")
    table.add_column("Saldo do Dia")

    for pag in pagamentos_por_dia:
        table.add_row(
            pag["data"],
            f'R$ {pag["valor_a_receber"]}',
            f'R$ {pag["valor_recebido"]}',
            f'R$ {pag["saldo_do_dia"]}',
        )

    titulo = "\n\nPagamentos por Dia"
    console.print(f"[bold cyan]{titulo}[/bold cyan]")
    console.print(table)

def rich_pagamentos_pagos(pagamentos_pagos):
    """
        Função que exibe os pagamentos pagos em uma tabela
        utilizando a biblioteca rich
    """
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Cliente")
    table.add_column("Valor")

    for pag in pagamentos_pagos:
        table.add_row(
            pag["cliente_nome"],
            f'R$ {pag["valor"]}',
        )

    titulo = "\n\nPagamentos Pagos"
    console.print(f"[bold cyan]{titulo}[/bold cyan]")
    console.print(table)

def rich_devedores(devedores):
    """
        Função que exibe os devedores em uma tabela
        utilizando a biblioteca rich
    """
    console = Console()
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Cliente")
    table.add_column("Valor")

    for devedor in devedores:
        table.add_row(
            devedor["cliente_nome"],
            f'R$ {devedor["valor"]}',
        )

    titulo = "\n\nDevedores"
    console.print(f"[bold cyan]{titulo}[/bold cyan]")
    console.print(table)
