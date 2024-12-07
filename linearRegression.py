import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Gerar um dataset
np.random.seed(0)
n_samples = 1000

# Variáveis do dataset
horas_estudo = np.random.uniform(0, 24, n_samples)
cansado = np.random.choice([0, 1], n_samples)
nota = np.minimum(horas_estudo * np.random.uniform(3, 5), 100) - (cansado * 10) + np.random.normal(0, 5, n_samples)
nota = np.clip(nota, 0, 100)

data = pd.DataFrame({'Horas de Estudo': horas_estudo, 'Cansado': cansado, 'Nota': nota})

# Treinamento
X = data[['Horas de Estudo', 'Cansado']]
y = data['Nota']
X_train, X_teste, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

model = LinearRegression()
model.fit(X_train, y_train)

# Função de predição
def prever_nota(horas_estudo, cansado):
    nota_previsao = model.predict(np.array([[horas_estudo, cansado]]))
    return nota_previsao[0]

# Interação com o usuário
try:
    while True:
        horas_estudo_input = float(input("Digite um valor entre 0 e 24 para horas de estudo: "))
        if horas_estudo_input < 0 or horas_estudo_input > 24:
            print("O valor deve estar entre 0 e 24!")
            continue

        cansado_input = int(input("Digite 1 para cansado e 0 para não cansado: "))
        if cansado_input not in [0, 1]:
            print("Digite 1 para cansado e 0 para não cansado!")
            continue

        nota_prevista = prever_nota(horas_estudo_input, cansado_input)
        print(f"A nota prevista é: {nota_prevista:.2f}")

except KeyboardInterrupt:
    print("\nFinalizando o programa...")
except ValueError:
    print("Por favor, insira valores válidos.")

# Avaliação do modelo
result = model.score(X_teste, y_test)
print(f"Acurácia do modelo: {result:.2f}")

# Visualização
fig, ax = plt.subplots()
for c in [0, 1]:
    subset = data[data['Cansado'] == c]
    ax.scatter(subset['Horas de Estudo'], subset['Nota'], label=f"Cansado={c}")
ax.set_xlabel('Horas de Estudo')
ax.set_ylabel('Nota')
ax.legend()
plt.show()
