.. _nam_grid_pre:

NAM_GRID_PRE
-----------------------------------------------------------------------------

.. csv-table:: NAM_GRID_PRE content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XLON0","REAL","0.0"
   "XLAT0","REAL","60.0"
   "XBETA","REAL","0.0"
   "XRPK","REAL","1.0"
   "XLONORI","REAL","350.0"
   "XLATORI","REAL","37.0"

* :code:`XLON0` : reference longitude for conformal projection and cartesian plane (if LCARTESIAN =.TRUE. this value can be usefull to compute local solar time)

* :code:`XLAT0` : reference latitude for conformal projection and cartesian plane

* :code:`XBETA` : rotation angle for conformal projection and cartesian plane

* :code:`XRPK` : cone factor for the projection (only if LCARTESIAN =.FALSE.):

  * XRPK=1: polar stereographic projection from south pole
  * 1>XRPK>0: Lambert projection from south pole
  * XRPK=0: Mercator projection from earth center
  * -1<XRPK<0: Lambert projection from north pole
  * XRPK=-1: polar stereographic projection from north pole

* :code:`XLONORI` : Longitude (in degrees) of the origine point (not used if LCARTESIAN =.TRUE.). This point is the mass point of conformal coordinates (x=0,y=0) of the Meso-NH grids.

* :code:`XLATORI` : Latitude (in degrees) of the origine point (not used if LCARTESIAN =.TRUE.)

