2Drelief
============

Case description
----------------
The 2Drelief case simulates the interaction between atmospheric flow and a 2D bell-shaped mountain. This is a classic test case for orographic flow dynamics and validates the model ability to reproduce mountain waves and gravity wave drag.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Idealized cases
   Dynamics, Non-hydrostatic
   Horizontal grid spacing, 5000 m (256x1 grid)
   Integration length, 10800 s (3 hours)
   Time step, 60 s
   Coriolis effect, disabled
   Turbulence, TKEL (3D)
   Cloud scheme, NONE
   Deep convection, NONE
   Radiation, NONE

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_prep_ideal, run_prep_ideal_case
   002_mesonh, run_mesonh

Specificities
----------------
**Scientific specificities**

- 2D bell-shaped mountain (Gaussian hill) with height 500m
- Horizontal domain: 256 points (10km half-width bell)
- 48 vertical levels from 0 to 5000m
- Open western boundary, cyclic eastern boundary
- 10m/s westerly flow

**Technical specificities**

- Stretched vertical grid (10m near surface, 500m near model top)
- Boussinesq disabled for full compressible dynamics
- Damping layer at model top (XALKTOP=0.005)
- Horizontal relaxation at boundaries

Validation
----------------
- Vertical velocity perturbation
- Pressure perturbation
- Mountain wave visualization

Numerical ressources
------------------
Single CPU (1 node, 1 core)

References
----------------
- Gallus, W.A., and R.A. Ahmadov (2021): Sensitivity of simulated 24-h forecasts to horizontal resolution in the US. Atmosphere, 12, 1686.