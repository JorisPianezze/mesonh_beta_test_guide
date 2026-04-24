EOLIENNE
========

Case description
----------------
Wind turbine farm case testing parameterizations for turbine-induced wake effects and electricity production.

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

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_prep_ideal_case, run_prep_ideal_case_xyz
   002_mesonh, run_mesonh_xyz

Specificities
----------------
**Scientific specificities**
- Wind turbine parameterization
- Wake effects
- Electricity production

**Technical specificities**
- Multiple turbine layouts
- Power curve validation

Validation
----------------
- Power production
- Wake deficit

Numerical ressources
----------------
HPC: 2 nodes, 256 cores (MPI parallel)

References
----------------
- Wind energy studies