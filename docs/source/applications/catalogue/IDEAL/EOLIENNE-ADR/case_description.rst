EOLIENNE-ADR
=============

Case description
----------------
Wind turbine farm case using Actuator Disk with Relaxation (ADR) method for wake modeling.
HPC optimization configuration with single wind turbine at low resolution.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Idealized cases
   Grid type, Cartesian
   Horizontal resolution, Variable
   Domain size, Variable
   Vertical levels, Variable
   Initial condition, Radiosounding (RSOU)
   Equation system, DURRAN

Declinations
----------------
.. csv-table::
   :header: Declination, Description, Nodes, Cores
   :widths: 30, 40, 10, 10

   01_1WT_opti, Single wind turbine optimization, 2, 256

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   01_PREP, run_prep_ideal_case_xyz
   02_RUN_EOL, run_mesonh

Specificities
----------------
**Scientific specificities**
- Actuator Disk with Relaxation method
- Reduced computational cost approach
- Wake relaxation zone

**Technical specificities**
- Single turbine configuration
- Optimization-focused setup

Validation
----------------
- Power production
- Wake deficit comparison

Numerical ressources
----------------
HPC: 2 nodes, 256 cores (MPI parallel)

References
----------------
- ADR method publications
- Wind farm optimization studies