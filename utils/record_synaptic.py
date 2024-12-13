import os
import pandas as pd
import numpy as np
from neuron import h


def measure_AMPA_current(model):
    """
    Measures AMPA receptor-mediated synaptic currents.

    Parameters:
        model (object): The NEURON model containing a list of AMPA synapses (`AMPAlist`).

    Returns:
        tuple:
            - AMPA (list): A list of `h.Vector` objects recording AMPA currents.
            - AMPA_segments (list): A list of segments where AMPA currents are recorded.
    """
    AMPA = []
    AMPA_segments = []

    for syn in model.AMPAlist:
        vec = h.Vector().record(syn._ref_i)
        AMPA.append(vec)
        AMPA_segments.append(syn.get_segment())
    return AMPA, AMPA_segments


def measure_NMDA_current(model):
    NMDA = []
    NMDA_segments = []

    for syn in model.NMDAlist:
        vec = h.Vector().record(syn._ref_i)
        NMDA.append(vec)
        NMDA_segments.append(syn.get_segment())
    return NMDA, NMDA_segments


def measure_GABA_current(model):
    GABA = []
    GABA_segments = []

    for syn in model.GABAlist:
        vec = h.Vector().record(syn._ref_i)
        GABA.append(vec)
        GABA_segments.append(syn.get_segment())
    return GABA, GABA_segments


def measure_GABA_B_current(model):
    GABA_B = []
    GABA_B_segments = []

    for syn in model.GABA_Blist:
        vec = h.Vector().record(syn._ref_i)
        GABA_B.append(vec)
        GABA_B_segments.append(syn.get_segment())
    return GABA_B, GABA_B_segments


def record_synaptic_currents(model):
    """
    Records synaptic currents for all synapse types (AMPA, NMDA, GABA, GABA-B).

    Parameters:
        model (object): The NEURON model containing lists of synapses (`AMPAlist`, `NMDAlist`, `GABAlist`, `GABA_Blist`).

    Returns:
        tuple:
            - synaptic_segments (dict): A dictionary where keys are synapse types and values are lists of segments.
            - synaptic_currents (dict): A dictionary where keys are synapse types and values are lists of `h.Vector` objects.
    """
    AMPA, AMPA_segments = measure_AMPA_current(model)
    NMDA, NMDA_segments = measure_NMDA_current(model)
    GABA, GABA_segments = measure_GABA_current(model)
    GABA_B, GABA_B_segments = measure_GABA_B_current(model)

    synaptic_currents = {
        'AMPA': AMPA,
        'NMDA': NMDA,
        'GABA': GABA,
        'GABA_B': GABA_B
    }

    synaptic_segments = {
        'AMPA': AMPA_segments,
        'NMDA': NMDA_segments,
        'GABA': GABA_segments,
        'GABA_B': GABA_B_segments
    }

    return synaptic_segments, synaptic_currents


def save_synaptic_data(synaptic_segments, synaptic_currents, output_dir):
    """
    Saves synaptic current data and segment information to disk.

    Parameters:
        synaptic_segments (dict): Keys are synapse types, and values are lists of segments where the synapse currents are recorded.
        synaptic_currents (dict): Keys are synapse types, and values are lists of recorded `h.Vector` objects.
        output_dir (str): Path to the directory where data will be saved.

    Outputs:
        - Segment information is saved as `.npy` files in the `synaptic_segments` subdirectory.
        - Current data is saved as `.npy` files in the `synaptic_currents` subdirectory.
    """
    os.makedirs(output_dir, exist_ok=True)

    segments_dir = os.path.join(output_dir, "synaptic_segments")
    currents_dir = os.path.join(output_dir, "synaptic_currents")

    os.makedirs(segments_dir, exist_ok=True)
    os.makedirs(currents_dir, exist_ok=True)

    for synapse_type in synaptic_segments.keys():
        segments_array = np.array(synaptic_segments[synapse_type]).astype('str')
        segments_npy_path = os.path.join(segments_dir, f"{synapse_type}_segments.npy")
        np.save(segments_npy_path, segments_array)

        currents_array = np.array(synaptic_currents[synapse_type])
        currents_npy_path = os.path.join(currents_dir, f"{synapse_type}_currents.npy")
        np.save(currents_npy_path, currents_array)

    print(f"Synaptic data saved in directory: {output_dir}")

