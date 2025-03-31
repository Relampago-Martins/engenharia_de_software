from abc import ABC, abstractmethod


class Observador(ABC):
    """classe que se inscreve em um observável.

    O observador é notificado quando o estado do observável muda.
    O observador deve implementar o método update para receber as notificações.
    """

    @abstractmethod
    def atualizar(self, *args: list, **kwargs: dict) -> None:
        """Método chamado quando o estado do observável muda."""


class ObservadorCoringa(Observador):
    """Se inscreve em um observável e aplica uma callback qualquer."""

    def __init__(self, callback: callable) -> None:
        """Inicializa o observador com uma callback opcional."""
        self.callback = callback

    def atualizar(self, *args: list, **kwargs: dict) -> None:
        """Método chamado quando o estado do observável muda."""
        if self.callback:
            self.callback(*args, **kwargs)
