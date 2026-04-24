KW78_ELEC
==========

Case description
----------------
The KW78_ELEC case simulates a cumulonimbus with electrification processes based on the 1978 Kansas case. This case tests the charge separation and lightning parameterization.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, HPC cases
   Dynamics, 3D LES
   Horizontal grid spacing, 1000 m (40x40)
   Vertical levels, 30
   Integration length, 7200 s (2 hours)
   Time step, 3 s
   Turbulence, TKEL (3D)
   Cloud scheme, ICE3 or LIMA
   Deep convection, NONE
   Radiation, NONE
   Electrical model, enabled

Declination
----------
.. csv-table::
   :header: Configuration, Cloud scheme, Description
   :widths: 30, 30, 30

   KW78_ELEC/ice3, ICE3, ICE3 microphysics without electrification
   KW78_ELEC/lima, LIMA, LIMA with electrical charging
   KW78_ELEC/lima2, LIMA, LIMA with enhanced charging

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_prep_ideal_case, run_prep
   002_mesonh, run_mesonh_xyz

Specificities
----------------
**Scientific specificities**

- Electrical charging in thunderstorms
- Non-inductive charging mechanisms
- Charge separation during collisions
- Lightning discharge parameterization

**Technical specificities**

- 40x40 horizontal grid (40km x 40km)
- 30 vertical levels
- Initial radiosounding from Kansas 1978
- Thermal perturbation to trigger convection

Validation
----------------
- Electric field evolution
- Charge distribution
- Lightning flash locations

Numerical ressources
----------------
Single CPU (1 node, 1 core)

References
----------------
- Krehbiel et al. (1978): An analysis of the charge structure of lightning discharges