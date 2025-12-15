.. _nam_pgd_grid:

NAM_PGD_GRID
-----------------------------------------------------------------------------

.. warning::

   This namelist comes from SURFEX 9.0.0 user guide https://www.umr-cnrm.fr/surfex/IMG/pdf/surfex_tecdoc.pdf.

This namelist defines the grid type, either specified or from an existing surface file.

.. csv-table:: NAM_PGD_GRID content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CGRID", "CHARACTER(LEN=10)", "'CONF PROJ'"
   "YINIFILE", "CHARACTER(LEN=28)", "'NONE'"
   "YINIFILETYPE", "CHARACTER(LEN=6)", "'NONE'"
   "NOVMX", "INTEGER", "1"
  
* :code:`CGRID` : type of grid and projection. It is used only if a file is not prescribed (see below). The different grid possibilities are:

  * "GAUSS ": this grid is a gaussian grid (global grid, that may be stretched, rotated, ...).
  * "CONF PROJ ": this grid is a regular grid (in meters in x and y perpendicular directions) on conformal projection plan (Mercator, Lambert or polar stereographic).
  * "CARTESIAN ": this grid is a regular grid (in meters in x and y perpendicular directions), with no reference to real geographical coordinates.
  * "LONLAT REG": this grid is defined as a regular latitude - longitude grid.
  * "LONLATVAL ": this grid is defined as a not regular latitude - longitude grid (all points and mesh sizes are defined).
  * "LONLAT ROT": rotated lonlat (from Hirlam).
  * "IGN ": this grid type contains all IGN (French National Geographical Institute) possible Lambert projections
  * "NONE ": this grid is not regular. Only the number of points and the size of each grid mesh is prescribed. There is no positioning of each point compared to any other.

  .. note::
  
     For each option of CGRID you need to fill other namelist. By example, for CGRID='CONF PROJ', you need to fill :ref:`nam_conf_proj` and :ref:`nam_conf_proj_grid` namelists.

* :code:`YINIFILE` : name of the file used to define the grid. It is possible to define the grid as a subgrid of a previously created file. This is currently possible only for files that have a "CONF PROJ " or "CARTESIAN " grid type. The exact definition of the subgrid grid chosen is prescribed in a namelist (described below), depending on the type of grid available in the file chosen. The use of a file has priority on the CGRID type.

* :code:`YINIFILETYPE` : type of the YINIFILE file, if the latter is provided. YFILETYPE must be given. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.
  * "LFI"/"ASCII": the file type is a PREP LFI or ASCII file.
  
* :code:`NOVMX` : number of points that can overlap each other in the user grid, for the calculation of physiographic fields.
