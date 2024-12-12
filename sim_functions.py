import numpy as np

import simulation
from numpy import loadtxt
from neuron import h

def sim_PlaceInput(model, Insyn, Irate, e_fname, i_fname, tstop, elimIspike=0): #sim_time in msec
    eitimes = readTrain(e_fname, i_fname)

    if ((Insyn > 0) & (Irate > 0)) :
        etimes = eitimes[0]
        itimes = eitimes[1]
        print(len(etimes[:,0]), 'E and ',  len(itimes[:,0]),  'I spikes read from file')
        if (elimIspike > 0):
            N_ispikes = len(itimes)
            i_index = np.sort(np.random.choice(N_ispikes, int(round((1-elimIspike) * N_ispikes)), replace=False))
            itimes = itimes[i_index]

    data.itimes = itimes
    data.etimes = etimes

    # Run
    fih = simulation.h.FInitializeHandler(1, initSpikes)
    simulation.simulate(model, tstop)


def initSpikes():
    if (len(data.etimes)>0):
        for s in data.etimes:
            model.ncAMPAlist[int(s[0])].event(float(s[1]))
            model.ncNMDAlist[int(s[0])].event(float(s[1]))

    if (len(data.itimes)>0):
        for s in data.itimes:
            model.ncGABAlist[int(s[0])].event(float(s[1]))
            model.ncGABA_Blist[int(s[0])].event(float(s[1]))

def readTrain(e_fname, i_fname):
    fname = e_fname
    Etimes = loadtxt(fname, comments="#", delimiter=" ", unpack=False)

    fname = i_fname
    Itimes = loadtxt(fname, comments="#", delimiter=" ", unpack=False)

    times = [Etimes, Itimes]

    return times

