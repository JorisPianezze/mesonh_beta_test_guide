IBM-CUBE (Cube/Flume obstacle)
=============================

Case description
----------------
The IBM-CUBE case tests the Immersed Boundary Method for flow past cubic obstacles and urban flume configurations. This tests the IBM representation of sharp-edged obstacles.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, HPC cases
   Dynamics, 3D LES
   Horizontal grid spacing, 2-4 m
   Vertical levels, Variable
   Turbulence, TKEL (3D)
   IBM, enabled (cubes)

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_prep_ideal_case, run_prep_ideal_case_xyz
   002_mesonh, run_mesonh

Specificities
----------------
**Scientific specificities**

- Flow past cubic obstacles
- Urban canyon flows
- Edge effects and separation
- Wake reattachment

**Technical specificities**

- Cube geometry in IBM
- CUBE_FLUME_4 configuration (4-cube array)

Validation
----------------
- Pressure distribution
- Reattachment length

Numerical ressources
----------------
HPC: 5 nodes, 480 cores (MPI parallel)

References
----------------
- Auguste, F., C. Lac, V. Masson, and D. Cariolle, 2020: Large-eddy simulations with an immersed boundary method: Pollutant dispersion over urban terrain, Atmosphere, 11, 113.