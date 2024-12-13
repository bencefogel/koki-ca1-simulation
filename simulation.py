import pandas as pd
from neuron import h, gui
import neuron
import numpy as np
import time

from utils.record_intrinsic import record_intrinsic_currents, save_intrinsic_data
from utils.record_synaptic import record_synaptic_currents, save_synaptic_data
from utils.record_membrane_potential import record_membrane_potential, save_membrane_potential_data


def simulate(model, tstop, out_dir):
    h.CVode().active(True)
    h.CVode().atol((1e-3))

    # Record time array
    trec = h.Vector()
    trec.record(h._ref_t)

    v_segments, v = record_membrane_potential()
    intrinsic_segments, intrinsic_currents = record_intrinsic_currents()
    synaptic_segments, synaptic_currents = record_synaptic_currents(model)

    h.celsius = 35
    h.finitialize(-68.3)

    h.continuerun(tstop)

    save_membrane_potential_data(v_segments, v, out_dir)
    save_intrinsic_data(intrinsic_segments, intrinsic_currents, out_dir)
    save_synaptic_data(synaptic_segments, synaptic_currents, out_dir)
    taxis = np.array(trec)
    np.save(f'{out_dir}/taxis.npy', taxis)

