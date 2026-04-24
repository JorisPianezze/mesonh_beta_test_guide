STERAO
======

Case description
----------------
Idealized deep convection case over the western tropical Atlantic with 1km horizontal resolution. Simulates the Stratosphere-Troposphere exchange in an Oceanic Region (STE/RAO).

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Idealized cases
   Grid type, Cartesian
   Horizontal resolution, 1km
   Domain size, 160x160 grid points
   Vertical levels, 50
   Initial condition, Radiosounding (RSOU)
   Surface, Flat (FLAT)
   Equation system, LHE
   Boussinesq approximation, Disabled
   Perturbation, Thermal (TH) with 3K amplitude

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_prep_ideal, run_prep_ideal_case_xyz
   002_run, run_mesonh_xyz

Specificities
----------------
**Scientific specificities**
- Deep convection in tropical atmosphere
- Stratosphere-troposphere exchange
- Clear-sky conditions

**Technical specificities**
- High vertical resolution in upper levels

Validation
----------------
- Vertical profiles comparison with observations

Numerical ressources
----------------
HPC: 4 nodes, 192 cores (MPI parallel)

References
----------------
- Various Atlantic campaigns