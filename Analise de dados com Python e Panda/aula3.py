# -*- coding: utf-8 -*-
"""Aula3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1q60fQEsWJZzKg4pOxTQpYqMSuqRopypQ

**Introdução a biblioteca Pandas**
"""

import pandas as pd

df = pd.read_csv("/content/drive/MyDrive/datasets/Gapminder.csv",error_bad_lines=False,sep=";")

df.head()

df=df.rename(columns={"country":"País", "continent":"Continente","year":"Ano","lifeExp":"Expectativa de vida","pop":"PopTotal","gdpPercap":"PIB"})

df.rename(columns={"country":"País", "continent":"Continente","year":"Ano","lifeExp":"Expectativa de vida","pop":"PopTotal","gdpPercap":"PIB"})

df.head(10)

df.shape

df.columns

df.dtypes

df.tail()

df.describe()

df['Continente'].unique()

Oceania=df.loc[df['Continente']=='Oceania']
Oceania.head()

df.groupby('Continente')['País'].unique()

df.groupby("Ano")["Expectativa de vida"].mean()

df['PIB'].mean()

df['PIB'].sum()