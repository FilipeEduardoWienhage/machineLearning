<h1 align="center">
Modelos de Machine Learning com CatBoost e LinearRegression
</h1>


<p align="center">
Modelo CatBoost

1° Problema de Negócio
Precisamos prever o resultado da temporada de colheita, ou seja, se a cultura seria:

1. Saudável (viva)
2. Danificada por pesticidas
3. Danificada por outros motivos.
Os dados são baseados em safras colhidas por vários agricultores no final da temporada de colheita.

2° Análise Exploratória dos Dados

1- ID - UniqueID
2- Estimated_Insects_Count - Contagem estimada de insetos por metro quadrado
3- Crop_Type - Categoria de cultivo (0,1)
4- Tipo_do solo - Categoria do solo (0,1)
5- Pesticide_Use_Category - Tipo de uso de pesticidas (1- 6. Nunca, 2-Usado anteriormente, 3-Usando atualmente)
6 -Number_Doses_Week - Número de doses por semana
7- Number_Weeks_Used - Número de semanas usadas
8- Number_Weeks_Quit - Número de semanas de desistência
9- Temporada - Categoria Temporada (1,2,3)
10- Crop_Damage - Categoria de dano de cultivo (0 = vivo, 1 = dano devido a outras causas, 2 = dano devido a pesticidas)


Modelo LinerRegression

Este projeto envolve a criação de uma solução que prevê a nota de um aluno com base em duas variáveis principais: Horas de Estudo e Fator Cansaço. O objetivo é utilizar técnicas de machine learning para modelar o impacto dessas variáveis no desempenho acadêmico e oferecer uma interface onde o usuário pode inserir as condições e receber uma estimativa de nota.

Contexto do Problema
Em cenários acadêmicos, o desempenho dos alunos pode ser influenciado por diversos fatores, sendo as horas de estudo uma das mais óbvias. No entanto, o cansaço também pode ser um fator relevante, onde estudar por muitas horas seguidas pode resultar em uma menor eficiência, refletindo em notas mais baixas. Portanto, a proposta aqui é:

Restringir o tempo máximo de estudo a 24 horas. Garantir que a nota final nunca ultrapasse o valor máximo de 100. Considerar se o aluno está "cansado" (0 para não cansado e 1 para cansado), o que impacta negativamente a nota.

Geração do Dataset
Para resolver o problema, começamos gerando um conjunto de dados sintéticos que simula os comportamentos esperados. As variáveis incluem:

Horas de Estudo: Um valor entre 0 e 24, onde quanto mais tempo o aluno estuda, maior a nota. No entanto, o efeito do estudo tem limites, e a produtividade começa a cair após um certo número de horas. Cansado: Um valor binário (0 ou 1), onde "1" indica que o aluno está cansado, resultando em uma redução na nota final. Nota: O desempenho final (nota) é calculado com base nas horas de estudo, mas limitado ao valor máximo de 100. Se o aluno está cansado, a nota é reduzida. As notas são geradas com base em uma função linear, multiplicando as horas de estudo por um fator aleatório (para simular variações na eficiência), e se o aluno estiver cansado, subtraímos pontos da nota final.

Modelo Preditivo
Uma vez que o dataset está pronto, treinamos um modelo de regressão linear para prever a nota com base nas duas variáveis de entrada (horas de estudo e cansaço). A regressão linear foi escolhida por ser uma abordagem simples e eficaz para esse tipo de problema, dado que queremos prever uma variável numérica (nota) a partir de duas variáveis contínuas (horas de estudo) e categóricas (cansaço).
</p>

## 💻 Projeto

Nesse projeto foi utilizado como forma de aprender/conhecer um dos modelos de aprendizado de máquina

## 🚀 Tecnologias

- Python

## 🚀 Créditos Tutorial

- SuperDev 