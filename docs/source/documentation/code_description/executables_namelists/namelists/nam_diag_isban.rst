.. _nam_diag_isban:

NAM_DIAG_ISBAN
-----------------------------------------------------------------------------

ISBA diagnostics.

.. csv-table:: NAM_DIAG_ISBAN content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LPGD", "LOGICAL", ".FALSE."
   "LSURF_EVAP_BUDGET", "LOGICAL", ".FALSE."
   "LSURF_MISC_BUDGET", "LOGICAL", ".FALSE."
   "LSURF_DIAG_ALBEDO", "LOGICAL", ".FALSE."
   "LPATCH_BUDGET", "LOGICAL", ".TRUE."
   "LSURF_MISC_DIF", "LOGICAL", ".FALSE."
   "LWATER_BUDGET", "LOGICAL", ".FALSE."
   "LLUTILES_BUDGET", "LOGICAL", ".FALSE."
   "LPROSNOW", "LOGICAL", ".FALSE."
   "LPROBANDS", "LOGICAL", ".FALSE."
   "LVOLUMETRIC_SNOWLIQ", "LOGICAL", ".FALSE."
   "LUTCI", "LOGICAL", ".FALSE."
   
* :code:`LPGD` : flag to save in the output file the physiographic fields of ISBA scheme that are computed from ecoclimap data from the ecosystem fractions.

* :code:`LSURF_EVAP_BUDGET` : flag to save in the output file the detailed terms of the water vapor fluxes, on each patch of the vegetation scheme if existing, and aggregated for the natural surface. The diagnosed fields are:

  * GPP: Gross primary production

* :code:`LSURF_MISC_BUDGET` : flag to save in the output file miscelleaneous fields. The diagnosed fields are:

  * HV: Halstead coefficient
  * SNG: snow fraction over bare ground
  * SNV: snow fraction over vegetation
  * SN: total snow fraction
  * SWI: soil wetness index for each ground layer (wg - wwilt)/(wfc - wwilt) where wg is the volumic water content, wfc is the porosity and wwilt corresponds to the plant wilting point.
  
* :code:`LSURF_DIAG_ALBEDO` : to write ALB..._ISBA et ALB..._S.

* :code:`LPATCH_BUDGET` : flag to save in the output file the diagnostics for each patch (default is .T.)

* :code:`LSURF_MISC_DIF` : to calculate and write specific DIF diagnostics

* :code:`LWATER_BUDGET` : to calculate and write the water budget

* :code:`LLUTILES_BUDGET` : flag to bring together diag from the ISBA patches into 4 surface covers type required for land-use-land-cover purpose (not implemented for ECOCLIMAP-SG) :

  * 1. Primary and secondary natural land (Forest, grassland, bare ground, etc.)
  * 2. Cropland (Agriculture)
  * 3. Pastureland (not yet implemented in ISBA)
  * 4. Urban settlement (not yet implemented; should be implemented if TEB is used).
  
* :code:`LPROSNOW` : add new diagnostic fields for the CROCUS snow scheme, reproject the snow mantel and other diagnostic fields on the vertical, according to the subgrid slope, and merges ISBA_PROGNOSTIC.OUT.nc and ISBA_DIAGNOSTICS.OUT.nc in ISBA_PROGNOSTIC.OUT.nc, in case of CTIMESERIES_FILETYPE = 'OFFLIN'.

* :code:`LPROBANDS` : enable the spectral resolution of Crocus diagnostics, necessary if you want to get spectral albedo and spectral direct/diffuse ratio diagnostics

* :code:`LVOLUMETRIC_SNOWLIQ`: convert the SNOWLIQ diagnostic field in kg / m3 (instead of m).

* :code:`LUTCI` : flag to compute UTCI (human thermal comfort indicator) quantities in rural areas
