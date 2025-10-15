import numpy as np


class Camada:
    """
    Representa uma camada totalmente conectada (fully connected).

    Atributos:
        entrada: número de neurônios de entrada
        saida: número de neurônios de saída
        pesos: matriz de pesos (entrada x saida)
        bias: vetor de vieses (saida,)
    """

    def __init__(self, entrada, saida):
        """
        Inicializa a camada com pesos aleatórios e vieses zero.

        Args:
            entrada: quantidade de neurônios de entrada
            saida: quantidade de neurônios de saída
        """
        # Inicialização de Xavier/Glorot para melhor convergência
        limite = np.sqrt(6 / (entrada + saida))
        self.pesos = np.random.uniform(-limite, limite, (entrada, saida))
        self.bias = np.zeros((1, saida))

    def forward(self, X):
        """
        Passa os dados para frente (forward pass).

        Args:
            X: entrada de forma (batch_size, entrada)

        Returns:
            Resultado da transformação linear: X @ pesos + bias
        """
        self.entrada = X
        return np.dot(X, self.pesos) + self.bias

    def backward(self, dL_dY, taxa_aprendizado):
        """
        Retropropagação (backward pass).

        Args:
            dL_dY: gradiente da perda em relação à saída
            taxa_aprendizado: taxa de aprendizado
        """
        batch_size = self.entrada.shape[0]

        # Gradiente em relação à entrada
        dL_dX = np.dot(dL_dY, self.pesos.T)

        # Gradiente em relação aos pesos
        dL_dW = np.dot(self.entrada.T, dL_dY) / batch_size

        # Gradiente em relação ao bias
        dL_dB = np.sum(dL_dY, axis=0, keepdims=True) / batch_size

        # Atualiza pesos e bias
        self.pesos -= taxa_aprendizado * dL_dW
        self.bias -= taxa_aprendizado * dL_dB

        return dL_dX


class AtivacaoReLU:
    """
    Função de ativação ReLU (Rectified Linear Unit).
    ReLU(x) = max(0, x)
    """

    def forward(self, X):
        """
        Forward pass da ReLU.

        Args:
            X: entrada

        Returns:
            max(0, X)
        """
        self.entrada = X
        return np.maximum(0, X)

    def backward(self, dL_dY):
        """
        Backward pass da ReLU.

        Args:
            dL_dY: gradiente da perda em relação à saída

        Returns:
            Gradiente propagado para trás
        """
        return dL_dY * (self.entrada > 0)


class AtivacaoSoftmax:
    """
    Função de ativação Softmax para saída de classificação.
    Converte logits em probabilidades.
    """

    def forward(self, X):
        """
        Forward pass da Softmax.

        Args:
            X: entrada (logits)

        Returns:
            Probabilidades normalizadas
        """
        # Subtrai o máximo para estabilidade numérica
        exp_X = np.exp(X - np.max(X, axis=1, keepdims=True))
        self.saida = exp_X / np.sum(exp_X, axis=1, keepdims=True)
        return self.saida

    def backward(self, Y_verdadeiro):
        """
        Backward pass da Softmax com entropia cruzada.

        Args:
            Y_verdadeiro: rótulos verdadeiros (one-hot encoded)

        Returns:
            Gradiente: probabilidade predita - rótulo verdadeiro
        """
        return self.saida - Y_verdadeiro


class RedeMLP:
    """
    Rede Neural MLP (Multi-Layer Perceptron).

    Responsabilidade ÚNICA: Definir a arquitetura e executar forward/backward passes.
    """

    def __init__(self, tamanho_entrada, tamanhos_ocultos, tamanho_saida):
        """
        Inicializa a rede neural.

        Args:
            tamanho_entrada: número de features de entrada
            tamanhos_ocultos: lista com número de neurônios em cada camada oculta
            tamanho_saida: número de classes/saídas
        """
        self.camadas = []
        self.ativacoes_relu = []

        # Cria camadas: entrada -> camadas ocultas -> saída
        tamanhos = [tamanho_entrada] + tamanhos_ocultos + [tamanho_saida]

        for i in range(len(tamanhos) - 1):
            self.camadas.append(Camada(tamanhos[i], tamanhos[i + 1]))

        # Softmax na saída
        self.softmax = AtivacaoSoftmax()

    def forward(self, X):
        """
        Forward pass pela rede toda.

        Args:
            X: entrada de forma (batch_size, tamanho_entrada)

        Returns:
            Probabilidades de saída
        """
        # Passa por todas as camadas ocultas com ReLU
        ativacao = X
        self.ativacoes_relu = []

        for camada in self.camadas[:-1]:
            ativacao = camada.forward(ativacao)
            relu = AtivacaoReLU()
            ativacao = relu.forward(ativacao)
            self.ativacoes_relu.append(relu)

        # Última camada (sem ReLU)
        ativacao = self.camadas[-1].forward(ativacao)

        # Softmax na saída
        return self.softmax.forward(ativacao)

    def backward(self, Y_verdadeiro, taxa_aprendizado):
        """
        Backward pass (retropropagação).

        Args:
            Y_verdadeiro: rótulos verdadeiros (one-hot encoded)
            taxa_aprendizado: taxa de aprendizado
        """
        # Gradiente da Softmax + entropia cruzada
        dL_dY = self.softmax.backward(Y_verdadeiro)

        # Retropropaga pela última camada
        dL_dY = self.camadas[-1].backward(dL_dY, taxa_aprendizado)

        # Retropropaga pelas camadas ocultas
        for i in range(len(self.camadas) - 2, -1, -1):
            dL_dY = self.ativacoes_relu[i].backward(dL_dY)
            dL_dY = self.camadas[i].backward(dL_dY, taxa_aprendizado)


