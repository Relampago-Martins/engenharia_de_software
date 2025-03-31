import tkinter as tk

from models.interfaces.observador import Observador
from models.interfaces.observavel import Observavel
from ui.text import Text


class DisplayClima(Observador):
    """Display que apresenta as condições atuais do clima."""

    def __init__(self, parent: tk.Tk, notificador: Observavel) -> None:
        """Inicializa o display com os widgets necessários.

        Args:
        ----
            parent: O widget pai onde os elementos serão colocados.
            notificador: O objeto que notifica as atualizações.

        """
        self.parent = parent
        self.notificador = notificador

        # Cria os widgets para exibir os dados atuais
        self.parametro1 = Text(parent, "Temperatura", "0", linha=0)
        self.parametro4 = Text(parent, "Humidade", "0", linha=1)
        self.parametro5 = Text(parent, "Pressão", "0", linha=2)

    def atualizar(self, temperatura: float, umidade: float, pressao: float) -> None:
        """Atualiza a tela com as informações do clima."""
        self.parametro1.label_valor.config(text=f"{temperatura:.2f} °C")
        self.parametro4.label_valor.config(text=f"{umidade:.2f} %")
        self.parametro5.label_valor.config(text=f"{pressao:.2f} hPa")
        self.parent.update_idletasks()
