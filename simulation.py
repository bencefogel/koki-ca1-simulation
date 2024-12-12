import pandas as pd
from neuron import h, gui
import neuron
import numpy as np
import time

from utils.record_intrinsic import measure_intrinsic, record_intrinsic, save_intrinsic


def simulate(model, tstop=100):
    h.CVode().active(True)
    h.CVode().atol((1e-3))

    # Record time array
    trec = h.Vector()
    trec.record(h._ref_t)

    allsec = h.allsec()

    intrinsic_segments, intrinsic_currents = record_intrinsic()

    h.celsius = 35
    h.finitialize(-68.3)

    neuron.run(tstop)

    save_intrinsic(intrinsic_segments, intrinsic_currents, 'L:/test')
