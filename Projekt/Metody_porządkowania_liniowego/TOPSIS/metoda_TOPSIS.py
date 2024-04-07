import pandas as pd

def strahl_method(dataframe):
    df = pd.read_excel(dataframe, index_col=0)
    max = df.max()
    print(max)
    output = df / max

    for i in range(4, 8):
        output.iloc[:, i] = -df.iloc[:, i] / max[i]
        print(df.iloc[:, i])

    output['Qi'] = output.sum(axis=1)/df.shape[1]
    output.to_excel('STRAHL_INPUT_2.xlsx', sheet_name='Qi')

    ranking = output.sort_values(by='Qi', ascending=False)

    ranking['Miejsce'] = range(1, len(ranking)+1)
    ranking = ranking[['Qi','Miejsce']]
    ranking.to_excel('STRAHL_INPUT_2.xlsx', sheet_name='Rank')

dataframe = 'INPUT_ABS.xlsx'
strahl_method(dataframe)
