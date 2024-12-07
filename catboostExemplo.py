# Esse algoritmo é usado para classificação
# Classificação binaria ou multiclasse
import pandas as pd
import numpy as np
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from catboost import CatBoostClassifier

train_d = pd.read_csv('C:/Users/filip/Documents/GitHub/machineLearning/treino.csv')

train_d.head(5)
train_d.describe()

train_d['Season'].value_counts()

ax = sns.countplot(x=train_d['Season'])

# verificar se tem valor nulo

train_d.isnull().sum()

# verificar se tem valor duplicado

train_d.duplicated().sum()

# excluir a variavel ID, porque ela está nos atrapalando
train_d.drop('ID', axis=1, inplace=True)

# verificar se tem valor duplicado sem o ID

train_d.duplicated().sum()

# Exclusão de valores ausentes

train_d.dropna(inplace=True)

# verificar se tem valor nulo

train_d.isnull().sum()

train_d['Crop_Damage'].count()

# One Hot Criar umas variaveis NUMERICAS

for col in ['Crop_Type', 'Soil_Type', 'Pesticide_Use_Category', 'Season']:
  train_d = pd.get_dummies(train_d,columns=[col])

train_d.describe()

# Separar os dados de Treinamento e teste
# todas as variaveis - a variavel alvo
X = train_d.drop(['Crop_Damage'], axis=1)
y = train_d['Crop_Damage'].values.reshape(-1,1)

# variaveis de Treino e Teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

#treinamento da maquina preditiva

maquina_preditiva = CatBoostClassifier(n_estimators=1000, max_depth=4, random_state=50)
maquina_preditiva.fit(X_train, y_train)
predicoes = maquina_preditiva.predict_proba(X_test)

# avalia se o medelo está bom...

result = maquina_preditiva.score(X_test, y_test)
print("A minha acuracia é : %.f%%" % (result * 100.0))

