.. _nam_conf_proj:

NAM_CONF_PROJ
-----------------------------------------------------------------------------

This namelist defines the projection in case CGRID="CONF PROJ ".

.. csv-table:: NAM_CONF_PROJ content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XLAT0", "real", "none"
   "XLON0", "real", "none"
   "XRPK", "real", "none"
   "XBETA", "real", "none"

* XLAT0: reference latitude for conformal projection (real, decimal degrees)

* XLON0: reference longitude for conformal projection (real, decimal degrees)

* XRPK: cone factor for the projection (real):

  * XRPK=1: polar stereographic projection from north pole
  * 1>XRPK>0: Lambert projection from south pole
  * XRPK=0: Mercator projection from earth center
  * -1<XRPK<0: Lambert projection from north pole
  * XRPK=-1: polar stereographic projection from south pole
  
* XBETA: rotation angle of the simulation domain around the reference longitude (real)
