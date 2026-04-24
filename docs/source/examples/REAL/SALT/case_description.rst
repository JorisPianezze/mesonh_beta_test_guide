Sea Salt Aerosols
=======

Case description
----------------
Real case simulation of sea salt aerosols in a cyclone. Uses LIMA microphysics scheme to simulate sea salt emission and transport in marine atmospheric conditions.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Real cases
   Horizontal resolution, High resolution
   Vertical levels, 50
   Chemistry, LIMA enabled
   Aerosols, Sea salt

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_pgd, run_pgd
   002_prep_real, run_prep_real_case
   003_run, run_mesonh

Specificities
----------------
**Scientific specificities**
- Sea salt aerosol simulation
- Marine boundary layer
- LIMA cloud microphysics

**Technical specificities**
- MESONH input format
- Sea salt aerosol emissions

Validation
----------------
- Aerosol concentrations
- Comparison with observations

Numerical ressources
----------------
1 node, 32 cores (MPI parallel)

References
----------------
- Sea salt measurement campaigns