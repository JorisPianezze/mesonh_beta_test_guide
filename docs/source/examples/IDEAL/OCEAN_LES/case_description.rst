OCEAN_LES
=========

Case description
----------------
Large Eddy Simulation of the oceanic atmospheric boundary layer. Simulates marine stratocumulus with ocean coupling.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Idealized cases
   Grid type, Cartesian
   Horizontal resolution, 125m
   Domain size, 128x128 grid points
   Vertical levels, 100
   Initial condition, Idealized ocean (IDEALOCE)
   Surface, Flat (FLAT)
   Equation system, LHE
   Ocean model, LOCEAN=.TRUE.
   Boussinesq approximation, Enabled

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_prep_ideal_case, run_prep_ideal_case_xyz
   002_run1, run_mesonh_xyz
   004_run2, run_mesonh_xyz

Specificities
----------------
**Scientific specificities**
- Oceanic LES
- Marine boundary layer
- Cloud-top mixing
- Ocean coupling

**Technical specificities**
- Cyclic boundary conditions
- Thin shell approximation

Validation
----------------
- Boundary layer structure
- Cloud properties

Numerical ressources
----------------
HPC: 64 processors (8x8)

References
----------------
- Stevens et al. (1999)