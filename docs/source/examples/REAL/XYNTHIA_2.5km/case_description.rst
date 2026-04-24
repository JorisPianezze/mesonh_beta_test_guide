Xynthia storm
=======

Case description
----------------
Real case simulation of the Xynthia storm that hit western France in February 2010. High-resolution simulation at 2.5km grid spacing with comprehensive physics including turbulence, radiation, and cloud microphysics.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Real cases
   Horizontal resolution, 2.5km
   Vertical levels, 46
   Advection scheme (U,V), CEN4TH
   Advection scheme (scalar), PPM_01
   Temporal scheme, RKC4
   Turbulence, TKEL
   Radiation, ECMW
   Cloud microphysics, ICE3
   Deep convection, NONE
   Shallow convection, EDKF
   Surface model, ISBA
   Nesting, 1 domain

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
- Severe storm simulation with strong winds
- Coastal flooding case study
- Explicit deep convection at 2.5km resolution

**Technical specificities**
- Use of WENO5 advection for V variable
- EDKF for shallow convection
- 2-way horizontal relaxations

Validation
----------------
- Comparison with observed wind speeds
- Surface pressure validation
- Rainfall patterns

Numerical ressources
----------------
10 nodes x 32 cores = 320 CPUs

References
----------------
- Xynthia storm observations (Meteo-France)