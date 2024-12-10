import pandas as pd
from neuron import h, gui
import neuron
import numpy as np
import time


def simulate(model, t_stop=100, progress_interval=100):
    h.CVode().active(True)
    h.CVode().atol((1e-3))

    # Record time array
    trec = h.Vector()
    trec.record(h._ref_t)

    h.celsius = 35  # model.CELSIUS
    h.finitialize(-68.3)  # model.v_init




