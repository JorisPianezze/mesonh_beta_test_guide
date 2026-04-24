SUPERCELL
==========

Case description
----------------
The SUPERCELL case simulates an idealized supercell thunderstorm with 500m horizontal resolution. Initialized with a radiosounding and a thermal perturbation to trigger convection.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, HPC cases
   Dynamics, 3D LES
   Horizontal grid spacing, 500 m (600x600)
   Vertical levels, 89
   Integration length, 3600 s (1 hour)
   Time step, 1.5 s
   Turbulence, TKEL (3D)
   Cloud scheme, ICE3 or LIMA
   Deep convection, NONE
   Radiation, NONE
   Boussinesq, disabled

Declination
----------
.. csv-table::
   :header: Configuration, Cloud scheme, Description
   :widths: 30, 30, 30

   SUPERCELL/ICE4, ICE4, ICE4 microphysics
   SUPERCELL/LIMA111111, LIMA, LIMA with 1 moment prognostic equations for all hydrometeors
   SUPERCELL/LIMA222110, LIMA, LIMA with 2 moments for rain, droplets, drizzle, 1 moment for snow and ice; no hail
   SUPERCELL/LIMA222222_JW_CIBU, LIMA, LIMA with 2 moments for all hydrometeors and Jean-Wurtz and CIBU options

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_prep_ideal, run_prep_ideal
   002_mesonh, run_mesonh

Specificities
----------------
**Scientific specificities**

- Supercell thunderstorm simulation
- ICE4 and LIMA microphysics
- Ice-phase processes (sedimentation, rain, snow, graupel, hail)
- With/without adjustment (LADJ)
- With/without time-splitting

**Technical specificities**

- 600x600 horizontal grid (300km x 300km)
- 89 vertical levels with thin shell
- Thermal perturbation (2K amplitude)
- Cyclic boundary conditions

Validation
----------------
- Vertical velocity evolution
- Hydrometeor distributions
- Precipitation patterns
- Mesocyclone development

Numerical ressources
----------------
20 nodes, 2560 cores (MPI parallel)

References
----------------
- Weisman and Klemp (1982): The simulation of numerically predicted supercellular thunderstorms