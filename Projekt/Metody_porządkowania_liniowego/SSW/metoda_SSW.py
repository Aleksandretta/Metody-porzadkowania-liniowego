import pandas as pd

def ssw_method(dataframe):
    df = pd.read_excel(dataframe, index_col=0,)

    srednia = df.mean()
    odchylenie_std = df.std()

    output = (df - srednia)/odchylenie_std

    output['Qi'] = output.sum(axis=1)/df.shape[1]
    output.to_excel('SSW_INPUT.xlsx', sheet_name='SSW')

    df_sorted = output.sort_values(by='Qi', ascending=False)

    df_sorted["Miejsce"] = range(1, len(df_sorted)+1)
    df_sorted = df_sorted[['Qi', 'Miejsce']]
    df_sorted.to_excel('SSW_INPUT.xlsx', sheet_name='SSW_ranking')

dataframe = "INPUT.xlsx"
ssw_method(dataframe)
