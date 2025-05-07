MNH-V5-7-2
============================================================================
Release date : XX/05/2025

We fully encourage all users to move to 5-7-2 especially those using grid-nesting (see major bugfix)

Major bugfix
*****************
* Spawning: interpolation of hydrometeors RRT, RIT, RST et RGT were set to RCT. This affects the initialization of all sub-domains from spawning.
* Spawning: interpolation of surface rain fields (INPRC,ACPRC,INDEP,ACDEP,INPRR,ACPRR,INPRR3D,INPRS,ACPRS,INPRG,ACPRG,INPRH,ACPRH) and EVAP3D were wrong
* Spawning on same resolution : the orography (ZS) was badly interpolated in the case (KDXRATIO==1 .AND. KDYRATIO==1)

I/O
*****************
* Useless .des file are not written any more (at PGD step)
* OUTPUT: compression parameters per variable
* OUTPUT: customize reduction of float precision per variable
* Stations/Profilers : add precipitation fields (instantaneous and accumulated) 
* Stations/ Profilers : possible with a dry atmosphere

SURFEX
*********************
* LCHECK_TEB adaptation for single precision
* Multiple fixes for multilayer TEB
* ZENITAL angle needs to be taken into account for URBTREE
* Fix PREP_REAL_CASE in real4 with surface PGD in Lfi real8

Mean field
**********************
* Fix initialization 

Lagrangian trajectories
****************************
* Computation optimization
* Z_TRAJ initial positions were not initialized correctly

Ocean-Atm-Wave coupling
**********************************
* Parallel compilation of the toy model
* Add sea surface currents in turbulence

Reproductibility
***********************
* Improve restart reproducibility (always force NITR to previous value) + reset it for starts (drop the value from the PREP step)

Cleaning
*******************
* Tabulations are removed (not conformant to Fortran standard)
* REMAP files are not written any more
* OUTPUT_LISTING0 not written any more if empty
* ZOOM_PGD is deleted

External libraries and tools
***********************************
* Fix MNH2LPDM
* Upgrade HDF5 1.14.6
* Upgrade libaec 1.1.3
* Upgrade netCDF-C 4.9.3

