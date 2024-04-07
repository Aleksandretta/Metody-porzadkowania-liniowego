import pandas as pd

def nowak_method(dataframe):
    df = pd.read_excel(dataframe, index_col=0)

    srednia = df.mean()

    output = df/srednia
    for i in range(4, 8): 
        output.iloc[:, i] = -df.iloc[:, i] / srednia[i]
        print(df.iloc[:, i])

    output['Qi'] = output.sum(axis=1)/df.shape[1]
    output.to_excel('NOWAK_INPUT_2.xlsx', sheet_name='Qi')

    df_sorted = output.sort_values(by='Qi', ascending=False)

    df_sorted['Miejsce'] = range(1, len(df_sorted)+1)
    df_sorted = df_sorted[['Qi','Miejsce']]
    df_sorted.to_excel('NOWAK_INPUT_2.xlsx', sheet_name='Rank')

dataframe = 'INPUT_ABS.xlsx'
nowak_method(dataframe)
