.. _nam_diag_tebn:

NAM_DIAG_TEBN
-----------------------------------------------------------------------------

TEB diagnostics.

.. csv-table:: NAM_DIAG_TEBN content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LPGD", "logical", "F"
   "LSURF_MISC_BUDGET", "logical", "F"
   "LSURF_DIAG_ALBEDO", "logical", "F"
   "LUTCI", "logical", "F"
   
* LPGD: gflag to save PGD fields if TEB garden is activated

* LSURF_MISC_BUDGET: flag to save in the output file miscelleaneous fields. The diagnosed fields are:

  * Z0_TOWN: groughness length for town
  * QF_BLD: gdomestic heating
  * QF_BLDWFR: gdomestic heating
  * FLX_BLD: gheat flux from bld
  * TI_BLD_EQ: ginternal temperature without heating
  * TI_BLDWFR: ginternal temperature without heating
  * QF_TOWN: gtotal anthropogenic heat
  * DQS_TOWN: gstorage inside building
  * H_WALL: gwall sensible heat flux
  * H_ROOF: roof sensible heat flux
  * H_ROAD: road sensible heat flux
  * RN_WALL: gnet radiation at wall
  * RN_ROOF: gnet radiation at roof
  * RN_ROAD: net radiation at road
  * GFLUX_WALL: gnet wall conduction flux
  * GFLUX_ROOF: gnet roof conduction flux
  * GFLUX_ROAD: gnet road conduction flux
  * LE_ROOF: groof latent heat flux
  * LE_ROAD: groad latent heat flux
  
* LSURF_DIAG_ALBEDO: gflag to save in the output file albedo diagnostics

* LUTCI: gto calculate and write UTCI diagnostics
