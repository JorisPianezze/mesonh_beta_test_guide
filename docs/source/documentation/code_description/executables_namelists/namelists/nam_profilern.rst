.. _nam_profilern:

NAM_PROFILERn
-----------------------------------------------------------------------------

This namelist is used to configure virtual vertical profilers by using the following described parameters or a .csv file. Calculations are done for all the nested models for which the namelist is provided and recorded in the corresponding diachronic files. 

.. csv-table:: NAM_PROFILERn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "NNUMB_PROF","INTEGER","0"
   "XSTEP_PROF","REAL","60.0"
   "XX_PROF","REAL(:)","NNUMB_PROF * XUNDEF"
   "XY_PROF","REAL(:)","NNUMB_PROF * XUNDEF"
   "XLAT_PROF","REAL(:)","NNUMB_PROF * XUNDEF"
   "XLON_PROF","REAL(:)","NNUMB_PROF * XUNDEF"
   "XZ_PROF","REAL(:)","NNUMB_PROF * XUNDEF"
   "CNAME_PROF","ARRAY(CHARACTER(LEN=10))","NNUMB_PROF * ' '"
   "CFILE_PROF","CHARACTER(LEN=128)","'NO_INPUT_CSV'"
   "LDIAG_SURFRAD","LOGICAL","TRUE"

* :code:`NNUMB_PROF` : number of profilers. Limited to 100 if not using a .csv file.

* :code:`XSTEP_PROF` : time (in seconds) between two sampling written in the diachronic file

* :code:`XX_PROF` : X-position (in meters) of the profiler in the cartesian coordinates (with LCARTESIAN=T only)

* :code:`XY_PROF` : Y-position (in meters) of the profiler in the cartesian coordinates (with LCARTESIAN=T only)

* :code:`XLAT_PROF` : latitude (in degrees) of the profiler (with LCARTESIAN=F only)

* :code:`XLON_PROF` : longitude (in degrees) of the profiler (with LCARTESIAN=F only)

* :code:`XZ_PROF` : height above the model orography (in meters) of the profiler

* :code:`CNAME_PROF` : name of the profiler

* :code:`CFILE_PROF` : name of the .csv file containing the definition of the profilers (see below). If CFILE_PROF='NO_INPUT_CSV', the .csv file is not read.

* :code:`LDIAG_SURFRAD` : if True, the surface and radiation variables are written. You must also set N2M=2 in :ref:`nam_diag_surfn` for a correct saving of SURFEX variables.

.. note::

   If a .csv file is provided, coordinates given in the namelist will be ignored. The .csv file should follow the format example hereafter:
   
   .. code-block::

      Name, X[m]/Lat[deg], Y[m]/Lon[deg], Z[m]
      prof1, 50.0,  50.0, 10.0
      prof2, 50.0,   1.0, 11.25
      prof3, 350.0, 50.0, 10.0

   The values of X,Y or Lat/Lon are read depending on LCARTESIAN.

