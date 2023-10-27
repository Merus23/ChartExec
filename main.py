import pandas as pd
import matplotlib.pyplot as plt
import platform
import sys
import os

def Chart():
    
    caminho = os.getcwd()
    itens = os.listdir(caminho)

    for item in itens:
        extension = item.split('.')[-1]
        if extension == 'xlsx':    
            data = pd.read_excel(item)
        elif extension == 'csv':
            data = pd.read_csv(item)
        elif extension == 'xls':
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

    so = platform.system()
    if so == 'Windows':
        name = source.split('\\')[-1].split('.')[0]
    else:
        name = source.split('/')[-1].split('.')[0]
   
    plt.savefig(name+'.png')



if __name__ == "__main__":
    print("Execute in the same directory of the sheets")
    Chart()