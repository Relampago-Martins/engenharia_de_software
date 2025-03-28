import threading
import time
import tkinter as tk

from models.notificador_climatico import NotificadorClimatico
from models.sensor import SensorClimatico
from ui.display_clima import DisplayClima


def coletar_dados_periodicamente(
    sensor: SensorClimatico,
    intervalo: int = 2,
) -> None:
    """Collects data from the sensor at regular intervals."""
    while True:
        sensor.coletar()
        time.sleep(intervalo)  # Wait for specified interval before next collection


if __name__ == "__main__":
    sensor = SensorClimatico()
    notificador = NotificadorClimatico(sensor)
    sensor.set_notificador_climatico(notificador)

    root = tk.Tk()
    info_clima = DisplayClima(root)

    notificador.adicionar_observador(info_clima)

    # Create and start the data collection thread
    thread_coleta = threading.Thread(
        target=coletar_dados_periodicamente,
        args=(sensor,),
        daemon=True,
    )
    thread_coleta.start()

    # Main thread runs the UI loop
    root.mainloop()
