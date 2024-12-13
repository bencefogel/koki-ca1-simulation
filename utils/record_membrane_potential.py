import numpy as np
from neuron import h
import os


def record_membrane_potential():
    v = []
    v_segments = []

    for sec in h.allsec():
        for seg in sec.allseg():
            v_segments.append(seg)
            v.append(h.Vector().record(seg._ref_v))
    return v_segments, v


def save_membrane_potential_data(v_segments, v, output_dir):
    os.makedirs(output_dir, exist_ok=True)

    vm_dir = os.path.join(output_dir, "membrane_potential_data")

    os.makedirs(vm_dir, exist_ok=True)

    # Save segments information
    segments_array = np.array([str(seg) for seg in v_segments])
    segments_npy_path = os.path.join(vm_dir, "segments.npy")
    np.save(segments_npy_path, segments_array)


    potential_array = np.array(v)
    potential_npy_path = os.path.join(vm_dir, f"v.npy")
    np.save(potential_npy_path, potential_array)

    print(f"Membrane potential data saved in directory: {output_dir}")

