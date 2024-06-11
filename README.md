## Descrição da Demonstração para o SBRC
A demonstração planejada para o Simpósio Brasileiro de Redes de Computadores e Sistemas Distribuídos (SBRC) apresenta o uso do simulador EON-Simulator para avaliação de desempenho em redes ópticas elásticas (EON) sob falhas em cascata.

## Equipamentos Necessários
Para realizar a demonstração, os seguintes equipamentos são necessários:

## Computador ou Servidor
Um computador ou servidor capaz de executar o simulador EON-Simulator.
Sistema operacional compatível com Python 3 (por exemplo, Windows, Linux ou macOS).
Conexão à internet para instalação de dependências e acesso a recursos externos, como vídeos tutoriais.
Software Requerido
Além dos equipamentos físicos, o seguinte software deve estar instalado:

## Python 3

Versão 3.x do Python instalada no sistema operacional.
Pode ser obtido em python.org.
Bibliotecas Python

As seguintes bibliotecas Python devem estar instaladas:
simpy
networkx
numpy
decorator
Estas podem ser instaladas via pip, um gerenciador de pacotes para Python.

Para executar o Python 3 e o simulador EON-Simulator com as bibliotecas mencionadas, um computador com pelo menos 4 GB de RAM e um processador de 3 GHz alem de 10Gb de espaco em disco disponivel, seria uma configuração mínima recomendada. 


## Simulador EON-Simulator

O código fonte do simulador EON-Simulator, disponível em GitHub.
Certifique-se de clonar ou baixar o repositório para o sistema local.
Instruções de Execução
Para executar o simulador EON-Simulator e realizar a avaliação de desempenho em redes ópticas elásticas sob falhas em cascata, siga estas instruções:

## Instalação de Dependências

Abra um terminal ou prompt de comando.
Execute o comando pip install networkx simpy numpy decorator para instalar as bibliotecas Python necessárias.

## Execução do Simulador

Navegue até o diretório onde o simulador EON-Simulator está localizado.
Execute o arquivo run.bat no prompt de comando do Windows.
Verificação das Variáveis de Ambiente Python

## Para verificar se as variáveis de ambiente do Python estão configuradas corretamente, execute os comandos:

import sys
print(sys.version)

import networkx
print(networkx.__version__)

import simpy
print(simpy.__version__)


## Resultados da Simulação

Os resultados da simulação serão colocados na pasta 'out' de acordo com a topologia escolhida.
Recursos Adicionais
Para mais informações sobre como executar o simulador EON-Simulator, consulte o tutorial em vídeo disponível em https://youtu.be/oYBNFZAtFR0.


# EON-Simulator
cascading-failure-EON-Simulator

# Elastic Optical Network Simulator

This simulator run arrival requests on an Elastic Optical Network Simulator cascading failure.

## Getting Started

These instructions will guide you to run this simulator.

### Files

'EON_SIM.py': It contains EON simulator, It defines the parameters of the simulator, It starts simulation of EON

### Installing

It requires: python 3, simpy, networkx , numpy, decorator

######

 sys.version
'3.11.1 (tags/v3.11.1:a7a450f, Dec  6 2022, 19:58:39) [MSC v.1934 64 bit (AMD64)]'

 print(networkx.__version__)
2.8.8

print(simpy.__version__)
4.0.2



## Commands Verify requires

import sys

sys.version

import networkx

print(networkx.\_\_version\_\_)

import simpy

print (simpy.\_\_version\_\_)

check the variables ambient python in the system

### Run the simulator

Pre fist run  
pip install networkx simpy numpy decorator


run.bat in commandline CMD windows

### Results

Results of the simulations are put in the folder out according to the choose topology

###  the video tutorial link

https://youtu.be/oYBNFZAtFR0

