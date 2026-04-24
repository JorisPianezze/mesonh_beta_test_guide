IBM
===

Case description
----------------
Idealized cases testing IBM (Immersed Boundary Method) for complex terrain and obstacle flows.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Idealized cases
   Grid type, Cartesian
   Horizontal resolution, Variable
   Domain size, Variable
   Vertical levels, Variable
   Initial condition, Radiosounding (RSOU)
   Surface, Complex (IBM)
   Equation system, DURRAN

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_prep_ideal_case, run_prep_ideal_case_xyz
   002_mesonh, run_mesonh_xyz

Specificities
----------------
**Scientific specificities**
- Immersed Boundary Method
- Flow past obstacles
- Complex geometry handling
- Multiple obstacles: Cylinder, Cube, Flume

**Technical specificities**
- IBM for terrain
- Object representation

Validation
----------------
- Flow patterns around obstacles

Numerical ressources
----------------
HPC: 5 nodes, 480 cores (MPI parallel)

References
----------------
- IBM development papers