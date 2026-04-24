16JAN
=======

Case description
----------------
2-domain grid-nesting real case from 16 January 1998. Tests the WENO-K advection scheme and coupling between two nested domains with lateral boundary conditions. Simulation uses ERAI analysis for initial and boundary conditions.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Technical cases
   NMODEL, 2
   XTSTEP, 120.
   XSEGLEN, 43200.
   NITR, 8
   CCLOUD, KESS
   CTURB, TKEL
   CRAD, ECRA
   CDCONV, KAFR
   CSCONV, KAFR
   CUVW_ADV_SCHEME, WENO_K
   NWENO_ORDER, 5
   CTEMP_SCHEME, RK53

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   PREP_PGD1, run_pgd
   PREP_PGD2, run_pgd
   PREP_NEST, run_pgd
   PRE_REAL1, run_prep_real_case
   PRE_REAL2, run_prep_real_case
   SPAWN1, run_spa_real
   run1, run_mesonh1 (16 CPUs)
   run2, run_mesonh2 (16 CPUs)
   DIAG1, run_diag

Specificities
----------------
- 2 nested domains with coupling
- 5th order WENO-K advection scheme
- Runge-Kutta 3rd order temporal scheme (RK53)
- ERAI analysis for initial conditions
- Lateral boundary conditions: OPEN boundaries
- 12-hour simulation (43200s)
- Multiple coupling files (CCPLFILE)

Validation
----------------
- WENO-K scheme stability and accuracy
- Domain nesting coupling
- Temporal evolution of meteorological fields

Numerical ressources
----------------
16 CPUs per run (HPC - 1 node, 16 cores)

References
----------------
- Jan 16, 1998 case study
- WENO scheme literature (Liu et al., 1994)