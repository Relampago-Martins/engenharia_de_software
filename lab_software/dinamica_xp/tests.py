import unittest
import pandas as pd
from index import get_devedores, float_to_currency

class TestClientesPagamentos(unittest.TestCase):
    """
    Testes para os arquivos clientes.csv e pagamentos.csv

    1. Testar se o arquivo pagamentos.csv foi acessado corretamente
    2. Testar se o arquivo clientes.csv foi acessado corretamente
    3. Testar se pagamentos.csv possui as colunas 'cliente_id', 'valor' e 'foi_pago'
    4. Testar se clientes.csv possui as colunas 'id' e 'nome'
    5. Testar se a função get_devedores retorna uma lista de dicionários
    6. Testar se os aquivos possuem dados além dos cabeçalhos
    7. Testar se a função float_to_currency retorna o valor correto
    8. Testar se a função get_devedores retorna o nome do cliente
    9. Testar se a função get_devedores retorna o valor correto do cliente

    """
    def setUp(self):
        self.CLIENTES_CSV = 'assets/clientes.csv'
        self.PAGAMENTOS_CSV = 'assets/pagamentos.csv'
        self.clientes_frame = pd.read_csv(
            self.CLIENTES_CSV, index_col=False, sep=';', encoding='utf-8')
        self.pagamentos_frame = pd.read_csv(
            self.PAGAMENTOS_CSV, index_col=False, sep=';', encoding='utf-8')

    def test_acesso_clientes_csv(self):
        """ Testar se o arquivo clientes.csv foi acessado corretamente """
        frame = pd.DataFrame()
        try:
            frame = pd.read_csv(
                self.CLIENTES_CSV, index_col=False, sep=';', encoding='utf-8')
        except FileNotFoundError:
            pass

        self.assertFalse(frame.empty)

    def test_acesso_pagamentos_csv(self):
        """ Testar se o arquivo pagamentos.csv foi acessado corretamente """
        frame = pd.DataFrame()
        try:
            frame = pd.read_csv(
                self.PAGAMENTOS_CSV, index_col=False, sep=';', encoding='utf-8')
        except FileNotFoundError:
            pass

        self.assertFalse(frame.empty)

    def test_colunas_pagamentos_csv(self):
        """ Testar se pagamentos.csv possui as colunas 'cliente_id', 'valor' e 'foi_pago' """
        expected_columns = ['cliente_id', 'valor', 'foi_pago']
        found_columns = list(self.pagamentos_frame.columns)
        result = all(column in found_columns for column in expected_columns)
        self.assertTrue(result)

    def test_colunas_clientes_csv(self):
        """ Testar se clientes.csv possui as colunas 'id' e 'nome' """
        expected_columns = ['id', 'nome']
        found_columns = list(self.clientes_frame.columns)
        result = all(column in found_columns for column in expected_columns)
        self.assertTrue(result)

    def test_dados_nao_vazios(self):
        """ Testar se os aquivos possuem dados além dos cabeçalhos """
        self.assertTrue(len(self.clientes_frame) > 0, 'clientes.csv está vazio')
        self.assertTrue(len(self.pagamentos_frame) > 0, 'pagamentos.csv está vazio')

    def test_retorno_get_devedores(self):
        """ Testar se a função get_devedores retorna uma lista de dicionários """
        devedores_list = get_devedores(self.pagamentos_frame)
        self.assertIsInstance(devedores_list, list, 'get_devedores não retorna uma lista')
        self.assertTrue(
            all(isinstance(devedor, dict) for devedor in devedores_list),
            'get_devedores não retorna uma lista de dicionários',
        )

    def test_float_to_currency(self):
        """ Testar se a função float_to_currency retorna o valor correto """
        self.assertEqual(float_to_currency(18.0), 'R$ 18,00')

    # def test_nome_cliente_em_devedores(self):
    #     """ Testar se o nome do cliente está presente na lista de devedores """
    #     devedores_list, _ = get_devedores(self.pagamentos_frame, self.clientes_frame)
    #     for devedor in devedores_list:
    #         self.assertTrue('cliente_nome' in devedor)

    # def test_valor_correto_devedores(self):
    #     """ Testar se o valor devido pelo cliente está correto """
    #     devedores_list, _ = get_devedores(self.pagamentos_frame, self.clientes_frame)
    #     for devedor in devedores_list:
    #         cliente_id = devedor['cliente_id']
    #         valor_esperado = self.pagamentos_frame[self.pagamentos_frame['cliente_id'] == cliente_id]['valor'].sum()
    #         self.assertEqual(devedor['valor'], valor_esperado)

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    tests = loader.loadTestsFromTestCase(TestClientesPagamentos)
    suite.addTests(tests)

    runner = unittest.TextTestRunner()
    runner.run(suite)