class Treinador:
    """
    Responsável pelo treinamento da rede neural.

    Responsabilidade ÚNICA: Gerenciar o loop de treinamento.
    """

    def __init__(self, rede, taxa_aprendizado=0.01):
        """
        Inicializa o treinador.

        Args:
            rede: instância de RedeMLP
            taxa_aprendizado: taxa de aprendizado
        """
        self.rede = rede
        self.taxa_aprendizado = taxa_aprendizado
        self.historico_perda = []

    def treinar_epoca(self, X, Y):
        """
        Executa uma época de treinamento.

        Args:
            X: dados de entrada
            Y: rótulos verdadeiros (one-hot encoded)

        Returns:
            Valor da perda na época
        """
        # Forward pass
        predicoes = self.rede.forward(X)

        # Calcula perda (entropia cruzada)
        perda = -np.mean(np.sum(Y * np.log(predicoes + 1e-8), axis=1))

        # Backward pass
        self.rede.backward(Y, self.taxa_aprendizado)

        return perda

    def treinar(self, X, Y, epocas=100):
        """
        Treina a rede neural por múltiplas épocas.

        Args:
            X: dados de entrada (num_amostras, tamanho_entrada)
            Y: rótulos verdadeiros (num_amostras, tamanho_saida) em one-hot
            epocas: número de épocas de treinamento
        """
        for epoca in range(epocas):
            perda = self.treinar_epoca(X, Y)
            self.historico_perda.append(perda)

            if (epoca + 1) % 10 == 0:
                print(f"Época {epoca + 1}/{epocas} - Perda: {perda:.4f}")


class Avaliador:
    """
    Responsável pela avaliação e predição da rede neural.

    Responsabilidade ÚNICA: Fazer predições e calcular métricas.
    """

    def __init__(self, rede):
        """
        Inicializa o avaliador.

        Args:
            rede: instância de RedeMLP
        """
        self.rede = rede

    def prever(self, X):
        """
        Faz predições das classes.

        Args:
            X: dados de entrada

        Returns:
            Classe predita (argmax das probabilidades)
        """
        probabilidades = self.rede.forward(X)
        return np.argmax(probabilidades, axis=1)

    def prever_probabilidades(self, X):
        """
        Retorna as probabilidades de cada classe.

        Args:
            X: dados de entrada

        Returns:
            Matriz de probabilidades
        """
        return self.rede.forward(X)

    def calcular_acuracia(self, X, Y_verdadeiro):
        """
        Calcula a acurácia da rede.

        Args:
            X: dados de entrada
            Y_verdadeiro: rótulos verdadeiros (one-hot encoded)

        Returns:
            Acurácia (0 a 1)
        """
        predicoes = self.prever(X)
        classes_verdadeiras = np.argmax(Y_verdadeiro, axis=1)
        acertos = np.sum(predicoes == classes_verdadeiras)
        return acertos / len(classes_verdadeiras)

    def calcular_perda(self, X, Y_verdadeiro):
        """
        Calcula a perda (entropia cruzada).

        Args:
            X: dados de entrada
            Y_verdadeiro: rótulos verdadeiros (one-hot encoded)

        Returns:
            Valor da perda
        """
        probabilidades = self.prever_probabilidades(X)
        perda = -np.mean(np.sum(Y_verdadeiro * np.log(probabilidades + 1e-8), axis=1))
        return perda


# ============= EXEMPLO DE USO =============

if __name__ == "__main__":
    # Gera dados de exemplo (dataset fictício simples)
    np.random.seed(42)

    # 300 amostras, 4 features
    X = np.random.randn(300, 4)

    # 3 classes (one-hot encoded)
    Y = np.zeros((300, 3))
    for i in range(300):
        classe = i % 3
        Y[i, classe] = 1

    # Divide em treino (70%) e teste (30%)
    indice_split = int(0.7 * len(X))
    X_treino, X_teste = X[:indice_split], X[indice_split:]
    Y_treino, Y_teste = Y[:indice_split], Y[indice_split:]

    # Cria a rede: 4 entrada -> 8 ocultos -> 3 saída
    rede = RedeMLP(tamanho_entrada=4, tamanhos_ocultos=[8], tamanho_saida=3)

    # Treina
    treinador = Treinador(rede, taxa_aprendizado=0.1)
    print("Treinando a rede neural...\n")
    treinador.treinar(X_treino, Y_treino, epocas=100)

    # Avalia
    avaliador = Avaliador(rede)
    print("\n--- Avaliação no Conjunto de Treino ---")
    acuracia_treino = avaliador.calcular_acuracia(X_treino, Y_treino)
    perda_treino = avaliador.calcular_perda(X_treino, Y_treino)
    print(f"Acurácia: {acuracia_treino:.4f}")
    print(f"Perda: {perda_treino:.4f}")

    print("\n--- Avaliação no Conjunto de Teste ---")
    acuracia_teste = avaliador.calcular_acuracia(X_teste, Y_teste)
    perda_teste = avaliador.calcular_perda(X_teste, Y_teste)
    print(f"Acurácia: {acuracia_teste:.4f}")
    print(f"Perda: {perda_teste:.4f}")

    print("\n--- Predições nas Primeiras 5 Amostras de Teste ---")
    predicoes = avaliador.prever(X_teste[:5])
    print(f"Predições: {predicoes}")
    print(f"Rótulos verdadeiros: {np.argmax(Y_teste[:5], axis=1)}")
