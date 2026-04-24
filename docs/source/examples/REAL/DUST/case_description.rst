DUST
=======

Case description
----------------
Real case of Saharan dust episode. Uses native dust module for mineral dust aerosol simulation and transport from Saharan region.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Real cases
   Horizontal resolution, Variable
   Vertical levels, 30
   Advection scheme (U,V), WENO_K (order 5)
   Advection scheme (scalar), PPM_01
   Temporal scheme, RK53
   Turbulence, TKEL
   Radiation, ECMWF with aerosols
   Cloud microphysics, ICE3
   Deep convection, KAFR
   Dust module, Native

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
- Saharan dust transport
- 3 dust modes
- Dust sedimentation

**Technical specificities**
- Daily analysis coupling
- 5-day simulation period

Validation
----------------
- AOD measurements
- Dust concentrations

Numerical ressources
----------------
Single node configuration

References
----------------
- Saharan dust observations