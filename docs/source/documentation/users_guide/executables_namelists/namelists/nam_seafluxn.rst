.. _nam_seafluxn:

NAM_SEAFLUXn
----------------------------------------------------------------------------- 

.. csv-table:: NAM_SEAFLUXn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CSEA_FLUX", "CHARACTER(LEN=6)", "'ECUME6'"
   "CSEA_ALB", "CHARACTER(LEN=4)", "'TA96'"
   "LPWG", "LOGICAL", ".FALSE."
   "LPRECIP", "LOGICAL", ".FALSE."
   "LPWEBB", "LOGICAL", ".FALSE."
   "LPROGSST", "LOGICAL", ".FALSE."
   "XOCEAN_TSTEP", "REAL", ""
   "CINTERPOL_SST", "CHARACTER(LEN=6)", "'NONE'"
   "CINTERPOL_SSS", "CHARACTER(LEN=6)", "'NONE'"
   "XICHCE", "REAL", "0.0"
   "CSEA_SFCO2", "CHARACTER(LEN=4)", "'NONE'"
   "NGRVWAVES", "INTEGER", "0"
   "NZ0", "INTEGER", "0"
   "LPERTFLUX", "LOGICAL", ".FALSE."
   "LWAVEWIND", "LOGICAL", ".TRUE."

* :code:`CSEA_FLUX` : type of flux computation physics. The following options are currently available:

  * "DIRECT": direct Charnock computation from :cite:t:`louis_parametric_1979`. No effect of convection in the the boundary layer on the fluxes formulae.
  * "ITERAT": iterative method proposed by :cite:t:`fairall_bulk_1996` from TOGA-COARE experiment, amended by :cite:t:`mondon_study_1998` to take into account effect of atmospheric convection on fluxes.
  * "COARE3": the COARE 3.0 iterative method proposed by :cite:t:`fairall_bulk_2003`.
  * "ECUME ": iterative method proposed by :cite:t:`fairall_bulk_1996` from TOGA-COARE experiment, amended by cnrm/memo to take into account effect of atmospheric convection, precipitation and gustiness on fluxes: improvement of surface exchange coefficients representation.
  * "ECUME6 ": to activate new ecumev6
  * "WASPV1": iterative bulk algorithm based on :cite:t:`fairall_bulk_2003` modified to take the wind-sea peak period into account.

* :code:`LPWG` : correction of fluxes due to gustiness

* :code:`LPRECIP` : correction of fluxes due to precipitation

* :code:`LPWEBB` :correction of fluxes due to convection (Webb effect)

* :code:`CSEA_ALB` : type of albedo formula. The following options are currently available:
  
  * "UNIF": a uniform value of 0.135 is used for water albedo
  * "TA96": :cite:t:`taylor_studies_1996` formula for water direct albedo, depending on solar zenith angle
  * "MK10": albedo from Marat Khairoutdinov
  * "RS14": albedo based on Morel and Gentilli 1991 and Salisbury 2014 eq(2)

* :code:`LPROGSST` : set it to T to make SST evolve with tendency when using the 1d oceanic model

* :code:`XOCEAN_TSTEP` : timestep for ocean model

* :code:`CINTERPOL_SST` : interpolate monthly SST to daily SST

  * LINEAR: Linear interpolation between 3 months. Current value is reached every 16 of each month, except in February every 15.
  * UNIF: uniform SST
  * QUADRA: Quadractic interpolation between 3 months, especially relevant to conserve the SST (or other) monthly mean value.
  * READAY: impose directly daily SST

* :code:`CINTERPOL_SSS` : interpolate monthly Sea Surface Salinity to daily SSS, used by ECUME6 and/or Gelato

  * LINEAR: Linear interpolation between 3 months. Current value is reached every 16 of each month, except in February every 15.
  * UNIF: uniform SSS
  * QUADRA: Quadractic interpolation between 3 months, especially relevant to conserve the SSS monthly mean value.
  * READAY: impose directly daily SSS

* :code:`XICHCE` : coefficient used in the Ecume formulation (computation of exchange coefficients over sea)

* :code:`CSEA_SFCO2` : Empirical CO2 emission from sea surface

  * NONE : no emission
  * WIND : Wanninkhof medium hypothesis using only wind speed as CO2 emission proxy (very empirical)

* :code:`NRGVWAVES` : Wave gravity in roughness length in coare30_flux

  * 0: no gravity waves action (Charnock)
  * 1: wave age parameterization of :cite:t:`oost_new_2002`
  * 2: model of :cite:t:`taylor_dependence_2001`

* :code:`NZ0` : to choose PZ0SEA formulation in ECUME6

  * 0: ARPEGE formulation
  * 1: :cite:t:`smith_coefficients_1988` formulation
  * 2: Direct computation using the stability functions

* :code:`LPERTFLUX` : True = stochastic flux perturbation of Ecume

* :code:`LWAVEWIND` : True for wave parameters computed from wind (default), put to False to take Hs or Tp values if initialized in PREP or if coupled.
