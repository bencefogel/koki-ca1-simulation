import numpy as np
from neuron import h
import os


def record_membrane_potential():
    """
    Records the membrane potential from all segments in all sections of the NEURON model.

    Returns:
        tuple:
            - v_segments (list): A list of segment objects where the membrane potential was recorded.
            - v (list): A list of `h.Vector` objects containing the recorded membrane potential data.
    """
    v = []
    v_segments = []

    for sec in h.allsec():
        for seg in sec.allseg():
            v_segments.append(seg)
            v.append(h.Vector().record(seg._ref_v))
    return v_segments, v


def save_membrane_potential_data(v_segments, v, output_dir):
    """
    Saves recorded membrane potential data and corresponding segment information to disk.

    Parameters:
        v_segments (list): A list of segment objects where the membrane potential was recorded.
        v (list): A list of `h.Vector` objects containing the recorded membrane potential data.
        output_dir (str): The path to the directory where the data will be saved.

    Outputs:
        - Segment information is saved as `segments.npy` in the `membrane_potential_data` subdirectory.
        - Membrane potential data is saved as `v.npy` in the same subdirectory.
    """
    os.makedirs(output_dir, exist_ok=True)

    vm_dir = os.path.join(output_dir, "membrane_potential_data")

    os.makedirs(vm_dir, exist_ok=True)

    segments_array = np.array([str(seg) for seg in v_segments])
    segments_npy_path = os.path.join(vm_dir, "segments.npy")
    np.save(segments_npy_path, segments_array)

    potential_array = np.array(v)
    potential_npy_path = os.path.join(vm_dir, f"v.npy")
    np.save(potential_npy_path, potential_array)

    print(f"Membrane potential data saved in directory: {output_dir}")

