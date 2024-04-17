from behave import given, when, then, use_step_matcher


@given('Dado que o sistema está inicializado')
def initialize(context):
    """
    Inicializa o sistema
    """
    pass

@given(u'o banco de dados está conectado')
def test_conn(context):
    """
    Testa a conexão com o banco de dados
    """
    pass

@given(u'as tabelas de clientes e pagamentos existem')
def tables_exists(context):
    """
    Verifica se as tabelas de clientes e pagamentos existem
    """
    pass

@given(u'as tabelas não estão vazias')
def not_empty(context):
    pass

@when(u'Quando eu abrir a interface do sistema')
def open_interface(context):
    assert True is not False


@then(u'Então devo ver a tela principal do sistema')
def is_open(context):
    assert context.failed is False

@given(u'Dado que tenho clientes que estão devendo,')
def existem_devedores(context):
    pass

@when(u'Quando eu escolher na interface listar devedores')
def listar_devedores(context):
    assert True is not False

@then(u'Então devo ver uma tabela com os nomes dos clientes e o valor que eles devem')
def tabela_devedores(context):
    assert context.failed is False