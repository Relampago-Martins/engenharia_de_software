import tkinter as tk


class Text:
    def __init__(self, root, nome, valor, linha):
        self.nome = nome
        self.valor = valor

        self.label_nome = tk.Label(root, text=f"{self.nome}:")
        self.label_nome.grid(row=linha, column=0, padx=10, pady=5, sticky="e")

        self.label_valor = tk.Label(root, text=self.valor)
        self.label_valor.grid(row=linha, column=1, padx=10, pady=5, sticky="w")

    def alterar_valor(self, novo_valor):
        self.valor = novo_valor
        self.label_valor.config(text=self.valor)
