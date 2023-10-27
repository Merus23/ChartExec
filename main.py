import pandas as pd
import matplotlib.pyplot as plt
import platform
import os

def Chart():
    
    caminho = os.getcwd()
    itens = os.listdir(caminho)

    for item in itens:
        extension = item.split('.')[-1]
        if extension == 'xlsx':    
            name = item.split('.')[0]
            data = pd.read_excel(item)
        elif extension == 'csv':
            name = item.split('.')[0]
            data = pd.read_csv(item)
        elif extension == 'xls':
            name = item.split('.')[0]
            data = pd.read_excel(item)

    x = data['X']
    y = data['Y']

    # Crie o gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker='o', linestyle='-', color='b', label='Dados')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.title('Gráfico de Dispersão')
    plt.legend()
    plt.grid(True)   
    plt.savefig(name+'.png')


if __name__ == "__main__":
    Chart()