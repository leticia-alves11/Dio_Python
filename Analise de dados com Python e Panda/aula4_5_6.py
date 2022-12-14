# -*- coding: utf-8 -*-
"""Aula4_5_6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ojJV3lEkoXjVbQD6A3xoc5LITFmrwzu9
"""

#importando a biblioteca
import pandas as pd

#Leitura dos arquivos
df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

#juntando todos os arquivos
df = pd.concat([df1, df2, df3, df4, df5])

#Exibindo as 5 primeiras linhas
df.head()

#Exibindo as 5 últimas linhas
df.tail()

#Verificando o tipo de dados de cada coluna
df.dtypes

#Alterando o tipo e dado da coluna LojaID
df["LojaID"] = df["LojaID"].astype("object")

df

df.dtypes

df.head()

df.isnull().sum()

df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)

df["Vendas"].mean()

df.isnull().sum()

df.sample(15)

df["Vendas"].fillna(0, inplace=True)

df.dropna(inplace=True)

df.dropna(subset=["Vendas"], inplace=True)

df.dropna(how="all", inplace=True)

"""**Criando colunas**"""

df["Receita"] = df["Vendas"].mul(df["Qtde"])

df.head()

df["Receita/Vendas"] = df["Receita"] / df["Vendas"]

df.head()

df["Receita"].max()

df["Receita"].min()

df.nlargest(3, "Receita")

df.nsmallest(3, "Receita")

df.groupby("Cidade")["Receita"].sum()

df.sort_values("Receita", ascending=False).head(10)

"""**Datas**"""

df["Data"] = df["Data"].astype("int64")

df.dtypes

df["Data"] = pd.to_datetime(df["Data"])

df.dtypes

df.groupby(df["Data"].dt.year)["Receita"].sum()

df["Ano_Venda"] = df["Data"].dt.year

df.sample(5)

df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)

df.sample(5)

df["Data"].min()

df["diferenca_dias"] = df["Data"] - df["Data"].min()

df.sample(5)

df["trimestre_venda"] = df["Data"].dt.quarter

df.sample(5)

vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]

vendas_marco_19.sample(20)

"""**Visualizando dados**"""

df["LojaID"].value_counts(ascending=False)

df["LojaID"].value_counts(ascending=False).plot.bar()

df["LojaID"].value_counts().plot.barh()

df["LojaID"].value_counts(ascending=True).plot.barh();

df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie()

df["Cidade"].value_counts()

import matplotlib.pyplot as plt
df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas");

df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade", color="red")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas");

plt.style.use("ggplot")

df.groupby(df["mes_venda"])["Qtde"].sum().plot(title = "Total Produtos vendidos x mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend();

df.groupby(df["mes_venda"])["Qtde"].sum()

df_2019 = df[df["Ano_Venda"] == 2019]

df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum()

df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "o")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend();

plt.hist(df["Qtde"], color="orangered");

plt.scatter(x=df_2019["dia_venda"], y = df_2019["Receita"]);

df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker = "v")
plt.title("Quantidade de produtos vendidos x mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos");
plt.legend()
plt.savefig("grafico QTDE x MES.png")