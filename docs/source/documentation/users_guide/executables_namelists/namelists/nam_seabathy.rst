.. _nam_seabathy:

NAM_SEABATHY
-----------------------------------------------------------------------------

.. warning::

   This namelist comes from SURFEX 9.0.0 user guide https://www.umr-cnrm.fr/surfex/IMG/pdf/surfex_tecdoc.pdf.

.. csv-table:: NAM_SEABATHY content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XUNIF_SEABATHY", "REAL", "300"
   "YSEABATHY",  "CHARACTER(LEN=28)", ""
   "YSEABATHYFILETYPE", "CHARACTER(LEN=6)", "'NONE'"
   "YNCVARNAME", "CHARACTER(LEN=28)", ""

* :code:`XUNIF_SEABATHY` : uniform value of bathymetry imposed on all points (real,meters). If XUNIF_SEABATHY is set, file YSEABATHY is not used ;

* :code:`YSEABATHY` : data file name. If XUNIF_SEABATHY is set, file YSEABATHY is not used. If neither XUNIF_SEABATHY and YSEABATHY is set, then bathymetry is set to zero ;

* :code:`YSEABATHYFILETYPE` : type of data file ('DIRECT', 'BINLLF', 'BINLLV', 'ASCLLV', 'NETCDF') ;

* :code:`YNCVARNAME` : name of variable to be read in NETCDF file.
