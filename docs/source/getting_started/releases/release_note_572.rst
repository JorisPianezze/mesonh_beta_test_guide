MNH-V5-7-2
============================================================================

Release date : XX/05/2025

.. warning::
   
   We fully encourage all users to move to 5-7-2 especially those using grid-nesting (see major bugfix)

Major bugfix
*****************
* Spawning: interpolation of hydrometeors RRT, RIT, RST et RGT were set to RCT. This affects the initialization of all sub-domains from spawning
* Spawning: interpolation of surface rain fields (INPRC, ACPRC, INDEP, ACDEP, INPRR, ACPRR, INPRR3D, INPRS, ACPRS, INPRG, ACPRG, INPRH, ACPRH) and EVAP3D were wrong
* Spawning on same resolution: the orography (ZS) was badly interpolated in the case (KDXRATIO==1 .AND. KDYRATIO==1)

I/O
*****************

Outputs: compression parameters per variable
-----------------

It is now possible to set the compression parameters independently for each variable.

To use it, you have to set the following parameters in the NAM_OUTPUT namelist (m: model number, NBM: maximum number of boxes/subdomains (20), NVM: maximum number of fields/variables (192)). Settings that take priority over global settings for the file:

* :code:`COUT_COMPRESS_LOSSY_ALGO(m) = 'NONE'` has been added (default value remains GranularBR)
* :code:`NOUT_VAR_REDUCE_FLOAT_PRECISION(m,NVM)`: reduction of floating point precision per variable (netCDF)
* :code:`NOUT_VAR_COMPRESS_LEVEL(m,NVM)`: compression level per variable (netCDF)
* :code:`COUT_VAR_COMPRESS_LOSSY_ALGO(m,NVM)`: lossy compression per variable (netCDF, only floating points fields)
* :code:`NOUT_VAR_COMPRESS_LOSSY_NSD(m,NVM)`: number of significant decimals (or bits) to keep per variable
* :code:`NOUT_BOX_VAR_REDUCE_FLOAT_PRECISION(m,NBM,NVM)`: reduction of floating point precision for variables in boxes/subdomains (netCDF)
* :code:`NOUT_BOX_VAR_COMPRESS_LEVEL(m,NBM,NVM)`: compression level for variables in boxes/subdomains (netCDF)
* :code:`COUT_BOX_VAR_COMPRESS_LOSSY_ALGO(m,NBM,NVM)`: lossy compression for variables in boxes/subdomains (netCDF, only floating points fields)
* :code:`NOUT_BOX_VAR_COMPRESS_LOSSY_NSD(m,NBM,NVM)`: number of significant decimals (or bits) to keep for variables in boxes/subdomains


Outputs: threshold filtering (per variable)
-----------------

It is now possible to filter the values of a field with different thresholds.

This is only available for variables stored in floating point format.

To use it, you have to set the following parameters in the NAM_OUTPUT namelist (m: model number, NBM: maximum number of boxes/subdomains (20), NVM: maximum number of fields/variables (192)):

* :code:`XOUT_VAR_THR_MIN(m,NVM)`, :code:`XOUT_VAR_THR_MAX(m,NVM)`, :code:`XOUT_VAR_THR_ABSMIN(m,NVM)`, :code:`XOUT_VAR_THR_ABSMAX(m,NVM)`: threshold values (min, max, absolute value min or max; not active by default)
* :code:`COUT_VAR_THR_MIN_BEHAVIOR(m,NVM)`, :code:`COUT_VAR_THR_MAX_BEHAVIOR(m,NVM)`, :code:`COUT_VAR_THR_ABSMIN_BEHAVIOR(m,NVM)`, :code:`COUT_VAR_THR_ABSMAX_BEHAVIOR(m,NVM)`: replacement value for filtered values. Possible options depend on the threshold type:

  * NONE
  * ZERO (default for MIN if >0 and for ABSMIN)
  * MIN, MAX
  * FILLVALUE (default for MIN si <0, MAX and ABSMAX)
  * VALIDMIN, VALIDMAX
  * UNDEF, NEGUNDEF
  * ABSMIN, ABSMAX
  * EXCLRANGE (to remove values in a range)

* :code:`XOUT_BOX_VAR_THR_MIN(m,NBM,NVM)`, :code:`XOUT_BOX_VAR_THR_MAX(m,NBM,NVM)`, :code:`XOUT_BOX_VAR_THR_ABSMIN(m,NBM,NVM)`, :code:`XOUT_BOX_VAR_THR_ABSMAX(m,NBM,NVM)`: threshold values for the variables inside the boxes/subdomains
* :code:`COUT_BOX_VAR_THR_MIN_BEHAVIOR(m,NBM,NVM)`, :code:`COUT_BOX_VAR_THR_MAX_BEHAVIOR(m,NBM,NVM)`, :code:`COUT_BOX_VAR_THR_ABSMIN_BEHAVIOR(m,NBM,NVM)`, :code:`COUT_BOX_VAR_THR_ABSMAX_BEHAVIOR(m,NBM,NVM)`: replacement value for filtered values for the variables inside the boxes/subdomains


