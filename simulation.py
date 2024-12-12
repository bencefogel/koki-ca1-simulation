import pandas as pd
from neuron import h, gui
import neuron
import numpy as np
import time

from utils.record_intrinsic import record_intrinsic_currents, save_intrinsic_data
from utils.record_synaptic import record_synaptic_currents, save_synaptic_data


def simulate(model, tstop=100):
    h.CVode().active(True)
    h.CVode().atol((1e-3))

    # Record time array
    trec = h.Vector()
    trec.record(h._ref_t)

    intrinsic_segments, intrinsic_currents = record_intrinsic_currents()
    synaptic_segments, synaptic_currents = record_synaptic_currents(model)

    h.celsius = 35
    h.finitialize(-68.3)

    save_intrinsic_data(intrinsic_segments, intrinsic_currents, 'L:/test')
    save_synaptic_data(synaptic_segments, synaptic_currents, 'L:/test')

