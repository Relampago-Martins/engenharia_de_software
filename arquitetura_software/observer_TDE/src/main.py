import tkinter as tk


class Parametro:
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


class InscricaoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface de Inscrição")

        # Criando os objetos de parâmetro
        self.parametro1 = Parametro(root, "Parâmetro 1", "0", linha=0)
        self.parametro2 = Parametro(root, "Parâmetro 2", "0", linha=1)
        self.parametro3 = Parametro(root, "Parâmetro 3", "0", linha=2)
        self.parametro4 = Parametro(root, "Parâmetro 4", "0", linha=3)
        self.parametro5 = Parametro(root, "Parâmetro 5", "0", linha=4)

        # Botão de inscrição como objeto
        self.botao_inscricao = BotaoInscricao(
            root,
            linha=6,
        )


# Executa o app
if __name__ == "__main__":
    root = tk.Tk()
    app = InscricaoApp(root)
    root.mainloop()
