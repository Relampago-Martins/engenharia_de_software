# Observer

Implemente duas classes para apresentar displays  diferentes que apresentam dados do clima obtidos do EquipamentoDeMonitoramento

* uma delas, DisplayDeCondicoesAtuais,  apresenta os dados de temperatura, umidade e pressão atuais, pode inclusive mostrar os últimos 10 valores lidos;

* outra, DisplayEstatistico, implementando um display que apresenta a temperatura e umidade médias e as temperaturas máxima e mínima (considerando as últimas 10 atualizações);

Os objetos Display serão implementações de "Observador" e devem disponibilizar um botão (ou dois) para conectá-los e desconectá-los do Publicador. Depois de completar a implementação, verifique e descreva o que seria necessário mudar nela para adaptar o exemplo à implementação do padrão Observer disponível na API do Java (classes no pacote java.util: Observer e Observable)

## Como rodar o projeto

### Pré configuração

* Ubuntu:

  ```bash
  sudo apt-get install python3-pip
  sudo apt-get install python3-tk
  ```

* Windows:
  * Não é necessário instalar nada, apenas o Python 3.8 ou superior.

### Instalação

Após configurar o ambiente, instale as dependências do projeto:

```bash
pip install -r requirements.txt
python3 src/main.py
```
