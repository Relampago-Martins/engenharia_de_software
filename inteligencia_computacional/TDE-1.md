# TDE-1

## K-means

### O que é?

K-means é um algoritmo de aprendizado de máquina não supervisionado usado para agrupamento de dados. Ele funciona dividindo um conjunto de dados em K grupos distintos, onde K é um número pré-definido de clusters.

### Objetivo

O objetivo principal é encontrar um perfil de características que diferenciem cada um dos grupos formados.

### Processo de funcionamento

1. **Inicialização**: Escolher K pontos iniciais (centroides) aleatoriamente a partir do conjunto de dados.
2. **Atribuição**: Atribuir cada ponto de dado ao cluster mais próximo, com base na distância em relação aos centroides.
3. **Atualização**: Recalcular os centroides de cada cluster, levando em conta todos os pontos atribuídos a ele.
4. **Convergência**: Repetir os passos 2 e 3 até que os centroides não mudem significativamente ou até que um critério de parada seja atendido.

### A qual cluster um ponto de dados pertence?

O K-means determina a qual cluster um ponto de dados pertence calculando a distância entre o ponto e os centroides de todos os clusters. O ponto é atribuído ao cluster cujo centroide está mais próximo dele, geralmente utilizando a distância euclidiana como métrica.

### O que acontece quando o algoritmo K-means converge?

Após a convergência o algoritmo é encerrado. Alcançar convergência no K-means, significa que os centroides dos clusters não mudaram significativamente entre as iterações.  A convergência pode ser definida por um critério de parada, como um número máximo de iterações ou uma mudança mínima nos centroides.

### Explique a importância da inicialização dos centroides no K-means. Quais técnicas podem ser usadas para melhorar a inicialização?

A inicialização dos centroides é crucial para o desempenho do K-means, pois uma má escolha inicial pode levar a resultados insatisfatórios e à convergência para mínimos locais. Algumas técnicas para melhorar a inicialização incluem:

1. **K-means++**: Uma abordagem que seleciona os centroides iniciais de forma mais inteligente, garantindo que eles estejam bem distribuídos no espaço de dados.
2. **Várias execuções**: Executar o algoritmo várias vezes com diferentes inicializações e escolher a melhor solução com base em uma métrica de avaliação, como a soma das distâncias quadráticas dentro dos clusters.

### Qual é a principal diferença entre K-means e K-means++?

A principal diferença entre K-means e K-means++ está na forma como os centroides iniciais são escolhidos. O K-means++ utiliza uma abordagem mais inteligente para selecionar os centroides iniciais, garantindo que eles estejam mais bem distribuídos no espaço de dados. Isso ajuda a evitar a convergência para mínimos locais e geralmente resulta em uma melhor qualidade de agrupamento em comparação com a inicialização aleatória simples do K-means.

### Como o K-means lida com clusters de tamanhos diferentes e densidades diferentes?

O K-means tem limitações ao lidar com clusters de diferentes tamanhos e densidades. Por ser um algoritmo que minimiza a soma das distâncias quadráticas, ele tende a formar clusters de tamanhos semelhantes, podendo resultar em clusters grandes sendo divididos em subclusters menores ou clusters pequenos sendo agrupados em um cluster maior. Além disso, o algoritmo assume que todos os clusters têm a mesma forma e densidade, o que pode não ser verdade em muitos conjuntos de dados do mundo real, levando a uma má representação de clusters mais densos e compactos em comparação com clusters mais dispersos.

### Explique como a métrica de inércia (ou soma das distâncias quadradas) é usada no contexto do K-means

A métrica de inércia, também conhecida como soma das distâncias quadradas, é uma medida da compactação dos clusters formados pelo K-means. Ela é calculada como a soma das distâncias quadradas entre cada ponto de dado e o centroide do cluster ao qual pertence. Quanto menor a soma, melhor, porque significa que os pontos de dados dentro do cluster são compactos ou mais semelhantes. O objetivo do K-means é minimizar essa métrica durante o processo de agrupamento.

### O que é a técnica do cotovelo (Elbow Method) e como ela é usada para determinar o número ideal de clusters em K-means?

A técnica do cotovelo é um método visual usado para determinar o número ideal de clusters em um algoritmo K-means. Um gráfico é plotado com o índice WCSS (soma dos quadrados dentro do cluster) em função do número de clusters. Há uma queda brusca no meio do gráfico, esta queda é chamada de "cotovelo". Na prática este ponto marca o início da desaceleração de ganhos com um novo cluster, indicando que adicionar mais clusters não resulta em uma melhoria significativa na compactação dos clusters. Esse ponto é considerado o número ideal de clusters, pois representa um bom equilíbrio entre a complexidade do modelo e a qualidade do agrupamento.

### Quais são as limitações do algoritmo K-means? Cite pelo menos três

1. Sensibilidade à inicialização: A escolha dos centroides iniciais pode afetar significativamente os resultados do agrupamento, levando a diferentes soluções em execuções diferentes.

2. Sensibilidade a outliers: O K-means é sensível a outliers, pois eles podem influenciar a posição dos centroides e, consequentemente, a formação dos clusters.

3. Limitação na forma dos clusters: O K-means assume que os clusters têm formas esféricas e tamanhos semelhantes, o que pode não ser verdade em muitos conjuntos de dados do mundo real.

## Métricas de Avaliação

### O que é a pontuação de silhueta e como ela é calculada?

