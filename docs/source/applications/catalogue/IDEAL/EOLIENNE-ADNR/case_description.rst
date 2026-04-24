EOLIENNE-ADNR
=============

Case description
----------------
Wind turbine farm case using Actuator Disk with Navier-Stokes/Resolved (ADNR) approach.
HPC configuration with resolved tip vortices in the wake.

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
   :header: Declination, Description
   :widths: 30, 40

   01-1WT, Single wind turbine simulation
   02-1WT_and_Nest, Single turbine with nesting
   03-2WT_Pre_and_Nest, Two turbines with preprocessing and nesting

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   01_PREP, run_prep_ideal_case_xyz
   02_RUN_PERE, run_mesonh
   03_RUN_PRE, run_mesonh
   04_RUN_EOL, run_mesonh

Specificities
----------------
**Scientific specificities**
- Actuator Disk method with resolved tip vortices
- Navier-Stokes resolved wake
- Tip vortex circulation decay

**Technical specificities**
- Preprocessing step for Initialization
- Grid nesting capability
- Multiple turbine configurations

Validation
----------------
- Wake deficit comparison
- Tip vortex trajectories
- Power production

Numerical ressources
----------------
HPC: 2 nodes, 256 cores (MPI parallel)

References
----------------
- Actuator Disk modeling papers
- Tip vortex resolution studies