Cyclone
=======

Case description
----------------
Real case simulation of a tropical cyclone. Uses ocean coupling and sea surface flux parameterizations for accurate cyclone development simulation.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Real cases
   Horizontal resolution, 4km
   Vertical levels, 50+
   Advection scheme (U,V), CEN4TH
   Advection scheme (scalar), PPM_01
   Temporal scheme, LEFR
   Turbulence, TKEL
   Radiation, ECMW
   Cloud microphysics, ICE3
   Ocean flux, ECUME
   Sea surface, Prognostic SST

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
- Tropical cyclone simulation
- Ocean coupling
- Sea surface flux parameterization

**Technical specificities**
- Prognostic SST
- Mercator ocean coupling

Validation
----------------
- Track forecast
- Intensity comparisons

Numerical ressources
----------------
24 nodes, 768 cores (MPI parallel)

References
----------------
- Tropical cyclone observations