EOLIENNE-ALM
=============

Case description
----------------
Wind turbine farm case using Actuator Line Method (ALM) - blade element approach for wake modeling.
HPC configuration with multiple declinations at different resolutions and nesting.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Idealized cases
   Grid type, Cartesian
   Horizontal resolution, Variable (100m to 2500m)
   Domain size, Variable
   Vertical levels, Variable (10-64 levels)
   Initial condition, Radiosounding (RSOU)
   Equation system, DURRAN

Declinations
----------------
.. csv-table::
   :header: Declination, Description, Nodes, Cores
   :widths: 30, 40, 10, 10

   01_1WT_low_res, Single wind turbine low resolution, 4, 512
   02_1WT_high_res, Single wind turbine high resolution, 32, 2048
   03_2WT_and_Nest, Two wind turbines with nesting, 2, 256

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
- Actuator Line Method (ALM) for blade-resolved wake modeling
- Tip loss correction
- Dynamic wake meandering

**Technical specificities**
- Multiple resolution levels (100m-2500m)
- Grid nesting capability
- Parallel file handling

Validation
----------------
- Power production against reference
- Wake deficit profiles
- Tip vortex visualization

Numerical ressources
----------------
HPC: 2 nodes, 256 cores to 32 nodes, 2048 cores (MPI parallel)

References
----------------
Joulin, P.-A., M. L. Mayol, V. Masson, F. Blondel, Q. Rodier, M. Cathelain, and C. Lac, The Actuator Line Method in the meteorological LES model Meso-NH to analyze the Horns Rev 1 wind farm photo case, Front. Earth Sci., 7, 350, 2020