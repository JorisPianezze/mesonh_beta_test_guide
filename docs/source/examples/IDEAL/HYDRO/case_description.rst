HYDRO
=====

Case description
----------------
Two-dimensional hydrostatic mountain wave case with Bell-shaped topography. Tests orographic forcing.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Idealized cases
   Grid type, Cartesian
   Horizontal resolution, 2km
   Domain size, 90x1 grid points
   Vertical levels, 121
   Initial condition, Constant (CSTN)
   Surface, Bell (BELL)
   Equation system, DURRAN

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_prep_ideal, run_prep_ideal_case_xyz
   002_mesonh, run_mesonh_xyz

Specificities
----------------
**Scientific specificities**
- Mountain wave simulation
- Hydrostatic flow
- Orographic drag

**Technical specificities**
- 2D configuration with Bell topography
- Thin shell approximation

Validation
----------------
- Wave structure
- Vertical velocity

Numerical ressources
----------------
Single CPU (1 node, 1 core)

References
----------------
- Mountain wave theory