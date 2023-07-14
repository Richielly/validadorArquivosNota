import pandas as pd
import grafico
#o arquivo deve estar no formato csv
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

def verifica_nome_documento(coluna_documento, coluna_nome):

    grouped_data = data.groupby(coluna_documento)[coluna_nome].nunique()
    # retorna quando em um mesmo documento existem nomes diferentes no arquivo
    documents_with_multiple_names = grouped_data[grouped_data > 1]

    return documents_with_multiple_names.sort_values(ascending=False)

def rank_prestador(top):

    # Convert column 1 and column 5 values to numeric, ignoring errors for non-numeric values
    data.loc[:, 1] = pd.to_numeric(data[1], errors='coerce')
    # Group the data by column 5, count the number of occurrences, and get the max value in column 1
    grouped_data = data.groupby(5)[1].agg(['count', 'max'])
    # Rename the columns for clarity
    grouped_data.columns = ['Number_of_Notes', 'Max_Note_Value']
    # Sort the data by the number of notes in descending order to get a ranking
    ranking = grouped_data.sort_values(by='Number_of_Notes', ascending=False)

    return ranking.head(top)

def rank_tomador():

    grouped_data = data.groupby([8, 9, 10]).size().reset_index(name='Count')
    # ordenando no maior para o menor
    sorted_grouped_data = grouped_data.sort_values(by='Count', ascending=False)

    return sorted_grouped_data

grafico.build_chart(rank_prestador(30))

