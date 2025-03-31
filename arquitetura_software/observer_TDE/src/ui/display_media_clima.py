import tkinter as tk

from models.interfaces.observador import Observador
from models.interfaces.observavel import Observavel
from ui.text import Text


class DisplayMediaClima(Observador):
    """Display que apresenta as estatísticas.

    - Média de temperatura
    - Média de umidade
    - Temperatura máxima
    - Temperatura mínima
    """

    def __init__(self, parent: tk.Tk, notificador: Observavel) -> None:
        """Inicializa o display com os widgets necessários."""
        self.parent = parent
        self.notificador = notificador

        # Criação dos elementos de texto na interface
        self.text_media_temp = Text(parent, "Temp Média", "0", linha=0)
        self.text_media_umidade = Text(parent, "Umidade Média", "0", linha=1)
        self.text_temp_max = Text(parent, "Temp Máxima", "0", linha=2)
        self.text_temp_min = Text(parent, "Temp Mínima", "0", linha=3)

        # Variáveis para acumular os dados
        self.soma_temp = 0.0
        self.soma_umidade = 0.0
        self.contador = 0
        self.temp_max = None
        self.temp_min = None

    def atualizar(self, temperatura: float, umidade: float, pressao: float) -> None:
        self.soma_temp += temperatura
        self.soma_umidade += umidade
        self.contador += 1

        # Calcula as médias
        media_temp = self.soma_temp / self.contador
        media_umidade = self.soma_umidade / self.contador

        # Define a temperatura máxima e mínima
        if self.temp_max is None or temperatura > self.temp_max:
            self.temp_max = temperatura
        if self.temp_min is None or temperatura < self.temp_min:
            self.temp_min = temperatura

        # Atualiza os widgets da interface
        self.text_media_temp.label_valor.config(text=f"{media_temp:.2f} °C")
        self.text_media_umidade.label_valor.config(text=f"{media_umidade:.2f} %")
        self.text_temp_max.label_valor.config(text=f"{self.temp_max:.2f} °C")
        self.text_temp_min.label_valor.config(text=f"{self.temp_min:.2f} °C")
        self.parent.update_idletasks()
