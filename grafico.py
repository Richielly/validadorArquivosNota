import seaborn as sns
from matplotlib import pyplot as plt

def build_chart(data):
    # Create a new figure for number of notes
    plt.figure(figsize=(12, 6))
    barplot1 = sns.barplot(x=data.index, y=data['Number_of_Notes'], palette="viridis")
    plt.title('Número de notas emitidas por empresa')
    plt.xlabel('Empresa')
    plt.ylabel('Quantidade de notas')
    plt.xticks(rotation=90)

    # Add data labels
    for p in barplot1.patches:
        barplot1.annotate(format(p.get_height(), '.0f'),
                          (p.get_x() + p.get_width() / 2., p.get_height()),
                          ha='center', va='center',
                          xytext=(0, 9),
                          textcoords='offset points')
    plt.show()

    # Create a new figure for max note value
    plt.figure(figsize=(12, 6))
    barplot2 = sns.barplot(x=data.index, y=data['Max_Note_Value'], palette="magma")
    plt.title('Última sequência de nota emitida pela empresa.')
    plt.xlabel('Empresa')
    plt.ylabel('Última nota')
    plt.xticks(rotation=90)

    # Add data labels
    for p in barplot2.patches:
        barplot2.annotate(format(p.get_height(), '.0f'),
                          (p.get_x() + p.get_width() / 2., p.get_height()),
                          ha='center', va='center',
                          xytext=(0, 9),
                          textcoords='offset points')
    plt.show()
