CHARMEX
=======

Case description
----------------
Real case simulation for the ChArMEx (Chemistry-Aerosols Mediterranean Experiment) campaign. Simulates aerosol and chemical transport in the Mediterranean basin with ORILAM aerosol model.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Real cases
   Horizontal resolution, 50km
   Vertical levels, 61
   Advection scheme (U,V), WENO_K (order 5)
   Advection scheme (scalar), PPM_01
   Temporal scheme, RK53
   Turbulence, TKEL
   Radiation, ECMW
   Cloud microphysics, ICE3
   Deep convection, KAFR
   Shallow convection, EDKF
   Chemistry, ReLACS3 with MEGAN
   Aerosols, ORILAM

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
- Mediterranean aerosol study
- Biogenic VOC emissions from MEGAN
- ORILAM aerosol model

**Technical specificities**
- Chemical solver EXQSSA
- Dry deposition Wes89
- 3-day simulation period

Validation
----------------
- Aerosol measurements
- Chemical concentrations

Numerical ressources
----------------
1 node, 4 cores (MPI parallel)

References
----------------
- ChArMEx campaign