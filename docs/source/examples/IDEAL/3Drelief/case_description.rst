3Drelief
============

Case description
----------------
The 3Drelief case simulates the interaction between atmospheric flow and a 3D bell-shaped mountain. This is a classic test case for orographic flow dynamics in 3D and validates the model ability to reproduce three-dimensional mountain waves and flow splitting.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Idealized cases
   Dynamics, Non-hydrostatic
   Horizontal grid spacing, 2000 m (128x96 grid)
   Integration length, 10000 s (2.8 hours)
   Time step, 80 s
   Coriolis effect, disabled
   Turbulence, NONE
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

- 3D bell-shaped mountain (Gaussian hill) with height 1000m
- Horizontal domain: 128x96 points (10km half-width)
- 72 vertical levels with 250m spacing
- Open boundary conditions on all sides
- Boussinesq enabled (LHE equations)
- 10 m/s westerly flow

**Technical specificities**

- Nested grid (9x49 inner points for mountain)
- Horizontal relaxation at boundaries (6x3 rim)
- Damping layer at model top
- No radiation, cloud or turbulence schemes (DNS mode)

Validation
----------------
- Vertical velocity field
- Wave breaking patterns
- Flow splitting visualization

Numerical ressources
------------------
Single CPU (1 node, 1 core)

References
----------------
- Gallus, W.A., and R.A. Ahmadov (2021): Sensitivity of simulated 24-h forecasts to horizontal resolution in the US. Atmosphere, 12, 1686.