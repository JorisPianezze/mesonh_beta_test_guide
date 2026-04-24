KMAP
=======

Case description
----------------
Real case simulation of the Korean Air Pollution project. Multi-domain nested configuration with grid nesting and WENO advection scheme for high accuracy tracer transport.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Real cases
   Number of domains, 3
   Vertical levels, 50
   Advection scheme (U,V), WENO_K (order 5)
   Advection scheme (scalar), PPM_01
   Temporal scheme, RK53
   Turbulence, TKEL
   Radiation, ECRA
   Cloud microphysics, ICE3
   Deep convection, KAFR

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_pgd, run_pgd
   002_prep_real, run_prep_real_case
   003_spawning, run_spa_real
   004_run, run_mesonh

Specificities
----------------
**Scientific specificities**
- Air pollution study over Korea
- Multi-scale nesting
- WENO high-order advection

**Technical specificities**
   - 3-domain grid nesting
   - Thin shell correction

Validation
----------------
- Pollutant concentrations
- Wind patterns

Numerical ressources
----------------
4 nodes, 64 cores (MPI parallel)

References
----------------
- KMAP campaign data