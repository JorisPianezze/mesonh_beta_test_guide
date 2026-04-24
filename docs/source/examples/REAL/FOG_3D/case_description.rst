FOG_3D
=======

Case description
----------------
The FOG_3D case is a real 3D fog simulation over the Paris area. This case tests radiation fog representation with detailed microphysics and urban effects.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Real cases
   Dynamics, 3D LES
   Horizontal grid spacing, 500 m
   Vertical levels, 34
   Integration length, 21600 s (6 hours)
   Time step, 5 s
   Turbulence, TKEL (3D)
   Cloud scheme, ICE3 or LIMA
   Radiation, NONE or ECMW
   Urban scheme, TEB
   Surface, ISBA

Declination
----------
.. csv-table::
   :header: Configuration, Cloud scheme, Radiation
   :widths: 30, 30, 30

   FOG_3D/ICE3, ICE3, ECMWF
   FOG_3D/LIMA_ECRAD, LIMA, ECRAD
   FOG_3D/LIMA_v22222, LIMA with 2 moments prognostic equations for all hydrometeors, ECMWF

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_pgd, run_pgd
   002_prep_real, run_prep_real_case
   003_mesonh, run_mesonh1 / run_mesonh2

Specificities
----------------
**Scientific specificities**

- 3D fog structure simulation
- Urban canopy effects (TEB)
- Cloud microphysics variations (ICE3 vs LIMA)
- Radiation fog lifecycle
- TEB-ISBA coupling

**Technical specificities**

- 500m horizontal resolution
- 34 vertical levels
- Multiple time segments

Validation
----------------
- Fog life cycle and surface expansion
- Surface temperature and wind speed

Numerical ressources
----------------
20 nodes, 200 cores (MPI parallel)

References
----------------
- Paris fog observations (Météo-France)