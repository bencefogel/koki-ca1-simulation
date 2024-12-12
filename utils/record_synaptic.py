import os
import pandas as pd
import numpy as np
from neuron import h


def measure_AMPA_current(model):
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
    # Measure currents for each synapse type
    AMPA, AMPA_segments = measure_AMPA_current(model)
    NMDA, NMDA_segments = measure_NMDA_current(model)
    GABA, GABA_segments = measure_GABA_current(model)
    GABA_B, GABA_B_segments = measure_GABA_B_current(model)

    # Store the results in dictionaries
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
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # Create subdirectories for synaptic segments and currents
    segments_dir = os.path.join(output_dir, "synaptic_segments")
    currents_dir = os.path.join(output_dir, "synaptic_currents")

    os.makedirs(segments_dir, exist_ok=True)
    os.makedirs(currents_dir, exist_ok=True)

    # Iterate through each synapse type
    for synapse_type in synaptic_segments.keys():
        # Convert segments to string and save as .npy files
        segments_array = np.array(synaptic_segments[synapse_type]).astype('str')
        segments_npy_path = os.path.join(segments_dir, f"{synapse_type}_segments.npy")
        np.save(segments_npy_path, segments_array)

        # Save currents as .npy files
        currents_array = np.array(synaptic_currents[synapse_type])
        currents_npy_path = os.path.join(currents_dir, f"{synapse_type}_currents.npy")
        np.save(currents_npy_path, currents_array)

    print(f"Synaptic data saved in directory: {output_dir}")

