from ui.botao import BotaoInscricao
from ui.text import Text


class InscricaoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Interface de Inscrição")

        # Criando os objetos de parâmetro
        self.parametro1 = Text(root, "Parâmetro 1", "0", linha=0)
        self.parametro2 = Text(root, "Parâmetro 2", "0", linha=1)
        self.parametro3 = Text(root, "Parâmetro 3", "0", linha=2)
        self.parametro4 = Text(root, "Parâmetro 4", "0", linha=3)
        self.parametro5 = Text(root, "Parâmetro 5", "0", linha=4)

        # Botão de inscrição como objeto
        self.botao_inscricao = BotaoInscricao(
            root,
            linha=6,
        )
