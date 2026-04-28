COPT81
======

Case description
----------------
The COPT81 case is a two-dimensional tropical deep convection case based on the 1981 COPT (Convection Promotion Tensisphere) campaign in the Caribbean.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Idealized cases
   Dynamics, 2D non-hydrostatic
   Horizontal grid spacing, 1.25 km (320x1)
   Vertical levels, 46
   Integration length, 10800 s (3 hours)
   Time step, 5 s
   Turbulence, TKEL (3D)
   Cloud scheme, LIMA
   Deep convection, NONE
   Radiation, NONE

Declination
----------
.. csv-table::
   :header: Configuration, Cloud scheme, Description
   :widths: 30, 30, 30

   COPT81_CART, ICE3, Standard cartesian with ICE3
   COPT81_CART_LIMA, LIMA, Cartesian with LIMA
   COPT81_MASK, ICE3, Masked terrain
   COPT81_MASK_LRED, ICE3, Masked with reduced resolution

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

- 2D tropical deep convection
- Caribbean soundings
- Deep convective transport
- Cloud microphysics (ICE3 or LIMA)

**Technical specificities**

- Cartesian 2D domain (320x1)
- 46 vertical levels
- Open boundary conditions
- Masked terrain variants

Validation
----------------
- Vertical velocity profiles
- Convective available potential energy (CAPE)
- Cloud properties

Numerical ressources
----------------
Single CPU (1 node, 1 core)

References
----------------
- Chauzy, S., Chong, M., Delannoy, A., & Despiau, S. (1985). The June 22 tropical squall line observed during COPT 81 experiment: Electrical signature associated with dynamical structure and precipitation. Journal of Geophysical Research: Atmospheres, 90(D4), 6091-6098.