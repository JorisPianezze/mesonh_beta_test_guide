IBM-MUST (Urban obstacle)
========================

Case description
----------------
The IBM-MUST case tests the Immersed Boundary Method (IBM) for flow around buildings and urban canopies. This case simulates the MUST (Marlborough Urban Siting Test) facility with building arrays.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, HPC cases
   Dynamics, 3D LES
   Horizontal grid spacing, 4 m
   Vertical levels, 80
   Turbulence, TKEL (3D)
   IBM, enabled (buildings)

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_prep_ideal_case, run_prep_ideal_case_xyz
   002_mesonh, run_mesonh

Specificities
----------------
**Scientific specificities**

- Urban canopy flow simulation
- Building array representation with IBM
- Wake and cavity flow dynamics
- Turbulent coherent structures

**Technical specificities**

- High resolution grid (4m)
- MUST building configuration
- 80 vertical levels

Validation
----------------
- Velocity profiles in wake
- Turbulence statistics

Numerical ressources
----------------
HPC: 15 nodes, 1600 cores (MPI parallel)

References
----------------
- Auguste, F., C. Lac, V. Masson, and D. Cariolle, 2020: Large-eddy simulations with an immersed boundary method: Pollutant dispersion over urban terrain, Atmosphere, 11, 113.