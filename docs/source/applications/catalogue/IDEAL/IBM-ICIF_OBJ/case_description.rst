IBM-ICIF_OBJ (Ice object)
=====================

Case description
----------------
The IBM-ICIF_OBJ case tests the Immersed Boundary Method (IBM) for representing ice crystals and aggregates in the atmosphere. This validates the IBM approach for complex ice particle geometries.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, HPC cases
   Dynamics, 3D LES
   Horizontal grid spacing, 1 m (1200x1200)
   Vertical levels, 150
   Integration length, 100 s
   Time step, 0.04 s
   Turbulence, TKEL (3D)
   Cloud scheme, NONE
   Deep convection, NONE
   Radiation, NONE
   IBM, enabled

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_prep_ideal, run_prep_ideal_case_xyz
   002_mesonh, run_mesonh

Specificities
----------------
**Scientific specificities**

- Ice crystal and aggregate representation
- IBM for complex ice geometries
- Fall velocity of ice particles
- Aerodynamic drag on irregular shapes

**Technical specificities**

- 1200x1200 horizontal grid (1.2km x 1.2km)
- 150 vertical levels
- WENO5 advection scheme
- Open boundary conditions

Validation
----------------
- Fall velocity comparison
- Particle orientation
- Drag coefficient

Numerical ressources
----------------
HPC: 15 nodes, 1600 cores (MPI parallel)

References
----------------
- IBM development papers (Coelho, 1995)
- Ice crystal studies