BIOMAIDIO
=======

Case description
----------------
Real case of biometeorological and air quality simulation over Southern France. Uses coupled chemistry and aerosol modules (ReLACS + ORILAM) with CAMS chemical initial conditions.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Real cases
   Number of domains, 2+
   Horizontal resolution, 8km -> higher
   Vertical levels, 45
   Chemistry, ReLACS with CAMS
   Aerosols, ORILAM + Sea Salt + Dust
   Cloud microphysics, LIMA

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_pgd1, run_pgd1
   002_pgd2, run_pgd2
   003_prep_nest, run_prep_nest
   004_prep_real_d1, run_prep_real_case_d1
   005_prep_real_d2, run_prep_real_case_d2
   006_mesonh, run_mesonh

Specificities
----------------
**Scientific specificities**
- Air quality simulation
- CAMS chemical initial conditions
- Multiple aerosol types (ORILAM, sea salt, dust)

**Technical specificities**
- CAMS aerosol coupling
- Domain nesting
- Canopy effects (ISBA + TEB)

Validation
----------------
- Air quality measurements
- Aerosol concentrations

Numerical ressources
----------------
Multi-node configuration

References
----------------
- CAMS analysis data