import pandas as pd
from neuron import h, gui
import neuron
import numpy as np
import time


def simulate(model, tstop=100):
    h.CVode().active(True)
    h.CVode().atol((1e-3))

    # Record time array
    trec = h.Vector()
    trec.record(h._ref_t)

    allsec = h.allsec()

    nax_vectors = []
    nad_vectors = []
    car_vectors = []
    kdr_vectors = []
    kap_vectors = []
    kad_vectors = []
    kslow_vectors = []
    passive_vectors = []
    capacitive_vectors = []
    segments = []  # To track segments

    for sec in h.allsec():
        for seg in sec.allseg():
            segments.append(seg)

            # Na_ax
            if hasattr(seg, '_ref_ina_nax'):
                vec_nax = h.Vector()
                vec_nax.record(seg._ref_ina_nax)
                nax_vectors.append(vec_nax)

            # Na_d
            if hasattr(seg, '_ref_ina_nad'):
                vec_nad = h.Vector()
                vec_nad.record(seg._ref_ina_nad)
                nad_vectors.append(vec_nad)

            # Ca_R
            if hasattr(seg, '_ref_ica_car'):
                vec_car = h.Vector()
                vec_car.record(seg._ref_ica_car)
                car_vectors.append(vec_car)

            # K_dr
            if hasattr(seg, '_ref_ik_kdr'):
                vec_kdr = h.Vector()
                vec_kdr.record(seg._ref_ik_kdr)
                kdr_vectors.append(vec_kdr)

            # K_ap
            if hasattr(seg, '_ref_ik_kap'):
                vec_kap = h.Vector()
                vec_kap.record(seg._ref_ik_kap)
                kap_vectors.append(vec_kap)

            # K_ad
            if hasattr(seg, '_ref_ik_kad'):
                vec_kad = h.Vector()
                vec_kad.record(seg._ref_ik_kad)
                kad_vectors.append(vec_kad)

            # K_slow
            if hasattr(seg, '_ref_ik_kslow'):
                vec_kslow = h.Vector()
                vec_kslow.record(seg._ref_ik_kslow)
                kslow_vectors.append(vec_kslow)

            # passive
            if hasattr(seg, '_ref_i_pas'):
                vec_ipas = h.Vector()
                vec_ipas.record(seg._ref_i_pas)
                passive_vectors.append(vec_ipas)

            # capacitive
            if hasattr(seg, '_ref_i_cap'):
                vec_icap = h.Vector()
                vec_icap.record(seg._ref_i_cap)
                capacitive_vectors.append(vec_icap)

    h.celsius = 35
    h.finitialize(-68.3)

    neuron.run(tstop)

    inax = np.array(nax_vectors)
