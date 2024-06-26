#!/usr/bin/env python
# -*- coding: utf-8 -*-

RANDOM_SEED = [50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,207,280,300,310,320,330,340,350,360,370,380,390,400]

MAX_TIME = 10000000  

ERLANG_MIN = 140

ERLANG_MAX = 220
 
ERLANG_INC = 20

REP = 16
# mudei rep de 2 para 10 e 1k para 100k, npath para 5 erlang 140a220
NUM_OF_REQUESTS = 100000

BANDWIDTH = [10,20,40,80,160,200,400]

CLASS_TYPE = [1,2,3]
#troquei por .33
CLASS_WEIGHT = [1/3, 1/3, 1/3]

TOPOLOGY = 'rnp'

HOLDING_TIME = 2.0

SLOTS = 300

SLOT_SIZE = 12.5

N_PATH = 5

PL_MAX = 9

#custos para 	BANDWIDTH =  [10,20,40,80,160,200,400]
COST_PER_LINK_CLASS_TYPE_1 = [10,20,40,80,160,200,400]
COST_PER_LINK_CLASS_TYPE_2 = [10,20,40,80,160,200,400]
COST_PER_LINK_CLASS_TYPE_3 = [10,20,40,80,160,200,400]


