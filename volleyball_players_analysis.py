#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 18:55:43 2024

@author: wiktoriazacharczuk
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#explory and identifying data
df= pd.read_csv("/Users/wiktoriazacharczuk/Desktop/projekt/VNL2023.csv")

df.head()

df.shape

df.describe()

df.isna().sum()

df.duplicated().sum()

numeric_cols= df.select_dtypes(include= ["int", "float"]).columns
correlation_matrix= df[numeric_cols].corr()
print(correlation_matrix)


sns.heatmap(correlation_matrix, annot=True, cmap= "coolwarm", linewidths= 5)
plt.title("Heatmap macierzy korelacji")
plt.show()

position_counts= df["Position"].value_counts()
position_counts

plt.pie(position_counts, labels=position_counts.index, autopct="%1.1f%%", startangle=90)
plt.title("Podział pozycji")
plt.show()

avg_attack_by_country= df.groupby("Country")["Attack"].mean()
avg_attack_by_country.sort_values(ascending=False).plot(kind="bar")
plt.title("Średnia ataku według krajów")
plt.xlabel("Country")
plt.ylabel("Średni atak")
plt.show()

avg_serve_by_age= df.groupby("Age")["Serve"].mean()
avg_serve_by_age.sort_values(ascending=False)
df.groupby(["Country","Position"])["Attack"].max().reset_index().sort_values(ascending=False, by="Attack")


sns.boxplot(x=df["Serve"])
plt.title("Box Plot: Podział wartości serwów")
plt.xlabel("Serw")
plt.show()

plt.hist(df["Age"], bins=20, color= "skyblue", edgecolor= "black")
plt.title("Podział zawodników ze względu na wiek")
plt.xlabel("Wiek")
plt.show()

avg_attack_by_position= df.groupby("Position")["Attack"].mean()
avg_attack_by_position.sort_values(ascending=True).plot(kind="bar", color="green")
plt.title("Średnia wartość ataku według pozycji")
plt.xlabel("Pozycja")
plt.ylabel("Średni atak")
plt.show()

serve_trend_by_age= df.groupby("Age")["Serve"].mean()
serve_trend_by_age.plot(kind="line", marker="o", linestyle="-", color="orange")
plt.title("Analiza trendu serwów dla danej grupy wiekowej")
plt.xlabel("Wiek")
plt.ylabel("Średnia serwów")
plt.show()

total_attack_block_by_country=df.groupby("Country")[["Attack", "Block"]].sum()
total_attack_block_by_country.sort_values(ascending=False, by="Attack").plot(
    kind="bar",stacked=True, colormap= "viridis")
plt.title("Suma bloków i ataków dla danego państwa")
plt.xlabel("Państwo")
plt.ylabel("Wartość całkowita")
plt.show()

df.rename(columns={"Receive ": "Receive"}, inplace=True)

plt.scatter(df["Block"], df["Receive"])
plt.title("Blok vs Przyjęcie")
plt.xlabel("Blok")
plt.ylabel("Przyjęcie")
plt.show()

total_power_by_country= df.groupby("Country")[["Attack","Dig", "Serve", "Block", "Receive", "Set"]].sum()
total_power_by_country.sort_values(ascending=False, by="Attack").plot(kind="bar", stacked=True, colormap="magma")
plt.title("Suma wszystkich zagrań")
plt.xlabel("Państwo")
plt.ylabel("Suma sił")
plt.show

best_setter= df[df["Set"] != 0]
best_setter= best_setter.groupby(["Player", "Country"])["Set"].sum()
best_setter.sort_values(ascending=False).head(16).plot(kind="bar", stacked=True, colormap="spring")
plt.title("Najlepszy rozgrywający")
plt.xlabel("Zawodnik")
plt.show

best_libero= df[df["Position"]=="L"]
best_libero= best_libero.groupby(["Player","Country"])[["Dig","Receive"]].sum()
best_libero.sort_values(ascending=False, by="Dig").plot(kind="bar", stacked=True, colormap="viridis")
plt.title("Najlepszy libero")
plt.xlabel("Zawodnik")
plt.show