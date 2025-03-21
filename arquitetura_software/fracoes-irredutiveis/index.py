class MathUtils:
    """Contém funções matemáticas úteis."""

    @staticmethod
    def calcula_mdc(x: int, y: int) -> int:
        """Calcula o MDC de dois números.

        - MDC = Máximo Divisor Comum;
        - Função implementa algoritmo de Euclides.
        """
        if x < y:
            x, y = y, x

        while y != 0:
            x, y = y, x % y
        return x


class Fracao:
    """Representa uma fração matemática."""

    numerador: int
    denominador: int

    def __init__(self, numerador: int, denominador: int) -> None:
        """Cria uma nova fração."""
        self.numerador = numerador
        self.denominador = denominador

    def __str__(self) -> str:
        """Retorna a representação da fração."""
        return f"\n{self.numerador}\n--\n{self.denominador}"

    def simplifica_fracao(self) -> None:
        """Altera a fração para a forma irredutível."""
        mdc = MathUtils.calcula_mdc(self.numerador, self.denominador)
        self.numerador //= mdc
        self.denominador //= mdc


class CalculadoraDeFracoes:
    """Realiza cálculos com frações."""

    def __init__(self) -> None:
        """Cria uma nova calculadora de frações."""

    def calcula_irredutivel(self, fracao1: Fracao, fracao2: Fracao) -> Fracao:
        """Calcula a fração irredutível de duas frações.

        1. Soma as duas frações.
        2. Simplifica a fração resultante.
        3. Retorna a fração simplificada.
        """
        soma = self.soma_fracoes(fracao1, fracao2)
        soma.simplifica_fracao()

        return soma

    def soma_fracoes(self, fracao1: Fracao, fracao2: Fracao) -> Fracao:
        """Soma duas frações."""
        novo_numerador = (
            fracao1.denominador * fracao2.numerador
            + fracao2.denominador * fracao1.numerador
        )
        novo_denominador = fracao1.denominador * fracao2.denominador

        return Fracao(
            numerador=novo_numerador,
            denominador=novo_denominador,
        )


if __name__ == "__main__":
    calculadora = CalculadoraDeFracoes()
    result = calculadora.calcula_irredutivel(
        Fracao(4, 12),
        Fracao(12, 16),
    )

    print(f"Canculando a fração irredutivel entre 4/12 e 12/16: {result}")
