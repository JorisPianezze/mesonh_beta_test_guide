ICCARE Corsica
=======

Case description
----------------
Real case simulation for the ICCARE campaign over Corsica. Nested domain configuration simulating Corsican orographic effects on atmospheric flow.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Real cases
   Number of domains, 2
   Nesting, Grid nesting
   Vertical levels, 50+
   Turbulence, TKEL
   Cloud microphysics, ICE3

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_pgd, run_pgd
   002_prep_real, run_prep_real_case_dom1
   003_spawning, run_spawning
   004_prep_real_dom2, run_prep_real_case_dom2
   005_run, run_mesonh

Specificities
----------------
**Scientific specificities**
- Mountain/island effect study
- Corsica orographic flows
- Sea-breeze simulations

**Technical specificities**
- 2-domain grid nesting
- CAM data for chemistry

Validation
----------------
- Surface observations
- Radar measurements

Numerical ressources
----------------
20 nodes, 1920 cores (MPI parallel)

References
----------------
- ICCARE campaign