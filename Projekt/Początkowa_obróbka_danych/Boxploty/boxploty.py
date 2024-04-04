import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

xlsx = pd.ExcelFile('Boxploty_INPUT.xlsx')
df_2004 = pd.read_excel(xlsx)
df_2004_bez_pk = df_2004.iloc[:, 1:]

# Iteracja po każdej cech i tworzenie wykresu pudełkowego
for column in df_2004_bez_pk.columns:
    plt.figure(figsize=(10, 6))
    sns.boxplot(x=df_2004[column])
    plt.title(f'{column}')
    plt.tight_layout()
    plt.savefig(f'{column}_boxplot.png')
    plt.close()
