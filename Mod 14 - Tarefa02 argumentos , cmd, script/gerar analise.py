import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys

sns.set()

def plota_pivot_table(df, value, index, func, ylabel, xlabel, opcao='nada'):
    if opcao == 'nada':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=func).plot(figsize=[15, 5])
    elif opcao == 'sort':
        pd.pivot_table(df, values=value, index=index, aggfunc=func).sort_values(
            value).plot(figsize=[15, 5])
    elif opcao == 'unstack':
        pd.pivot_table(df, values=value, index=index,
                       aggfunc=func).unstack().plot(figsize=[15, 5])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    return None

lista_meses = sys.argv[1:]

for mes in lista_meses:
    mes

    sinasc = pd.read_csv('./input/SINASC_RO_2019_'+mes+'.csv')

    max_data = sinasc.DTNASC.max()[: 7]
    print(max_data)

    os.makedirs('./output/figs/'+max_data, exist_ok=True)

    plota_pivot_table(sinasc, 'IDADEMAE', 'DTNASC', 'count', 'Quantidade de Nascimento', 'Data de Nascimento')
    plt.savefig('./output/figs/'+max_data+'/quantidade-de-nascimento.png')

    plota_pivot_table(sinasc, 'IDADEMAE', [ 'DTNASC', 'SEXO'], 'mean', 'Media Idade Mae', 'Data de Nascimento', 'unstack')
    plt.savefig('./output/figs/'+max_data+'/media-idade-mae-por-sexo.png')

    plota_pivot_table(sinasc, 'PESO', [ 'DTNASC', 'SEXO'], 'mean', 'Media Peso Bebe', 'Data de Nascimento', 'unstack')
    plt.savefig('./output/figs/'+max_data+'/media-peso-bebe-por-sexo.png')

    plota_pivot_table(sinasc, 'PESO', 'ESCMAE', 'median', 'Apgar1 Medio', 'Gestacao', 'sort')
    plt.savefig('./output/figs/'+max_data+'/media-apgar1-por-escolaridade-mae.png')

    plota_pivot_table(sinasc, 'APGAR1', 'GESTACAO', 'mean', 'Apgar1 Aedio', 'Gestacao', 'sort')
    plt.savefig('./output/figs/'+max_data+'/media-apgar1-por-gestacao.png')

    plota_pivot_table(sinasc, 'APGAR5', 'GESTACAO', 'mean', 'Apgar5 Medio', 'Gestacao', 'sort')
    plt.savefig('./output/figs/'+max_data+'/media-apgar5-por-gestacao.png')