"""
    O objetivo desse script é encontrar o melhor modelo de machine learning
    para classificar flores do tipo Iris em 3 categorias:
    [0] - Setosa
    [1] - Versicolor
    [2] - Virginica
"""
from sklearn import tree
from sklearn import datasets
from  sklearn.utils._bunch import Bunch
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Cria duas tabelas
# X é a tabela de dados
# Y é a tabela de classificação
iris: Bunch = datasets.load_iris()
X = pd.DataFrame(iris.get('data'))
Y = pd.DataFrame(iris.get('target'))



