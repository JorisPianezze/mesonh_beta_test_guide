IHOP
=====

Case description
----------------
The IHOP (International H2O Observing Phase) case simulates a moist convective boundary layer based on the IHOP field campaign. This case tests the boundary layer parameterization with realistic large-scale forcing.

Configuration
----------------
.. csv-table::
   :header: Parameter, 1D, 3D
   :widths: 30, 30, 30

   Category, HPC cases, HPC cases
   Dynamics, 3D with 1D turbulence, 3D LES
   Horizontal grid spacing, 1000 m (1x1), 50 m (256x256)
   Vertical levels, 90, 90
   Integration length, 43200 s (12 hours), 43200 s (12 hours)
   Time step, 60 s, 1 s
   Coriolis effect, enabled, enabled
   Turbulence, TKEL (1D), TKEL (3D)
   Cloud scheme, LIMA, LIMA
   Deep convection, NONE, NONE
   Shallow convection, EDKF, NONE
   Radiation, NONE, NONE

Declination
----------
.. csv-table::
   :header: Configuration, Description
   :widths: 30, 30

   IHOP/1D, Single column with 1D turbulence
   IHOP/3D, Large-eddy simulation with 3D turbulence

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_prep_ideal, run_prep_ideal_case_xyz
   002_mesonh, run_mesonh

Specificities
----------------
**Scientific specificities**

- Moist convective boundary layer
- Large-scale forcing from IHOP campaign
- Geostrophic forcing with vertical motion
- Cloud microphysics (LIMA)
- Shallow convection (EDKF for 1D)

**Technical specificities**

- 1D: single point domain
- 3D: 256x256 horizontal grid (12.8km x 12.8km)
- 90 vertical levels
- Cyclic boundary conditions for 3D
- High vertical resolution near surface

Validation
----------------
- Boundary layer height evolution
- Heat and moisture budgets
- Cloud fraction
- Vertical velocity profiles

Numerical ressources
----------------
1D: Single CPU (1 node, 1 core)
3D: 20 nodes, 2560 cores (MPI parallel)

References
----------------
- IHOP_2002 field campaign (Weckwerth et al., 2004)