import tkinter as tk


class BotaoInscricao:
    def __init__(self, root, linha):
        self.ativado = False
        self.botao = tk.Button(root, text="Se inscrever", command=self.toggle)
        self.botao.grid(row=linha, column=0, columnspan=2, pady=20)

    def toggle(self):
        self.ativado = not self.ativado
        novo_texto = "Desinscrever-se" if self.ativado else "Se inscrever"
        self.botao.config(text=novo_texto)
        print(f"Botão ativado? {self.ativado}")
