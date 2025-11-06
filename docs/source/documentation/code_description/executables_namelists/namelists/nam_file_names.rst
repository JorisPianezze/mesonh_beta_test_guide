.. _nam_file_names:

NAM_FILE_NAMES
-----------------------------------------------------------------------------

.. csv-table:: NAM_FILE_NAMES content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "HATMFILE","CHARACTER(LEN=128)","''"
   "HATMFILETYPE","CHARACTER(LEN=6)","'MESONH'"
   "HPGDFILE","CHARACTER(LEN=128)","''"
   "HSURFFILE","CHARACTER(LEN=128)","''"
   "HSURFFILETYPE","CHARACTER(LEN=6)","'MESONH'"
   "HCHEMFILE","CHARACTER(LEN=128)","''"
   "HCHEMFILETYPE","CHARACTER (LEN=6)","'MESONH'"
   "HCAMSFILE","CHARACTER(LEN=128)","''"
   "HCAMSFILETYPE","CHARACTER(LEN=6)","'NETCDF'"
   "CINIFILE","CHARACTER(LEN=128)","'INIFILE'"

* :code:`HATMFILE` : name of the atmospheric file.

* :code:`HATMFILETYPE` : type of  atmospheric file ('GRIBEX', 'MESONH')

* :code:`HPGDFILE` : name of the Physiographic Data File.

* :code:`HSURFFILE` : optional name of the file containing the surface fields.

* :code:`HSURFFILETYPE` : type of surface file ('GRIBEX', 'MESONH')

* :code:`HCHEMFILE` : optional name of the file containing the chemical species if they are not in the HATMFILE or if the ones of the HATMFILE are not used (only if HATMFILETYPE is 'GRIBEX'). The grids must be the same as the ones of the output file (CINIFILE).

* :code:`HCHEMFILETYPE` : type of the chemical file ('GRIBEX', 'MESONH', 'MOZART','CAMSEU'). MOZART and CAMSEU must be in netcdf format

* :code:`HCAMSFILE` : optional name of the CAMS file containing the aerosols species. The file must be a NETCDF.

* :code:`HCAMSFILETYPE` : type of the CAMS file ('NETCDF')

* :code:`CINIFILE` : name of the Meso-NH file, used as initial or coupling file in a Meso-NH simulation
