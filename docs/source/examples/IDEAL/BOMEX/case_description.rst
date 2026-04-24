BOMEX shallow cumulus
===================

Case description
----------------
The BOMEX (BOundary Layer EXperiment) case simulates shallow cumulus convection over tropical ocean. This is a classic case for testing shallow convection parameterization and LES modeling of marine boundary layer clouds.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Idealized cases
   Dynamics, 3D with 1D turbulence
   Horizontal grid spacing, 40000 m (1x1 grid)
   Integration length, 28800 s (8 hours)
   Time step, 120 s
   Coriolis effect, enabled
   Turbulence, TKEL (1D)
   Cloud scheme, ICE3
   Deep convection, NONE
   Shallow convection, EDKF
   Radiation, NONE
   LES diagnostics, enabled

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

- Quasi-steady state shallow cumulus layer under weak large-scale forcing
- Constant surface fluxes (sensible heat: 9.2 W/m², latent heat: 6.16e-5 kg/m²/s)
- Friction velocity: 0.28 m/s
- Geostrophic forcing with vertical motion above 2600m
- 1D turbulence (TKEL) with BL89 length scale
- LES diagnostics averaged over 18000-21600s (6th hour)

**Technical specificities**

- Cartesian flat domain with single point (NIMAX=1, NJMAX=1)
- 75 vertical levels from 0 to 3000m
- 40m spacing near surface increasing to 300m aloft
- Surface using external roughness length (Z0=0.035m)

Validation
----------------
- Vertical profiles of mean quantities (THL, RC, U, V)
- Subgrid turbulent fluxes
- Cloud fraction evolution
- Boundary layer height

Numerical ressources
------------------
Single CPU (1 node, 1 core)

References
----------------
- Siebesma, A.P., et al. (2003): A shallow cumulus parametrization for the ECMWF model. Mon. Wea. Rev., 131, 2094-2104.