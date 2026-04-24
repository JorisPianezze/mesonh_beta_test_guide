COLD BUBBLE
============

Case description
----------------
The COLD BUBBLE case simulates a density current (cold air outbreak) in the atmosphere. This is a classic test case for non-hydrostatic dynamics and validates the model ability to reproduce propagating gravity currents.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Idealized cases
   Dynamics, Non-hydrostatic
   Horizontal grid spacing, 50 m (1024x1 grid)
   Integration length, 900 s (15 minutes)
   Time step, 0.5 s
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

- Cold pool perturbation with temperature anomaly of -16.2 K
- Perturbation centered at 3000m with radius 4000x4000x2000m (x,y,z)
- Open lateral boundary conditions on x-axis, cyclic on y-axis
- No physics (DNS-like configuration)
- Resolution: 1024 x 1 x 128 grid points

**Technical specificities**

- Cartesian domain with 1024x1 horizontal points
- 128 vertical levels with 50m spacing
- Stretched vertical grid (2.5x factor above 5000m)
- Boussinesq approximation disabled

Validation
----------------
- Vertical velocity evolution (W)
- Temperature perturbation propagation
- Cloud visualization

Numerical ressources
------------------
Single CPU (1 node, 1 core)

References
----------------
- Straka, J.M., et al. (1993): Numerical simulation of a cold pool with a temperature perturbation. Mon. Wea. Rev., 121, 1490-1513.