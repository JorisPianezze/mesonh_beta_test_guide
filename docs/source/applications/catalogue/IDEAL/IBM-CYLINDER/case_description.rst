IBM-CYLINDER (Cylinder obstacle)
==============================

Case description
----------------
The IBM-CYLINDER case tests the Immersed Boundary Method for flow past a circular cylinder. This is a classic test case for validation of IBM against known analytical and experimental results.

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
   IBM, enabled (cylinder)

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

- Flow past cylinder
- Von Karman vortex street
- Wake turbulence
- IBM validation

**Technical specificities**

- Cylinder geometry in IBM
- High resolution near obstacle

Validation
----------------
- Drag coefficient
- Strouhal number
- Wake velocity profiles

Numerical ressources
----------------
HPC: 5 nodes, 480 cores (MPI parallel)

References
----------------
- Auguste, F., C. Lac, V. Masson, and D. Cariolle, 2020: Large-eddy simulations with an immersed boundary method: Pollutant dispersion over urban terrain, Atmosphere, 11, 113.