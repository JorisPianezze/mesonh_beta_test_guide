.. _nam_conf_proj_grid:

NAM_CONF_PROJ_GRID
-----------------------------------------------------------------------------

This namelists defines the horizontal domain in case CGRID="CONF PROJ ".

.. csv-table:: NAM_CONF_PROJ_GRID content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XLATCEN", "real", "none"
   "XLONCEN", "real", "none"
   "NIMAX", "integer", "none"
   "NJMAX", "integer", "none"
   "XDX", "real", "none"
   "XDY", "real", "none"

* XLATCEN: latitude of the point of the center of the domain (real, decimal degrees)

* XLONCEN: longitude of the point of the center of the domain (real, decimal degrees)

* NIMAX: number of surface points of the grid in direction x.

* NJMAX: number of surface points of the grid in direction y.

* XDX: grid mesh size on the conformal plane in x direction (real, meters).

* XDY: grid mesh size on the conformal plane in y direction (real, meters).
