BLAZE
=====

Case description
----------------
The BLAZE case tests the fire spread parameterization with coupled atmosphere-fire interactions. The case exists in two configurations: local (flat terrain) and HPC (with orography).

Configuration
----------------
.. csv-table::
   :header: Parameter, Local (BLAZE), HPC (BLAZE_OROG)
   :widths: 30, 30, 30

   Category, Idealized cases, HPC cases
   Dynamics, Non-hydrostatic, Non-hydrostatic
   Horizontal grid spacing, 25 m, 25 m
   Domain size, 100x50, 100x50
   Vertical levels, 30, 30
   Integration length, 600 s, 600 s
   Time step, 1 s, 1 s
   Turbulence, NONE, NONE
   Cloud scheme, NONE, NONE
   Fire spread, enabled, enabled

Declination
----------
.. csv-table::
   :header: Configuration, Surface, Description
   :widths: 30, 30, 30

   BLAZE/01_flat_2WC, ISBA, Flat terrain with 2-way coupling
   BLAZE/02_flat_A2F, ISBA, Flat terrain with atmosphere-to-fire coupling
   BLAZE/03_flat_F2A, ISBA, Flat terrain with fire-to-atmosphere coupling
   BLAZE_OROG, ISBA, Orographic terrain with coupling

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_prep_ideal_case, run_prep / run_prep_ideal_case
   002_mesonh, run_test / run_mesonh

Specificities
----------------
**Scientific specificities**

- Fire spread model with vegetation burning
- Atmosphere-fire coupling (different coupling schemes)
- ISBA land surface model
- Fire front propagation validation

**Technical specificities**

- 25m horizontal resolution
- 30 vertical levels with stretching
- Open boundary conditions
- Multiple fire coupling variants (2WC, A2F, F2A)
- Fuel map input for fire propagation

Validation
----------------
- Fire front propagation
- Heat release rates
- Velocity fields

Numerical ressources
----------------
Local: Single CPU (1 node, 1 core)
HPC: 1 node, 128 cores (MPI parallel)

References
----------------
- Fire modeling studies with Meso-NH