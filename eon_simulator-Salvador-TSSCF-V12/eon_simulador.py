#!/usr/bin/env python
# -*- coding: utf-8 -*-

import simpy
from random import *
import numpy as np
import networkx as nx
import math
from itertools import islice


import sys
sys.path.append('..')  # Adicione o diretório pai ao sys.path
from config import *


topology = nx.read_weighted_edgelist('../topology/'+TOPOLOGY, nodetype=int)


HTMAX = 1

class Desalocate(object):
	def __init__(self, env):
		self.env = env
	def Run(self, count, path, spectro, holding_time):
		global topology
		yield self.env.timeout(holding_time)
		for i in range(0, (len(path)-1)):
			for slot in range(spectro[0],spectro[1]+1):
				topology[path[i]][path[i+1]]['capacity'][slot] = 0

class Simulador(object):
	def __init__(self, env):
		self.env = env
		global topology, HTMAX
		for u, v in list(topology.edges):
			topology[u][v]['capacity'] = [0] * SLOTS
		self.nodes = list(topology.nodes())
		self.random = Random()
		self.NumReqBlocked = 0 
		self.cont_req = 0
		self.NumReq_10 = 0 
		self.NumReq_20 = 0 
		self.NumReq_40 = 0 
		self.NumReq_80 = 0 
		self.NumReq_160 = 0 
		self.NumReq_200 = 0 
		self.NumReq_400 = 0 
		self.NumReq_classe1 = 0 
		self.NumReq_classe2 = 0 
		self.NumReq_classe3 = 0 
		self.NumReqBlocked_10 = 0
		self.NumReqBlocked_20 = 0
		self.NumReqBlocked_40 = 0
		self.NumReqBlocked_80 = 0
		self.NumReqBlocked_160 = 0
		self.NumReqBlocked_200 = 0
		self.NumReqBlocked_400 = 0
		self.NumReqBlocked_classe1 = 0
		self.NumReqBlocked_classe2 = 0
		self.NumReqBlocked_classe3 = 0
		self.k_paths = {}

		#custo
		self.COS1_NumReqBlocked_10 = 0
		self.COS1_NumReqBlocked_20 = 0
		self.COS1_NumReqBlocked_40 = 0
		self.COS1_NumReqBlocked_80 = 0
		self.COS1_NumReqBlocked_160 = 0
		self.COS1_NumReqBlocked_200 = 0
		self.COS1_NumReqBlocked_400 = 0
		
		self.COS2_NumReqBlocked_10 = 0
		self.COS2_NumReqBlocked_20 = 0
		self.COS2_NumReqBlocked_40 = 0
		self.COS2_NumReqBlocked_80 = 0
		self.COS2_NumReqBlocked_160 = 0
		self.COS2_NumReqBlocked_200 = 0
		self.COS2_NumReqBlocked_400 = 0

		self.COS3_NumReqBlocked_10 = 0
		self.COS3_NumReqBlocked_20 = 0
		self.COS3_NumReqBlocked_40 = 0
		self.COS3_NumReqBlocked_80 = 0
		self.COS3_NumReqBlocked_160 = 0
		self.COS3_NumReqBlocked_200 = 0
		self.COS3_NumReqBlocked_400 = 0
		
		self.Frag = 0
		self.Eal = 0

	def Run(self, rate):
		global topology,HTMAX
		for i in list(topology.nodes()):
			for j in list(topology.nodes()):
				if i!= j:
					self.k_paths[i,j] = self.k_shortest_paths(topology, i, j, N_PATH, weight='weight')

		for count in range(1, NUM_OF_REQUESTS + 1):
			yield self.env.timeout(self.random.expovariate(rate))
			class_type = np.random.choice(CLASS_TYPE, p=CLASS_WEIGHT)
			src, dst = self.random.sample(self.nodes, 2)
			bandwidth = self.random.choice(BANDWIDTH)
			holding_time = self.random.expovariate(HOLDING_TIME)
			self.conta_requisicao_banda(bandwidth)
			self.conta_requisicao_classe(class_type)
			paths = self.k_paths[src,dst]
			flag = 0
			#cost=(COSi/COSmax)+(PL/PLmax)+(FS/FSmax)
			costI = [[0, 0] for _ in range(N_PATH)]
			for xi in range(N_PATH):
				n_slots = int(math.ceil(self.Modulation(int(self.Distance(paths[xi])), bandwidth)))
				#se for todas testadas e aqui
				#if holding_time > HTMAX:
				#	HTMAX = holding_time
				costI[xi][1] = (class_type/len(CLASS_TYPE))+(len(paths[xi])/PL_MAX)+(holding_time/HTMAX)
				costI[xi][0] = xi
			#ordena os resultados do menor para o maior valor, se incluir , Reverse=True fica do maior para o menor
			costI = sorted(costI, key=lambda x: x[1])
            # Extrair os valores da primeira coluna em uma lista
			KcostI = [linha[0] for linha in costI]
            # mudei N_PATH para KcostI
			tipo_bloqueio = []
			for i in KcostI:
				distance = int(self.Distance(paths[i]))
				num_slots = int(math.ceil(self.Modulation(distance, bandwidth)))
				self.check_path = self.PathIsAble(num_slots,paths[i])
				if self.check_path[0] == False:
					tipo_bloqueio.append(self.PathBlockIs(num_slots,paths[i]))
				if self.check_path[0] == True:
					#se for so as aocadas e aqui
					if holding_time > HTMAX:
						HTMAX = holding_time
					self.cont_req += 1
					self.FirstFit(count, self.check_path[1],self.check_path[2],paths[i])
					spectro = [self.check_path[1], self.check_path[2]]
					desalocate = Desalocate(self.env)
					self.env.process(desalocate.Run(count,paths[i],spectro,holding_time))
					tipo_bloqueio = []
					flag = 1
					break 
			if flag == 0:
					self.NumReqBlocked +=1
					self.conta_bloqueio_requisicao_banda(bandwidth)
					self.conta_bloqueio_requisicao_classe(class_type)
					self.Custo_conta_bloqueio_requisicao_banda(bandwidth, class_type)
					for elemento in tipo_bloqueio:
						self.conta_tipo_bloqueio(elemento)
					tipo_bloqueio = []

	# Calcula a dist�ncia do caminho de acordo com os pesos das arestas               
	def Distance(self, path):
		global topology 
		soma = 0
		for i in range(0, (len(path)-1)):
			soma += topology[path[i]][path[i+1]]['weight']
		return (soma)

	#Calcula os k-menores caminhos entre pares o-d
	def k_shortest_paths(self,G, source, target, k, weight='weight'):
		return list(islice(nx.shortest_simple_paths(G, source, target, weight=weight), k))

	# Calcula o formato de modula��o de acordo com a dist�ncia do caminho    
	def Modulation(self, dist, demand):
		if dist <= 500:
			return (float(demand) / float(4 * SLOT_SIZE))
		elif 500 < dist <= 1000:
			return (float(demand) / float(3 * SLOT_SIZE))
		elif 1000 < dist <= 2000:
			return (float(demand) / float(2 * SLOT_SIZE)) 
		else:
			return (float(demand) / float(1 * SLOT_SIZE))

	#Realiza a aloca��o de espectro utilizando First-fit
	def FirstFit(self,count,i,j,path):
		global topology
		inicio = i 
		fim =j
		for i in range(0,len(path)-1):
			for slot in range(inicio,fim):
				#print slot
				topology[path[i]][path[i+1]]['capacity'][slot] = count
			topology[path[i]][path[i+1]]['capacity'][fim] = 'GB'

	# Verifica se o caminho escolhido possui espectro dispon�vel para a demanda requisitada
	def PathIsAble(self, nslots,path):
		global topology
		cont = 0
		t = 0
		for slot in range (0,len(topology[path[0]][path[1]]['capacity'])):
			if topology[path[0]][path[1]]['capacity'][slot] == 0:
				k = 0
				for ind in range(0,len(path)-1):
					if topology[path[ind]][path[ind+1]]['capacity'][slot] == 0:
						k += 1
				if k == len(path)-1:
					cont += 1
					if cont == 1:
						i = slot
					if cont > nslots:
						j = slot
						return [True,i,j]
					if slot == len(topology[path[0]][path[1]]['capacity'])-1:
							return [False,0,0]
				else:
					cont = 0
					if slot == len(topology[path[0]][path[1]]['capacity'])-1:
						return [False,0,0]
			else:
				cont = 0
				if slot == len(topology[path[0]][path[1]]['capacity'])-1:
					return [False,0,0]

	def PathBlockIs(self, nslots,path):
		global topology
		available_slots=0
		for ind in range(len(path) - 1):
			if topology[path[ind]][path[ind + 1]]['capacity'].count(0) >= nslots:
				available_slots += 1
		if available_slots == len(path) - 1:
			return "FRAG"
		return "EAL"

	# Computa numero de requesi��es por banda
	def conta_requisicao_banda(self, banda):
		if banda == 10:
			self.NumReq_10 +=1
		elif banda == 20:
			self.NumReq_20 +=1
		elif banda == 40: 
			self.NumReq_40 +=1
		elif banda == 80: 
			self.NumReq_80 +=1
		elif banda == 160:
			self.NumReq_160 += 1 
		elif banda == 200:
			self.NumReq_200 += 1
		else:
			self.NumReq_400 += 1

	# Computa numero de bloqueio por banda
	def conta_bloqueio_requisicao_banda(self, banda):
		if banda == 10:
			self.NumReqBlocked_10 +=1
		elif banda == 20:
			self.NumReqBlocked_20 +=1
		elif banda == 40: 
			self.NumReqBlocked_40 +=1
		elif banda == 80: 
			self.NumReqBlocked_80 +=1
		elif banda == 160:
			self.NumReqBlocked_160 +=1
		elif banda == 200:
			self.NumReqBlocked_200 +=1
		else:
			self.NumReqBlocked_400 +=1

	# Computa o n�mero de requisi��es por classe
	def conta_requisicao_classe(self, classe):
		if classe == 1:
			self.NumReq_classe1 +=1
		elif classe == 2:
			self.NumReq_classe2 +=1
		else:
			self.NumReq_classe3 +=1

	# Computa n�mero de requisi��es bloqueadas por classe
	def conta_bloqueio_requisicao_classe(self, classe):
		if classe == 1:
			self.NumReqBlocked_classe1 +=1
		elif classe == 2:
			self.NumReqBlocked_classe2 +=1
		else: 
			self.NumReqBlocked_classe3 +=1



	# Computa numero de bloqueio por banda e classe
	def Custo_conta_bloqueio_requisicao_banda(self, banda, classe):
		if banda == 10 and classe == 1:
			self.COS1_NumReqBlocked_10 +=1
		elif banda == 20 and classe == 1:
			self.COS1_NumReqBlocked_20 +=1
		elif banda == 40 and classe == 1: 
			self.COS1_NumReqBlocked_40 +=1
		elif banda == 80 and classe == 1: 
			self.COS1_NumReqBlocked_80 +=1
		elif banda == 160 and classe == 1:
			self.COS1_NumReqBlocked_160 +=1
		elif banda == 200 and classe == 1:
			self.COS1_NumReqBlocked_200 +=1
		elif banda == 400 and classe == 1:
			self.COS1_NumReqBlocked_400 +=1

		elif banda == 10 and classe == 2:
			self.COS2_NumReqBlocked_10 +=1
		elif banda == 20 and classe == 2:
			self.COS2_NumReqBlocked_20 +=1
		elif banda == 40 and classe == 2: 
			self.COS2_NumReqBlocked_40 +=1
		elif banda == 80 and classe == 2: 
			self.COS2_NumReqBlocked_80 +=1
		elif banda == 160 and classe == 2:
			self.COS2_NumReqBlocked_160 +=1
		elif banda == 200 and classe == 2:
			self.COS2_NumReqBlocked_200 +=1
		elif banda == 400 and classe == 2:
			self.COS2_NumReqBlocked_400 +=1

		elif banda == 10 and classe == 3:
			self.COS3_NumReqBlocked_10 +=1
		elif banda == 20 and classe == 3:
			self.COS3_NumReqBlocked_20 +=1
		elif banda == 40 and classe == 3: 
			self.COS3_NumReqBlocked_40 +=1
		elif banda == 80 and classe == 3: 
			self.COS3_NumReqBlocked_80 +=1
		elif banda == 160 and classe == 3:
			self.COS3_NumReqBlocked_160 +=1
		elif banda == 200 and classe == 3:
			self.COS3_NumReqBlocked_200 +=1
		elif banda == 400 and classe == 3:
			self.COS3_NumReqBlocked_400 +=1


	# Computa numero de bloqueio por banda e classe
	def conta_tipo_bloqueio(self, tipo):
		if tipo == "FRAG":
			self.Frag +=1
		elif tipo == "EAL":
			self.Eal +=1