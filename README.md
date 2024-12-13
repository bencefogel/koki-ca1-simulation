# CA1 Pyramidal Neuron Simulation

This repository contains code to simulate a CA1 pyramidal neuron under in vivo-like input conditions. It includes tools for modeling and saving simulation results.

## Features
The simulation saves the following variables:
- **Membrane potential** of all segments.
- **Intrinsic currents**, including passive and capacitive currents.
- **Synaptic currents**.
- **Segment information**: The code is designed to save data for each current type only if that current type is present in the corresponding segment.

## Configuration and parameters
To run the simulation, you need to configure the following parameters in `main.py`:

1. **Cluster locations**  
   Cluster locations can be set by changing the seed in line 22:
   ```python
   Elocs, ind_clust, clDends = addClustLocs(model, nsyn=2000, Nclust=12, Ncell_per_clust=20, seed=30, midle=True, clocs=[], Lmin=60)
   ```
2. **Simulation time**  
   Set the simulation duration with the parameter ```tstop```
   
3. **Output directory**  
   Specify the output directory using the parameter ```out_dir```

## Performance (for a 10 second long simulation)
- Simulation time: Approximately 30 minutes
- Output size: Approximately 23GB

## How to run
1. Configure the parameters as described above.
2. Run the main simulation script (```main.py```)
   
   