Outputs: rounding factor (per variable)
-----------------

It is now possible to round each value of a field to a multiple of a choosen value.

* For example, all the values of a field can be rounded to a multiple of 0.1. In that case, the range of possible and stored values will look like this: ..., -0.2, -0.1, 0.0, 0.1, 0.2,...
* This is useful to reduce the number of existing different values of a variable
* This approach can strongly increase the compression and therefore reduce the size of the output files
* This is available only for variables stored in floating point format
* It is advised to not enable lossy compression when enabling this option because the 2 approaches have similarities and too much information could be lost
* The rounding factor can be set variable per variable

To use it, you have to set the following parameters in the NAM_OUTPUT namelist (m: model number, NBM: maximum number of boxes/subdomains (20), NVM: maximum number of fields/variables (192)):

* :code:`XOUT_VAR_RND_FACTOR(m,NVM)`: rounding factor (non active by default)
* :code:`XOUT_BOX_VAR_RND_FACTOR(m,NBM,NVM)`: same for the variables inside the boxes/subdomains


Other changes
-----------------

* Compression: all datatypes can be compressed (only floating point data could be compressed in previous Meso-NH versions)
* Stations / Profilers: add precipitation fields (instantaneous and accumulated) 
* Stations / Profilers: possible with a dry atmosphere
* Stations / Profilers: possible with a cartesian domain
* Zsplit files: automatic detection of the number of Zsplit files (NB_PROCIO_R` in namelist NAM_CONFZ not necessary anymore to read netCDF files written from version Meso-NH 5.7.2)
* MNH_COMPRESS_LEVEL, MNH_NSUBFILES and MNH_IS_ROOTFILE attributes have been added in all netCDF files
* level and MNH_SUBFILE_TYPE attributes added in Zsplit netCDF files
* Useless .des file are not written any more (mainly at :program:`PGD` and :program:`DIAG` steps)
* Useless files not written any more (empty OUTPUT_LISTING0, file_for_xtransfer and pressure solver statistics files)

Restarts: better reproducibility
-----------------

The behavior related to the :code:`NITR` parameter of the NAM_DYNn namelist has been modified.

* in case of START, if :code:`NITR` is provided, it is used (unchanged from the previous Meso-NH versions). If not provided, it is set to a default value (instead of using the value from the .des file). Most of the time, this should (slightly) reduce the computation time at start (due to the fact that NITR should generally be higher at the PREP stage).
* in case of restart, :code:`NITR` may not be provided (before: it was forced to the value of EXSEGn.nam if provided). The value used is the previous one (found in the .des file from which the restart is performed).
 

SURFEX
*********************
* :code:`LCHECK_TEB` adaptation for single precision
* Multiple fixes for multilayer TEB
* ZENITAL angle needs to be taken into account for URBTREE
* Fix :program:`PREP_REAL_CASE` in real4 with surface PGD in Lfi real8

Mean field
**********************
* Fix initialization 

Lagrangian trajectories
****************************
* Computation optimization
* Z_TRAJ initial positions were not initialized correctly

Ocean-Atmosphere-Wave coupling
**********************************
* Fixed a bug in the parallel compilation of the toy model (when using :code:`export VER_OASIS=OASISAUTO` before configure)
* Added sea surface currents in the turbulence scheme (by default, sea surface currents are set to 0 m/s)

Chemistry
**********************************
* Modified the read CAMS routine to support the new extracted NetCDF files using the CDS API (https://ads.atmosphere.copernicus.eu/how-to-api).

Cleaning
*******************
* Tabulations are removed (not conformant to Fortran standard)
* :program:`ZOOM_PGD` is deleted
* Changed LA to LAERO in some output files

External libraries and tools
***********************************
* Fix MNH2LPDM
* Due to changes in Anaconda's licensing terms in 31 March 2024 (https://legal.anaconda.com/policies/), we migrate from Anaconda (:file:`README_MNH_COND`) to Miniforge (:file:`README_MNH_CONDA_MINIFORGE`) for Python environment management
* Upgrade HDF5 to version 1.14.6 (instead of 1.14.2)
* Upgrade libaec to version 1.1.3 (instead of 1.1.2)
* Upgrade netCDF-C to version 4.9.3 (instead of 4.9.2).

.. note::
   
   A bugfix has been applied to the library netCDF-C (see https://github.com/Unidata/netcdf-c/issues/3091)
