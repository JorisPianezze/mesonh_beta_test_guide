.. _nam_pgd_schemes:

NAM_PGD_SCHEMES
-----------------------------------------------------------------------------

This namelist defines the four schemes that will be used, one for each type of surface (sea, inland water,
town, vegetation).

.. csv-table:: NAM_PGD_SCHEMES content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CNATURE", "character(LEN=6)", "ISBA"
   "CSEA", "character(LEN=6)", "SEAFLX"
   "CWATER", "character(LEN=6)", "WATFLX"
   "CTOWN", "character(LEN=6)", "TEB"

* CNATURE: scheme used for vegegation and natural soil covers. The different possibilities are:

  * "NONE ": no scheme used. No fluxes will be cmputed at the surface.
  * "FLUX ": ideal fluxes are prescribed. The have to be set in the fortran routine init_ideal_flux.f90.
  * "TSZ0 ": In this cheme, the fluxes are computed according to the ISBA physics, but the surface characteristics (temperature, humidity, etc...) remain constant with time.
  * "ISBA ": this is the full ISBA scheme (Noilhan and Planton 1989), with all options developped since this initial paper.
  
* CSEA: scheme used for sea and ocean . The different possibilities are:

  * "NONE ": no scheme used. No fluxes will be cmputed at the surface.
  * "FLUX ": ideal fluxes are prescribed. The have to be set in the fortran routine init_ideal_flux.f90.
  * "SEAFLX": this is a relatively simple scheme, using the Charnock formula.
  
* CWATER: scheme used for inland water . The different possibilities are:
  
  * "NONE ": no scheme used. No fluxes will be cmputed at the surface.
  * "FLUX ": ideal fluxes are prescribed. The have to be set in the fortran routine init_ideal_flux.f90.
  * "WATFLX": this is a relatively simple scheme, using the Charnock formula.
  * "FLAKE ": this is lake scheme from Mironov, 2005.
  
* CTOWN: scheme used for towns . The different possibilities are:

  * "NONE ": no scheme used. No fluxes will be cmputed at the surface.
  * "FLUX ": ideal fluxes are prescribed. The have to be set in the fortran routine init_ideal_flux.f90.
  * "TEB ": this is the Town Energy Balance scheme (Masson 2000), with all the subsequent ameliorations of the scheme.
  
* LGARDEN: general flag to activate TEB_GARDEN
