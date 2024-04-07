import pandas as pd

# Wczytaj plik Excel do ramki danych
data = pd.read_excel('INPUT_boxplot.xlsx')

# Pomijaj pierwszą kolumnę
data_without_first_column = data.iloc[:, 1:]

# Oblicz wartości minimalne dla każdej kolumny
min_values = data_without_first_column.min()

# Oblicz wartości maksymalne dla każdej kolumny
max_values = data_without_first_column.max()

# Zastosuj wzór dla każdej komórki
for column in data_without_first_column.columns:
    min_val = min_values[column]
    max_val = max_values[column]
    data[column] = (data[column] - min_val) / (max_val - min_val)

# Oblicz q_i
m = len(data_without_first_column.columns)
data['qi'] = data.iloc[:, 1:].sum(axis=1) / m

# Zapisz zaktualizowane dane do nowego pliku Excel
data.to_excel('MUZ_INPUT_boxplot.xlsx', index=False)
