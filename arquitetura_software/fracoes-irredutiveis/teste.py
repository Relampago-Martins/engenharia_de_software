"""Testes para a calculadora de frações irredutíveis."""

import unittest

from index import CalculadoraDeFracoes, Fracao


class TestCalculadoraDeFracoes(unittest.TestCase):
    """Verifica se os cálculos de frações estão corretos."""

    def test_calcula_irredutivel(self) -> None:
        """Faz o teste de cálculo da fração irredutível entre duas frações.

        4/12 + 12/16 deve resultar em 13/12
        """
        calculadora = CalculadoraDeFracoes()
        fracao1 = Fracao(4, 12)
        fracao2 = Fracao(12, 16)
        resultado = calculadora.calcula_irredutivel(fracao1, fracao2)

        self.assertEqual(resultado.numerador, 13)
        self.assertEqual(resultado.denominador, 12)

    def test_soma_fracoes(self) -> None:
        """Faz o teste de soma de duas frações.

        1/2 + 1/3 deve resultar em 5/6
        """
        calculadora = CalculadoraDeFracoes()
        fracao1 = Fracao(1, 2)
        fracao2 = Fracao(1, 3)
        resultado = calculadora.soma_fracoes(fracao1, fracao2)

        self.assertEqual(resultado.numerador, 5)
        self.assertEqual(resultado.denominador, 6)


if __name__ == "__main__":
    unittest.main()
