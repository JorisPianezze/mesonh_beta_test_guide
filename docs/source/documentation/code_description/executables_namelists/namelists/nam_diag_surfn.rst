.. _nam_diag_surfn:

NAM_DIAG_SURFN
-----------------------------------------------------------------------------

Diagnostics for each grid cell and each tile.

.. csv-table:: NAM_DIAG_SURFN content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "N2M", "INTEGER", "2"
   "LSURF_BUDGET", "LOGICAL", ".FALSE."
   "LSURF_BUDGETC", "LOGICAL", ".FALSE."
   "LRESET_BUDGETC", "LOGICAL", ".FALSE."
   "LRAD_BUDGET", "LOGICAL", ".FALSE."
   "LCOEF", "LOGICAL", ".FALSE."
   "LSURF_VARS", "LOGICAL", ".FALSE."
   "L2M_MIN_ZS", "LOGICAL", ".FALSE."
   
* :code:`N2M` : flag to compute surface boundary layer characteristics:

  * N2M=2 : computes temperature at 2 m, specific humidity at 2 m, relative humidity, zonal and meridian wind at 10 m, and Richardson number. 2m and 10m quantities are calculated interpolating between atmospheric forcing variables and surface temperature and humidity.

* :code:`LSURF_BUDGET` : flag to save in the output file the terms of the surface energy balance (net radiation, sensible heat flux, latent heat flux, ground flux), for each scheme (on the four separate tiles), on each patch of the vegetation scheme if existing, and aggregated for the whole surface. The diagnosed fields are (* stands for the scheme considered (* = nothing: gfield aggregated on the whole surface; * = name of a scheme : field for this scheme):

  * RN_*: net radiation
  * H_*: turbulent sensible heat flux
  * LE_*: turbulent latent heat flux
  * GFLUX_*: round or storage heat flux
  * FMU_*: zonal wind stress
  * FMV_*: meridian wind stress

.. note::

   If both LSURF_BUDGET and LRAD_BUDGET are T then downward and upward short-wave radiation per spectral band will be written into output file (they are computed even if LRAD_BUDGET is False). The following output fields are then available:

     * SWD_*: downward short wave radiation
     * SWU_*: upward short wave radiation
     * SWBD_*: downward short wave radiation for each spectral band
     * SWBU_*: upward short wave radiation for each spectral band
     * LWD_*: downward long wave radiation
     * LWU_*: upward long wave radiation
  
* :code:`LSURF_BUDGETC` : flag to save in the output file the time integrated values of all budget terms that have been activated

* :code:`LRESET_BUDGETC` : flag to reset cumulatives variables at the beginning of a run

* :code:`LCOEF` : flag to save in the output file the transfer coefficients used in the computation of the surface energy fluxes, for each scheme (on the four separate tiles) and aggregated for the whole surface. The diagnosed fields are (* stands for the scheme considered * = nothing: field aggregated on the whole surface; * = name of a scheme : field for this scheme):

  * CD_*: gdrag coefficient for momentum
  * CH_*: gdrag coefficient for heat
  * CE_*: gdrag coefficient for evaporation (differs from CH only over sea)
  * Z0_*: groughness length
  * Z0H_*: gthermal roughness length
  
* :code:`LSURF_VARS` : flag to save in the output file the surface specific humidity for each scheme (on the four separate tiles), on each patch of the vegetation scheme if existing. The diagnosed fields are (* stands for the scheme considered (* = nothing: gfield aggregated on the whole surface; * = name of a scheme :< field for this scheme):

  *  QS_*: specific humidity

* :code:`L2M_MIN_ZS` : flag for 2 meters quantities evaluated on the minimum orography of the grid
