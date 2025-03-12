.. _nam_diag_surfn:

NAM_DIAG_SURFN
-----------------------------------------------------------------------------

Diagnostics for each grid cell and each tile.

.. csv-table:: NAM_DIAG_SURFN content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "N2M", "integer", "2"
   "LSURF_BUDGET", "logical", "F"
   "LSURF_BUDGETC", "logical", "F"
   "LRESET_BUDGETC", "logical", "F"
   "LRAD_BUDGET", "logical", "F"
   "LCOEF", "logical", "F"
   "LSURF_VARS", "logical", "F"
   "L2M_MIN_ZS", "logical", "F"
   
• N2M: gflag to compute surface boundary layer characteristics:

  * N2M=2: gcomputes temperature at 2 m, specific humidity at 2 m, relative humidity, zonal and meridian wind at 10 m, and Richardson number. 2m and 10m quantities are calculated interpolating between atmospheric forcing variables and surface temperature and humidity.

* LSURF_BUDGET: flag to save in the output file the terms of the surface energy balance (net radiation, sensible heat flux, latent heat flux, ground flux), for each scheme (on the four separate tiles), on each patch of the vegetation scheme if existing, and aggregated for the whole surface. The diagnosed fields are (* stands for the scheme considered (*=nothing: gfield aggregated on the whole surface;*=name of a scheme : field for this scheme):

  * RN_*: gnet radiation
  * H_*: gturbulent sensible heat flux
  * LE_*: gturbulent latent heat flux
  * GFLUX_*: ground or storage heat flux
  * FMU_*: gzonal wind stress
  * FMV_*: gmeridian wind stress

If both LSURF_BUDGET and LRAD_BUDGET are T then downward and upward short-wave radiation per spectral band will be written into output file (they are computed even if LRAD_BUDGET is False). The following output fields are then available:

  * SWD_*: gdownward short wave radiation
  * SWU_*: upward short wave radiation
  * SWBD_*: gdownward short wave radiation for each spectral band
  * SWBU_*: gupward short wave radiation for each spectral band
  * LWD_*:downward long wave radiation
  * LWU_*: gupward long wave radiation
  
* LSURF_BUDGETC: flag to save in the output file the time integrated values of all budget terms that have been activated

* LRESET_BUDGETC: flag to reset cumulatives variables at the beginning of a run

* LCOEF: flag to save in the output file the transfer coefficients used in the computation of the surface energy fluxes, for each scheme (on the four separate tiles) and aggregated for the whole surface. The diagnosed fields are (* stands for the scheme considered (*=nothing: gfield aggregated on the whole surface; *=name of a scheme : field for this scheme):

  * CD_*: gdrag coefficient for momentum
  * CH_*: gdrag coefficient for heat
  * CE_*: gdrag coefficient for evaporation (differs from CH only over sea)
  * Z0_*: groughness length
  * Z0H_*: gthermal roughness length
  
* LSURF_VARS: flag to save in the output file the surface specific humidity for each scheme (on the four separate tiles), on each patch of the vegetation scheme if existing. The diagnosed fields are (* stands for the scheme considered (*=nothing: gfield aggregated on the whole surface; *=name of a scheme :< field for this scheme):

  *  QS_*: gspecific humidity

* L2M_MIN_ZS: flag for 2 meters quantities evaluated on the minimum orographyy of the grid
