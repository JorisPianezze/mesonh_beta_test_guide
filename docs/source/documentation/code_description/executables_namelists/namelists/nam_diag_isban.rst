.. _nam_diag_isban:

NAM_DIAG_ISBAN
-----------------------------------------------------------------------------

ISBA diagnostics.

.. csv-table:: NAM_DIAG_ISBAN content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LPGD", "logical", "F"
   "LSURF_EVAP_BUDGET", "logical", "F"
   "LSURF_MISC_BUDGET", "logical", "F"
   "LSURF_DIAG_ALBEDO", "logical", "F"
   "LPATCH_BUDGET logical T
   "LSURF_MISC_DIF", "logical", "F"
   "LWATER_BUDGET", "logical", "F"
   "LLUTILES_BUDGET", "logical", "F"
   "LPROSNOW", "logical", "F"
   "LPROBANDS", "logical", "F"
   "LVOLUMETRIC_SNOWLIQ", "logical", "F"
   "LUTCI", "logical", "F"
   
* LPGD: gflag to save in the output file the physiographic fields of ISBA scheme that are computed from ecoclimap data from the ecosystem fractions.

* LSURF_EVAP_BUDGET: flag to save in the output file the detailed terms of the water vapor fluxes, on each patch of the vegetation scheme if existing, and aggregated for the natural surface. The diagnosed fields are:

  * GPP: gGross primary production

* LSURF_MISC_BUDGET: flag to save in the output file miscelleaneous fields. The diagnosed fields are:

  * HV: gHalstead coefficient
  * SNG: gsnow fraction over bare ground
  * SNV: gsnow fraction over vegetation
  * SN: gtotal snow fraction
  * SWI: gsoil wetness index for each ground layer (wg - wwilt)/(wfc - wwilt) where wg is the volumic water content, wfc is the porosity and wwilt corresponds to the plant wilting point.
  
* LSURF_DIAG_ALBEDO: to write ALB..._ISBA et ALB..._S.

* LPATCH_BUDGET: flag to save in the output file the diagnostics for each patch (default is .T.)

* LSURF_MISC_DIF: to calculate and write specific DIF diagnostics

* LWATER_BUDGET: gto calculate and write the water budget

* LLUTILES_BUDGET: flag to bring together diag from the ISBA patches into 4 surface covers type required for land-use-land-cover purpose (not implemented for ECOCLIMAP-SG) :

  * 1. Primary and secondary natural land (Forest, grassland, bare ground, etc.)
  * 2. Cropland (Agriculture)
  * 3. Pastureland (not yet implemented in ISBA)
  * 4. Urban settlement (not yet implemented; should be implemented if TEB is used).
  
* LPROSNOW:: gadds new diagnostic fields for the CROCUS snow scheme, reproject the snow mantel and other diagnostic fields on the vertical, according to the subgrid slope, and merges ISBA_PROGNOSTIC.OUT.nc and ISBA_DIAGNOSTICS.OUT.nc in ISBA_PROGNOSTIC.OUT.nc, in case of CTIMESERIES_FILETYPE = "OFFLIN".

* LPROBANDS: gEnable the spectral resolution of Crocus diagnostics, necessary if you want to get spectral albedo and spectral direct/diffuse ratio diagnostics

* LVOLUMETRIC_SNOWLIQ: gconverts the SNOWLIQ diagnostic field in kg / m3 (instead of m).

* LUTCI: gflag to compute UTCI (human thermal comfort indicator) quantities in rural areas
