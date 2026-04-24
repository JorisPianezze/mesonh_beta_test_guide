GRIB
=======

Case description
----------------
GRIB atmospheric data interpolation cases. Tests the PREP_REAL_CASE tool to interpolate external atmospheric GRIB data (ERA5, GFS, ICON, HRRR, ARPEGFS) to MesoNH initial conditions. Multiple data sources supported.

Configuration
----------------
.. csv-table::
   :header: Parameter, Value
   :widths: 30, 30

   Category, Technical cases
   NMODEL, 1
   NKMAX, 40 (ERA5)
   CEQNSYS, DUR
   JPHEXT, 1
   NHALO, 1

Steps
----------------
.. csv-table::
   :header: Step, Script
   :widths: 30, 30

   PGD, run_pgd
   ERA5_run, run_prep_real_case
   ERA5_hPa_run, run_prep_real_case
   ARO_41t1_run, run_prep_real_case
   ARO_43t2_run, run_prep_real_case
   ARO_46t1_run, run_prep_real_case
   ARO_48t1_run, run_prep_real_case
   GFS_run, run_prep_real_case
   HRRR_run, run_prep_real_case
   ICONEU_run, run_prep_real_case
   ICONGLOBAL_run, run_prep_real_case
   IFS_run, run_prep_real_case
   IFS_PY_run, run_prep_real_case
   ARP_run, run_prep_real_case
   plotting, run_python (post-processing)

Specificities
----------------
- Multiple GRIB data sources: ERA5, ERA5_hPa, ARPEGFS (41t1, 43t2, 46t1, 48t1), GFS, HRRR, ICON-EU, ICON-Global, IFS, ARP
- Python plotting tools for GRIB visualization
- Vertical interpolation from GRIB levels to model levels
- Horizontal interpolation to target domain

Validation
----------------
- GRIB field interpolation quality
- Vertical level conversion
- Horizontal domain coverage

Numerical ressources
----------------
HPC: 1 node, 2 cores (MPI parallel)

References
----------------
- ECMWF ERA5 documentation
- NOAA GFS documentation
- DWD ICON model documentation