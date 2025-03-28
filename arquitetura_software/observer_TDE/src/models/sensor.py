import random
import time

from models.interfaces.observavel import Observavel


class SensorClimatico:
    """Responsável por coletar dados climáticos."""

    def __init__(self) -> None:
        """Inicializa o sensor climático."""
        self._notificador: Observavel = None
        self._temperatura_atual: float = None
        self._humidade_atual: float = None
        self._pressao_atual: float = None

    def coletar(self) -> None:
        """Coleta dados de temperatura, humidade e pressão."""
        for _ in range(10):
            self._temperatura_atual = self._gerar_numero(0.0, 35.0)
            self._humidade_atual = self._gerar_numero(10.0, 100.0)
            self._pressao_atual = self._gerar_numero(900, 1100)

            self._notificador.dados_mudaram()

            time.sleep(1)

    def _gerar_numero(self, min_num: int, max_num: int) -> int:
        """Gera um número aleatório entre min e max."""
        return random.random() * (max_num - min_num) + min_num

    def set_notificador_climatico(self, notificador: Observavel) -> None:
        """Define notificador climático.

        O notificador climático é responsável por propagar os dados que se modificam.
        """
        self._notificador = notificador

    def get_humidade_atual(self) -> float:
        """Retorna a humidade atual."""
        return self._humidade_atual

    def get_pressao_atual(self) -> float:
        """Retorna a pressão atual."""
        return self._pressao_atual

    def get_temperatura_atual(self) -> float:
        """Retorna a temperatura atual."""
        return self._temperatura_atual
