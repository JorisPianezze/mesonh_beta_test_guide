Reunion
=======

Case description
----------------
Idealized real case based on Reunion Island observations with topography and realistic forcing.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Idealized cases
   Grid type, Non-Cartesian (Conformal)
   Horizontal resolution, 1.5km
   Domain size, Variable
   Vertical levels, 50
   Initial condition, Constant (CSTN)
   Surface, PGD file (REUNION_PGD_1km5)
   Equation system, LHE (Hydrostatic)
   Boussinesq approximation, Disabled

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_prep_pgd, run_prep_pgd_xyz
   002_prep_ideal, run_prep_ideal_case_xyz
   003_mesonh, run_mesonh_xyz
   004_diag, run_diag_xyz

Specificities
----------------
**Scientific specificities**
- Island case with topography
- Lava shield terrain
- Convective events

**Technical specificities**
- Real PGD file preparation
- Uses PGD file with terrain

Validation
----------------
- Comparison with Reunion observations

Numerical ressources
----------------
Single CPU (1 node, 1 core)

References
----------------
- Reunion Island field campaigns