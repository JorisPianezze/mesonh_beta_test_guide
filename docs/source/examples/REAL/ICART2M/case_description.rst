ICART2M
=======

Case description
----------------
Real case simulation for the ICART (Idealized/CART) model intercomparison project at 2km resolution. Tests coupled chemistry and aerosol representation.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Real cases
   Horizontal resolution, 2.5km
   Vertical levels, 50+
   Advection scheme (scalar), PPM_01
   Temporal scheme, RKC4
   Turbulence, TKEL
   Radiation, ECMW
   Cloud microphysics, ICE3
   Deep convection, KAFR
   Shallow convection, EDKF
   Chemistry, ReLACS enabled
   Aerosols, ORILAM

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_pgd, run_pgd
   002_preal1, run_preal_xyz
   003_preal2, run_preal_xyz_2
   004_mesonh1, run_mesonh_xyz
   005_mesonh2, run_mesonh_xyz_2

Specificities
----------------
**Scientific specificities**
- Chemical transport intercomparison
- ORILAM aerosol model
- Multi-step nesting

**Technical specificities**
- 2-step spawning process
- Chemistry splitting

Validation
----------------
- Chemical tracer comparisons
- Aerosol distributions

Numerical ressources
----------------
Single node configuration

References
----------------
- ICART model intercomparison