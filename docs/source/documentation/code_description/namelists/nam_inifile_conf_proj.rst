.. _nam_inifile_conf_proj:

NAM_INIFILE_CONF_PROJ
-----------------------------------------------------------------------------

This namelists defines the horizontal domain from an existing surface file in which grid type is "CONF
PROJ". If nothing is set in the namelist, a grid identical as the one in the file is chosen.

.. csv-table:: NAM_INIFILE_CONF_PROJ content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "IXOR", "integer", "1"
   "IYOR", "integer", "1"
   "IXSIZE", "integer", "YINIFILE size"
   "IYSIZE", "integer", "YINIFILE size"
   "IDXRATIO", "integer", "1"
   "IDYRATIO", "integer", "1"

* IXOR: first point I index, according to the YINIFILE grid, left to and out of the new physical domain.

* IYOR: first point J index, according to the YINIFILE grid, under and out of the new physical domain.

* IXSIZE: number of grid points in I direction, according to YINIFILE grid, recovered by the new domain. If to be used in MESONH, it must only be factor of 2,3 or 5.

* IYSIZE: number of grid points in J direction, according to YINIFILE grid, recovered by the new domain. If to be used in MESONH, it must only be factor of 2,3 or 5.

* IDXRATIO: resolution factor in I direction between the YINIFILE grid and the new grid. If to be used in MESONH, it must only be factor of 2,3 or 5.

* IDYRATIO: resolution factor in J direction between the YINIFILE grid and the new grid. If to be used in MESONH, it must only be factor of 2,3 or 5.
