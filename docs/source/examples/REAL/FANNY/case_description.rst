FANNY
======

Case description
----------------
The FANNY case is a real supercell simulation during the FANNY IOP (Intensive Observation Period). This case tests deep convective cloud and mesocyclone structures with different microphysics configurations.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Real cases
   Dynamics, 3D LES
   Horizontal grid spacing, 2500 m
   Vertical levels, 40
   Integration length, 10800 s (3 hours)
   Time step, 5 s
   Turbulence, TKEL (3D)
   Cloud scheme, ICE3 or LIMA
   Deep convection, NONE
   Shallow convection, EDKF
   Radiation, ECMW

Declination
----------
.. csv-table::
   :header: Configuration, Cloud scheme, Description
   :widths: 30, 30, 30

   FANNY/ICE3, ICE3, ICE3 with LRED=F
   FANNY/ICE3_LRED, ICE3, ICE3 with LRED=T
   FANNY/ICE3_LRED_MOENG, ICE3, ICE3 with LRED=T and turbulence Moeng terms
   FANNY/LIMA, LIMA, default values of LIMA
   FANNY/LIMA_CAMS, LIMA, LIMA with CAMS aerosols
   FANNY/LIMA_v222222, LIMA, LIMA variant 2 moment prognostic equations for all hydrometeors
   FANNY/REPRO_DEBUG, LIMA, Reproducibility debug

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_pgd, run_pgd
   002_prep_real, run_prep_real_case
   003_mesonh, run_mesonh

Specificities
----------------
**Scientific specificities**

- Real case supercell simulation
- LIMA microphysics with aerosol activation
- Mesocyclone development
- ICE3 and LIMA comparisons
- CAMS aerosol scheme variants

**Technical specificities**

- 2.5km horizontal resolution
- 40 vertical levels
- WENO advection scheme (order 5)
- Real case initialization from observations

Validation
----------------
- Radar reflectivity comparison
- Storm structure evolution
- Mesocyclone track

Numerical ressources
----------------
20 nodes, 320 cores (MPI parallel)

References
----------------
- FANNY campaign observations (1997)