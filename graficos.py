import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import FixedLocator, FixedFormatter
import os

#descomentar para esconder o warring
#import warnings
#warnings.filterwarnings("ignore")

# Obtém o diretório de trabalho atual
home_path = os.getcwd()

from config import *

#caminho que lê os arquivos do primeiro algoritmo
local_path_1 = home_path+'\\eon_simulator-Salvador-CostI-V12\\out\\'+TOPOLOGY+'\\'
#caminho que lê os arquivos do segundo algoritmo
local_path_2 = home_path+'\\eon_simulator-Salvador-P-KSP-V12\\out\\'+TOPOLOGY+'\\'
#caminho que lê os arquivos do segundo algoritmo
local_path_3 = home_path+'\\eon_simulator_salvador_V12\\out\\'+TOPOLOGY+'\\'
#caminho que lê os arquivos do segundo algoritmo
local_path_4 = home_path+'\\eon_simulator-Salvador-TSSCF-v12\\out\\'+TOPOLOGY+'\\'
#caminho onde salva os plots
local_path = home_path+'\\plots\\'


#legenda do 1 e 2 programa nos graficos 
prog1 = 'CFCoSP'
prog2 = 'P-KSP'
prog3 = 'CRIA'
prog4 = 'TSSCF'

# Configurar tamanho padrão da fonte para todo o gráfico
plt.rcParams.update({'font.size': 16})


# Carrega os dados dos arquivos de bloqueio para os três algoritmos
data_alg1 = np.loadtxt(local_path_1+"bloqueio.dat")
data_alg2 = np.loadtxt(local_path_2+"bloqueio.dat")
data_alg3 = np.loadtxt(local_path_3+"bloqueio.dat")
data_alg4 = np.loadtxt(local_path_4+"bloqueio.dat")

