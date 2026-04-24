SNOW_BLOW
=========

Case description
----------------
Idealized blowing snow case simulating snow transport by wind in polar boundary layer conditions. 
The case uses a column setup for local testing and a 30x30km domain at 50m resolution for HPC simulations.

Configuration
----------------
.. csv-table::
   :header: Parameter, Local (BLOWSNOW_c1b1D), HPC (SNOW_BLOW)
   :widths: 30, 30, 30

   Category, Idealized cases, HPC cases
   Grid type, Cartesian (1D column), Cartesian (2D)
   Horizontal resolution, Variable (wind 11-16 m/s), 50m
   Domain size, 1 column, 30x30km (600x600 grid)
   Vertical levels, Variable, 70
   Initial condition, RSOU (radiosounding), RSOU (radiosounding 2011-03-18)
   Surface, Flat (FLAT), External (EXTE)
   Equation system, LHE (liquid-ice), DUR (dry)
   Lateral boundaries, CYCL (cyclic), OPEN
   Turbulence, TKEL (TKE-length), TKEL (TKE-length)
   Time step, 0.5s (local), 1.5s (HPC)
   Segment length, 1200s (20min), 10800s (3h)
   Physics, Blowing snow (no sublimation), Blowing snow + sublimation

Declination
----------
.. csv-table::
   :header: Configuration, Description
   :widths: 30, 30

   BLOWSNOW_c1b1D_U11, Column with 11 m/s wind speed
   BLOWSNOW_c1b1D_U16, Column with 16 m/s wind speed
   SNOW_BLOW_0100_UnifSnw, Initial condition with uniform snow
   SNOW_BLOW_0200, Time 2h - evolving state
   SNOW_BLOW_0300, Time 4h - evolving state
   SNOW_BLOW_0400, Time 6h - evolving state

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_prep_ideal, run_prep_ideal_case_xyz
   002_run, run_mesonh_xyz
   HPC_prep_ideal, run_prep_ideal_case
   HPC_run, run_mesonh

Specificities
----------------
**Scientific specificities**
- Blowing snow parameterization (LBLOWSNOW=T)
- Snow saltation and suspension (CSNOW_SALT='TSOR')
- Snow sedimentation (CSNOW_SEDIM='TABC')
- Snow sublimation (only HPC: LSNOWSUBL=T)
- Canopy snow processes (LBLOWSNW_CANOSUBL on HPC)
- WENO advection scheme (5th order)
- Ice phase microphysics (ICE3)

**Technical specificities**
- Multiple wind speed variants (local)
- Four sequential time steps (HPC: 0100-0400)
- 20-layer snow scheme (CRO)
- ISBA-Canopy (LISBA_CANOPY=T)
- SLEVE vertical coordinate

Validation
----------------
- Snow mass balance
- Vertical profiles of snow concentration
- Surface snow mass evolution
- Saltation flux comparison

Numerical ressources
----------------
Local: Single CPU
HPC: 1 node (128 cores) via SLURM

References
----------------
- Gordon et al. (2007): Blowing snow parameterization
- Vignon et al. (2021): Blowing snow at Antarctic station
- Box et al. (2022): Arctic snow transport modeling