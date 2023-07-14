import pandas as pd

data = pd.read_csv(r'C:\Users\Equiplano\Downloads\notas.csv', sep="|")
# Precisa separar os dados das linhas por colunas separando pelo pipe
data = data['extractnota'].str.split("|", expand=True)


def verifica_duplicidade(colunas):
    # esta é a especificação de quais colunas devem ser verificadas como chave na duplicidade
    data_subset = data.iloc[:, colunas]

    # esta linha verifica as linhas duplicadas, e retorna True quando é econtrado uma duplicidade
    duplicate_rows = data_subset.duplicated()

    # retorna a quantidade de linhas duplicadas conforme filtro estabelecido
    num_duplicate_rows = duplicate_rows.sum()

    # retorna a linha que esta duplicada
    duplicate_data = data_subset[duplicate_rows]

    num_duplicate_rows, duplicate_data.head()

    return num_duplicate_rows, duplicate_data.head()

def verifica_tomador():
    # agrupando pelas colunas de tipo pessoa, documento e nome, retornando uma coluna com a quantidade encontrada
    grouped_data = data.groupby([8, 9, 10]).size().reset_index(name='Count')

    return grouped_data

def rank_tomador():
    grouped_data = data.groupby([8, 9, 10]).size().reset_index(name='Count')
    # ordenando no maior para o menor
    sorted_grouped_data = grouped_data.sort_values(by='Count', ascending=False)

    return sorted_grouped_data

