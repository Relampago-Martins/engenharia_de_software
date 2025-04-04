from __future__ import annotations

import tkinter as tk


class BotaoInscricao:
    """Classe que representa um botão de inscrição à eventos."""

    def __init__(
        self,
        root: tk.Tk,
        linha: int,
        callback: callable | None = None,
    ) -> None:
        """Inicializa o botão de inscrição."""
        self.ativado = False
        self.callback = callback
        self.botao = tk.Button(root, text="Se inscrever", command=self.toggle)
        self.botao.grid(row=linha, column=0, columnspan=2, pady=20)

    def toggle(self) -> None:
        """Alterna o estado de inscrição do botão."""
        self.ativado = not self.ativado
        novo_texto = "Desinscrever-se" if self.ativado else "Se inscrever"
        self.botao.config(text=novo_texto)
        print(f"Botão ativado? {self.ativado}")
        if self.callback:
            self.callback(self.ativado)
