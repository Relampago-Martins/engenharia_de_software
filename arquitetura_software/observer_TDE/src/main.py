import tkinter as tk

from models.interfaces.observador import ObservadorCoringa
from models.notificador_climatico import NotificadorClimatico
from models.sensor import SensorClimatico
from ui.janela import InscricaoApp

if __name__ == "__main__":
    # root = tk.Tk()
    # app = InscricaoApp(root)
    # root.mainloop()

    sensor = SensorClimatico()
    notificador = NotificadorClimatico(sensor)

    observador = ObservadorCoringa(
        lambda temperatura, humidade, pressao: print(
            f"Temperatura: {temperatura}, Humidade: {humidade}, Pressão: {pressao}",
        ),
    )
    notificador.adicionar_observador(observador)

    sensor.set_notificador_climatico(notificador)
    sensor.coletar()