# Converte os dados em DataFrames do pandas para facilitar o manuseio
data_pd_alg1 = pd.DataFrame(data_alg1, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg2 = pd.DataFrame(data_alg2, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg3 = pd.DataFrame(data_alg3, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg4 = pd.DataFrame(data_alg4, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])


 
 
# Configurar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(data_pd_alg1['Erlangs'], data_pd_alg1['Medio'], marker='o', label='Médio',color='g' )
plt.plot(data_pd_alg2['Erlangs'], data_pd_alg2['Medio'], marker='D', label='Médio',color='b', linestyle='dashed' )
plt.plot(data_pd_alg3['Erlangs'], data_pd_alg3['Medio'], marker='x', label='Médio',color='r' , linestyle=':')
plt.plot(data_pd_alg4['Erlangs'], data_pd_alg4['Medio'], marker='d', label='Médio',color='black' , linestyle='-.')


plt.vlines(data_pd_alg1['Erlangs'], ymin=data_pd_alg1['Minimo'], ymax=data_pd_alg1['Maximo'], colors='g')
plt.vlines(data_pd_alg2['Erlangs'], ymin=data_pd_alg2['Minimo'], ymax=data_pd_alg2['Maximo'], colors='b', linestyle='dashed')
plt.vlines(data_pd_alg3['Erlangs'], ymin=data_pd_alg3['Minimo'], ymax=data_pd_alg3['Maximo'], colors='r', linestyle=':')
plt.vlines(data_pd_alg4['Erlangs'], ymin=data_pd_alg4['Minimo'], ymax=data_pd_alg4['Maximo'], colors='black', linestyle='-.')

# Linhas horizontais no início e no fim do intervalo de confiança
for i in range(len(data_pd_alg1)):
    plt.plot([data_pd_alg1['Erlangs'][i] - 0.02, data_pd_alg1['Erlangs'][i] + 0.02], [data_pd_alg1['Minimo'][i], data_pd_alg1['Minimo'][i]], color='g')
    plt.plot([data_pd_alg1['Erlangs'][i] - 0.02, data_pd_alg1['Erlangs'][i] + 0.02], [data_pd_alg1['Maximo'][i], data_pd_alg1['Maximo'][i]], color='g')
    plt.plot([data_pd_alg2['Erlangs'][i] - 0.02, data_pd_alg2['Erlangs'][i] + 0.02], [data_pd_alg2['Minimo'][i], data_pd_alg2['Minimo'][i]], color='b', linestyle='dashed')
    plt.plot([data_pd_alg2['Erlangs'][i] - 0.02, data_pd_alg2['Erlangs'][i] + 0.02], [data_pd_alg2['Maximo'][i], data_pd_alg2['Maximo'][i]], color='b', linestyle='dashed')
    plt.plot([data_pd_alg3['Erlangs'][i] - 0.02, data_pd_alg3['Erlangs'][i] + 0.02], [data_pd_alg3['Minimo'][i], data_pd_alg3['Minimo'][i]], color='r', linestyle=':')
    plt.plot([data_pd_alg3['Erlangs'][i] - 0.02, data_pd_alg3['Erlangs'][i] + 0.02], [data_pd_alg3['Maximo'][i], data_pd_alg3['Maximo'][i]], color='r', linestyle=':')
    plt.plot([data_pd_alg4['Erlangs'][i] - 0.02, data_pd_alg4['Erlangs'][i] + 0.02], [data_pd_alg4['Minimo'][i], data_pd_alg4['Minimo'][i]], color='black', linestyle='-.')
    plt.plot([data_pd_alg4['Erlangs'][i] - 0.02, data_pd_alg4['Erlangs'][i] + 0.02], [data_pd_alg4['Maximo'][i], data_pd_alg4['Maximo'][i]], color='black', linestyle='-.')



plt.ylabel('% Bloqueio de circuitos')
plt.xlabel(f'Carga em Erlangs na Topologia {TOPOLOGY.upper()}')
# plt.title(f'Probabilidade de Bloqueio de circuitos na Topologia {TOPOLOGY.upper()}')
plt.legend(labels=[prog1, prog2, prog3, prog4])
plt.savefig(local_path+'bloqueio.png', bbox_inches='tight')
plt.close()

print('Grafico % Bloqueio')




data_alg1 = np.loadtxt(local_path_1+"bloqueio_banda.dat")
data_alg2 = np.loadtxt(local_path_2+"bloqueio_banda.dat")
data_alg3 = np.loadtxt(local_path_3+"bloqueio_banda.dat")
data_alg4 = np.loadtxt(local_path_4+"bloqueio_banda.dat")
# Converte os dados em DataFrames do pandas para facilitar o manuseio
data_pd_alg1  = pd.DataFrame(data_alg1, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg2 = pd.DataFrame(data_alg2, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg3 = pd.DataFrame(data_alg3, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg4 = pd.DataFrame(data_alg4, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])


 
 
# Configurar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(data_pd_alg1['Erlangs'], data_pd_alg1['Medio'], marker='o', label='Médio',color='g' )
plt.plot(data_pd_alg2['Erlangs'], data_pd_alg2['Medio'], marker='D', label='Médio',color='b', linestyle='dashed' )
plt.plot(data_pd_alg3['Erlangs'], data_pd_alg3['Medio'], marker='x', label='Médio',color='r' , linestyle=':')
plt.plot(data_pd_alg4['Erlangs'], data_pd_alg4['Medio'], marker='d', label='Médio',color='black' , linestyle='-.')


plt.vlines(data_pd_alg1['Erlangs'], ymin=data_pd_alg1['Minimo'], ymax=data_pd_alg1['Maximo'], colors='g')
plt.vlines(data_pd_alg2['Erlangs'], ymin=data_pd_alg2['Minimo'], ymax=data_pd_alg2['Maximo'], colors='b', linestyle='dashed')
plt.vlines(data_pd_alg3['Erlangs'], ymin=data_pd_alg3['Minimo'], ymax=data_pd_alg3['Maximo'], colors='r', linestyle=':')
plt.vlines(data_pd_alg4['Erlangs'], ymin=data_pd_alg4['Minimo'], ymax=data_pd_alg4['Maximo'], colors='black', linestyle='-.')

# Linhas horizontais no início e no fim do intervalo de confiança
for i in range(len(data_pd_alg1)):
    plt.plot([data_pd_alg1['Erlangs'][i] - 0.02, data_pd_alg1['Erlangs'][i] + 0.02], [data_pd_alg1['Minimo'][i], data_pd_alg1['Minimo'][i]], color='g')
    plt.plot([data_pd_alg1['Erlangs'][i] - 0.02, data_pd_alg1['Erlangs'][i] + 0.02], [data_pd_alg1['Maximo'][i], data_pd_alg1['Maximo'][i]], color='g')
    plt.plot([data_pd_alg2['Erlangs'][i] - 0.02, data_pd_alg2['Erlangs'][i] + 0.02], [data_pd_alg2['Minimo'][i], data_pd_alg2['Minimo'][i]], color='b', linestyle='dashed')
    plt.plot([data_pd_alg2['Erlangs'][i] - 0.02, data_pd_alg2['Erlangs'][i] + 0.02], [data_pd_alg2['Maximo'][i], data_pd_alg2['Maximo'][i]], color='b', linestyle='dashed')
    plt.plot([data_pd_alg3['Erlangs'][i] - 0.02, data_pd_alg3['Erlangs'][i] + 0.02], [data_pd_alg3['Minimo'][i], data_pd_alg3['Minimo'][i]], color='r', linestyle=':')
    plt.plot([data_pd_alg3['Erlangs'][i] - 0.02, data_pd_alg3['Erlangs'][i] + 0.02], [data_pd_alg3['Maximo'][i], data_pd_alg3['Maximo'][i]], color='r', linestyle=':')
    plt.plot([data_pd_alg4['Erlangs'][i] - 0.02, data_pd_alg4['Erlangs'][i] + 0.02], [data_pd_alg4['Minimo'][i], data_pd_alg4['Minimo'][i]], color='black', linestyle='-.')
    plt.plot([data_pd_alg4['Erlangs'][i] - 0.02, data_pd_alg4['Erlangs'][i] + 0.02], [data_pd_alg4['Maximo'][i], data_pd_alg4['Maximo'][i]], color='black', linestyle='-.')



plt.ylabel('% Bloqueio de Banda')
plt.xlabel(f'Carga em Erlangs na Topologia {TOPOLOGY.upper()}')
# plt.title(f'Probabilidade de Bloqueio de Banda na Topologia {TOPOLOGY.upper()}')
plt.legend(labels=[prog1, prog2, prog3, prog4])
plt.savefig(local_path+'bloqueio_banda.png', bbox_inches='tight')
plt.close()
print('Grafico Bloqueio de Banda')

data_alg1 = np.loadtxt(local_path_1+"bloqueio_classe1.dat")
data_alg2 = np.loadtxt(local_path_2+"bloqueio_classe1.dat")
data_alg3 = np.loadtxt(local_path_3+"bloqueio_classe1.dat")
data_alg4 = np.loadtxt(local_path_4+"bloqueio_classe1.dat")
# Converte os dados em DataFrames do pandas para facilitar o manuseio
data_pd_alg1  = pd.DataFrame(data_alg1, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg2 = pd.DataFrame(data_alg2, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg3 = pd.DataFrame(data_alg3, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg4 = pd.DataFrame(data_alg4, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])


 
 
# Configurar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(data_pd_alg1['Erlangs'], data_pd_alg1['Medio'], marker='o', label='Médio',color='g' )
plt.plot(data_pd_alg2['Erlangs'], data_pd_alg2['Medio'], marker='D', label='Médio',color='b', linestyle='dashed' )
plt.plot(data_pd_alg3['Erlangs'], data_pd_alg3['Medio'], marker='x', label='Médio',color='r' , linestyle=':')
plt.plot(data_pd_alg4['Erlangs'], data_pd_alg4['Medio'], marker='d', label='Médio',color='black' , linestyle='-.')


plt.vlines(data_pd_alg1['Erlangs'], ymin=data_pd_alg1['Minimo'], ymax=data_pd_alg1['Maximo'], colors='g')
plt.vlines(data_pd_alg2['Erlangs'], ymin=data_pd_alg2['Minimo'], ymax=data_pd_alg2['Maximo'], colors='b', linestyle='dashed')
plt.vlines(data_pd_alg3['Erlangs'], ymin=data_pd_alg3['Minimo'], ymax=data_pd_alg3['Maximo'], colors='r', linestyle=':')
plt.vlines(data_pd_alg4['Erlangs'], ymin=data_pd_alg4['Minimo'], ymax=data_pd_alg4['Maximo'], colors='black', linestyle='-.')

# Linhas horizontais no início e no fim do intervalo de confiança
for i in range(len(data_pd_alg1)):
    plt.plot([data_pd_alg1['Erlangs'][i] - 0.02, data_pd_alg1['Erlangs'][i] + 0.02], [data_pd_alg1['Minimo'][i], data_pd_alg1['Minimo'][i]], color='g')
    plt.plot([data_pd_alg1['Erlangs'][i] - 0.02, data_pd_alg1['Erlangs'][i] + 0.02], [data_pd_alg1['Maximo'][i], data_pd_alg1['Maximo'][i]], color='g')
    plt.plot([data_pd_alg2['Erlangs'][i] - 0.02, data_pd_alg2['Erlangs'][i] + 0.02], [data_pd_alg2['Minimo'][i], data_pd_alg2['Minimo'][i]], color='b', linestyle='dashed')
    plt.plot([data_pd_alg2['Erlangs'][i] - 0.02, data_pd_alg2['Erlangs'][i] + 0.02], [data_pd_alg2['Maximo'][i], data_pd_alg2['Maximo'][i]], color='b', linestyle='dashed')
    plt.plot([data_pd_alg3['Erlangs'][i] - 0.02, data_pd_alg3['Erlangs'][i] + 0.02], [data_pd_alg3['Minimo'][i], data_pd_alg3['Minimo'][i]], color='r', linestyle=':')
    plt.plot([data_pd_alg3['Erlangs'][i] - 0.02, data_pd_alg3['Erlangs'][i] + 0.02], [data_pd_alg3['Maximo'][i], data_pd_alg3['Maximo'][i]], color='r', linestyle=':')
    plt.plot([data_pd_alg4['Erlangs'][i] - 0.02, data_pd_alg4['Erlangs'][i] + 0.02], [data_pd_alg4['Minimo'][i], data_pd_alg4['Minimo'][i]], color='black', linestyle='-.')
    plt.plot([data_pd_alg4['Erlangs'][i] - 0.02, data_pd_alg4['Erlangs'][i] + 0.02], [data_pd_alg4['Maximo'][i], data_pd_alg4['Maximo'][i]], color='black', linestyle='-.')

plt.ylabel('% Bloqueio Classe 1')
plt.xlabel(f'Carga em Erlangs na Topologia {TOPOLOGY.upper()}')
# plt.title(f'Probabilidade de Bloqueio Classe 1 na Topologia {TOPOLOGY.upper()}')
plt.legend(labels=[prog1, prog2, prog3, prog4])
plt.savefig(local_path+'bloqueio_classe1.png', bbox_inches='tight')

print('Grafico Bloqueio de Classe 1')
 
fig = plt.figure()
fig.add_subplot(121)
data_alg1 = np.loadtxt(local_path_1+"bloqueio_classe2.dat")
data_alg2 = np.loadtxt(local_path_2+"bloqueio_classe2.dat")
data_alg3 = np.loadtxt(local_path_3+"bloqueio_classe2.dat")
data_alg4 = np.loadtxt(local_path_4+"bloqueio_classe2.dat")
# Converte os dados em DataFrames do pandas para facilitar o manuseio
data_pd_alg1  = pd.DataFrame(data_alg1, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg2 = pd.DataFrame(data_alg2, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg3 = pd.DataFrame(data_alg3, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg4 = pd.DataFrame(data_alg4, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])


 
 
# Configurar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(data_pd_alg1['Erlangs'], data_pd_alg1['Medio'], marker='o', label='Médio',color='g' )
plt.plot(data_pd_alg2['Erlangs'], data_pd_alg2['Medio'], marker='D', label='Médio',color='b', linestyle='dashed' )
plt.plot(data_pd_alg3['Erlangs'], data_pd_alg3['Medio'], marker='x', label='Médio',color='r' , linestyle=':')
plt.plot(data_pd_alg4['Erlangs'], data_pd_alg4['Medio'], marker='d', label='Médio',color='black' , linestyle='-.')


plt.vlines(data_pd_alg1['Erlangs'], ymin=data_pd_alg1['Minimo'], ymax=data_pd_alg1['Maximo'], colors='g')
plt.vlines(data_pd_alg2['Erlangs'], ymin=data_pd_alg2['Minimo'], ymax=data_pd_alg2['Maximo'], colors='b', linestyle='dashed')
plt.vlines(data_pd_alg3['Erlangs'], ymin=data_pd_alg3['Minimo'], ymax=data_pd_alg3['Maximo'], colors='r', linestyle=':')
plt.vlines(data_pd_alg4['Erlangs'], ymin=data_pd_alg4['Minimo'], ymax=data_pd_alg4['Maximo'], colors='black', linestyle='-.')

# Linhas horizontais no início e no fim do intervalo de confiança
for i in range(len(data_pd_alg1)):
    plt.plot([data_pd_alg1['Erlangs'][i] - 0.02, data_pd_alg1['Erlangs'][i] + 0.02], [data_pd_alg1['Minimo'][i], data_pd_alg1['Minimo'][i]], color='g')
    plt.plot([data_pd_alg1['Erlangs'][i] - 0.02, data_pd_alg1['Erlangs'][i] + 0.02], [data_pd_alg1['Maximo'][i], data_pd_alg1['Maximo'][i]], color='g')
    plt.plot([data_pd_alg2['Erlangs'][i] - 0.02, data_pd_alg2['Erlangs'][i] + 0.02], [data_pd_alg2['Minimo'][i], data_pd_alg2['Minimo'][i]], color='b', linestyle='dashed')
    plt.plot([data_pd_alg2['Erlangs'][i] - 0.02, data_pd_alg2['Erlangs'][i] + 0.02], [data_pd_alg2['Maximo'][i], data_pd_alg2['Maximo'][i]], color='b', linestyle='dashed')
    plt.plot([data_pd_alg3['Erlangs'][i] - 0.02, data_pd_alg3['Erlangs'][i] + 0.02], [data_pd_alg3['Minimo'][i], data_pd_alg3['Minimo'][i]], color='r', linestyle=':')
    plt.plot([data_pd_alg3['Erlangs'][i] - 0.02, data_pd_alg3['Erlangs'][i] + 0.02], [data_pd_alg3['Maximo'][i], data_pd_alg3['Maximo'][i]], color='r', linestyle=':')
    plt.plot([data_pd_alg4['Erlangs'][i] - 0.02, data_pd_alg4['Erlangs'][i] + 0.02], [data_pd_alg4['Minimo'][i], data_pd_alg4['Minimo'][i]], color='black', linestyle='-.')
    plt.plot([data_pd_alg4['Erlangs'][i] - 0.02, data_pd_alg4['Erlangs'][i] + 0.02], [data_pd_alg4['Maximo'][i], data_pd_alg4['Maximo'][i]], color='black', linestyle='-.')

plt.ylabel('% Bloqueio Classe 2')
plt.xlabel(f'Carga em Erlangs na Topologia {TOPOLOGY.upper()}')
# plt.title(f'Probabilidade de Bloqueio Classe 2 na Topologia {TOPOLOGY.upper()}')
plt.legend(labels=[prog1, prog2, prog3, prog4])
plt.savefig(local_path+'bloqueio_classe2.png', bbox_inches='tight')
plt.close()
print('Grafico Bloqueio de Classe 2')

fig = plt.figure()
fig.add_subplot(121)
data_alg1 = np.loadtxt(local_path_1+"bloqueio_classe3.dat")
data_alg2 = np.loadtxt(local_path_2+"bloqueio_classe3.dat")
data_alg3 = np.loadtxt(local_path_3+"bloqueio_classe3.dat")
data_alg4 = np.loadtxt(local_path_4+"bloqueio_classe3.dat")

# Converte os dados em DataFrames do pandas para facilitar o manuseio
data_pd_alg1  = pd.DataFrame(data_alg1, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg2 = pd.DataFrame(data_alg2, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg3 = pd.DataFrame(data_alg3, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
data_pd_alg4 = pd.DataFrame(data_alg4, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])


 
 
# Configurar o gráfico
plt.figure(figsize=(10, 6))
plt.plot(data_pd_alg1['Erlangs'], data_pd_alg1['Medio'], marker='o', label='Médio',color='g' )
plt.plot(data_pd_alg2['Erlangs'], data_pd_alg2['Medio'], marker='D', label='Médio',color='b', linestyle='dashed' )
plt.plot(data_pd_alg3['Erlangs'], data_pd_alg3['Medio'], marker='x', label='Médio',color='r' , linestyle=':')
plt.plot(data_pd_alg4['Erlangs'], data_pd_alg4['Medio'], marker='d', label='Médio',color='black' , linestyle='-.')


plt.vlines(data_pd_alg1['Erlangs'], ymin=data_pd_alg1['Minimo'], ymax=data_pd_alg1['Maximo'], colors='g')
plt.vlines(data_pd_alg2['Erlangs'], ymin=data_pd_alg2['Minimo'], ymax=data_pd_alg2['Maximo'], colors='b', linestyle='dashed')
plt.vlines(data_pd_alg3['Erlangs'], ymin=data_pd_alg3['Minimo'], ymax=data_pd_alg3['Maximo'], colors='r', linestyle=':')
plt.vlines(data_pd_alg4['Erlangs'], ymin=data_pd_alg4['Minimo'], ymax=data_pd_alg4['Maximo'], colors='black', linestyle='-.')

# Linhas horizontais no início e no fim do intervalo de confiança
for i in range(len(data_pd_alg1)):
    plt.plot([data_pd_alg1['Erlangs'][i] - 0.02, data_pd_alg1['Erlangs'][i] + 0.02], [data_pd_alg1['Minimo'][i], data_pd_alg1['Minimo'][i]], color='g')
    plt.plot([data_pd_alg1['Erlangs'][i] - 0.02, data_pd_alg1['Erlangs'][i] + 0.02], [data_pd_alg1['Maximo'][i], data_pd_alg1['Maximo'][i]], color='g')
    plt.plot([data_pd_alg2['Erlangs'][i] - 0.02, data_pd_alg2['Erlangs'][i] + 0.02], [data_pd_alg2['Minimo'][i], data_pd_alg2['Minimo'][i]], color='b', linestyle='dashed')
    plt.plot([data_pd_alg2['Erlangs'][i] - 0.02, data_pd_alg2['Erlangs'][i] + 0.02], [data_pd_alg2['Maximo'][i], data_pd_alg2['Maximo'][i]], color='b', linestyle='dashed')
    plt.plot([data_pd_alg3['Erlangs'][i] - 0.02, data_pd_alg3['Erlangs'][i] + 0.02], [data_pd_alg3['Minimo'][i], data_pd_alg3['Minimo'][i]], color='r', linestyle=':')
    plt.plot([data_pd_alg3['Erlangs'][i] - 0.02, data_pd_alg3['Erlangs'][i] + 0.02], [data_pd_alg3['Maximo'][i], data_pd_alg3['Maximo'][i]], color='r', linestyle=':')
    plt.plot([data_pd_alg4['Erlangs'][i] - 0.02, data_pd_alg4['Erlangs'][i] + 0.02], [data_pd_alg4['Minimo'][i], data_pd_alg4['Minimo'][i]], color='black', linestyle='-.')
    plt.plot([data_pd_alg4['Erlangs'][i] - 0.02, data_pd_alg4['Erlangs'][i] + 0.02], [data_pd_alg4['Maximo'][i], data_pd_alg4['Maximo'][i]], color='black', linestyle='-.')

plt.ylabel(f'% Bloqueio Classe 3')
# plt.ylabel(f'% Bloqueio Classe 3  na Topologia {TOPOLOGY.upper()}')
plt.xlabel(f'Carga em Erlangs na Topologia {TOPOLOGY.upper()}')
# plt.title(f'Probabilidade de Bloqueio Classe 3 na Topologia {TOPOLOGY.upper()}')
plt.legend(labels=[prog1, prog2, prog3, prog4])
plt.savefig(local_path+'bloqueio_classe3.png', bbox_inches='tight')
plt.close()
print('Grafico Bloqueio de Classe 3')


print('Grafico Receita Cessante')


#labels do grafico com EARGLES utilizados na simulacao 
#labels = ['300', '300', '320', '340', '360', '380']
labels = [str(e) for e in range(ERLANG_MIN, ERLANG_MAX + ERLANG_INC, ERLANG_INC)]
labels.insert(0, '0')
X = np.arange(5)

cls100_400_cls = [str(valor) for valor in BANDWIDTH] # ['10','20','40','80','160','200','400']

for i in range(0,len(cls100_400_cls)):
    fig = plt.figure()
    fig.add_subplot(121)
    data_alg1 = np.loadtxt(local_path_1+"Bloqueio_"+cls100_400_cls[i]+".dat")
    data_alg2 = np.loadtxt(local_path_2+"Bloqueio_"+cls100_400_cls[i]+".dat")
    data_alg3 = np.loadtxt(local_path_3+"Bloqueio_"+cls100_400_cls[i]+".dat")
    data_alg4 = np.loadtxt(local_path_4+"Bloqueio_"+cls100_400_cls[i]+".dat")
    data_pd_alg1 = pd.DataFrame(data_alg1, columns = ['Erlangs','Medio','Minimo','Maximo'])
    data_pd_alg2 = pd.DataFrame(data_alg2, columns = ['Erlangs','Medio','Minimo','Maximo'])
    data_pd_alg3 = pd.DataFrame(data_alg3, columns = ['Erlangs','Medio','Minimo','Maximo'])
    data_pd_alg4 = pd.DataFrame(data_alg4, columns = ['Erlangs','Medio','Minimo','Maximo'])
    ax = fig.add_axes([0,0,1,1])
    ax.plot(X , data_pd_alg1['Medio'], color = 'g', marker='o')
    ax.plot(X , data_pd_alg2['Medio'], color = 'b', marker='D',linestyle='dashed')
    ax.plot(X , data_pd_alg3['Medio'], color = 'r', marker='x',linestyle=':')
    ax.plot(X , data_pd_alg4['Medio'], color = 'black', marker='d',linestyle='-.')
    # Configurar os ticks do eixo x
    locator = FixedLocator(X)
    formatter = FixedFormatter(labels[1:])
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    ax.set_ylabel("% Bloqueio de Banda "+cls100_400_cls[i])
    ax.set_xlabel(f' Carga em Erlangs na Topologia {TOPOLOGY.upper()}')
    # ax.set_title("Bloqueio Banda "+cls100_400_cls[i])
    ax.legend(labels=[prog1, prog2, prog3, prog4])
    plt.savefig(local_path+'Bloqueio_Banda_'+cls100_400_cls[i]+'.png', bbox_inches='tight')
    print('Grafico Bloqueio de Banda' + cls100_400_cls[i])
    plt.close(fig)


print('Grafico Receita Cessante')


cls100_400_cls = [str(valor) for valor in BANDWIDTH] # ['10','20','40','80','160','200','400']


for i in range(0,len(cls100_400_cls)):
    fig = plt.figure()
    fig.add_subplot(121)
    data_alg1 = np.loadtxt(local_path_1+"Custo_bloqueio_"+cls100_400_cls[i]+".dat")
    data_alg2 = np.loadtxt(local_path_2+"Custo_bloqueio_"+cls100_400_cls[i]+".dat")
    data_alg3 = np.loadtxt(local_path_3+"Custo_bloqueio_"+cls100_400_cls[i]+".dat")
    data_alg4 = np.loadtxt(local_path_4+"Custo_bloqueio_"+cls100_400_cls[i]+".dat")
    data_pd_alg1 = pd.DataFrame(data_alg1, columns = ['Erlangs','Medio','Minimo','Maximo'])
    data_pd_alg2 = pd.DataFrame(data_alg2, columns = ['Erlangs','Medio','Minimo','Maximo'])
    data_pd_alg3 = pd.DataFrame(data_alg3, columns = ['Erlangs','Medio','Minimo','Maximo'])
    data_pd_alg4 = pd.DataFrame(data_alg4, columns = ['Erlangs','Medio','Minimo','Maximo'])
    ax = fig.add_axes([0,0,1,1])
    ax.plot(X , data_pd_alg1['Medio'], color = 'g', marker='o')
    ax.plot(X , data_pd_alg2['Medio'], color = 'b', marker='D',linestyle='dashed')
    ax.plot(X , data_pd_alg3['Medio'], color = 'r', marker='x',linestyle=':')
    ax.plot(X , data_pd_alg4['Medio'], color = 'black', marker='d',linestyle='-.')
    # Configurar os ticks do eixo x
    locator = FixedLocator(X)
    formatter = FixedFormatter(labels[1:])
    ax.xaxis.set_major_locator(locator)
    ax.xaxis.set_major_formatter(formatter)
    #labels = [str(e) for e in range(ERLANG_MIN, ERLANG_MAX + ERLANG_INC, ERLANG_INC)]
    #labels.insert(0, '0')
    #ax.set_xticklabels(labels)
    ax.set_ylabel("Receita Cessante em U$ por Bloqueio\n na Banda"+cls100_400_cls[i])
    ax.set_xlabel(f'Carga em Erlangs na Topologia {TOPOLOGY.upper()}')
    # ax.set_title("Receita Cessante em U$ por Bloqueio \n na Banda"+cls100_400_cls[i])
    ax.legend(labels=[prog1, prog2, prog3, prog4])
    plt.savefig(local_path+'Custo_Bloqueio_Banda_'+cls100_400_cls[i]+'.png', bbox_inches='tight')
    print('Receita Cessante em U$ por Bloqueio na Banda' + cls100_400_cls[i])
    plt.close(fig)



fig = plt.figure()
fig.add_subplot(121)
data_alg1 = np.loadtxt(local_path_1+"Custo_bloqueio.dat")
data_alg2 = np.loadtxt(local_path_2+"Custo_bloqueio.dat")
data_alg3 = np.loadtxt(local_path_3+"Custo_bloqueio.dat")
data_alg4 = np.loadtxt(local_path_4+"Custo_bloqueio.dat")
data_pd_alg1 = pd.DataFrame(data_alg1, columns = ['Erlangs','Medio','Minimo','Maximo'])
data_pd_alg2 = pd.DataFrame(data_alg2, columns = ['Erlangs','Medio','Minimo','Maximo'])
data_pd_alg3 = pd.DataFrame(data_alg3, columns = ['Erlangs','Medio','Minimo','Maximo'])
data_pd_alg4 = pd.DataFrame(data_alg4, columns = ['Erlangs','Medio','Minimo','Maximo'])
ax = fig.add_axes([0,0,1,1])
ax.plot(X , data_pd_alg1['Medio'], color = 'g', marker='o')
ax.plot(X , data_pd_alg2['Medio'], color = 'b', marker='D',linestyle='dashed')
ax.plot(X , data_pd_alg3['Medio'], color = 'r', marker='x',linestyle=':')
ax.plot(X , data_pd_alg4['Medio'], color = 'black', marker='d',linestyle='-.')
# Configurar os ticks do eixo x
locator = FixedLocator(X)
formatter = FixedFormatter(labels[1:])
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.set_ylabel('Receita Cessante U$ - Bloqueio Total')
ax.set_xlabel(f'Carga em Erlangs na Topologia {TOPOLOGY.upper()}')
# ax.set_title('Receita Cessante em U$ por Bloqueio Total')
ax.legend(labels=[prog1, prog2, prog3, prog4])
plt.savefig(local_path+'Custo_bloqueio_banda.png', bbox_inches='tight')
plt.close(fig)
print('Receita Cessante em U$ por Bloqueio Total')


fig = plt.figure()
fig.add_subplot(121)
data_alg1 = np.loadtxt(local_path_1+"bloqueio_banda_classe1.dat")
data_alg2 = np.loadtxt(local_path_2+"bloqueio_banda_classe1.dat")
data_alg3 = np.loadtxt(local_path_3+"bloqueio_banda_classe1.dat")
data_alg4 = np.loadtxt(local_path_4+"bloqueio_banda_classe1.dat")
data_pd_alg1 = pd.DataFrame(data_alg1, columns = ['Erlangs','Medio','Minimo','Maximo'])
data_pd_alg2 = pd.DataFrame(data_alg2, columns = ['Erlangs','Medio','Minimo','Maximo'])
data_pd_alg3 = pd.DataFrame(data_alg3, columns = ['Erlangs','Medio','Minimo','Maximo'])
data_pd_alg4 = pd.DataFrame(data_alg4, columns = ['Erlangs','Medio','Minimo','Maximo'])
ax = fig.add_axes([0,0,1,1])
ax.plot(X , data_pd_alg1['Medio'], color = 'g', marker='o')
ax.plot(X , data_pd_alg2['Medio'], color = 'b', marker='D',linestyle='dashed')
ax.plot(X , data_pd_alg3['Medio'], color = 'r', marker='x',linestyle=':')
ax.plot(X , data_pd_alg4['Medio'], color = 'black', marker='d',linestyle='-.')
# Configurar os ticks do eixo x
locator = FixedLocator(X)
formatter = FixedFormatter(labels[1:])
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.set_ylabel('Receita Cessante em U$ \n por Bloqueio na Classe 1')
ax.set_xlabel(f'Carga em Erlangs na Topologia {TOPOLOGY.upper()}')
# ax.set_title('Receita Cessante em U$ por Bloqueio na Classe 1')
ax.legend(labels=[prog1, prog2, prog3, prog4])
plt.savefig(local_path+'valor_bloqueio_classe1.png', bbox_inches='tight')
# troquei U$ custo bloqueio por Receita Cessante em U$ por Bloqueio na Classe 1
plt.close(fig)
print('Receita Cessante em U$ por Bloqueio na Classe 1')
 
fig = plt.figure()
fig.add_subplot(121)
data_alg1 = np.loadtxt(local_path_1+"bloqueio_banda_classe2.dat")
data_alg2 = np.loadtxt(local_path_2+"bloqueio_banda_classe2.dat")
data_alg3 = np.loadtxt(local_path_3+"bloqueio_banda_classe2.dat")
data_alg4 = np.loadtxt(local_path_4+"bloqueio_banda_classe2.dat")
data_pd_alg1 = pd.DataFrame(data_alg1, columns = ['Erlangs','Medio','Minimo','Maximo'])
data_pd_alg2 = pd.DataFrame(data_alg2, columns = ['Erlangs','Medio','Minimo','Maximo'])
data_pd_alg3 = pd.DataFrame(data_alg3, columns = ['Erlangs','Medio','Minimo','Maximo'])
data_pd_alg4 = pd.DataFrame(data_alg4, columns = ['Erlangs','Medio','Minimo','Maximo'])
ax = fig.add_axes([0,0,1,1])
ax.plot(X , data_pd_alg1['Medio'], color = 'g', marker='o')
ax.plot(X , data_pd_alg2['Medio'], color = 'b', marker='D',linestyle='dashed')
ax.plot(X , data_pd_alg3['Medio'], color = 'r', marker='x',linestyle=':')
ax.plot(X , data_pd_alg4['Medio'], color = 'black', marker='d',linestyle='-.')
# Configurar os ticks do eixo x
locator = FixedLocator(X)
formatter = FixedFormatter(labels[1:])
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.set_ylabel('Receita Cessante em U$ \n por Bloqueio na Classe 2')
ax.set_xlabel(f'Carga em Erlangs na Topologia {TOPOLOGY.upper()}')
# ax.set_title('Receita Cessante em U$ por Bloqueio na Classe 2')
ax.legend(labels=[prog1, prog2, prog3, prog4])
plt.savefig(local_path+'valor_bloqueio_classe2.png', bbox_inches='tight')
plt.close(fig)
print('Receita Cessante em U$ por Bloqueio na Classe 2')

fig = plt.figure()
fig.add_subplot(121)
data_alg1 = np.loadtxt(local_path_1+"bloqueio_banda_classe3.dat")
data_alg2 = np.loadtxt(local_path_2+"bloqueio_banda_classe3.dat")
data_alg3 = np.loadtxt(local_path_3+"bloqueio_banda_classe3.dat")
data_alg4 = np.loadtxt(local_path_4+"bloqueio_banda_classe3.dat")
data_pd_alg1 = pd.DataFrame(data_alg1, columns = ['Erlangs','Medio','Minimo','Maximo'])
data_pd_alg2 = pd.DataFrame(data_alg2, columns = ['Erlangs','Medio','Minimo','Maximo'])
data_pd_alg3 = pd.DataFrame(data_alg3, columns = ['Erlangs','Medio','Minimo','Maximo'])
data_pd_alg4 = pd.DataFrame(data_alg4, columns = ['Erlangs','Medio','Minimo','Maximo'])
ax = fig.add_axes([0,0,1,1])
ax.plot(X , data_pd_alg1['Medio'], color = 'g', marker='o')
ax.plot(X , data_pd_alg2['Medio'], color = 'b', marker='D',linestyle='dashed')
ax.plot(X , data_pd_alg3['Medio'], color = 'r', marker='x',linestyle=':')
ax.plot(X , data_pd_alg4['Medio'], color = 'black', marker='d',linestyle='-.')
# Configurar os ticks do eixo x
locator = FixedLocator(X)
formatter = FixedFormatter(labels[1:])
ax.xaxis.set_major_locator(locator)
ax.xaxis.set_major_formatter(formatter)
ax.set_ylabel('Receita Cessante em U$ \n por Bloqueio na Classe 3')
ax.set_xlabel(f'Carga em Erlangs na Topologia {TOPOLOGY.upper()}')
# ax.set_title('Receita Cessante em U$ por Bloqueio na Classe 3')
ax.legend(labels=[prog1, prog2, prog3, prog4])
plt.savefig(local_path+'valor_bloqueio_classe3.png', bbox_inches='tight')
plt.close(fig)
print('Receita Cessante em U$ por Bloqueio na Classe 3')


# Cores para cada banda
cores = {
    10.0: 'b',
    20.0: 'g',
    40.0: 'r',
    80.0: 'c',
    160.0: 'm',
    200.0: 'y',
    400.0: 'k'
}

# Largura e deslocamento das barras
largura = 2.5



data_alg3 = np.loadtxt(local_path_3+"bloqueio_bandaXclasse1.dat")
data_pd_alg3 = pd.DataFrame(data_alg3, columns = ['Erlangs','banda','Medio','Minimo','Maximo'])
pivot_data = data_pd_alg3.pivot(index='Erlangs', columns='banda', values='Medio')

erlangs = pivot_data.index

# Crie o gráfico de barras
fig, ax = plt.subplots(figsize=(12, 6))
for banda in pivot_data.columns:
    ax.bar(erlangs, pivot_data[banda], width=largura, label=f'Banda {banda}', color=cores[banda])
    erlangs = [x + largura for x in erlangs]
ax.set_xlabel(f'Valores de perdas por Erlangs e Banda Classe 1 \n Algoritmo CRIA na Topologia {TOPOLOGY.upper()}')
ax.set_ylabel("Receita Cessante em U$")
# ax.set_title(f"Valores de perdas por Erlangs e Banda Classe 1 \n Topologia {TOPOLOGY.upper()} Algoritmo {prog3}")
ax.legend()

plt.savefig(local_path+'bloqueio_bandaXclasse1.png', bbox_inches='tight')
plt.close(fig)
print('Grafico bloqueio_bandaXclasse1')


data_alg3 = np.loadtxt(local_path_3+"bloqueio_bandaXclasse2.dat")
data_pd_alg3 = pd.DataFrame(data_alg3, columns = ['Erlangs','banda','Medio','Minimo','Maximo'])
pivot_data = data_pd_alg3.pivot(index='Erlangs', columns='banda', values='Medio')

erlangs = pivot_data.index

# Crie o gráfico de barras
fig, ax = plt.subplots(figsize=(12, 6))
for banda in pivot_data.columns:
    ax.bar(erlangs, pivot_data[banda], width=largura, label=f'Banda {banda}', color=cores[banda])
    erlangs = [x + largura for x in erlangs]
ax.set_xlabel(f'Valores de perdas por Erlangs e Banda Classe 2 \n Algoritmo CRIA na Topologia {TOPOLOGY.upper()}')
ax.set_ylabel("Receita Cessante em U$")
# ax.set_title(f"Valores de perdas por Erlangs e Banda Classe 2 \n Topologia {TOPOLOGY.upper()} Algoritmo {prog3}")
ax.legend()

plt.savefig(local_path+'bloqueio_bandaXclasse2.png', bbox_inches='tight')
plt.close(fig)
print('Grafico bloqueio_bandaXclasse2')


data_alg3 = np.loadtxt(local_path_3+"bloqueio_bandaXclasse3.dat")
data_pd_alg3 = pd.DataFrame(data_alg3, columns = ['Erlangs','banda','Medio','Minimo','Maximo'])
pivot_data = data_pd_alg3.pivot(index='Erlangs', columns='banda', values='Medio')

erlangs = pivot_data.index

# Crie o gráfico de barras
fig, ax = plt.subplots(figsize=(12, 6))
for banda in pivot_data.columns:
    ax.bar(erlangs, pivot_data[banda], width=largura, label=f'Banda {banda}', color=cores[banda])
    erlangs = [x + largura for x in erlangs]
ax.set_xlabel(f'Valores de perdas por Erlangs e Banda Classe 3 \n Algoritmo CRIA na Topologia {TOPOLOGY.upper()}')
ax.set_ylabel("Receita Cessante em U$")
# ax.set_title(f"Valores de perdas por Erlangs e Banda Classe 3 \n Topologia {TOPOLOGY.upper()} Algoritmo {prog3}")
ax.legend()

plt.savefig(local_path+'bloqueio_bandaXclasse3.png', bbox_inches='tight')
plt.close(fig)
print('Grafico bloqueio_bandaXclasse3')





COS = ['COS1', 'COS2', 'COS3']
BANDS = list(map(str, BANDWIDTH))
ELG = [el for el in range(ERLANG_MIN, ERLANG_MAX + 1, ERLANG_INC)]

for EL in ELG:

	# Dicionário para armazenar os valores
	valores = {}

	for band in BANDS:
		data_alg1 = np.loadtxt(local_path_1 + f"1Nbloqueio_{band}.dat")
		data_alg2 = np.loadtxt(local_path_1 + f"2Nbloqueio_{band}.dat")
		data_alg3 = np.loadtxt(local_path_1 + f"3Nbloqueio_{band}.dat")
        

		data_pd_alg1 = pd.DataFrame(data_alg1, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
		data_pd_alg2 = pd.DataFrame(data_alg2, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
		data_pd_alg3 = pd.DataFrame(data_alg3, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])

		valor1 = data_pd_alg1[data_pd_alg1['Erlangs'] == EL]['Medio'].values[0]
		valor2 = data_pd_alg2[data_pd_alg2['Erlangs'] == EL]['Medio'].values[0]
		valor3 = data_pd_alg3[data_pd_alg3['Erlangs'] == EL]['Medio'].values[0]

		valores[band] = np.array([valor1, valor2, valor3]) 



	valores = {cos: [valores[band][i] for band in BANDS] for i, cos in enumerate(COS)}
	valores = {cos: np.array(values) for cos, values in valores.items()}



	# Dicionário para armazenar os valores
	valores2 = {}

	for band in BANDS:
		data_alg1 = np.loadtxt(local_path_2 + f"1Nbloqueio_{band}.dat")
		data_alg2 = np.loadtxt(local_path_2 + f"2Nbloqueio_{band}.dat")
		data_alg3 = np.loadtxt(local_path_2 + f"3Nbloqueio_{band}.dat")

		data_pd_alg1 = pd.DataFrame(data_alg1, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
		data_pd_alg2 = pd.DataFrame(data_alg2, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
		data_pd_alg3 = pd.DataFrame(data_alg3, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])

		valor1 = data_pd_alg1[data_pd_alg1['Erlangs'] == EL]['Medio'].values[0]
		valor2 = data_pd_alg2[data_pd_alg2['Erlangs'] == EL]['Medio'].values[0]
		valor3 = data_pd_alg3[data_pd_alg3['Erlangs'] == EL]['Medio'].values[0]

		valores2[band] = np.array([valor1, valor2, valor3])
		
	valores2 = {cos: [valores2[band][i] for band in BANDS] for i, cos in enumerate(COS)}
	valores2 = {cos: np.array(values) for cos, values in valores2.items()}



		# Dicionário para armazenar os valores
	valores3 = {}

	for band in BANDS:
		data_alg1 = np.loadtxt(local_path_3 + f"1Nbloqueio_{band}.dat")
		data_alg2 = np.loadtxt(local_path_3 + f"2Nbloqueio_{band}.dat")
		data_alg3 = np.loadtxt(local_path_3 + f"3Nbloqueio_{band}.dat")

		data_pd_alg1 = pd.DataFrame(data_alg1, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
		data_pd_alg2 = pd.DataFrame(data_alg2, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
		data_pd_alg3 = pd.DataFrame(data_alg3, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])

		valor1 = data_pd_alg1[data_pd_alg1['Erlangs'] == EL]['Medio'].values[0]
		valor2 = data_pd_alg2[data_pd_alg2['Erlangs'] == EL]['Medio'].values[0]
		valor3 = data_pd_alg3[data_pd_alg3['Erlangs'] == EL]['Medio'].values[0]

		valores3[band] = np.array([valor1, valor2, valor3])

	valores3 = {cos: [valores3[band][i] for band in BANDS] for i, cos in enumerate(COS)}
	valores3 = {cos: np.array(values) for cos, values in valores3.items()}


		# Dicionário para armazenar os valores
	valores4 = {}

	for band in BANDS:
		data_alg1 = np.loadtxt(local_path_4 + f"1Nbloqueio_{band}.dat")
		data_alg2 = np.loadtxt(local_path_4 + f"2Nbloqueio_{band}.dat")
		data_alg3 = np.loadtxt(local_path_4 + f"3Nbloqueio_{band}.dat")

		data_pd_alg1 = pd.DataFrame(data_alg1, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
		data_pd_alg2 = pd.DataFrame(data_alg2, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
		data_pd_alg3 = pd.DataFrame(data_alg3, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])

		valor1 = data_pd_alg1[data_pd_alg1['Erlangs'] == EL]['Medio'].values[0]
		valor2 = data_pd_alg2[data_pd_alg2['Erlangs'] == EL]['Medio'].values[0]
		valor3 = data_pd_alg3[data_pd_alg3['Erlangs'] == EL]['Medio'].values[0]

		valores4[band] = np.array([valor1, valor2, valor3])

	valores4 = {cos: [valores4[band][i] for band in BANDS] for i, cos in enumerate(COS)}
	valores4 = {cos: np.array(values) for cos, values in valores4.items()}

	# Largura das barras
	bar_width = 0.2

	# Criando a posição das barras
	x = np.arange(len(BANDS))

	# Aumentando o gráfico
	plt.figure(figsize=(10, 5))

	# Deslocamento para a esquerda e direita
	offset = 0.2

	# Plotando as barras para cada conjunto com deslocamento


	plt.bar(x - offset, valores[COS[0]], bar_width, label=COS[0], color=(0, 1, 0))
	plt.bar(x - offset, valores[COS[1]], bar_width, label=COS[1], color=(0.3, 1, 0.3), bottom = valores[COS[0]])
	plt.bar(x - offset, valores[COS[2]], bar_width, label=COS[2], color=(0.6, 1, 0.6), bottom = valores[COS[0]]+valores[COS[1]])

	plt.bar(x, valores2[COS[0]], bar_width, label=COS[0], color=(0, 0, 1))
	plt.bar(x, valores2[COS[1]], bar_width, label=COS[1], color=(0.3, 0.3, 1), bottom = valores2[COS[0]])
	plt.bar(x, valores2[COS[2]], bar_width, label=COS[2], color=(0.6, 0.6, 1), bottom = valores2[COS[0]]+valores2[COS[1]])

	plt.bar(x + offset, valores3[COS[0]], bar_width, label=COS[0], color=(1, 0, 0))
	plt.bar(x + offset, valores3[COS[1]], bar_width, label=COS[1], color=(1, 0.3, 0.3), bottom = valores3[COS[0]])
	plt.bar(x + offset, valores3[COS[2]], bar_width, label=COS[2], color=(1, 0.6, 0.6), bottom = valores3[COS[0]]+valores3[COS[1]])
     
	plt.bar(x + offset + offset, valores4[COS[0]], bar_width, label=COS[0], color=(0, 0, 0))
	plt.bar(x + offset + offset, valores4[COS[1]], bar_width, label=COS[1], color=(0.3, 0.3, 0.3), bottom = valores4[COS[0]])
	plt.bar(x + offset + offset, valores4[COS[2]], bar_width, label=COS[2], color=(0.6, 0.6, 0.6), bottom = valores4[COS[0]]+valores4[COS[1]])


	
	# plt. bar (BANDS, valores[COS[2]], color = (1, 0.6, 0.6), bottom = valores[COS[0]] + valores[COS[1]])
	# Adiciando legendas as barras
	plt.xlabel (f'Gráfico de Bandas X Algoritmos \n Carga em Erlangs {EL} Topologia {TOPOLOGY.upper()}')
	plt.ylabel ('Quantidade de Bloqueios')
	# plt.title(f'Gráfico de Bandas X Algoritmos \nErlangs {EL} Topologia {TOPOLOGY.upper()}')
	plt.xticks(x, BANDS)
	plt.legend(labels=[prog1+" "+COS[0], prog1+" "+COS[1], prog1+" "+COS[2], prog2+" "+COS[0], prog2+" "+COS[1], prog2+" "+COS[2], prog3+" "+COS[0], prog3+" "+COS[1], prog3+" "+COS[2], prog4+" "+COS[0], prog4+" "+COS[1], prog4+" "+COS[2]], fontsize='small', loc='center left', bbox_to_anchor=(1, 0.5))
	# plt. show()

	plt.savefig(local_path+'QTD_Bloqueio_Erlangs_'+str(EL)+'.png', bbox_inches='tight')
	plt.close(fig)
	print('POR_Bloqueio_Erlangs' , str(EL))


# Carrega os dados dos arquivos de bloqueio para os três algoritmos
fdata_alg1 = np.loadtxt(local_path_1+"tipo_bloqueio_frag.dat")
fdata_alg2 = np.loadtxt(local_path_2+"tipo_bloqueio_frag.dat")
fdata_alg3 = np.loadtxt(local_path_3+"tipo_bloqueio_frag.dat")
fdata_alg4 = np.loadtxt(local_path_4+"tipo_bloqueio_frag.dat")

edata_alg1 = np.loadtxt(local_path_1+"tipo_bloqueio_eal.dat")
edata_alg2 = np.loadtxt(local_path_2+"tipo_bloqueio_eal.dat")
edata_alg3 = np.loadtxt(local_path_3+"tipo_bloqueio_eal.dat")
edata_alg4 = np.loadtxt(local_path_4+"tipo_bloqueio_eal.dat")

# Converte os dados em DataFrames do pandas para facilitar o manuseio
fdata_pd_alg1 = pd.DataFrame(fdata_alg1, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
fdata_pd_alg2 = pd.DataFrame(fdata_alg2, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
fdata_pd_alg3 = pd.DataFrame(fdata_alg3, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
fdata_pd_alg4 = pd.DataFrame(fdata_alg4, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])

edata_pd_alg1 = pd.DataFrame(edata_alg1, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
edata_pd_alg2 = pd.DataFrame(edata_alg2, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
edata_pd_alg3 = pd.DataFrame(edata_alg3, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
edata_pd_alg4 = pd.DataFrame(edata_alg4, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])

# Largura das barras
bar_width = 0.2

# Criando a posição das barras
x = np.arange(len(list(range(ERLANG_MIN, ERLANG_MAX + 1, ERLANG_INC))))

# Aumentando o gráfico
plt.figure(figsize=(10, 5))

# Deslocamento para a esquerda e direita
offset = 0.2

labels = [str(e) for e in range(ERLANG_MIN, ERLANG_MAX + ERLANG_INC, ERLANG_INC)]
plt.xticks(x, labels)



plt.bar(x - offset, edata_pd_alg1['Medio'], bar_width, label=prog1+" EAL", color=(0, 1, 0))
plt.bar(x - offset, fdata_pd_alg1['Medio'], bar_width, label=prog1+" FRAG", color=(0.5, 1, 0.5), bottom = edata_pd_alg1['Medio'])

plt.bar(x , edata_pd_alg2['Medio'], bar_width, label=prog2+" EAL", color=(0, 0, 1))
plt.bar(x , fdata_pd_alg2['Medio'], bar_width, label=prog2+" FRAG", color=(0.5, 0.5, 1), bottom = edata_pd_alg2['Medio'])

plt.bar(x + offset, edata_pd_alg3['Medio'], bar_width, label=prog3+" EAL", color=(1, 0, 0))
plt.bar(x + offset, fdata_pd_alg3['Medio'], bar_width, label=prog3+" FRAG", color=(1, 0.5, 0.5), bottom = edata_pd_alg3['Medio'])

plt.bar(x + offset + offset, edata_pd_alg4['Medio'], bar_width, label=prog4+" EAL", color=(0.5, 0.5, 0.5))
plt.bar(x + offset + offset, fdata_pd_alg4['Medio'], bar_width, label=prog4+" FRAG", color=(0.8, 0.8, 0.8), bottom = edata_pd_alg4['Medio'])
 
 

plt.ylabel('Tipo de Bloqueio de circuitos')
plt.xlabel(f'Carga em Erlangs na Topologia {TOPOLOGY.upper()}')
# plt.title(f'Tipo de Bloqueio de circuitos na Topologia {TOPOLOGY.upper()}')
plt.legend(fontsize='small', loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig(local_path+'tipo_bloqueio.png', bbox_inches='tight')

print('tipo de bloqueio')


# Carrega os dados dos arquivos de bloqueio para os três algoritmos
fdata_alg1 = np.loadtxt(local_path_1+"tipo_bloqueio_frag_p.dat")
fdata_alg2 = np.loadtxt(local_path_2+"tipo_bloqueio_frag_p.dat")
fdata_alg3 = np.loadtxt(local_path_3+"tipo_bloqueio_frag_p.dat")
fdata_alg4 = np.loadtxt(local_path_4+"tipo_bloqueio_frag_p.dat")

edata_alg1 = np.loadtxt(local_path_1+"tipo_bloqueio_eal_p.dat")
edata_alg2 = np.loadtxt(local_path_2+"tipo_bloqueio_eal_p.dat")
edata_alg3 = np.loadtxt(local_path_3+"tipo_bloqueio_eal_p.dat")
edata_alg4 = np.loadtxt(local_path_4+"tipo_bloqueio_eal_p.dat")

# Converte os dados em DataFrames do pandas para facilitar o manuseio
fdata_pd_alg1 = pd.DataFrame(fdata_alg1, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
fdata_pd_alg2 = pd.DataFrame(fdata_alg2, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
fdata_pd_alg3 = pd.DataFrame(fdata_alg3, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
fdata_pd_alg4 = pd.DataFrame(fdata_alg4, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])

edata_pd_alg1 = pd.DataFrame(edata_alg1, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
edata_pd_alg2 = pd.DataFrame(edata_alg2, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
edata_pd_alg3 = pd.DataFrame(edata_alg3, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])
edata_pd_alg4 = pd.DataFrame(edata_alg4, columns=['Erlangs', 'Medio', 'Minimo', 'Maximo'])



def ajustar_medios(df1, df2):
    soma = df1['Medio'] + df2['Medio']
    mask = soma < 1
    df1.loc[mask, 'Medio'] = 1 - df2.loc[mask, 'Medio']
    return df1

fdata_pd_alg1 = ajustar_medios(fdata_pd_alg1, edata_pd_alg1)
fdata_pd_alg2 = ajustar_medios(fdata_pd_alg2, edata_pd_alg2)
fdata_pd_alg3 = ajustar_medios(fdata_pd_alg3, edata_pd_alg3)
fdata_pd_alg4 = ajustar_medios(fdata_pd_alg4, edata_pd_alg4)

# Largura das barras
bar_width = 0.2

# Criando a posição das barras
x = np.arange(len(list(range(ERLANG_MIN, ERLANG_MAX + 1, ERLANG_INC))))

# Aumentando o gráfico
plt.figure(figsize=(10, 5))

# Deslocamento para a esquerda e direita
offset = 0.2

labels = [str(e) for e in range(ERLANG_MIN, ERLANG_MAX + ERLANG_INC, ERLANG_INC)]
plt.xticks(x, labels)



plt.bar(x - offset, edata_pd_alg1['Medio'], bar_width, label=prog1+" EAL", color=(0, 1, 0))
plt.bar(x - offset, fdata_pd_alg1['Medio'], bar_width, label=prog1+" FRAG", color=(0.5, 1, 0.5), bottom = edata_pd_alg1['Medio'])

plt.bar(x , edata_pd_alg2['Medio'], bar_width, label=prog2+" EAL", color=(0, 0, 1))
plt.bar(x , fdata_pd_alg2['Medio'], bar_width, label=prog2+" FRAG", color=(0.5, 0.5, 1), bottom = edata_pd_alg2['Medio'])

plt.bar(x + offset, edata_pd_alg3['Medio'], bar_width, label=prog3+" EAL", color=(1, 0, 0))
plt.bar(x + offset, fdata_pd_alg3['Medio'], bar_width, label=prog3+" FRAG", color=(1, 0.5, 0.5), bottom = edata_pd_alg3['Medio'])

plt.bar(x + offset + offset, edata_pd_alg4['Medio'], bar_width, label=prog4+" EAL", color=(0.5, 0.5, 0.5))
plt.bar(x + offset + offset, fdata_pd_alg4['Medio'], bar_width, label=prog4+" FRAG", color=(0.8, 0.8, 0.8), bottom = edata_pd_alg4['Medio'])
 
 

plt.ylabel('Tipo de Bloqueio de circuitos em %')
plt.xlabel(f'Carga em Erlangs na Topologia {TOPOLOGY.upper()}')
# plt.title(f'Tipo de Bloqueio de circuitos na Topologia {TOPOLOGY.upper()}')
plt.legend(fontsize='small', loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig(local_path+'Per_tipo_bloqueio.png', bbox_inches='tight')

print('tipo de bloqueio %')

#######################################################################################################################


# Ler o conteúdo de cada arquivo e armazenar em listas
with open(local_path_1+"bloqueio.dat", 'r') as f:
    block_data_1 = [line.strip().split() for line in f.readlines()]

with open(local_path_1+"tipo_bloqueio_frag.dat", 'r') as f:
    frag_data_1 = [line.strip().split() for line in f.readlines()]

with open(local_path_1+"tipo_bloqueio_eal.dat", 'r') as f:
    eal_data_1 = [line.strip().split() for line in f.readlines()]

# Calcular os valores para cada linha
result_data_1 = []
for i in range(len(block_data_1)):
    if (float(frag_data_1[i][1]) + float(eal_data_1[i][1])) > 0:
        value1 = (float(block_data_1[i][1]) * float(frag_data_1[i][1])) / (float(frag_data_1[i][1]) + float(eal_data_1[i][1]))
        value3 = (float(block_data_1[i][1]) * float(eal_data_1[i][1])) / (float(frag_data_1[i][1]) + float(eal_data_1[i][1]))
        value4 = float(block_data_1[i][1])
        result_data_1.append([block_data_1[i][0], value1, value3, value4])
    else:
        value1 = 0.0
        value3 = 0.0
        value4 = float(block_data_1[i][1])
        result_data_1.append([block_data_1[i][0], value1, value3, value4]) 
 
# Ler o conteúdo de cada arquivo e armazenar em listas
with open(local_path_2+"bloqueio.dat", 'r') as f:
    block_data_2 = [line.strip().split() for line in f.readlines()]

with open(local_path_2+"tipo_bloqueio_frag.dat", 'r') as f:
    frag_data_2 = [line.strip().split() for line in f.readlines()]

with open(local_path_2+"tipo_bloqueio_eal.dat", 'r') as f:
    eal_data_2 = [line.strip().split() for line in f.readlines()]

# Calcular os valores para cada linha
result_data_2 = []
for i in range(len(block_data_2)):
    if (float(frag_data_2[i][1]) + float(eal_data_2[i][1])) > 0:
        value1 = (float(block_data_2[i][1]) * float(frag_data_2[i][1])) / (float(frag_data_2[i][1]) + float(eal_data_2[i][1]))
        value3 = (float(block_data_2[i][1]) * float(eal_data_2[i][1])) / (float(frag_data_2[i][1]) + float(eal_data_2[i][1]))
        value4 = float(block_data_2[i][1])
        result_data_2.append([block_data_2[i][0], value1, value3, value4])
    else:
        value1 = 0.0
        value3 = 0.0
        value4 = float(block_data_2[i][1])
        result_data_2.append([block_data_2[i][0], value1, value3, value4])  
    

# Ler o conteúdo de cada arquivo e armazenar em listas
with open(local_path_3+"bloqueio.dat", 'r') as f:
    block_data_3 = [line.strip().split() for line in f.readlines()]

with open(local_path_3+"tipo_bloqueio_frag.dat", 'r') as f:
    frag_data_3 = [line.strip().split() for line in f.readlines()]

with open(local_path_3+"tipo_bloqueio_eal.dat", 'r') as f:
    eal_data_3 = [line.strip().split() for line in f.readlines()]

# Calcular os valores para cada linha
result_data_3 = []
for i in range(len(block_data_3)):
    if (float(frag_data_3[i][1]) + float(eal_data_3[i][1])) > 0:
        value1 = (float(block_data_3[i][1]) * float(frag_data_3[i][1])) / (float(frag_data_3[i][1]) + float(eal_data_3[i][1]))
        value3 = (float(block_data_3[i][1]) * float(eal_data_3[i][1])) / (float(frag_data_3[i][1]) + float(eal_data_3[i][1]))
        value4 = float(block_data_3[i][1])
        result_data_3.append([block_data_3[i][0], value1, value3, value4])
    else:
        value1 = 0.0
        value3 = 0.0
        value4 = float(block_data_3[i][1])
        result_data_3.append([block_data_3[i][0], value1, value3, value4]) 
    
	# Ler o conteúdo de cada arquivo e armazenar em listas
with open(local_path_4+"bloqueio.dat", 'r') as f:
    block_data_4 = [line.strip().split() for line in f.readlines()]

with open(local_path_4+"tipo_bloqueio_frag.dat", 'r') as f:
    frag_data_4 = [line.strip().split() for line in f.readlines()]

with open(local_path_4+"tipo_bloqueio_eal.dat", 'r') as f:
    eal_data_4 = [line.strip().split() for line in f.readlines()]

# Calcular os valores para cada linha
result_data_4 = []
for i in range(len(block_data_4)):
    value1 = (float(block_data_4[i][1]) * float(frag_data_4[i][1])) / (float(frag_data_4[i][1]) + float(eal_data_4[i][1]))
    value3 = (float(block_data_4[i][1]) * float(eal_data_4[i][1])) / (float(frag_data_4[i][1]) + float(eal_data_4[i][1]))
    value4 = float(block_data_4[i][1])
    result_data_4.append([block_data_4[i][0], value1, value3, value4])
    

# Largura das barras
bar_width = 0.2

# Criando a posição das barras
x = np.arange(len(list(range(ERLANG_MIN, ERLANG_MAX + 1, ERLANG_INC))))

# Aumentando o gráfico
plt.figure(figsize=(10, 5))

# Deslocamento para a esquerda e direita
offset = 0.2

labels = [str(e) for e in range(ERLANG_MIN, ERLANG_MAX + ERLANG_INC, ERLANG_INC)]
plt.xticks(x, labels)



plt.bar(x - offset, [row[1] for row in result_data_1] , bar_width, label=prog1+" EAL", color=(0.5, 1, 0.5))
plt.bar(x - offset, [row[2] for row in result_data_1] , bar_width, label=prog1+" FRAG", color=(0, 1, 0), bottom = [row[1] for row in result_data_1] )

plt.bar(x , [row[1] for row in result_data_2], bar_width, label=prog2+" EAL", color=(0.5, 0.5, 1))
plt.bar(x , [row[2] for row in result_data_2], bar_width, label=prog2+" FRAG", color=(0, 0, 1), bottom = [row[1] for row in result_data_2])

plt.bar(x + offset, [row[1] for row in result_data_3], bar_width, label=prog3+" EAL", color=(1, 0.5, 0.5))
plt.bar(x + offset, [row[2] for row in result_data_3], bar_width, label=prog3+" FRAG", color=(1, 0, 0), bottom = [row[1] for row in result_data_3])

plt.bar(x + offset + offset, [row[1] for row in result_data_4], bar_width, label=prog4+" EAL", color=(0.8, 0.8, 0.8))
plt.bar(x + offset + offset, [row[2] for row in result_data_4], bar_width, label=prog4+" FRAG", color=(0.5, 0.5, 0.5), bottom = [row[1] for row in result_data_4])
 
 

plt.ylabel('Tipo de Bloqueio de circuitos %')
plt.xlabel(f'Carga em Erlangs na Topologia {TOPOLOGY.upper()}')
# plt.title(f'% Tipo de Bloqueio de circuitos na Topologia {TOPOLOGY.upper()}')
plt.legend(fontsize='small', loc='center left', bbox_to_anchor=(1, 0.5))
plt.savefig(local_path+'new_tipo_bloqueio.png', bbox_inches='tight')

print('tipo de bloqueio 2 %')


# plt.show()