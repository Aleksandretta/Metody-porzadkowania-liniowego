import pandas as pd

# Wczytanie danych z arkusza "boxplot_qi"
df = pd.read_excel('podzial_na_grupy.xlsx', sheet_name='boxplot_qi')

# Obliczenie R, max_i_qi i min_i_qi
max_i_qi = df['strahl_qi'].max()
min_i_qi = df['strahl_qi'].min()
R = max_i_qi - min_i_qi

# Funkcja do przypisywania qi do odpowiedniej grupy
def assign_group(qi):
    if max_i_qi - 0.25*R < qi <= max_i_qi:
        return 1
    elif max_i_qi - 0.5*R < qi <= max_i_qi - 0.25*R:
        return 2
    elif max_i_qi - 0.75*R < qi <= max_i_qi - 0.5*R:
        return 3
    elif min_i_qi <= qi <= max_i_qi - 0.75*R:
        return 4

# Dodanie nowej kolumny z grupami do danych
df['group'] = df['strahl_qi'].apply(assign_group)
as_gr = assign_group(-0.186888386133246)
print(as_gr)

# Zapisanie danych do nowego pliku Excel
df.to_excel('podzial_na_grupy_boxplot_poprawne.xlsx', index=False)


#ksasiadow
import pandas as pd

# Wczytanie danych z arkusza "boxplot_qi"
df = pd.read_excel('podzial_na_grupy.xlsx', sheet_name='k_sasiadow_qi')

# Obliczenie R, max_i_qi i min_i_qi
max_i_qi = df['ssw_qi'].max()
min_i_qi = df['ssw_qi'].min()
R = max_i_qi - min_i_qi

# Funkcja do przypisywania qi do odpowiedniej grupy
def assign_group(qi):
    if max_i_qi - 0.25*R < qi <= max_i_qi:
        return 1
    elif max_i_qi - 0.5*R < qi <= max_i_qi - 0.25*R:
        return 2
    elif max_i_qi - 0.75*R < qi <= max_i_qi - 0.5*R:
        return 3
    elif min_i_qi <= qi <= max_i_qi - 0.75*R:
        return 4

# Dodanie nowej kolumny z grupami do danych
df['group'] = df['ssw_qi'].apply(assign_group)
as_gr = assign_group(-0.186888386133246)
print(as_gr)

# Zapisanie danych do nowego pliku Excel
df.to_excel('podzial_na_grupy_k_sasiadow_poprawne.xlsx', index=False)
