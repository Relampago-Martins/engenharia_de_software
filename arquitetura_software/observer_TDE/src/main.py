import threading
import time
import tkinter as tk

from models.notificador_climatico import NotificadorClimatico
from models.sensor import SensorClimatico
from ui.botao import BotaoInscricao
from ui.display_clima import DisplayClima
from ui.display_media_clima import DisplayMediaClima


def coletar_dados_periodicamente(sensor: "SensorClimatico", intervalo: int = 2) -> None:
    """Coleta dados do sensor em intervalos regulares."""
    while True:
        sensor.coletar()
        time.sleep(intervalo)


if __name__ == "__main__":
    sensor = SensorClimatico()
    notificador = NotificadorClimatico(sensor)
    sensor.set_notificador_climatico(notificador)

    root = tk.Tk()
    root.title("Sistema de Monitoramento Climático")

    # Criação dos frames para os displays lado a lado
    frame_clima = tk.Frame(root, borderwidth=2, relief="groove")
    frame_media = tk.Frame(root, borderwidth=2, relief="groove")
    frame_clima.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
    frame_media.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

    # Instancia os displays usando os frames criados
    display_clima = DisplayClima(frame_clima, notificador)
    display_media = DisplayMediaClima(frame_media, notificador)

    # Cria o botão único de inscrição abaixo dos displays
    def toggle_subscription(inscrito: bool) -> None:
        """Alterna a inscrição dos displays no notificador."""
        if inscrito:
            notificador.adicionar_observador(display_clima)
            notificador.adicionar_observador(display_media)
            print("Displays inscritos.")
        else:
            notificador.remover_observador(display_clima)
            notificador.remover_observador(display_media)
            print("Displays desinscritos.")

    botao_inscricao = BotaoInscricao(root, linha=1, callback=toggle_subscription)
    botao_inscricao.botao.grid(row=1, column=0, columnspan=2, pady=10)

    # Inicia a thread de coleta dos dados
    thread_coleta = threading.Thread(
        target=coletar_dados_periodicamente,
        args=(sensor,),
        daemon=True,
    )
    thread_coleta.start()

    root.mainloop()
