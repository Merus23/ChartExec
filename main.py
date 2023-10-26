import pandas as pd
import matplotlib.pyplot as plt

# Leia o arquivo (substitua 'seu_arquivo.xlsx' pelo nome do seu arquivo)
# Para arquivos XLSX
data = pd.read_excel('dataset/dates.xlsx')

# Para arquivos CSV
# data = pd.read_csv('seu_arquivo.csv')

# Para arquivos ODS (precisa da biblioteca 'pyexcel-ods3')
# data = pd.read_excel('seu_arquivo.ods', engine='odf')

# Vamos assumir que suas colunas são chamadas 'X' e 'Y'
# Se os nomes das colunas forem diferentes, ajuste os nomes na linha abaixo
# Por exemplo, se suas colunas forem 'ColunaX' e 'ColunaY', você usaria:
# x = data['ColunaX']
# y = data['ColunaY']

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
plt.show()
