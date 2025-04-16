.. _nam_stationn:

NAM_STATIONn
----------------------------------------------------------------------------- 

This namelist is used to configure a virtual observed point at a station by using the following described parameters or a .csv file. Calculations are done for all the nested models for which the namelist is provided and recorded in the corresponding diachronic files. Before the version 5.5 of MesoNH, this was done by modifying :file:`ini_stationn.f90` and re-compiling the code.

.. csv-table:: NAM_STATIONn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "NNUMB_STAT","INTEGER","0"
   "XSTEP_STAT","REAL","60.0"
   "XX_STAT","REAL(:)","NNUMB_STAT * XUNDEF"
   "XY_STAT","REAL(:)","NNUMB_STAT * XUNDEF"
   "XLAT_STAT","REAL(:)","NNUMB_STAT * XUNDEF"
   "XLON_STAT","REAL(:)","NNUMB_STAT * XUNDEF"
   "XZ_STAT","REAL(:)","NNUMB_STAT * XUNDEF"
   "CNAME_STAT","ARRAY(CHARACTER(LEN=10))","NNUMB_STAT * ' '"
   "CFILE_STAT","CHARACTER(LEN=128)","'NO_INPUT_CSV'"
   "LDIAG_SURFRAD","LOGICAL",".TRUE."

* :code:`NNUMB_STAT` : number of stations. Limited to 100 if not using a .csv file.

* :code:`XSTEP_STAT` : time (in seconds) between two sampling written in the diachronic file

* :code:`XX_STAT` : X-position (in meters) of the station in the cartesian coordinates (with LCARTESIAN=T only)

* :code:`XY_STAT` : Y-position (in meters) of the station in the cartesian coordinates (with LCARTESIAN=T only)

* :code:`XLAT_STAT` : latitude (in degrees) of the station (with LCARTESIAN=F only)

* :code:`XLON_STAT` : longitude (in degrees) of the station (with LCARTESIAN=F only)

* :code:`XZ_STAT` : height above the model orography (in meters) of the station

* :code:`CNAME_STAT` : name of the station

* :code:`CFILE_STAT` : name of the .csv file containing the definition of the stations (see below). If CFILE_STAT='NO_INPUT_CSV', the .csv file is not read.

* :code:`LDIAG_SURFRAD` : if True, the surface and radiation variables are written. You must also set N2M=2 in :ref:`nam_diag_surfn` for a correct saving of SURFEX variables.

.. note::

   If a .csv file is provided, coordinates given in the namelist will be ignored. The .csv file should follow the format example hereafter:

   .. code-block::

      Name, X[m]/Lat[deg], Y[m]/Lon[deg], Z[m]
      probe1, 50.0,  50.0, 10.0
      probe2, 50.0,   1.0, 11.25
      probe3, 350.0, 50.0, 10.0
      
   The values of X,Y or Lat/Lon are read depending on LCARTESIAN.

