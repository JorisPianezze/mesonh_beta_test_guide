FOG_1D
======

Case description
----------------
The FOG_1D case simulates one-dimensional radiative fog with soil-atmosphere interactions using the ISBA land surface model.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Idealized cases
   Dynamics, 1D with 3D turbulence
   Horizontal grid spacing, 1000 m (1x1)
   Vertical levels, 40
   Integration length, 43200 s (12 hours)
   Time step, 60 s
   Coriolis effect, enabled
   Turbulence, TKEL (3D)
   Cloud scheme, ICE3 or LIMA
   Radiation, ECMWF or NONE
   Surface, ISBA

Declination
----------
.. csv-table::
   :header: Configuration, Cloud scheme, Radiation
   :widths: 30, 30, 30

   FOG_1D/ICE3, ICE3, ECMWF
   FOG_1D/ICE3_ECRAD, ICE3, ECRAD
   FOG_1D/LIMA, LIMA, ECMWF
   FOG_1D/LIMA_ECRAD, LIMA, ECRAD

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_prep_ideal, run_prep_ideal_case_xyz
   002_mesonh, run_mesonh_xyz

Specificities
----------------
**Scientific specificities**

- 1D radiative fog formation
- ISBA land surface coupling
- Soil moisture interactions
- Cloud phase (ICE3 or LIMA)
- Radiation interactions (ECMWF variant)

**Technical specificities**

- Single column with 3D turbulence
- 40 vertical levels
- Boussinesq disabled
- Forcing enabled

Validation
----------------
- Fog lifecycle (formation, dissipation)
- Temperature and humidity profiles
- Surface fluxes

Numerical ressources
----------------
Single CPU (1 node, 1 core)

References
----------------
- Fog modeling studies with Meso-NH