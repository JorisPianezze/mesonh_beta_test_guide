LIMA_2D
========

Case description
----------------
The LIMA_2D case is a two-dimensional test using the LIMA (Liquid Ice Multiple Aerosol) microphysics scheme. It tests warm cloud and ice-phase interactions with different aerosol activation configurations.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Idealized cases
   Dynamics, 2D non-hydrostatic
   Horizontal grid spacing, 5000 m (180x1)
   Vertical levels, 50
   Integration length, 7200 s (2 hours)
   Time step, 10 s
   Turbulence, NONE
   Cloud scheme, LIMA
   Radiation, NONE
   Surface, Schafran

Declination
----------
.. csv-table::
   :header: Configuration, Description
   :widths: 30, 30

   LIMA_2D/NOLADJ, LIMA without saturation adjustment
   LIMA_2D/LSPRO, LIMA with sigma prognostic

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

- LIMA microphysics with 2-moment scheme
- Aerosol activation/deposition
- Ice-phase interactions

**Technical specificities**

- 2D configuration (NJMAX=1)
- 50 vertical levels
- Single column setup

Validation
----------------
- Cloud droplet spectra
- Precipitation development
- Aerosol budgets

Numerical ressources
----------------
Single CPU (1 node, 1 core)

References
----------------
- LIMA scheme development (Richard et al., 2001)