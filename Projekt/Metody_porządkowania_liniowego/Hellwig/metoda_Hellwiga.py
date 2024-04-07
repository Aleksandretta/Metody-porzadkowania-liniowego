import pandas as pd
import numpy as np

# Wczytaj dane z pliku Excela
df = pd.read_excel('INPUT_ABS.xlsx')
df = df.iloc[:, 1:]

# Normalizacja zmiennych - standardyzacja
df_normalized = df.apply(lambda x: (x - x.mean()) / x.std())

# Współrzędne wzorca z_0j
z_0j = pd.concat([df_normalized.iloc[:, :4].max(), df_normalized.iloc[:, 4:].min()])

# Odległości obiektów od wzorca
d_i0 = np.sqrt(((df_normalized - z_0j) ** 2).sum(axis=1))
print(d_i0)

# Wartosci zmiennej agregatowej
d_0 = d_i0.mean()
S_d = d_i0.std()
q_i = 1 - (d_i0 / (d_0 + 2 * S_d))

# Dodanie wyników do DataFrame
df['q_i'] = q_i
df['Rank'] = df['q_i'].rank(ascending=False)

# Zapis do nowego pliku Excela
output_filename = 'HELLWIG_INPUT.xlsx'
with pd.ExcelWriter(output_filename, engine='openpyxl') as writer:
    df.to_excel(writer, index=False)

print(f"Plik '{output_filename}' został zapisany.")
