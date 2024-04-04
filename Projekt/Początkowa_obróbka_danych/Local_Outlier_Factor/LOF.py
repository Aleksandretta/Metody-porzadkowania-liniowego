#Wyszukuje obserwacje odstajace metodą Local Outlier Factor (LOF) dla datasetow z lat 2004 i 2016, a następnie generuje plik Excela z wynikami (oddzielny arkusz na oddzielny rok)

import pandas as pd
xlsx = pd.ExcelFile('data.xlsx')
df_2004 = pd.read_excel(xlsx, dtype = float, sheet_name='2004')

from sklearn.neighbors import LocalOutlierFactor
lof = LocalOutlierFactor()
outliers_2004 = lof.fit_predict(df_2004)
outliers_df_2004 = df_2004[outliers_2004 == -1]

xlsx2 = pd.ExcelFile('data.xlsx')
df_2016 = pd.read_excel(xlsx, dtype = float, sheet_name='2016')

from sklearn.neighbors import LocalOutlierFactor
lof = LocalOutlierFactor()
outliers_2016 = lof.fit_predict(df_2016)
outliers_df_2016 = df_2016[outliers_2016 == -1]

# Save outliers to an Excel file with two different sheets
with pd.ExcelWriter('outliers_2004_2016.xlsx') as writer:
    outliers_df_2004.to_excel(writer, sheet_name='Outliers_2004', index=False)
    outliers_df_2016.to_excel(writer, sheet_name='Outliers_2016', index=False)
