from abc import ABC, abstractmethod

from models.interfaces.observador import Observador


class Observavel(ABC):
    """Classe que representa um objeto observável.

    O observável mantém uma lista de observadores e notifica-os quando seu estado muda.
    Os observadores devem implementar o método update para receber as notificações.
    """

    @abstractmethod
    def adicionar_observador(self, observador: Observador) -> None:
        """Inscreve um observador para receber notificações."""

    @abstractmethod
    def remover_observador(self, observador: Observador) -> None:
        """Desinscreve um observador para não receber mais notificações."""

    @abstractmethod
    def notificar_observadores(self, *args: list, **kwargs: dict) -> None:
        """Notifica todos os observadores sobre uma mudança de estado."""
