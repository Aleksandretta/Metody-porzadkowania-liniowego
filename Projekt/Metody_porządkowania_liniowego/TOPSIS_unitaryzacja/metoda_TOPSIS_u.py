import pandas as pd
import numpy as np

df2 = pd.read_excel('INPUT_ABS.xlsx')
df2 = df2.iloc[:, 1:]

# Unitaryzacja danych
normalized_df = (df2 - df2.min()) / (df2.max() - df2.min())

# Wyznaczenie współrzędnych wzorca
z_0_plus = pd.concat([normalized_df.iloc[:, :4].max(), normalized_df.iloc[:, 4:].min()])
z_0_minus = pd.concat([normalized_df.iloc[:, :4].min(), normalized_df.iloc[:, 4:].max()])

# Obliczenie odległości obiektów od wzorca i antywzorca
d_i_0_plus = np.sqrt(np.sum((normalized_df - z_0_plus)**2, axis=1))
d_i_0_minus = np.sqrt(np.sum((normalized_df - z_0_minus)**2, axis=1))

# Obliczenie wartości zmiennej agregatowej
df2['qi'] = d_i_0_minus / (d_i_0_plus + d_i_0_minus)

# Przyporządkowanie rang
df2['Rank'] = df2['qi'].rank(ascending=False)

with pd.ExcelWriter('TOPSIS_U_INPUT.xlsx', engine='openpyxl') as writer:
    df2.to_excel(writer, index=False)

print("Plik 'topsis_k-sas_unitar.xlsx' został zapisany z sukcesem.")
