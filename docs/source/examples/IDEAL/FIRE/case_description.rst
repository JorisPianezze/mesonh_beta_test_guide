FIRE Stratocumulus
=================

Case description
----------------
The FIRE (First ISCCP Regional Experiment) case simulates marine stratocumulus clouds off the coast of California. This is a classic case for testing cloud-radiation interactions and LES modeling of marine boundary layer clouds. The case exists in two configurations: 1D (single column) and 3D (LES).

Configuration
----------------
.. csv-table::
   :header: Parameter, 1D (FIRE_1D), 3D (FIRE)
   :widths: 30, 30, 30

   Category, Idealized cases, HPC cases
   Dynamics, 3D with 1D turbulence, 3D LES
   Horizontal grid spacing, 2500 m (1x1), 50 m (50x50)
   Integration length, 90000 s (25 hours), 90000 s (25 hours)
   Time step, 120 s, 1 s
   Coriolis effect, enabled, enabled
   Turbulence, TKEL (1D), TKEL (3D)
   Cloud scheme, KHKO, KHKO
   Deep convection, NONE, NONE
   Radiation, ECMWF, ECMW
   LES diagnostics, enabled, enabled

Declination
----------
.. csv-table::
   :header: Configuration, Cloud scheme, Radiation
   :widths: 30, 30, 30

   FIRE_1D/KHKO, KHKO, ECMWF
   FIRE_1D/KHKO_MALA, KHKO, MALA
   FIRE_1D/LIMA_ECRAD, LIMA, ECRAD
   FIRE_1D/LIMA_MALA, LIMA, MALA
   FIRE/CEN4TH_RKC4, KHKO, ECMW
   FIRE/CEN4TH_LEFR, KHKO, ECMW
   FIRE/CEN4TH_RKC4_LIMA_ECRAD, LIMA, ECRAD
   FIRE/WENO5, KHKO, ECMW

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_prep_ideal, run_prep_ideal_case_xyz / run_prep_ideal
   002_mesonh, run_mesonh_xyz / run_mesonh

Specificities
----------------
**Scientific specificities**

- Marine stratocumulus layer with cloud-top radiative cooling
- Sea surface temperature: 289 K prescribed
- July 14, 1987 initialization (25200s UTC)
- Geostrophic forcing with vertical motion
- Cloud-radiation interactions
- Different turbulence length scales (BL89 for 1D, DEAR for 3D)

**Technical specificities**

- 1D: single point domain with 120 vertical levels
- 3D: 50x50 horizontal grid (2.5km x 2.5km domain)
- Cyclic boundary conditions for 3D
- Initial perturbation (0.1 m/s vertical for 3D)

Validation
----------------
- Cloud fraction evolution
- Liquid water path
- Radiative fluxes
- Turbulent fluxes

Numerical ressources
----------------
1D: Single CPU (1 node, 1 core)
3D: 4 nodes, 256 cores (MPI parallel)

References
----------------
- Randall, D.A., et al. (1996): Intercomparison of stratocumulus cloud fields during FIRE. Mon. Wea. Rev., 124, 137-156.