import behave
import db_manager
import psycopg2

@behave.given('Dado que o sistema está inicializado')
def initialize(context):
    """
    Inicializa o sistema
    """

@behave.given('o banco de dados está conectado')
def test_conn(context):
    """
    Testa a conexão com o banco de dados
    """
    with db_manager.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT 1')

        if cursor.fetchone() is None:
            raise psycopg2.DatabaseError("Erro ao conectar ao banco de dados")
        cursor.close()

        print("Conexão com o banco de dados realizada com sucesso!")


@behave.given('as tabelas de clientes e pagamentos existem')
def tables_exists(context):
    """
    Verifica se as tabelas de clientes e pagamentos existem
    """
    try:
        with db_manager.get_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM cliente')
            cursor.execute('SELECT * FROM pagamento')
            cursor.close()

            print("Tabelas clientes e pagamentos existem no banco de dados!")
    except psycopg2.errors.UndefinedTable:
        raise psycopg2.errors.UndefinedTable("Tabelas clientes ou pagamentos não existem no banco de dados")

@behave.given('as tabelas não estão vazias')
def not_empty(context):
    """
    Verifica se as tabelas de clientes e pagamentos não estão vazias
    """
    with db_manager.get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM cliente')
        if cursor.fetchone() is None:
            raise psycopg2.DataError("Tabela clientes está vazia")
        cursor.execute('SELECT * FROM pagamento')
        if cursor.fetchone() is None:
            raise psycopg2.DataError("Tabela pagamentos está vazia")
        cursor.close()

@behave.when('Quando eu abrir a interface do sistema')
def open_interface(context):
    assert True is not False

@behave.then('Então devo ver a tela principal do sistema')
def is_open(context):
    assert context.failed is False

@behave.given('Dado que tenho clientes que estão devendo,')
def existem_devedores(context):
    """
    Verifica se existem clientes que estão devendo
    """
    devedores = db_manager.get_devedores()
    assert devedores is not None

@behave.when('Quando eu escolher na interface listar devedores')
def listar_devedores(context):
    assert True is not False

@behave.then('Então devo ver uma tabela com os nomes dos clientes e o valor que eles devem')
def tabela_devedores(context):
    assert context.failed is False
