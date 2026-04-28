EOLIENNE
=======

Case description
----------------
Wind turbine farm case testing parameterizations for turbine-induced wake effects and electricity production.
Uses local fast configuration (EOLIENNE_FAST) with two declinations: ALM and ADNR.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Idealized cases
   Grid type, Cartesian
   Horizontal resolution, 100m
   Domain size, 1km x 1km (10x10 grid points)
   Vertical levels, 10 levels at 100m spacing
   Initial condition, Radiosounding (RSOU)
   Equation system, DURRAN

Declinations
----------------
.. csv-table::
   :header: Declination, Description
   :widths: 30, 50

   ALM, Actuator Line Method - blade element model
   ADNR, Actuator Disk with Navier-Stokes/Resolved tip

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_prep_ideal, run_prep_ideal_xyz
   002_mesonh, run_mesonh_xyz

Specificities
----------------

**Technical specificities**
- ALM: Actuator Line Method with blade resolved model
- ADNR: Actuator Disk approach with resolved tip vortices

Validation
----------------
- Very fast test cases for debugging purpose

Numerical ressources
----------------
Local: Single CPU (1 node, 1 core)

References
----------------
- Joulin, P.-A., M. L. Mayol, V. Masson, F. Blondel, Q. Rodier, M. Cathelain, and C. Lac, The Actuator Line Method in the meteorological LES model Meso-NH to analyze the Horns Rev 1 wind farm photo case, Front. Earth Sci., 7, 350, 2020