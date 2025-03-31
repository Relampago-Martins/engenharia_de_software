import tkinter as tk


class Text:
    """Classe que representa um elemento de texto na interface gráfica."""

    def __init__(self, root: tk.Tk, nome: str, valor: str, linha: int) -> None:
        """Inicializa o elemento de texto com nome e valor."""
        self.nome = nome
        self.valor = valor

        self.label_nome = tk.Label(root, text=f"{self.nome}:")
        self.label_nome.grid(row=linha, column=0, padx=10, pady=5, sticky="e")

        self.label_valor = tk.Label(root, text=self.valor)
        self.label_valor.grid(row=linha, column=1, padx=10, pady=5, sticky="w")

    def alterar_valor(self, novo_valor: str) -> None:
        """Altera o valor exibido no elemento de texto."""
        self.valor = novo_valor
        self.label_valor.config(text=self.valor)