A pontuação de silhueta é uma métrica usada para avaliar a qualidade dos clusters formados por um algoritmo de agrupamento, como o K-means. Ela mede o quão bem cada ponto de dado está agrupado em relação aos outros pontos do mesmo cluster e aos pontos dos clusters vizinhos.

### Explique a métrica do coeficiente de Davies-Bouldin. Como ela é interpretada?

O coeficiente de Davies-Bouldin é uma métrica que avalia a qualidade dos clusters com base na separação e na compactação. Ele é calculado como a razão entre a soma das distâncias intra-cluster e a distância inter-cluster. Um valor mais baixo do coeficiente indica melhores clusters, pois significa que os clusters são mais compactos e mais bem separados.

### O que é a matriz de confusão e como pode ser usada para avaliar o desempenho de um algoritmo de clustering?

A matriz de confusão é uma ferramenta usada para avaliar o desempenho de algoritmos de classificação, mas pode ser adaptada para avaliar algoritmos de clustering quando há rótulos verdadeiros disponíveis. Ela mostra a contagem de verdadeiros positivos, falsos positivos, verdadeiros negativos e falsos negativos, permitindo a análise detalhada do desempenho do modelo.

### Descreva a métrica de entropia no contexto da avaliação de clusters

A entropia é uma medida da incerteza ou impureza em um conjunto de dados. No contexto da avaliação de clusters, a entropia pode ser usada para medir a pureza dos clusters formados. Um cluster com baixa entropia é considerado mais puro, pois contém principalmente pontos de dados de uma única classe. A entropia é calculada com base na distribuição das classes dentro de cada cluster.

### Como a análise de variância (ANOVA) pode ser usada para avaliar a qualidade dos clusters?

A análise de variância (ANOVA) pode ser usada para avaliar a qualidade dos clusters comparando a variância entre os clusters com a variância dentro dos clusters. Se a variância entre os clusters for significativamente maior do que a variância dentro dos clusters, isso indica que os clusters são bem definidos e distintos.

### Explique o índice de Rand ajustado (Adjusted Rand Index) e sua aplicação na avaliação de clusters

O índice de Rand ajustado é uma métrica que mede a similaridade entre duas partições de dados, levando em consideração o acaso. Ele varia de -1 a 1, onde 1 indica que as duas partições são idênticas, 0 indica que a similaridade é equivalente ao acaso e valores negativos indicam menos similaridade do que o esperado ao acaso. Essa métrica é útil na avaliação de clusters, pois permite comparar a partição resultante do algoritmo de clustering com uma partição verdadeira ou conhecida.

### O que é a métrica de variância inter e intra-cluster e como elas são usadas para avaliar clusters?

A variância intra-cluster mede a dispersão dos pontos dentro de cada cluster, enquanto a variância inter-cluster mede a dispersão entre os clusters. Uma boa configuração de clusters deve ter baixa variância intra-cluster (os pontos dentro de cada cluster estão próximos uns dos outros) e alta variância inter-cluster (os clusters estão bem separados). Essas métricas podem ser usadas para ajustar e validar a qualidade dos clusters formados.

## Questões sobre aprendizado não supervisionado

### Qual é a principal diferença entre aprendizado supervisionado e aprendizado não supervisionado?

A principal diferença entre aprendizado supervisionado e aprendizado não supervisionado está na presença de rótulos nos dados de treinamento. No aprendizado supervisionado, o modelo é treinado com um conjunto de dados que contém entradas e saídas correspondentes (rótulos), permitindo que o modelo aprenda a mapear entradas para saídas. Em contraste, no aprendizado não supervisionado, o modelo é treinado com dados que não possuem rótulos, e o objetivo é identificar padrões ou estruturas subjacentes nos dados, como agrupamentos ou associações.

### Explique a diferença entre algoritmos de clustering particional e hierárquico. Dê exemplos de cada

Algoritmos de clustering particional dividem o conjunto de dados em um número pré-definido de clusters, onde cada ponto de dado pertence a exatamente um cluster. Esses algoritmos geralmente tentam otimizar uma função objetivo, como a minimização da soma das distâncias dentro dos clusters. Um exemplo comum de algoritmo particional é o K-means.

Já os algoritmos de clustering hierárquico constroem uma árvore de clusters, onde os clusters são organizados em uma estrutura hierárquica. Eles podem ser aglomerativos (começando com cada ponto como um cluster separado e fundindo-os) ou divisivos (começando com todos os pontos em um único cluster e dividindo-os). Um exemplo de algoritmo hierárquico é o Agglomerative Clustering.

### Além do K-means, cite e explique brevemente dois outros algoritmos de clustering não supervisionados

1. **DBSCAN (Density-Based Spatial Clustering of Applications with Noise)**: Este algoritmo identifica clusters com base na densidade de pontos em uma região. Ele agrupa pontos que estão próximos uns dos outros e marca como ruído os pontos que estão em regiões de baixa densidade. O DBSCAN é eficaz para encontrar clusters de forma arbitrária e pode lidar com ruído nos dados.

2. **Mean Shift**: Este algoritmo busca encontrar "modas" na densidade dos dados. Ele funciona movendo cada ponto de dado em direção à média dos pontos em sua vizinhança, até que não haja mais movimento. O Mean Shift é útil para identificar clusters de forma arbitrária e não requer a especificação do número de clusters a priori.
