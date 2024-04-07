import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Wczytanie danych
df = pd.read_excel('Porownanie_metod_do_radara.xlsx')

# Lista metod do iteracji
methods = [
    ('Hellwig', 'Hellwig Boxplot Rank', 'Hellwig K-NN Rank'),
    ('Topsis', 'Topsis Boxplot Rank', 'Topsis K-NN Rank'),
    ('Topsis_u', 'Topsis u Boxplot Rank', 'Topsis u K-NN Rank'),
    ('SSW', 'SSW Boxplot Rank', 'SSW K-NN Rank'),
    ('Nowak', 'Nowak Boxplot Rank', 'Nowak K-NN Rank'),
    ('MUZ', 'MUZ Boxplot Rank', 'MUZ K-NN Rank'),
    ('STRAHL', 'STRAHL Boxplot Rank', 'STRAHL K-NN Rank')
]

# Generowanie wykresów dla każdej metody
for method_name, boxplot_col, knn_col in methods:
    # Wybór danych
    countries = df['Kraj']
    ranking_boxplot = df[boxplot_col]
    ranking_knn = df[knn_col]

    # Liczba państw i wartości kątów
    num_countries = len(countries.dropna())
    angles = np.linspace(0, 2 * np.pi, num_countries, endpoint=False).tolist()
    angles += [angles[0]]  # Dodanie pierwszego kąta na koniec listy, aby zamknąć wykres radarowy

    # Dodanie danych do wykresu
    ranking_boxplot = ranking_boxplot.tolist() + [ranking_boxplot[0]]
    ranking_knn = ranking_knn.tolist() + [ranking_knn[0]]

    fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(polar=True))
    ax.plot(angles, ranking_boxplot, linewidth=1, linestyle='solid', label=f'{method_name} (Boxplot)')
    ax.plot(angles, ranking_knn, linewidth=1, linestyle='solid', label=f'{method_name} (K-NN)')

    for i, country in enumerate(countries.dropna()):
        ax.text(angles[i], max(max(ranking_boxplot), max(ranking_knn)) + 0.1, country, fontsize=3, ha='center')

    ax.set_title(f'Porównanie rankingów metodą {method_name} (Boxplot vs K-NN)')
    ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

    # Zapisanie wykresu
    plt.savefig(f'radar_{method_name}.jpg', dpi=600)
    plt.close()  # Zamknięcie figury, aby uniknąć nakładania się wykresów