from models.interfaces.observador import Observador
from models.interfaces.observavel import Observavel
from models.sensor import SensorClimatico


class NotificadorClimatico(Observavel):
    """Responsável por notifcar mudanças de dados climáticos.

    Objetos que queiram obter dados climáticos atualizados devem
    se inscrever como observadores nesse objeto.
    """

    def __init__(self, equipamento: SensorClimatico) -> None:
        """Inicializa a lista de observadores."""
        self._observadores: list[Observador] = []
        self._equipamento: SensorClimatico = equipamento

        # Dados climáticos
        self._temperatura: float = None
        self._humidade: float = None
        self._pressao: float = None

    def adicionar_observador(self, observador: Observador) -> None:
        """Inscreve um observador para receber notificações."""
        self._observadores.append(observador)

    def remover_observador(self, observador: Observador) -> None:
        """Desinscreve um observador para não receber mais notificações."""
        self._observadores.remove(observador)

    def notificar_observadores(self) -> None:
        """Notifica todos os observadores sobre uma mudança de estado."""
        for observador in self._observadores:
            observador.atualizar(
                self._temperatura,
                self._humidade,
                self._pressao,
            )

    def dados_mudaram(self) -> None:
        """Notifica os observadores que os dados mudaram."""
        self._temperatura = self._equipamento.get_temperatura_atual()
        self._humidade = self._equipamento.get_humidade_atual()
        self._pressao = self._equipamento.get_pressao_atual()

        self.notificar_observadores()
