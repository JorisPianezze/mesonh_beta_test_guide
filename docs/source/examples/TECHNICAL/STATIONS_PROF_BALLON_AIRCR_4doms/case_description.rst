STATIONS_PROF_BALLON_AIRCR_4doms
=======

Case description
----------------
4-domain grid-nesting case with moving objects: balloons, aircraft, stations and profilers. This real case (16 January 1998) tests the trajectory and lagrangian features of moving objects (balloons, aircraft) coupled with multi-domain grid nesting.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Technical cases
   NMODEL, 4
   XTSTEP, 10.
   XSEGLEN, 600.
   NITR, 8
   CCLOUD, KESS
   CTURB, TKEL
   CRAD, ECMW
   CDCONV, KAFR
   CSCONV, KAFR

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_pgd1, run_prep_pgd
   002_pgd2, run_prep_pgd
   003_pgd3, run_prep_pgd
   004_pgd4, run_prep_pgd
   005_nest, run_prep_nest_pgd_xyz
   006_preal1, run_arp2lfi_xyz
   007_spa_mod1_mod2, run_spawning_xyz
   008_preal2, run_preal_xyz
   009_spa_mod2_mod3, run_spawning_xyz
   010_preal3, run_preal_xyz
   011_spa_mod3_mod4, run_spawning_xyz
   012_preal4, run_preal_xyz
   013_run, run_mesonh_xyz
   014_run2, run_mesonh_xyz

Specificities
----------------
- 4 nested domains with grid ratios [1, 2, 2, 2]
- NAM_BUDGET enabled for cartesian budget output
- NAM_BALLOONS: 2 CVBALL balloons with different ascent rates
- NAM_AIRCRAFTS: 2 aircraft trajectories from CSV files
- NAM_STATIONn and NAM_PROFILERn for fixed point outputs
- Horizontal relaxation on boundaries

Validation
----------------
- Moving object trajectories and coupling with nested domains
- Budget terms computation
- Station and profiler diagnostics

Numerical ressources
----------------
Single CPU (1 node, 1 core)

References
----------------
- Lac et al. (2018) - MesoNH balloon/aircraft validation