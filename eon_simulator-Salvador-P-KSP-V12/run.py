#!/usr/bin/env python
# -*- coding: utf-8 -*-


from eon_simulador import Simulador
import simpy
from random import *
import numpy as np
import subprocess


import sys
sys.path.append('..')  # Adicione o diretório pai ao sys.path
from config import *



def CalculaIntervalo(amostra):
	# calcula média e intervalo de confiança de uma amostra (t de Student) 95%. 
	media = np.mean(amostra)
	desvio = np.std(amostra, ddof=1)
	intervalo = (desvio/len(amostra))*1.833
	return [media,intervalo]

def main(args):
	topologia = TOPOLOGY
	arquivo1  = open('out/'+topologia+'/bloqueio'+'.dat', 'w')
	arquivo2  = open('out/'+topologia+'/bloqueio_10'+'.dat', 'w')
	arquivo3  = open('out/'+topologia+'/bloqueio_20'+'.dat', 'w')
	arquivo4  = open('out/'+topologia+'/bloqueio_40'+'.dat', 'w')
	arquivo5  = open('out/'+topologia+'/bloqueio_80'+'.dat', 'w')
	arquivo6  = open('out/'+topologia+'/bloqueio_160'+'.dat', 'w')
	arquivo7  = open('out/'+topologia+'/bloqueio_200'+'.dat', 'w')
	arquivo8  = open('out/'+topologia+'/bloqueio_400'+'.dat', 'w')
	arquivo9  = open('out/'+topologia+'/bloqueio_classe1'+'.dat', 'w')
	arquivo10  = open('out/'+topologia+'/bloqueio_classe2'+'.dat', 'w')
	arquivo11  = open('out/'+topologia+'/bloqueio_classe3'+'.dat', 'w')
	arquivo12  = open('out/'+topologia+'/bloqueio_banda'+'.dat', 'w')
	
	arquivo13  = open('out/'+topologia+'/Custo_bloqueio'+'.dat', 'w')
	arquivo14  = open('out/'+topologia+'/Custo_bloqueio_10'+'.dat', 'w')
	arquivo15  = open('out/'+topologia+'/Custo_bloqueio_20'+'.dat', 'w')
	arquivo16  = open('out/'+topologia+'/Custo_bloqueio_40'+'.dat', 'w')
	arquivo17  = open('out/'+topologia+'/Custo_bloqueio_80'+'.dat', 'w')
	arquivo18  = open('out/'+topologia+'/Custo_bloqueio_160'+'.dat', 'w')
	arquivo19  = open('out/'+topologia+'/Custo_bloqueio_200'+'.dat', 'w')
	arquivo20  = open('out/'+topologia+'/Custo_bloqueio_400'+'.dat', 'w')

	
	arquivo21  = open('out/'+topologia+'/bloqueio_banda_classe1'+'.dat', 'w')
	arquivo22  = open('out/'+topologia+'/bloqueio_banda_classe2'+'.dat', 'w')
	arquivo23  = open('out/'+topologia+'/bloqueio_banda_classe3'+'.dat', 'w')
	
	arquivo24  = open('out/'+topologia+'/bloqueio_bandaXclasse1'+'.dat', 'w')
	arquivo25  = open('out/'+topologia+'/bloqueio_bandaXclasse2'+'.dat', 'w')
	arquivo26  = open('out/'+topologia+'/bloqueio_bandaXclasse3'+'.dat', 'w')
	
	arquivo311  = open('out/'+topologia+'/1Nbloqueio'+'.dat', 'w')
	arquivo321  = open('out/'+topologia+'/1Nbloqueio_10'+'.dat', 'w')
	arquivo331  = open('out/'+topologia+'/1Nbloqueio_20'+'.dat', 'w')
	arquivo341  = open('out/'+topologia+'/1Nbloqueio_40'+'.dat', 'w')
	arquivo351  = open('out/'+topologia+'/1Nbloqueio_80'+'.dat', 'w')
	arquivo361  = open('out/'+topologia+'/1Nbloqueio_160'+'.dat', 'w')
	arquivo371  = open('out/'+topologia+'/1Nbloqueio_200'+'.dat', 'w')
	arquivo381  = open('out/'+topologia+'/1Nbloqueio_400'+'.dat', 'w')

	arquivo312  = open('out/'+topologia+'/2Nbloqueio'+'.dat', 'w')
	arquivo322  = open('out/'+topologia+'/2Nbloqueio_10'+'.dat', 'w')
	arquivo332  = open('out/'+topologia+'/2Nbloqueio_20'+'.dat', 'w')
	arquivo342  = open('out/'+topologia+'/2Nbloqueio_40'+'.dat', 'w')
	arquivo352  = open('out/'+topologia+'/2Nbloqueio_80'+'.dat', 'w')
	arquivo362  = open('out/'+topologia+'/2Nbloqueio_160'+'.dat', 'w')
	arquivo372  = open('out/'+topologia+'/2Nbloqueio_200'+'.dat', 'w')
	arquivo382  = open('out/'+topologia+'/2Nbloqueio_400'+'.dat', 'w')

	arquivo313  = open('out/'+topologia+'/3Nbloqueio'+'.dat', 'w')
	arquivo323  = open('out/'+topologia+'/3Nbloqueio_10'+'.dat', 'w')
	arquivo333  = open('out/'+topologia+'/3Nbloqueio_20'+'.dat', 'w')
	arquivo343  = open('out/'+topologia+'/3Nbloqueio_40'+'.dat', 'w')
	arquivo353  = open('out/'+topologia+'/3Nbloqueio_80'+'.dat', 'w')
	arquivo363  = open('out/'+topologia+'/3Nbloqueio_160'+'.dat', 'w')
	arquivo373  = open('out/'+topologia+'/3Nbloqueio_200'+'.dat', 'w')
	arquivo383  = open('out/'+topologia+'/3Nbloqueio_400'+'.dat', 'w')

	arquivo400  = open('out/'+topologia+'/tipo_bloqueio_frag'+'.dat', 'w')
	arquivo500  = open('out/'+topologia+'/tipo_bloqueio_eal'+'.dat', 'w')

	arquivo600  = open('out/'+topologia+'/tipo_bloqueio_frag_p'+'.dat', 'w')
	arquivo700  = open('out/'+topologia+'/tipo_bloqueio_eal_p'+'.dat', 'w')
	
	
	

	for e in range(ERLANG_MIN, ERLANG_MAX+1, ERLANG_INC):
		Bloqueio = []
		Bloqueio_10 = []
		Bloqueio_20 = []
		Bloqueio_40 = []
		Bloqueio_80 = []
		Bloqueio_160 = []
		Bloqueio_200 = []
		Bloqueio_400 = []
		Bloqueio_classe1 = []
		Bloqueio_classe2 = []
		Bloqueio_classe3 = []
		Bloqueio_banda = []
		
		#custo
		Custo_Bloqueio_10 = []
		Custo_Bloqueio_20 = []
		Custo_Bloqueio_40 = []
		Custo_Bloqueio_80 = []
		Custo_Bloqueio_160 = []
		Custo_Bloqueio_200 = []
		Custo_Bloqueio_400 = []
		Custo_bloqueio_total = []
		Custo_bloqueio_banda_classe1 = []
		Custo_bloqueio_banda_classe2 = []
		Custo_bloqueio_banda_classe3 = []
		
		Custo_bloqueio_bandaXclasse1_10 = []
		Custo_bloqueio_bandaXclasse1_20 = []
		Custo_bloqueio_bandaXclasse1_40 = []
		Custo_bloqueio_bandaXclasse1_80 = []
		Custo_bloqueio_bandaXclasse1_160 = []
		Custo_bloqueio_bandaXclasse1_200 = []
		Custo_bloqueio_bandaXclasse1_400 = []
		Custo_bloqueio_bandaXclasse2_10 = []
		Custo_bloqueio_bandaXclasse2_20 = []
		Custo_bloqueio_bandaXclasse2_40 = []
		Custo_bloqueio_bandaXclasse2_80 = []
		Custo_bloqueio_bandaXclasse2_160 = []
		Custo_bloqueio_bandaXclasse2_200 = []
		Custo_bloqueio_bandaXclasse2_400 = []
		Custo_bloqueio_bandaXclasse3_10 = []
		Custo_bloqueio_bandaXclasse3_20 = []
		Custo_bloqueio_bandaXclasse3_40 = []
		Custo_bloqueio_bandaXclasse3_80 = []
		Custo_bloqueio_bandaXclasse3_160 = []
		Custo_bloqueio_bandaXclasse3_200 = []
		Custo_bloqueio_bandaXclasse3_400 = []

		C1NBloqueio = []
		C1NBloqueio_10 = []
		C1NBloqueio_20 = []
		C1NBloqueio_20 = []
		C1NBloqueio_40 = []
		C1NBloqueio_80 = []
		C1NBloqueio_160 = []
		C1NBloqueio_200 = []
		C1NBloqueio_400 = []

		C2NBloqueio = []
		C2NBloqueio_10 = []
		C2NBloqueio_20 = []
		C2NBloqueio_40 = []
		C2NBloqueio_80 = []
		C2NBloqueio_160 = []
		C2NBloqueio_200 = []
		C2NBloqueio_400 = []

		C3NBloqueio = []
		C3NBloqueio_10 = []
		C3NBloqueio_20 = []
		C3NBloqueio_40 = []
		C3NBloqueio_80 = []
		C3NBloqueio_160 = []
		C3NBloqueio_200 = []
		C3NBloqueio_400 = []






		C1Nintervalo = []
		C1Nintervalo_10 = []
		C1Nintervalo_20 = []
		C1Nintervalo_20 = []
		C1Nintervalo_40 = []
		C1Nintervalo_80 = []
		C1Nintervalo_160 = []
		C1Nintervalo_200 = []
		C1Nintervalo_400 = []

		C2Nintervalo = []
		C2Nintervalo_10 = []
		C2Nintervalo_20 = []
		C2Nintervalo_40 = []
		C2Nintervalo_80 = []
		C2Nintervalo_160 = []
		C2Nintervalo_200 = []
		C2Nintervalo_400 = []

		C3Nintervalo = []
		C3Nintervalo_10 = []
		C3Nintervalo_20 = []
		C3Nintervalo_40 = []
		C3Nintervalo_80 = []
		C3Nintervalo_160 = []
		C3Nintervalo_200 = []
		C3Nintervalo_400 = []

		tipo_bloqueio_Frag = []
		tipo_bloqueio_Eal = []
		Intervalo_Frag = []
		Intervalo_Eal =  []

		p_Frag = []
		p_Eal =  []







		for rep in range(REP):
			rate = e / HOLDING_TIME
			seed(RANDOM_SEED[rep])
			env = simpy.Environment()
			simulador = Simulador(env)
			env.process(simulador.Run(rate))
			env.run()
			print("Erlang", e, "Simulacao...", rep)
			print("bloqueadas", simulador.NumReqBlocked, "de", NUM_OF_REQUESTS)
			Bloqueio.append(simulador.NumReqBlocked / float(NUM_OF_REQUESTS))
			Bloqueio_10.append(simulador.NumReqBlocked_10/float(simulador.NumReq_10))
			Bloqueio_20.append(simulador.NumReqBlocked_20/float(simulador.NumReq_20))
			Bloqueio_40.append(simulador.NumReqBlocked_40/float(simulador.NumReq_40))
			Bloqueio_80.append(simulador.NumReqBlocked_80/float(simulador.NumReq_80))
			Bloqueio_160.append(simulador.NumReqBlocked_160/float(simulador.NumReq_160))
			Bloqueio_200.append(simulador.NumReqBlocked_200/float(simulador.NumReq_200))
			Bloqueio_400.append(simulador.NumReqBlocked_400/float(simulador.NumReq_400))
			Bloqueio_classe1.append(simulador.NumReqBlocked_classe1/float(simulador.NumReq_classe1))
			Bloqueio_classe2.append(simulador.NumReqBlocked_classe2/float(simulador.NumReq_classe2))
			Bloqueio_classe3.append(simulador.NumReqBlocked_classe3/float(simulador.NumReq_classe3))
			BD_solicitada = ((simulador.NumReq_10)*10+(simulador.NumReq_20)*20+(simulador.NumReq_40)*40+(simulador.NumReq_80)*80+(simulador.NumReq_160)*160+(simulador.NumReq_200)*200+(simulador.NumReq_400)*400)
			BD_bloqueada = ((simulador.NumReqBlocked_10)*10+(simulador.NumReqBlocked_20)*20+(simulador.NumReqBlocked_40)*40+(simulador.NumReqBlocked_80)*80+(simulador.NumReqBlocked_160)*160+(simulador.NumReqBlocked_200)*200+(simulador.NumReqBlocked_400)*400)
			Bloqueio_banda.append(BD_bloqueada/float(BD_solicitada))
			
			#custo 
			Custo_Bloqueio_10.append(simulador.NumReqBlocked_10*float(10))
			Custo_Bloqueio_20.append(simulador.NumReqBlocked_20*float(20))
			Custo_Bloqueio_40.append(simulador.NumReqBlocked_40*float(40))
			Custo_Bloqueio_80.append(simulador.NumReqBlocked_80*float(80))
			Custo_Bloqueio_160.append(simulador.NumReqBlocked_160*float(160))
			Custo_Bloqueio_200.append(simulador.NumReqBlocked_200*float(200))
			Custo_Bloqueio_400.append(simulador.NumReqBlocked_400*float(400))
			Custo_bloqueio_total.append(BD_bloqueada)

			Custo_bloqueio_banda_classe1.append((simulador.COS1_NumReqBlocked_10*COST_PER_LINK_CLASS_TYPE_1[0])+(simulador.COS1_NumReqBlocked_20*COST_PER_LINK_CLASS_TYPE_1[1])+(simulador.COS1_NumReqBlocked_40*COST_PER_LINK_CLASS_TYPE_1[2])+(simulador.COS1_NumReqBlocked_80*COST_PER_LINK_CLASS_TYPE_1[3])+(simulador.COS1_NumReqBlocked_160*COST_PER_LINK_CLASS_TYPE_1[4])+(simulador.COS1_NumReqBlocked_200*COST_PER_LINK_CLASS_TYPE_1[5])+(simulador.COS1_NumReqBlocked_400*COST_PER_LINK_CLASS_TYPE_1[6]))
			Custo_bloqueio_banda_classe2.append((simulador.COS2_NumReqBlocked_10*COST_PER_LINK_CLASS_TYPE_2[0])+(simulador.COS2_NumReqBlocked_20*COST_PER_LINK_CLASS_TYPE_2[1])+(simulador.COS2_NumReqBlocked_40*COST_PER_LINK_CLASS_TYPE_2[2])+(simulador.COS2_NumReqBlocked_80*COST_PER_LINK_CLASS_TYPE_2[3])+(simulador.COS2_NumReqBlocked_160*COST_PER_LINK_CLASS_TYPE_2[4])+(simulador.COS2_NumReqBlocked_200*COST_PER_LINK_CLASS_TYPE_2[5])+(simulador.COS2_NumReqBlocked_400*COST_PER_LINK_CLASS_TYPE_2[6]))
			Custo_bloqueio_banda_classe3.append((simulador.COS3_NumReqBlocked_10*COST_PER_LINK_CLASS_TYPE_3[0])+(simulador.COS3_NumReqBlocked_20*COST_PER_LINK_CLASS_TYPE_3[1])+(simulador.COS3_NumReqBlocked_40*COST_PER_LINK_CLASS_TYPE_3[2])+(simulador.COS3_NumReqBlocked_80*COST_PER_LINK_CLASS_TYPE_3[3])+(simulador.COS3_NumReqBlocked_160*COST_PER_LINK_CLASS_TYPE_3[4])+(simulador.COS3_NumReqBlocked_200*COST_PER_LINK_CLASS_TYPE_3[5])+(simulador.COS3_NumReqBlocked_400*COST_PER_LINK_CLASS_TYPE_3[6]))
			
			
			
			Custo_bloqueio_bandaXclasse1_10.append((simulador.COS1_NumReqBlocked_10*COST_PER_LINK_CLASS_TYPE_1[0]))
			Custo_bloqueio_bandaXclasse1_20.append((simulador.COS1_NumReqBlocked_20*COST_PER_LINK_CLASS_TYPE_1[1]))
			Custo_bloqueio_bandaXclasse1_40.append((simulador.COS1_NumReqBlocked_40*COST_PER_LINK_CLASS_TYPE_1[2]))
			Custo_bloqueio_bandaXclasse1_80.append((simulador.COS1_NumReqBlocked_80*COST_PER_LINK_CLASS_TYPE_1[3]))
			Custo_bloqueio_bandaXclasse1_160.append((simulador.COS1_NumReqBlocked_160*COST_PER_LINK_CLASS_TYPE_1[4]))
			Custo_bloqueio_bandaXclasse1_200.append((simulador.COS1_NumReqBlocked_200*COST_PER_LINK_CLASS_TYPE_1[5]))
			Custo_bloqueio_bandaXclasse1_400.append((simulador.COS1_NumReqBlocked_400*COST_PER_LINK_CLASS_TYPE_1[6]))
			
			Custo_bloqueio_bandaXclasse2_10.append((simulador.COS2_NumReqBlocked_10*COST_PER_LINK_CLASS_TYPE_2[0]))
			Custo_bloqueio_bandaXclasse2_20.append((simulador.COS2_NumReqBlocked_20*COST_PER_LINK_CLASS_TYPE_2[1]))
			Custo_bloqueio_bandaXclasse2_40.append((simulador.COS2_NumReqBlocked_40*COST_PER_LINK_CLASS_TYPE_2[2]))
			Custo_bloqueio_bandaXclasse2_80.append((simulador.COS2_NumReqBlocked_80*COST_PER_LINK_CLASS_TYPE_2[3]))
			Custo_bloqueio_bandaXclasse2_160.append((simulador.COS2_NumReqBlocked_160*COST_PER_LINK_CLASS_TYPE_2[4]))
			Custo_bloqueio_bandaXclasse2_200.append((simulador.COS2_NumReqBlocked_200*COST_PER_LINK_CLASS_TYPE_2[5]))
			Custo_bloqueio_bandaXclasse2_400.append((simulador.COS2_NumReqBlocked_400*COST_PER_LINK_CLASS_TYPE_2[6]))
			
			Custo_bloqueio_bandaXclasse3_10.append((simulador.COS3_NumReqBlocked_10*COST_PER_LINK_CLASS_TYPE_3[0]))
			Custo_bloqueio_bandaXclasse3_20.append((simulador.COS3_NumReqBlocked_20*COST_PER_LINK_CLASS_TYPE_3[1]))
			Custo_bloqueio_bandaXclasse3_40.append((simulador.COS3_NumReqBlocked_40*COST_PER_LINK_CLASS_TYPE_3[2]))
			Custo_bloqueio_bandaXclasse3_80.append((simulador.COS3_NumReqBlocked_80*COST_PER_LINK_CLASS_TYPE_3[3]))
			Custo_bloqueio_bandaXclasse3_160.append((simulador.COS3_NumReqBlocked_160*COST_PER_LINK_CLASS_TYPE_3[4]))
			Custo_bloqueio_bandaXclasse3_200.append((simulador.COS3_NumReqBlocked_200*COST_PER_LINK_CLASS_TYPE_3[5]))
			Custo_bloqueio_bandaXclasse3_400.append((simulador.COS3_NumReqBlocked_400*COST_PER_LINK_CLASS_TYPE_3[6]))

			tipo_bloqueio_Frag.append(simulador.Frag)
			tipo_bloqueio_Eal.append(simulador.Eal)
			if float(simulador.Frag+simulador.Eal) > 0:
				p_Frag.append(simulador.Frag/float(simulador.Frag+simulador.Eal))
				p_Eal.append(simulador.Eal/float(simulador.Frag+simulador.Eal))
			else:
				p_Frag.append(float(0.0))
				p_Eal.append(float(0.0))


			C1NBloqueio.append(simulador.NumReqBlocked_classe1)
			C1NBloqueio_10.append(simulador.COS1_NumReqBlocked_10)
			C1NBloqueio_20.append(simulador.COS1_NumReqBlocked_20)
			C1NBloqueio_40.append(simulador.COS1_NumReqBlocked_40)
			C1NBloqueio_80.append(simulador.COS1_NumReqBlocked_80)
			C1NBloqueio_160.append(simulador.COS1_NumReqBlocked_160)
			C1NBloqueio_200.append(simulador.COS1_NumReqBlocked_200)
			C1NBloqueio_400.append(simulador.COS1_NumReqBlocked_400)

			C2NBloqueio.append(simulador.NumReqBlocked_classe2)
			C2NBloqueio_10.append(simulador.COS2_NumReqBlocked_10)
			C2NBloqueio_20.append(simulador.COS2_NumReqBlocked_20)
			C2NBloqueio_40.append(simulador.COS2_NumReqBlocked_40)
			C2NBloqueio_80.append(simulador.COS2_NumReqBlocked_80)
			C2NBloqueio_160.append(simulador.COS2_NumReqBlocked_160)
			C2NBloqueio_200.append(simulador.COS2_NumReqBlocked_200)
			C2NBloqueio_400.append(simulador.COS2_NumReqBlocked_400)

			C3NBloqueio.append(simulador.NumReqBlocked_classe3)
			C3NBloqueio_10.append(simulador.COS3_NumReqBlocked_10)
			C3NBloqueio_20.append(simulador.COS3_NumReqBlocked_20)
			C3NBloqueio_40.append(simulador.COS3_NumReqBlocked_40)
			C3NBloqueio_80.append(simulador.COS3_NumReqBlocked_80)
			C3NBloqueio_160.append(simulador.COS3_NumReqBlocked_160)
			C3NBloqueio_200.append(simulador.COS3_NumReqBlocked_200)
			C3NBloqueio_400.append(simulador.COS3_NumReqBlocked_400)
			

			
			

		intervalo = CalculaIntervalo(Bloqueio)# total req
		intervalo_10 = CalculaIntervalo(Bloqueio_10)
		intervalo_20 = CalculaIntervalo(Bloqueio_20)
		intervalo_40 = CalculaIntervalo(Bloqueio_40)
		intervalo_80 = CalculaIntervalo(Bloqueio_80)
		intervalo_160 = CalculaIntervalo(Bloqueio_160)
		intervalo_200 = CalculaIntervalo(Bloqueio_200)
		intervalo_400 = CalculaIntervalo(Bloqueio_400)
		intervalo_classe1 = CalculaIntervalo(Bloqueio_classe1)#total classe1
		intervalo_classe2 = CalculaIntervalo(Bloqueio_classe2)
		intervalo_classe3 = CalculaIntervalo(Bloqueio_classe3)
		intervalo_bloqueio_banda = CalculaIntervalo(Bloqueio_banda)
		
		#CUSTO
		intervalo_Custo_Bloqueio_10 = CalculaIntervalo(Custo_Bloqueio_10)
		intervalo_Custo_Bloqueio_20 = CalculaIntervalo(Custo_Bloqueio_20)
		intervalo_Custo_Bloqueio_40 = CalculaIntervalo(Custo_Bloqueio_40)
		intervalo_Custo_Bloqueio_80 = CalculaIntervalo(Custo_Bloqueio_80)
		intervalo_Custo_Bloqueio_160 = CalculaIntervalo(Custo_Bloqueio_160)
		intervalo_Custo_Bloqueio_200 = CalculaIntervalo(Custo_Bloqueio_200)
		intervalo_Custo_Bloqueio_400 = CalculaIntervalo(Custo_Bloqueio_400)
		intervalo_Custo_bloqueio_total = CalculaIntervalo(Custo_bloqueio_total)

		bloqueio_banda_classe1 = CalculaIntervalo(Custo_bloqueio_banda_classe1)
		bloqueio_banda_classe2 = CalculaIntervalo(Custo_bloqueio_banda_classe2)
		bloqueio_banda_classe3 = CalculaIntervalo(Custo_bloqueio_banda_classe3)
		
		
		bloqueio_bandaXclasse1_10 = CalculaIntervalo(Custo_bloqueio_bandaXclasse1_10)
		bloqueio_bandaXclasse1_20 = CalculaIntervalo(Custo_bloqueio_bandaXclasse1_20)
		bloqueio_bandaXclasse1_40 = CalculaIntervalo(Custo_bloqueio_bandaXclasse1_40)
		bloqueio_bandaXclasse1_80 = CalculaIntervalo(Custo_bloqueio_bandaXclasse1_80)
		bloqueio_bandaXclasse1_160 = CalculaIntervalo(Custo_bloqueio_bandaXclasse1_160)
		bloqueio_bandaXclasse1_200 = CalculaIntervalo(Custo_bloqueio_bandaXclasse1_200)
		bloqueio_bandaXclasse1_400 = CalculaIntervalo(Custo_bloqueio_bandaXclasse1_400)
		
		bloqueio_bandaXclasse2_10 = CalculaIntervalo(Custo_bloqueio_bandaXclasse2_10)
		bloqueio_bandaXclasse2_20 = CalculaIntervalo(Custo_bloqueio_bandaXclasse2_20)
		bloqueio_bandaXclasse2_40 = CalculaIntervalo(Custo_bloqueio_bandaXclasse2_40)
		bloqueio_bandaXclasse2_80 = CalculaIntervalo(Custo_bloqueio_bandaXclasse2_80)
		bloqueio_bandaXclasse2_160 = CalculaIntervalo(Custo_bloqueio_bandaXclasse2_160)
		bloqueio_bandaXclasse2_200 = CalculaIntervalo(Custo_bloqueio_bandaXclasse2_200)
		bloqueio_bandaXclasse2_400 = CalculaIntervalo(Custo_bloqueio_bandaXclasse2_400)
		
		bloqueio_bandaXclasse3_10 = CalculaIntervalo(Custo_bloqueio_bandaXclasse3_10)
		bloqueio_bandaXclasse3_20 = CalculaIntervalo(Custo_bloqueio_bandaXclasse3_20)
		bloqueio_bandaXclasse3_40 = CalculaIntervalo(Custo_bloqueio_bandaXclasse3_40)
		bloqueio_bandaXclasse3_80 = CalculaIntervalo(Custo_bloqueio_bandaXclasse3_80)
		bloqueio_bandaXclasse3_160 = CalculaIntervalo(Custo_bloqueio_bandaXclasse3_160)
		bloqueio_bandaXclasse3_200 = CalculaIntervalo(Custo_bloqueio_bandaXclasse3_200)
		bloqueio_bandaXclasse3_400 = CalculaIntervalo(Custo_bloqueio_bandaXclasse3_400)


		C1Nintervalo = CalculaIntervalo(C1NBloqueio)# total req
		C1Nintervalo_10 = CalculaIntervalo(C1NBloqueio_10)
		C1Nintervalo_20 = CalculaIntervalo(C1NBloqueio_20)
		C1Nintervalo_40 = CalculaIntervalo(C1NBloqueio_40)
		C1Nintervalo_80 = CalculaIntervalo(C1NBloqueio_80)
		C1Nintervalo_160 = CalculaIntervalo(C1NBloqueio_160)
		C1Nintervalo_200 = CalculaIntervalo(C1NBloqueio_200)
		C1Nintervalo_400 = CalculaIntervalo(C1NBloqueio_400)

		C2Nintervalo = CalculaIntervalo(C2NBloqueio)# total req
		C2Nintervalo_10 = CalculaIntervalo(C2NBloqueio_10)
		C2Nintervalo_20 = CalculaIntervalo(C2NBloqueio_20)
		C2Nintervalo_40 = CalculaIntervalo(C2NBloqueio_40)
		C2Nintervalo_80 = CalculaIntervalo(C2NBloqueio_80)
		C2Nintervalo_160 = CalculaIntervalo(C2NBloqueio_160)
		C2Nintervalo_200 = CalculaIntervalo(C2NBloqueio_200)
		C2Nintervalo_400 = CalculaIntervalo(C2NBloqueio_400)

		C3Nintervalo = CalculaIntervalo(C3NBloqueio)# total req
		C3Nintervalo_10 = CalculaIntervalo(C3NBloqueio_10)
		C3Nintervalo_20 = CalculaIntervalo(C3NBloqueio_20)
		C3Nintervalo_40 = CalculaIntervalo(C3NBloqueio_40)
		C3Nintervalo_80 = CalculaIntervalo(C3NBloqueio_80)
		C3Nintervalo_160 = CalculaIntervalo(C3NBloqueio_160)
		C3Nintervalo_200 = CalculaIntervalo(C3NBloqueio_200)
		C3Nintervalo_400 = CalculaIntervalo(C3NBloqueio_400)

		Intervalo_Frag =  CalculaIntervalo(tipo_bloqueio_Frag)
		Intervalo_Eal =  CalculaIntervalo(tipo_bloqueio_Eal)

		Intervalo_Frag_p =  CalculaIntervalo(p_Frag)
		Intervalo_Eal_p =  CalculaIntervalo(p_Eal)







		
		
		

		arquivo1.write(str(e))
		arquivo1.write("\t")
		arquivo1.write(str(intervalo[0]))
		arquivo1.write("\t")
		arquivo1.write(str(intervalo[0]-intervalo[1]))
		arquivo1.write("\t")
		arquivo1.write(str(intervalo[0]+intervalo[1]))
		arquivo1.write("\n")

		arquivo2.write(str(e))
		arquivo2.write("\t")
		arquivo2.write(str(intervalo_10[0]))
		arquivo2.write("\t")
		arquivo2.write(str(intervalo_10[0]-intervalo_10[1]))
		arquivo2.write("\t")
		arquivo2.write(str(intervalo_10[0]+intervalo_10[1]))
		arquivo2.write("\n")

		arquivo3.write(str(e))
		arquivo3.write("\t")
		arquivo3.write(str(intervalo_20[0]))
		arquivo3.write("\t")
		arquivo3.write(str(intervalo_20[0]-intervalo_20[1]))
		arquivo3.write("\t")
		arquivo3.write(str(intervalo_20[0]+intervalo_20[1]))
		arquivo3.write("\n")

		arquivo4.write(str(e))
		arquivo4.write("\t")
		arquivo4.write(str(intervalo_40[0]))
		arquivo4.write("\t")
		arquivo4.write(str(intervalo_40[0]-intervalo_40[1]))
		arquivo4.write("\t")
		arquivo4.write(str(intervalo_40[0]+intervalo_40[1]))
		arquivo4.write("\n")

		arquivo5.write(str(e))
		arquivo5.write("\t")
		arquivo5.write(str(intervalo_80[0]))
		arquivo5.write("\t")
		arquivo5.write(str(intervalo_80[0]-intervalo_80[1]))
		arquivo5.write("\t")
		arquivo5.write(str(intervalo_80[0]+intervalo_80[1]))
		arquivo5.write("\n")

		arquivo6.write(str(e))
		arquivo6.write("\t")
		arquivo6.write(str(intervalo_160[0]))
		arquivo6.write("\t")
		arquivo6.write(str(intervalo_160[0]-intervalo_160[1]))
		arquivo6.write("\t")
		arquivo6.write(str(intervalo_160[0]+intervalo_160[1]))
		arquivo6.write("\n")

		arquivo7.write(str(e))
		arquivo7.write("\t")
		arquivo7.write(str(intervalo_200[0]))
		arquivo7.write("\t")
		arquivo7.write(str(intervalo_200[0]-intervalo_200[1]))
		arquivo7.write("\t")
		arquivo7.write(str(intervalo_200[0]+intervalo_200[1]))
		arquivo7.write("\n")

		arquivo8.write(str(e))
		arquivo8.write("\t")
		arquivo8.write(str(intervalo_400[0]))
		arquivo8.write("\t")
		arquivo8.write(str(intervalo_400[0]-intervalo_400[1]))
		arquivo8.write("\t")
		arquivo8.write(str(intervalo_400[0]+intervalo_400[1]))
		arquivo8.write("\n")

		arquivo9.write(str(e))
		arquivo9.write("\t")
		arquivo9.write(str(intervalo_classe1[0]))
		arquivo9.write("\t")
		arquivo9.write(str(intervalo_classe1[0]-intervalo_classe1[1]))
		arquivo9.write("\t")
		arquivo9.write(str(intervalo_classe1[0]+intervalo_classe1[1]))
		arquivo9.write("\n")

		arquivo10.write(str(e))
		arquivo10.write("\t")
		arquivo10.write(str(intervalo_classe2[0]))
		arquivo10.write("\t")
		arquivo10.write(str(intervalo_classe2[0]-intervalo_classe2[1]))
		arquivo10.write("\t")
		arquivo10.write(str(intervalo_classe2[0]+intervalo_classe2[1]))
		arquivo10.write("\n")

		arquivo11.write(str(e))
		arquivo11.write("\t")
		arquivo11.write(str(intervalo_classe3[0]))
		arquivo11.write("\t")
		arquivo11.write(str(intervalo_classe3[0]-intervalo_classe3[1]))
		arquivo11.write("\t")
		arquivo11.write(str(intervalo_classe3[0]+intervalo_classe3[1]))
		arquivo11.write("\n")

		arquivo12.write(str(e))
		arquivo12.write("\t")
		arquivo12.write(str(intervalo_bloqueio_banda[0]))
		arquivo12.write("\t")
		arquivo12.write(str(intervalo_bloqueio_banda[0]-intervalo_bloqueio_banda[1]))
		arquivo12.write("\t")
		arquivo12.write(str(intervalo_bloqueio_banda[0]+intervalo_bloqueio_banda[1]))
		arquivo12.write("\n")
		
		arquivo13.write(str(e))
		arquivo13.write("\t")
		arquivo13.write(str(intervalo_Custo_bloqueio_total[0]))
		arquivo13.write("\t")
		arquivo13.write(str(intervalo_Custo_bloqueio_total[0]-intervalo_Custo_bloqueio_total[1]))
		arquivo13.write("\t")
		arquivo13.write(str(intervalo_Custo_bloqueio_total[0]+intervalo_Custo_bloqueio_total[1]))
		arquivo13.write("\n")
		
		arquivo14.write(str(e))
		arquivo14.write("\t")
		arquivo14.write(str(intervalo_Custo_Bloqueio_10[0]))
		arquivo14.write("\t")
		arquivo14.write(str(intervalo_Custo_Bloqueio_10[0]-intervalo_Custo_Bloqueio_10[1]))
		arquivo14.write("\t")
		arquivo14.write(str(intervalo_Custo_Bloqueio_10[0]+intervalo_Custo_Bloqueio_10[1]))
		arquivo14.write("\n")
		
		arquivo15.write(str(e))
		arquivo15.write("\t")
		arquivo15.write(str(intervalo_Custo_Bloqueio_20[0]))
		arquivo15.write("\t")
		arquivo15.write(str(intervalo_Custo_Bloqueio_20[0]-intervalo_Custo_Bloqueio_20[1]))
		arquivo15.write("\t")
		arquivo15.write(str(intervalo_Custo_Bloqueio_20[0]+intervalo_Custo_Bloqueio_20[1]))
		arquivo15.write("\n")
		
		arquivo16.write(str(e))
		arquivo16.write("\t")
		arquivo16.write(str(intervalo_Custo_Bloqueio_40[0]))
		arquivo16.write("\t")
		arquivo16.write(str(intervalo_Custo_Bloqueio_40[0]-intervalo_Custo_Bloqueio_40[1]))
		arquivo16.write("\t")
		arquivo16.write(str(intervalo_Custo_Bloqueio_40[0]+intervalo_Custo_Bloqueio_40[1]))
		arquivo16.write("\n")
		
		arquivo17.write(str(e))
		arquivo17.write("\t")
		arquivo17.write(str(intervalo_Custo_Bloqueio_80[0]))
		arquivo17.write("\t")
		arquivo17.write(str(intervalo_Custo_Bloqueio_80[0]-intervalo_Custo_Bloqueio_80[1]))
		arquivo17.write("\t")
		arquivo17.write(str(intervalo_Custo_Bloqueio_80[0]+intervalo_Custo_Bloqueio_80[1]))
		arquivo17.write("\n")
		
		arquivo18.write(str(e))
		arquivo18.write("\t")
		arquivo18.write(str(intervalo_Custo_Bloqueio_160[0]))
		arquivo18.write("\t")
		arquivo18.write(str(intervalo_Custo_Bloqueio_160[0]-intervalo_Custo_Bloqueio_160[1]))
		arquivo18.write("\t")
		arquivo18.write(str(intervalo_Custo_Bloqueio_160[0]+intervalo_Custo_Bloqueio_160[1]))
		arquivo18.write("\n")
		
		arquivo19.write(str(e))
		arquivo19.write("\t")
		arquivo19.write(str(intervalo_Custo_Bloqueio_200[0]))
		arquivo19.write("\t")
		arquivo19.write(str(intervalo_Custo_Bloqueio_200[0]-intervalo_Custo_Bloqueio_200[1]))
		arquivo19.write("\t")
		arquivo19.write(str(intervalo_Custo_Bloqueio_200[0]+intervalo_Custo_Bloqueio_200[1]))
		arquivo19.write("\n")
		
		arquivo20.write(str(e))
		arquivo20.write("\t")
		arquivo20.write(str(intervalo_Custo_Bloqueio_400[0]))
		arquivo20.write("\t")
		arquivo20.write(str(intervalo_Custo_Bloqueio_400[0]-intervalo_Custo_Bloqueio_400[1]))
		arquivo20.write("\t")
		arquivo20.write(str(intervalo_Custo_Bloqueio_400[0]+intervalo_Custo_Bloqueio_400[1]))
		arquivo20.write("\n")

		arquivo21.write(str(e))
		arquivo21.write("\t")
		arquivo21.write(str(bloqueio_banda_classe1[0]))
		arquivo21.write("\t")
		arquivo21.write(str(bloqueio_banda_classe1[0]-bloqueio_banda_classe1[1]))
		arquivo21.write("\t")
		arquivo21.write(str(bloqueio_banda_classe1[0]+bloqueio_banda_classe1[1]))
		arquivo21.write("\n")

		arquivo22.write(str(e))
		arquivo22.write("\t")
		arquivo22.write(str(bloqueio_banda_classe2[0]))
		arquivo22.write("\t")
		arquivo22.write(str(bloqueio_banda_classe2[0]-bloqueio_banda_classe2[1]))
		arquivo22.write("\t")
		arquivo22.write(str(bloqueio_banda_classe2[0]+bloqueio_banda_classe2[1]))
		arquivo22.write("\n")

		arquivo23.write(str(e))
		arquivo23.write("\t")
		arquivo23.write(str(bloqueio_banda_classe3[0]))
		arquivo23.write("\t")
		arquivo23.write(str(bloqueio_banda_classe3[0]-bloqueio_banda_classe3[1]))
		arquivo23.write("\t")
		arquivo23.write(str(bloqueio_banda_classe3[0]+bloqueio_banda_classe3[1]))
		arquivo23.write("\n")
		
		arquivo24.write(str(e))
		arquivo24.write("\t")
		arquivo24.write(str(BANDWIDTH[0]))
		arquivo24.write("\t")
		arquivo24.write(str(bloqueio_bandaXclasse1_10[0]))
		arquivo24.write("\t")
		arquivo24.write(str(bloqueio_bandaXclasse1_10[0]-bloqueio_bandaXclasse1_10[1]))
		arquivo24.write("\t")
		arquivo24.write(str(bloqueio_bandaXclasse1_10[0]+bloqueio_bandaXclasse1_10[1]))
		arquivo24.write("\n")
		arquivo24.write(str(e))
		arquivo24.write("\t")
		arquivo24.write(str(BANDWIDTH[1]))
		arquivo24.write("\t")
		arquivo24.write(str(bloqueio_bandaXclasse1_20[0]))
		arquivo24.write("\t")
		arquivo24.write(str(bloqueio_bandaXclasse1_20[0]-bloqueio_bandaXclasse1_20[1]))
		arquivo24.write("\t")
		arquivo24.write(str(bloqueio_bandaXclasse1_20[0]+bloqueio_bandaXclasse1_20[1]))
		arquivo24.write("\n")
		arquivo24.write(str(e))
		arquivo24.write("\t")
		arquivo24.write(str(BANDWIDTH[2]))
		arquivo24.write("\t")
		arquivo24.write(str(bloqueio_bandaXclasse1_40[0]))
		arquivo24.write("\t")
		arquivo24.write(str(bloqueio_bandaXclasse1_40[0]-bloqueio_bandaXclasse1_40[1]))
		arquivo24.write("\t")
		arquivo24.write(str(bloqueio_bandaXclasse1_40[0]+bloqueio_bandaXclasse1_40[1]))
		arquivo24.write("\n")
		arquivo24.write(str(e))
		arquivo24.write("\t")
		arquivo24.write(str(BANDWIDTH[3]))
		arquivo24.write("\t")
		arquivo24.write(str(bloqueio_bandaXclasse1_80[0]))
		arquivo24.write("\t")
		arquivo24.write(str(bloqueio_bandaXclasse1_80[0]-bloqueio_bandaXclasse1_80[1]))
		arquivo24.write("\t")
		arquivo24.write(str(bloqueio_bandaXclasse1_80[0]+bloqueio_bandaXclasse1_80[1]))
		arquivo24.write("\n")
		arquivo24.write(str(e))
		arquivo24.write("\t")
		arquivo24.write(str(BANDWIDTH[4]))
		arquivo24.write("\t")
		arquivo24.write(str(bloqueio_bandaXclasse1_160[0]))
		arquivo24.write("\t")
		arquivo24.write(str(bloqueio_bandaXclasse1_160[0]-bloqueio_bandaXclasse1_160[1]))
		arquivo24.write("\t")
		arquivo24.write(str(bloqueio_bandaXclasse1_160[0]+bloqueio_bandaXclasse1_160[1]))
		arquivo24.write("\n")
		arquivo24.write(str(e))
		arquivo24.write("\t")
		arquivo24.write(str(BANDWIDTH[5]))
		arquivo24.write("\t")
		arquivo24.write(str(bloqueio_bandaXclasse1_200[0]))
		arquivo24.write("\t")
		arquivo24.write(str(bloqueio_bandaXclasse1_200[0]-bloqueio_bandaXclasse1_200[1]))
		arquivo24.write("\t")
		arquivo24.write(str(bloqueio_bandaXclasse1_200[0]+bloqueio_bandaXclasse1_200[1]))
		arquivo24.write("\n")
		arquivo24.write(str(e))
		arquivo24.write("\t")
		arquivo24.write(str(BANDWIDTH[6]))
		arquivo24.write("\t")
		arquivo24.write(str(bloqueio_bandaXclasse1_400[0]))
		arquivo24.write("\t")
		arquivo24.write(str(bloqueio_bandaXclasse1_400[0]-bloqueio_bandaXclasse1_400[1]))
		arquivo24.write("\t")
		arquivo24.write(str(bloqueio_bandaXclasse1_400[0]+bloqueio_bandaXclasse1_400[1]))
		arquivo24.write("\n")
		
		
		arquivo25.write(str(e))
		arquivo25.write("\t")
		arquivo25.write(str(BANDWIDTH[0]))
		arquivo25.write("\t")
		arquivo25.write(str(bloqueio_bandaXclasse2_10[0]))
		arquivo25.write("\t")
		arquivo25.write(str(bloqueio_bandaXclasse2_10[0]-bloqueio_bandaXclasse2_10[1]))
		arquivo25.write("\t")
		arquivo25.write(str(bloqueio_bandaXclasse2_10[0]+bloqueio_bandaXclasse2_10[1]))
		arquivo25.write("\n")
		arquivo25.write(str(e))
		arquivo25.write("\t")
		arquivo25.write(str(BANDWIDTH[1]))
		arquivo25.write("\t")
		arquivo25.write(str(bloqueio_bandaXclasse2_20[0]))
		arquivo25.write("\t")
		arquivo25.write(str(bloqueio_bandaXclasse2_20[0]-bloqueio_bandaXclasse2_20[1]))
		arquivo25.write("\t")
		arquivo25.write(str(bloqueio_bandaXclasse2_20[0]+bloqueio_bandaXclasse2_20[1]))
		arquivo25.write("\n")
		arquivo25.write(str(e))
		arquivo25.write("\t")
		arquivo25.write(str(BANDWIDTH[2]))
		arquivo25.write("\t")
		arquivo25.write(str(bloqueio_bandaXclasse2_40[0]))
		arquivo25.write("\t")
		arquivo25.write(str(bloqueio_bandaXclasse2_40[0]-bloqueio_bandaXclasse2_40[1]))
		arquivo25.write("\t")
		arquivo25.write(str(bloqueio_bandaXclasse2_40[0]+bloqueio_bandaXclasse2_40[1]))
		arquivo25.write("\n")
		arquivo25.write(str(e))
		arquivo25.write("\t")
		arquivo25.write(str(BANDWIDTH[3]))
		arquivo25.write("\t")
		arquivo25.write(str(bloqueio_bandaXclasse2_80[0]))
		arquivo25.write("\t")
		arquivo25.write(str(bloqueio_bandaXclasse2_80[0]-bloqueio_bandaXclasse2_80[1]))
		arquivo25.write("\t")
		arquivo25.write(str(bloqueio_bandaXclasse2_80[0]+bloqueio_bandaXclasse2_80[1]))
		arquivo25.write("\n")
		arquivo25.write(str(e))
		arquivo25.write("\t")
		arquivo25.write(str(BANDWIDTH[4]))
		arquivo25.write("\t")
		arquivo25.write(str(bloqueio_bandaXclasse2_160[0]))
		arquivo25.write("\t")
		arquivo25.write(str(bloqueio_bandaXclasse2_160[0]-bloqueio_bandaXclasse2_160[1]))
		arquivo25.write("\t")
		arquivo25.write(str(bloqueio_bandaXclasse2_160[0]+bloqueio_bandaXclasse2_160[1]))
		arquivo25.write("\n")
		arquivo25.write(str(e))
		arquivo25.write("\t")
		arquivo25.write(str(BANDWIDTH[5]))
		arquivo25.write("\t")
		arquivo25.write(str(bloqueio_bandaXclasse2_200[0]))
		arquivo25.write("\t")
		arquivo25.write(str(bloqueio_bandaXclasse2_200[0]-bloqueio_bandaXclasse2_200[1]))
		arquivo25.write("\t")
		arquivo25.write(str(bloqueio_bandaXclasse2_200[0]+bloqueio_bandaXclasse2_200[1]))
		arquivo25.write("\n")
		arquivo25.write(str(e))
		arquivo25.write("\t")
		arquivo25.write(str(BANDWIDTH[6]))
		arquivo25.write("\t")
		arquivo25.write(str(bloqueio_bandaXclasse2_400[0]))
		arquivo25.write("\t")
		arquivo25.write(str(bloqueio_bandaXclasse2_400[0]-bloqueio_bandaXclasse2_400[1]))
		arquivo25.write("\t")
		arquivo25.write(str(bloqueio_bandaXclasse2_400[0]+bloqueio_bandaXclasse2_400[1]))
		arquivo25.write("\n")
		
		
		arquivo26.write(str(e))
		arquivo26.write("\t")
		arquivo26.write(str(BANDWIDTH[0]))
		arquivo26.write("\t")
		arquivo26.write(str(bloqueio_bandaXclasse3_10[0]))
		arquivo26.write("\t")
		arquivo26.write(str(bloqueio_bandaXclasse3_10[0]-bloqueio_bandaXclasse3_10[1]))
		arquivo26.write("\t")
		arquivo26.write(str(bloqueio_bandaXclasse3_10[0]+bloqueio_bandaXclasse3_10[1]))
		arquivo26.write("\n")
		arquivo26.write(str(e))
		arquivo26.write("\t")
		arquivo26.write(str(BANDWIDTH[1]))
		arquivo26.write("\t")
		arquivo26.write(str(bloqueio_bandaXclasse3_20[0]))
		arquivo26.write("\t")
		arquivo26.write(str(bloqueio_bandaXclasse3_20[0]-bloqueio_bandaXclasse3_20[1]))
		arquivo26.write("\t")
		arquivo26.write(str(bloqueio_bandaXclasse3_20[0]+bloqueio_bandaXclasse3_20[1]))
		arquivo26.write("\n")
		arquivo26.write(str(e))
		arquivo26.write("\t")
		arquivo26.write(str(BANDWIDTH[2]))
		arquivo26.write("\t")
		arquivo26.write(str(bloqueio_bandaXclasse3_40[0]))
		arquivo26.write("\t")
		arquivo26.write(str(bloqueio_bandaXclasse3_40[0]-bloqueio_bandaXclasse3_40[1]))
		arquivo26.write("\t")
		arquivo26.write(str(bloqueio_bandaXclasse3_40[0]+bloqueio_bandaXclasse3_40[1]))
		arquivo26.write("\n")
		arquivo26.write(str(e))
		arquivo26.write("\t")
		arquivo26.write(str(BANDWIDTH[3]))
		arquivo26.write("\t")
		arquivo26.write(str(bloqueio_bandaXclasse3_80[0]))
		arquivo26.write("\t")
		arquivo26.write(str(bloqueio_bandaXclasse3_80[0]-bloqueio_bandaXclasse3_80[1]))
		arquivo26.write("\t")
		arquivo26.write(str(bloqueio_bandaXclasse3_80[0]+bloqueio_bandaXclasse3_80[1]))
		arquivo26.write("\n")
		arquivo26.write(str(e))
		arquivo26.write("\t")
		arquivo26.write(str(BANDWIDTH[4]))
		arquivo26.write("\t")
		arquivo26.write(str(bloqueio_bandaXclasse3_160[0]))
		arquivo26.write("\t")
		arquivo26.write(str(bloqueio_bandaXclasse3_160[0]-bloqueio_bandaXclasse3_160[1]))
		arquivo26.write("\t")
		arquivo26.write(str(bloqueio_bandaXclasse3_160[0]+bloqueio_bandaXclasse3_160[1]))
		arquivo26.write("\n")
		arquivo26.write(str(e))
		arquivo26.write("\t")
		arquivo26.write(str(BANDWIDTH[5]))
		arquivo26.write("\t")
		arquivo26.write(str(bloqueio_bandaXclasse3_200[0]))
		arquivo26.write("\t")
		arquivo26.write(str(bloqueio_bandaXclasse3_200[0]-bloqueio_bandaXclasse3_200[1]))
		arquivo26.write("\t")
		arquivo26.write(str(bloqueio_bandaXclasse3_200[0]+bloqueio_bandaXclasse3_200[1]))
		arquivo26.write("\n")
		arquivo26.write(str(e))
		arquivo26.write("\t")
		arquivo26.write(str(BANDWIDTH[6]))
		arquivo26.write("\t")
		arquivo26.write(str(bloqueio_bandaXclasse3_400[0]))
		arquivo26.write("\t")
		arquivo26.write(str(bloqueio_bandaXclasse3_400[0]-bloqueio_bandaXclasse3_400[1]))
		arquivo26.write("\t")
		arquivo26.write(str(bloqueio_bandaXclasse3_400[0]+bloqueio_bandaXclasse3_400[1]))
		arquivo26.write("\n")






		arquivo311.write(str(e))
		arquivo311.write("\t")
		arquivo311.write(str(C1Nintervalo[0]))
		arquivo311.write("\t")
		arquivo311.write(str(C1Nintervalo[0]-C1Nintervalo[1]))
		arquivo311.write("\t")
		arquivo311.write(str(C1Nintervalo[0]+C1Nintervalo[1]))
		arquivo311.write("\n")

		arquivo321.write(str(e))
		arquivo321.write("\t")
		arquivo321.write(str(C1Nintervalo_10[0]))
		arquivo321.write("\t")
		arquivo321.write(str(C1Nintervalo_10[0]-C1Nintervalo_10[1]))
		arquivo321.write("\t")
		arquivo321.write(str(C1Nintervalo_10[0]+C1Nintervalo_10[1]))
		arquivo321.write("\n")

		arquivo331.write(str(e))
		arquivo331.write("\t")
		arquivo331.write(str(C1Nintervalo_20[0]))
		arquivo331.write("\t")
		arquivo331.write(str(C1Nintervalo_20[0]-C1Nintervalo_20[1]))
		arquivo331.write("\t")
		arquivo331.write(str(C1Nintervalo_20[0]+C1Nintervalo_20[1]))
		arquivo331.write("\n")

		arquivo341.write(str(e))
		arquivo341.write("\t")
		arquivo341.write(str(C1Nintervalo_40[0]))
		arquivo341.write("\t")
		arquivo341.write(str(C1Nintervalo_40[0]-C1Nintervalo_40[1]))
		arquivo341.write("\t")
		arquivo341.write(str(C1Nintervalo_40[0]+C1Nintervalo_40[1]))
		arquivo341.write("\n")

		arquivo351.write(str(e))
		arquivo351.write("\t")
		arquivo351.write(str(C1Nintervalo_80[0]))
		arquivo351.write("\t")
		arquivo351.write(str(C1Nintervalo_80[0]-C1Nintervalo_80[1]))
		arquivo351.write("\t")
		arquivo351.write(str(C1Nintervalo_80[0]+C1Nintervalo_80[1]))
		arquivo351.write("\n")

		arquivo361.write(str(e))
		arquivo361.write("\t")
		arquivo361.write(str(C1Nintervalo_160[0]))
		arquivo361.write("\t")
		arquivo361.write(str(C1Nintervalo_160[0]-C1Nintervalo_160[1]))
		arquivo361.write("\t")
		arquivo361.write(str(C1Nintervalo_160[0]+C1Nintervalo_160[1]))
		arquivo361.write("\n")

		arquivo371.write(str(e))
		arquivo371.write("\t")
		arquivo371.write(str(C1Nintervalo_200[0]))
		arquivo371.write("\t")
		arquivo371.write(str(C1Nintervalo_200[0]-C1Nintervalo_200[1]))
		arquivo371.write("\t")
		arquivo371.write(str(C1Nintervalo_200[0]+C1Nintervalo_200[1]))
		arquivo371.write("\n")


		arquivo381.write(str(e))
		arquivo381.write("\t")
		arquivo381.write(str(C1Nintervalo_400[0]))
		arquivo381.write("\t")
		arquivo381.write(str(C1Nintervalo_400[0]-C1Nintervalo_400[1]))
		arquivo381.write("\t")
		arquivo381.write(str(C1Nintervalo_400[0]+C1Nintervalo_400[1]))
		arquivo381.write("\n")


		arquivo312.write(str(e))
		arquivo312.write("\t")
		arquivo312.write(str(C2Nintervalo[0]))
		arquivo312.write("\t")
		arquivo312.write(str(C2Nintervalo[0]-C2Nintervalo[1]))
		arquivo312.write("\t")
		arquivo312.write(str(C2Nintervalo[0]+C2Nintervalo[1]))
		arquivo312.write("\n")

		arquivo322.write(str(e))
		arquivo322.write("\t")
		arquivo322.write(str(C2Nintervalo_10[0]))
		arquivo322.write("\t")
		arquivo322.write(str(C2Nintervalo_10[0]-C2Nintervalo_10[1]))
		arquivo322.write("\t")
		arquivo322.write(str(C2Nintervalo_10[0]+C2Nintervalo_10[1]))
		arquivo322.write("\n")

		arquivo332.write(str(e))
		arquivo332.write("\t")
		arquivo332.write(str(C2Nintervalo_20[0]))
		arquivo332.write("\t")
		arquivo332.write(str(C2Nintervalo_20[0]-C2Nintervalo_20[1]))
		arquivo332.write("\t")
		arquivo332.write(str(C2Nintervalo_20[0]+C2Nintervalo_20[1]))
		arquivo332.write("\n")

		arquivo342.write(str(e))
		arquivo342.write("\t")
		arquivo342.write(str(C2Nintervalo_40[0]))
		arquivo342.write("\t")
		arquivo342.write(str(C2Nintervalo_40[0]-C2Nintervalo_40[1]))
		arquivo342.write("\t")
		arquivo342.write(str(C2Nintervalo_40[0]+C2Nintervalo_40[1]))
		arquivo342.write("\n")

		arquivo352.write(str(e))
		arquivo352.write("\t")
		arquivo352.write(str(C2Nintervalo_80[0]))
		arquivo352.write("\t")
		arquivo352.write(str(C2Nintervalo_80[0]-C2Nintervalo_80[1]))
		arquivo352.write("\t")
		arquivo352.write(str(C2Nintervalo_80[0]+C2Nintervalo_80[1]))
		arquivo352.write("\n")

		arquivo362.write(str(e))
		arquivo362.write("\t")
		arquivo362.write(str(C2Nintervalo_160[0]))
		arquivo362.write("\t")
		arquivo362.write(str(C2Nintervalo_160[0]-C2Nintervalo_160[1]))
		arquivo362.write("\t")
		arquivo362.write(str(C2Nintervalo_160[0]+C2Nintervalo_160[1]))
		arquivo362.write("\n")

		arquivo372.write(str(e))
		arquivo372.write("\t")
		arquivo372.write(str(C2Nintervalo_200[0]))
		arquivo372.write("\t")
		arquivo372.write(str(C2Nintervalo_200[0]-C2Nintervalo_200[1]))
		arquivo372.write("\t")
		arquivo372.write(str(C2Nintervalo_200[0]+C2Nintervalo_200[1]))
		arquivo372.write("\n")


		arquivo382.write(str(e))
		arquivo382.write("\t")
		arquivo382.write(str(C2Nintervalo_400[0]))
		arquivo382.write("\t")
		arquivo382.write(str(C2Nintervalo_400[0]-C2Nintervalo_400[1]))
		arquivo382.write("\t")
		arquivo382.write(str(C2Nintervalo_400[0]+C2Nintervalo_400[1]))
		arquivo382.write("\n")




		arquivo313.write(str(e))
		arquivo313.write("\t")
		arquivo313.write(str(C3Nintervalo[0]))
		arquivo313.write("\t")
		arquivo313.write(str(C3Nintervalo[0]-C3Nintervalo[1]))
		arquivo313.write("\t")
		arquivo313.write(str(C3Nintervalo[0]+C3Nintervalo[1]))
		arquivo313.write("\n")

		arquivo323.write(str(e))
		arquivo323.write("\t")
		arquivo323.write(str(C3Nintervalo_10[0]))
		arquivo323.write("\t")
		arquivo323.write(str(C3Nintervalo_10[0]-C3Nintervalo_10[1]))
		arquivo323.write("\t")
		arquivo323.write(str(C3Nintervalo_10[0]+C3Nintervalo_10[1]))
		arquivo323.write("\n")

		arquivo333.write(str(e))
		arquivo333.write("\t")
		arquivo333.write(str(C3Nintervalo_20[0]))
		arquivo333.write("\t")
		arquivo333.write(str(C3Nintervalo_20[0]-C3Nintervalo_20[1]))
		arquivo333.write("\t")
		arquivo333.write(str(C3Nintervalo_20[0]+C3Nintervalo_20[1]))
		arquivo333.write("\n")

		arquivo343.write(str(e))
		arquivo343.write("\t")
		arquivo343.write(str(C3Nintervalo_40[0]))
		arquivo343.write("\t")
		arquivo343.write(str(C3Nintervalo_40[0]-C3Nintervalo_40[1]))
		arquivo343.write("\t")
		arquivo343.write(str(C3Nintervalo_40[0]+C3Nintervalo_40[1]))
		arquivo343.write("\n")

		arquivo353.write(str(e))
		arquivo353.write("\t")
		arquivo353.write(str(C3Nintervalo_80[0]))
		arquivo353.write("\t")
		arquivo353.write(str(C3Nintervalo_80[0]-C3Nintervalo_80[1]))
		arquivo353.write("\t")
		arquivo353.write(str(C3Nintervalo_80[0]+C3Nintervalo_80[1]))
		arquivo353.write("\n")

		arquivo363.write(str(e))
		arquivo363.write("\t")
		arquivo363.write(str(C3Nintervalo_160[0]))
		arquivo363.write("\t")
		arquivo363.write(str(C3Nintervalo_160[0]-C3Nintervalo_160[1]))
		arquivo363.write("\t")
		arquivo363.write(str(C3Nintervalo_160[0]+C3Nintervalo_160[1]))
		arquivo363.write("\n")

		arquivo373.write(str(e))
		arquivo373.write("\t")
		arquivo373.write(str(C3Nintervalo_200[0]))
		arquivo373.write("\t")
		arquivo373.write(str(C3Nintervalo_200[0]-C3Nintervalo_200[1]))
		arquivo373.write("\t")
		arquivo373.write(str(C3Nintervalo_200[0]+C3Nintervalo_200[1]))
		arquivo373.write("\n")


		arquivo383.write(str(e))
		arquivo383.write("\t")
		arquivo383.write(str(C3Nintervalo_400[0]))
		arquivo383.write("\t")
		arquivo383.write(str(C3Nintervalo_400[0]-C3Nintervalo_400[1]))
		arquivo383.write("\t")
		arquivo383.write(str(C3Nintervalo_400[0]+C3Nintervalo_400[1]))
		arquivo383.write("\n")


		arquivo400.write(str(e))
		arquivo400.write("\t")
		arquivo400.write(str(Intervalo_Frag[0]))
		arquivo400.write("\t")
		arquivo400.write(str(Intervalo_Frag[0]-Intervalo_Frag[1]))
		arquivo400.write("\t")
		arquivo400.write(str(Intervalo_Frag[0]+Intervalo_Frag[1]))
		arquivo400.write("\n")


		arquivo500.write(str(e))
		arquivo500.write("\t")
		arquivo500.write(str(Intervalo_Eal[0]))
		arquivo500.write("\t")
		arquivo500.write(str(Intervalo_Eal[0]-Intervalo_Eal[1]))
		arquivo500.write("\t")
		arquivo500.write(str(Intervalo_Eal[0]+Intervalo_Eal[1]))
		arquivo500.write("\n")

		arquivo600.write(str(e))
		arquivo600.write("\t")
		arquivo600.write(str(Intervalo_Frag_p[0]))
		arquivo600.write("\t")
		arquivo600.write(str(Intervalo_Frag_p[0]-Intervalo_Frag_p[1]))
		arquivo600.write("\t")
		arquivo600.write(str(Intervalo_Frag_p[0]+Intervalo_Frag_p[1]))
		arquivo600.write("\n")


		arquivo700.write(str(e))
		arquivo700.write("\t")
		arquivo700.write(str(Intervalo_Eal_p[0]))
		arquivo700.write("\t")
		arquivo700.write(str(Intervalo_Eal_p[0]-Intervalo_Eal_p[1]))
		arquivo700.write("\t")
		arquivo700.write(str(Intervalo_Eal_p[0]+Intervalo_Eal_p[1]))
		arquivo700.write("\n")














	
	arquivo1.close()
	arquivo2.close()
	arquivo3.close()
	arquivo4.close()
	arquivo5.close()
	arquivo6.close()
	arquivo7.close()
	arquivo8.close()
	arquivo10.close()
	arquivo11.close()
	arquivo12.close()
	arquivo13.close()
	arquivo14.close()
	arquivo15.close()
	arquivo16.close()
	arquivo17.close()
	arquivo18.close()
	arquivo19.close()
	arquivo20.close()
	arquivo21.close()
	arquivo22.close()
	arquivo23.close()
	arquivo24.close()
	arquivo25.close()
	arquivo26.close()


	arquivo311.close()
	arquivo321.close()
	arquivo331.close()
	arquivo341.close()
	arquivo351.close()
	arquivo361.close()
	arquivo371.close()
	arquivo381.close()

	arquivo312.close()
	arquivo322.close()
	arquivo332.close()
	arquivo342.close()
	arquivo352.close()
	arquivo362.close()
	arquivo372.close()
	arquivo382.close()

	arquivo313.close()
	arquivo323.close()
	arquivo333.close()
	arquivo343.close()
	arquivo353.close()
	arquivo363.close()
	arquivo373.close()
	arquivo383.close()

	arquivo400.close()
	arquivo500.close()

	arquivo600.close()
	arquivo700.close()

	#acrescentei prints
	print("Requisicoes bloqueadas e totais na classe 1")	
	print("bloqueadas", simulador.NumReqBlocked_classe1, "de", simulador.NumReq_classe1)
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))
