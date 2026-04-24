RECYCLING
========

Case description
----------------
Idealized case with recycling boundary conditions to test long-term simulation stability. Uses cyclic lateral boundaries.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Idealized cases
   Grid type, Cartesian
   Horizontal resolution, 96m
   Domain size, 200x200 grid points
   Vertical levels, 125
   Initial condition, Radiosounding (RSOU)
   Surface, Flat (FLAT)
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
- Cyclic boundary conditions in X and Y
- Tests long-term stability
- Surface flux forcing

**Technical specificities**
- Recycling mechanism for water vapor

Validation
----------------
- Long-term mass conservation

Numerical ressources
----------------
HPC: 64 processors (8x8)

References
----------------
- Recycling case development