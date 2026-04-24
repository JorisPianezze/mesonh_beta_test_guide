ARM Cumulus
===========

Case description
----------------
The ARM Cumulus (ARMCU) case simulates a diurnal cycle of shallow cumulus convection over the ARM (Atmospheric Radiation Measurement) Southern Great Plains site. This is a classic case for testing cumulus parameterization and LES modeling of continental shallow convection. The case exists in two configurations: 1D (single column) and 3D (LES).

Configuration
----------------
.. csv-table::
   :header: Parameter, 1D (ARMCU_1D_CONDSAMP), 3D (ARMCU_LES)
   :widths: 30, 30, 30

   Category, Idealized cases, HPC cases
   Dynamics, 3D with 1D turbulence, 3D LES
   Horizontal grid spacing, 40000 m (1x1), 500 m (64x64)
   Integration length, 54000 s (15 hours), 43200 s (12 hours)
   Time step, 100 s, 2 s
   Coriolis effect, enabled, enabled
   Turbulence, TKEL (1D), TKEL (3D)
   Cloud scheme, ICE3, ICE3
   Deep convection, NONE, NONE
   Shallow convection, EDKF, NONE
   Radiation, NONE, NONE
   LES diagnostics, enabled, enabled

Declination
----------
.. csv-table::
   :header: Configuration, Turbulence, Grid
   :widths: 30, 30, 30

   ARMCU_1D_CONDSAMP, TKEL (BL89), 1x1
   ARMCU_LES/HM21, TKEL (HM21), 64x64
   ARMCU_LES/DEAR, TKEL (DEAR), 64x64

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

- Idealized forcing using time-varying surface fluxes (heat, moisture, momentum)
- Surface latent heat flux switches from positive to negative during the transition from daytime heating to nighttime cooling
- Deep large-scale forcing from ARM field campaign data
- Conditional sampling (CONDSAMP) enabled with 3 sample levels for cloud statistics
- LES diagnostics with time-averaging from 3600s to 43200s (12h daytime period)

**Technical specificities**

- 1D: Cartesian flat domain with single point (NIMAX=1, NJMAX=1), 100 vertical levels
- 3D: 64x64 horizontal grid, 100 vertical levels with 40m spacing
- Model top at 1000m
- Initialization from ARM SGP sounding (June 21, 1997)
- Cyclic boundary conditions for 3D

Validation
----------------
- Vertical profiles of mean quantities: MEAN_RC, MEAN_RR, MEAN_U, MEAN_V, MEAN_W, MEAN_THL
- Subgrid flux profiles: SBG_WTHL, SBG_WRT
- Total water and mass flux: MEAN_RT, MEAN_MF
- Cloud fraction validation at different levels

Numerical ressources
----------------
1D: Single CPU (1 node, 1 core)
3D: 2 nodes, 128 cores (MPI parallel)

References
----------------
- Brown, A.R., et al. (1999): Large-Eddy Simulation of Atmospheric Boundary Layer, BLM, 91, 271-289.
- Xu, K.M., and D.K. Araker (1995): The behavior of macrophage-like cells in small cumulus clouds. J. Atmos. Sci., 52, 2923-2942.