import time

import numpy as np
import pandas as pd
from ca1_model import CA1
from ca1_functions import init_activeCA1, addClustLocs, genRandomLocs, add_syns
from sim_functions import sim_PlaceInput
import saveClass as sc
from neuron import h
import matplotlib.pyplot as plt
from tqdm import tqdm

# Data saving object
data = sc.emptyObject()
exec(open("./sim_functions.py").read())

# INITIALIZE model
model = CA1()
init_activeCA1(model)

# GENERATE EXCITATORY synapse locations
Elocs, ind_clust, clDends = addClustLocs(model, nsyn=2000, Nclust=12, Ncell_per_clust=20, seed=30, midle=True, clocs=[], Lmin=60)
#  original data: clocs=[8, 13, 36, 59], seed 26

# GENERATE INHIBITORY synapse locations
Isomalocs = []
np.random.seed(1 + 10000)  # seed=1
for p in np.arange(0, 80):  # nsyn_soma=80
    Isomalocs.append([-1, 0.5])
Idendlocs = genRandomLocs(model, int(200 - 80), 1 + 10000)  # Insyn=80
np.random.shuffle(Idendlocs)
np.random.shuffle(Isomalocs)
Ilocs = Isomalocs + Idendlocs

# ADD excitatory and inhibitory synapses to the model
add_syns(model, Elocs, Ilocs)

# MODIFIY clustered excitatory synapses
for syn_id in ind_clust:
    model.ncAMPAlist[syn_id].weight[0] = 0.0010  # 1/1000 Set in nS and convert to muS
    model.ncNMDAlist[syn_id].weight[0] = 0.0012  # 1.2/1000 Set in nS and convert to muS

# # RUN simualtion
start = time.perf_counter()
e_fname = 'synaptic_input/Espikes_d10_Ne2000_Re0.5_rseed1_rep0.dat'
i_fname = 'synaptic_input/Ispikes_d10_Ni200_Ri7.4_rseed1_rep0.dat'

tstop = 10 * 1000
out_dir = 'L:/test'
sim_PlaceInput(model, Insyn=200, Irate=7.4, e_fname=e_fname, i_fname=i_fname, tstop=tstop, out_dir=out_dir,
                 elimIspike=False)
end = time.perf_counter()

print(f'Simulation time: {np.round(end-start,2)} seconds')