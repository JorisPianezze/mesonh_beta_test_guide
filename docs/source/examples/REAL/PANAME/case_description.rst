Paris Area
=======

Case description
----------------
Real case simulation of summer conditions over Paris metropolitan area. Uses TEB (Town Energy Balance) scheme for urban canopy effects and includes nested domains at multiple resolutions.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Real cases
   Number of domains, 3
   Domain 1 resolution, 1200m
   Domain 2 resolution, 300m
   Domain 3 resolution, 100m
   Vertical levels, 50+
   Urban scheme, TEB
   Isba scheme, ISBA
   Nesting, Grid nesting with ratios

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_pgd, run_pgd1
   002_pgd2, run_pgd2
   003_pgd3, run_pgd3
   004_nest_pgd, run_nest_pgd
   005_coupling1, run_preal_xyz_1
   006_spawning12, run_spawning_xyz_1_2
   007_coupling2, run_preal_xyz
   008_spawning23, run_spawning_xyz_2_3
   009_coupling3, run_preal_xyz
   010_run, run_mesonh_xyz_mod123

Specificities
----------------
**Scientific specificities**
- Urban heat island effect
- Multi-scale nesting over Paris
- TEB urban canopy model

**Technical specificities**
- 3-level grid nesting
- 11 nodes x 1400 CPUs for run
- ECRAD radiation

Validation
----------------
- Urban heat island intensity
- Temperature forecasts

Numerical ressources
----------------
11 nodes x 128 cores = 1408 CPUs

References
----------------
- Paris urban climate observations