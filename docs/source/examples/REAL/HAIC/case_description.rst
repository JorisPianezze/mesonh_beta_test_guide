HAIC
=====

Case description
----------------
The HAIC (High Altitude Ice Crystals) project case simulates icing conditions at high altitude. This case focuses on accurate ice crystal representation for aircraft icing predictions.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Real cases
   Dynamics, 3D LES
   Horizontal grid spacing, 2000 m
   Vertical levels, 70
   Integration length, 36000 s (10 hours)
   Time step, 10 s
   Turbulence, TKEL (3D)
   Cloud scheme, ICE3 or LIMA
   Deep convection, NONE
   Shallow convection, EDKF
   Radiation, ECMW

Declination
----------
.. csv-table::
   :header: Configuration, Cloud scheme, Description
   :widths: 30, 30, 30

   HAIC/03_ICE3, ICE3, ICE3 microphysics
   HAIC/03_ICE3_SNOWT, ICE3, ICE3 with snowt
   HAIC/03_LIMA, LIMA, LIMA microphysics
   HAIC/03_LIMA_222222, LIMA, LIMA variant 222222
   HAIC/03_LIMA_Ice1m, LIMA, LIMA with 1-moment ice
   HAIC/03_LIMA_ICE1M_SNOWT, LIMA, LIMA with snowt

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_pgd, run_pgd
   002_prep_real, run_prep_real_case
   003_mesonh, run_mesonh

Specificities
----------------
**Scientific specificities**

- High altitude icing study
- LIMA ice microphysics
- Ice crystal simulations
- Aircraft icing predictions
- Snowt (sedimentation) variants

**Technical specificities**

- 2km horizontal resolution
- 70 vertical levels
- CEN4TH advection for winds
- Budget computations

Validation
----------------
- Icing observations
- Ice crystal concentrations
- Vertical profiles

Numerical ressources
----------------
8 nodes, 1024 cores (MPI parallel)

References
----------------
- HAIC project observations (GRTP, Météo-France)