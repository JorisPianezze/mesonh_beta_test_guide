.. _nam_inifile_conf_proj:

NAM_INIFILE_CONF_PROJ
-----------------------------------------------------------------------------

This namelists defines the horizontal domain from an existing surface file in which grid type is "CONF PROJ". If nothing is set in the namelist, a grid identical as the one in the file is chosen.

.. csv-table:: NAM_INIFILE_CONF_PROJ content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "IXOR", "INTEGER", "1"
   "IYOR", "INTEGER", "1"
   "IXSIZE", "INTEGER", "YINIFILE size"
   "IYSIZE", "INTEGER", "YINIFILE size"
   "IDXRATIO", "INTEGER", "1"
   "IDYRATIO", "INTEGER", "1"

* :code:`IXOR` : first point I index, according to the YINIFILE grid, left to and out of the new physical domain.

* :code:`IYOR` : first point J index, according to the YINIFILE grid, under and out of the new physical domain.

* :code:`IXSIZE` : number of grid points in I direction, according to YINIFILE grid, recovered by the new domain. If to be used in Meso-NH, it must only be factor of 2,3 or 5.

* :code:`IYSIZE` : number of grid points in J direction, according to YINIFILE grid, recovered by the new domain. If to be used in Meso-NH, it must only be factor of 2,3 or 5.

* :code:`IDXRATIO` : resolution factor in I direction between the YINIFILE grid and the new grid. If to be used in Meso-NH, it must only be factor of 2,3 or 5.

* :code:`IDYRATIO` : resolution factor in J direction between the YINIFILE grid and the new grid. If to be used in Meso-NH, it must only be factor of 2,3 or 5.
