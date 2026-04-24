AZF_2M
=======

Case description
----------------
Real case of Alziare (AZF) pollutant dispersion incident. Uses PASPOL for Lagrangian particle dispersion modeling and nested domains to simulate tracer transport.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Real cases
   Number of domains, 2
   Domain 1 resolution, 2.5km
   Domain 2 resolution, 500m
   Vertical levels, 50+
   Advection scheme (U,V), CEN4TH
   Advection scheme (scalar), PPM_01
   Temporal scheme, RKC4
   Turbulence, TKEL
   Cloud microphysics, ICE3
   Shallow convection, EDKF
   Dispersion model, PASPOL

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   001_pgd, run_pgd
   002_pgd_nested, run_pgd_nested
   003_preal, run_preal_xyz
   004_run, run_mesonh

Specificities
----------------
**Scientific specificities**
- Pollutant dispersion simulation
- Particle tracking with PASPOL
- 2 release points

**Technical specificities**
- 2-domain nesting (1:5 ratio)
- Short simulation (1 hour)

Validation
----------------
- Tracer concentration measurements
- Dispersion patterns

Numerical ressources
----------------
Single node configuration

References
----------------
- AZF incident observations