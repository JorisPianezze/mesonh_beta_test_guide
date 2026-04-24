TROCCINOX
=======

Case description
----------------
Real case模拟热带气旋与nox排放物的化学反应,模拟2005年2月的气旋Troc案例。该案例用于研究对流层化学物质与气旋的相互作用。

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Real cases
   Horizontal resolution, 30km
   Vertical levels, 70
   Advection scheme (U,V), CEN4TH
   Advection scheme (scalar), PPM_01
   Temporal scheme, RKC4
   Turbulence, TKEL
   Radiation, ECMW
   Cloud microphysics, ICE3
   Deep convection, KAFR
   Shallow convection, NONE
   Chemistry, LINOX enabled

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
- Cyclone case study with chemistry
- Chemical coupling with LINOX
- ECMWF analysis data for initialization

**Technical specificities**
- 3-hourly coupling files
- Multiple time segments
- Vertical relaxation at top

Validation
----------------
- Ozone and NOX comparisons
- Meteorological validation

Numerical ressources
----------------
1 node x 128 cores

References
----------------
- TROCCINOX campaign data