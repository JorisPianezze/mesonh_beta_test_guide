.. _nam_diag_tebn:

NAM_DIAG_TEBN
-----------------------------------------------------------------------------

TEB diagnostics.

.. csv-table:: NAM_DIAG_TEBN content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LPGD", "LOGICAL", ".FALSE."
   "LSURF_MISC_BUDGET", "LOGICAL", ".FALSE."
   "LSURF_DIAG_ALBEDO", "LOGICAL", ".FALSE."
   "LUTCI", "LOGICAL", ".FALSE."
   
* :code:`LPGD` : flag to save PGD fields if TEB garden is activated

* :code:`LSURF_MISC_BUDGET` : flag to save in the output file miscelleaneous fields. The diagnosed fields are:

  * Z0_TOWN: roughness length for town
  * QF_BLD: domestic heating
  * QF_BLDWFR: domestic heating
  * FLX_BLD: heat flux from bld
  * TI_BLD_EQ: internal temperature without heating
  * TI_BLDWFR: internal temperature without heating
  * QF_TOWN: total anthropogenic heat
  * DQS_TOWN: storage inside building
  * H_WALL: wall sensible heat flux
  * H_ROOF: roof sensible heat flux
  * H_ROAD: road sensible heat flux
  * RN_WALL: net radiation at wall
  * RN_ROOF: net radiation at roof
  * RN_ROAD: net radiation at road
  * GFLUX_WALL: net wall conduction flux
  * GFLUX_ROOF: net roof conduction flux
  * GFLUX_ROAD: net road conduction flux
  * LE_ROOF: roof latent heat flux
  * LE_ROAD: road latent heat flux
  
* :code:`LSURF_DIAG_ALBEDO` : flag to save in the output file albedo diagnostics

* :code:`LUTCI` : to calculate and write UTCI diagnostics
