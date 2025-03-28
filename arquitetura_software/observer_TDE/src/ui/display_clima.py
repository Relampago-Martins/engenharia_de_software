import tkinter as tk

from models.interfaces.observador import Observador
from ui.botao import BotaoInscricao
from ui.text import Text


class DisplayClima(Observador):
    """Pinta uma tela com as informações do clima atualizadas."""

    def __init__(self, root: tk.Tk):
        """Construtor da classe DisplayClima."""
        self.root = root
        self.root.title("Interface de Inscrição")

        # Criando os objetos de parâmetro
        self.parametro1 = Text(root, "Temperatura", "0", linha=0)
        self.parametro4 = Text(root, "Humidade", "0", linha=3)
        self.parametro5 = Text(root, "Pressão", "0", linha=4)

        # Botão de inscrição como objeto
        self.botao_inscricao = BotaoInscricao(
            root,
            linha=6,
        )

    def atualizar(self, temperatura: float, umidade: float, pressao: float) -> None:
        """Atualiza a tela com as informações do clima."""
        self._temperatura = temperatura
        self._humidade = umidade

        self.parametro1.label_valor.config(text=f"{temperatura:.2f} °C")
        self.parametro4.label_valor.config(text=f"{umidade:.2f} %")
        self.parametro5.label_valor.config(text=f"{pressao:.2f} hPa")

        self.root.update_idletasks()
        self.root.update()
