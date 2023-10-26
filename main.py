import pandas as pd
import matplotlib.pyplot as plt
import platform


def Chart(source):
    extension = source.split('.')[-1]
    if extension == 'xlsx':    
        data = pd.read_excel(source)
    elif extension == 'csv':
        data = pd.read_csv(source)
    else:
        data = pd.read_excel(source, engine='odf')


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
    if len(sys.argv) < 2:
        print("Usage: python main.py <source path>")
        sys.exit(1)
    
    source = sys.argv[1]

    Chart(source=source)