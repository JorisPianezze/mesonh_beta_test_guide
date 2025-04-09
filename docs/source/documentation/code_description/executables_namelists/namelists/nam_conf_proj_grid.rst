.. _nam_conf_proj_grid:

NAM_CONF_PROJ_GRID
-----------------------------------------------------------------------------

This namelists defines the horizontal domain in case CGRID="CONF PROJ ".

.. csv-table:: NAM_CONF_PROJ_GRID content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XLATCEN", "REAL", ""
   "XLONCEN", "REAL", ""
   "NIMAX", "INTEGER", ""
   "NJMAX", "INTEGER", ""
   "XDX", "REAL", ""
   "XDY", "REAL", ""

* :code:`XLATCEN` : latitude of the point of the center of the domain (real, decimal degrees)

* :code:`XLONCEN` : longitude of the point of the center of the domain (real, decimal degrees)

* :code:`NIMAX` : number of surface points of the grid in direction x.

* :code:`NJMAX` : number of surface points of the grid in direction y.

* :code:`XDX` : grid mesh size on the conformal plane in x direction (real, meters).

* :code:`XDY` : grid mesh size on the conformal plane in y direction (real, meters).
