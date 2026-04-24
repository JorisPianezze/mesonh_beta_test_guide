DOUBLE_GRIDNESTING
=======

Case description
----------------
Two-domain double grid nesting coupling case. This test verifies the coupling between two grids with different horizontal resolutions, where the second domain inherits from the first one and then spawns a child domain. Tests both INIT and CPL (coupling) modes.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Technical cases
   NMODEL, 2
   XTSTEP, 100.
   XSEGLEN, 3600.
   NITR, 12
   CCLOUD, ICE3
   CTURB, TKEL
   CRAD, ECMW
   CDCONV, KAFR
   CSCONV, EDKF
   NDTRATIO(2), 2
   XWAY(2), 2.

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   SIMU1_001_pgd1, run_prep_pgd
   SIMU1_002_pgd2, run_prep_pgd
   SIMU1_003_prep_nest_pgd, run_prep_nest
   SIMU1_004_prep_real_d1, run_prep_real_case
   SIMU1_005_spawning, run_spawning
   SIMU1_006_prep_real_d2, run_prep_real_case
   SIMU1_007_run, run_mesonh
   SIMU2_001_pgd3, run_prep_pgd
   SIMU2_002_pgd4, run_prep_pgd
   SIMU2_003_prep_nest_pgd, run_prep_nest
   SIMU2_004_spawning_d2tod3_INIT, run_spawning
   SIMU2_005_prep_real_d3_INIT, run_prep_real_case
   SIMU2_006_spawning_d2tod3_CPL1, run_spawning
   SIMU2_007_prep_real_d3_CPL1, run_prep_real_case
   SIMU2_008_spawning_d4, run_spawning
   SIMU2_009_prep_real_d4, run_prep_real_case
   SIMU2_010_run, run_mesonh

Specificities
----------------
- Two simulation setups (SIMU1 and SIMU2)
- Double grid nesting: different horizontal resolutions per domain
- Tests both INIT and CPL nesting modes
- WENO-K advection scheme (5th order)
- EDKF subgrid convection scheme

Validation
----------------
- Coupling between two grids with different resolutions
- INIT vs CPL mode nesting comparison
- Mass flux and cloud coupling

Numerical ressources
----------------
Single CPU or nodes/cores (local execution)
