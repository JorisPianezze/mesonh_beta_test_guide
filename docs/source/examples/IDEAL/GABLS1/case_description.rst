GABLS1
========

Case description
----------------
The GABLS1 (GEWEX Atmospheric Boundary Layer Study) case simulates a stable boundary layer over Arctic land during winter. This case tests the model ability to reproduce nocturnal boundary layer turbulence and low-level jets.

Configuration
----------------
.. csv-table::
   :header: Parameter, 1D, 3D
   :widths: 30, 30, 30

   Category, HPC cases, HPC cases
   Dynamics, 3D with 1D turbulence, 3D LES
   Horizontal grid spacing, 2 m (1x1), 2 m (100x100)
   Integration length, 32400 s (9 hours), 32400 s (9 hours)
   Time step, 10 s, 0.2 s
   Coriolis effect, enabled, enabled
   Turbulence, TKEL (1D), TKEL (3D)
   Cloud scheme, NONE, NONE
   Radiation, NONE, NONE
   LES diagnostics, enabled, enabled

Declination
----------
.. csv-table::
   :header: Configuration, Turbulence, Description
   :widths: 30, 30, 30

   GABLS1/1D/BL89, TKEL (BL89), 1D with Blackadar length scale
   GABLS1/1D/RM17, TKEL (RM17), 1D with RM17 length scale
   GABLS1/3D, TKEL (DEAR), 3D LES

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_prep_ideal, run_prep_ideal_case
   002_mesonh, run_mesonh

Specificities
----------------
**Scientific specificities**

- Stable boundary layer with sustained cooling
- Weak surface temperature gradient (-0.25 K for first 8 hours)
- Geostrophic forcing (8 m/s)
- Low-level jet development
- Very high vertical resolution (2m near surface, stretching to 6m)
- 155 vertical levels

**Technical specificities**

- 1D: single point domain (1x1 grid), two turbulence variants (BL89, RM17)
- 3D: 100x100 horizontal grid with DEAR length scale
- ISBA surface scheme for snow/ice
- Arctic location (73°N)

Validation
----------------
- Turbulent heat flux profiles
- Temperature evolution
- Wind profile (low-level jet)
- Boundary layer height

Numerical ressources
----------------
1D: Single CPU (1 node, 1 core)
3D: 4 nodes, 256 cores (MPI parallel)

References
----------------
- GABLS1 intercomparison study (Beare et al., 2006)