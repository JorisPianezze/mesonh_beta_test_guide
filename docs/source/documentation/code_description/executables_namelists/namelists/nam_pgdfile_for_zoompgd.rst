.. _nam_pgdfile_for_zoompgd:

NAM_PGDFILE
-----------------------------------------------------------------------------

.. csv-table:: NAM_PGDFILE content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CPGDFILE", "CHARACTER(LEN=128)", ""
   "YZOOMFILE","CHARACTER(LEN=128)",""
   "YZOOMNBR","CHARACTER(LEN=2)","'00'"

* :code:`CPGDFILE` : name of the input Physiographic Data File.

* :code:`YZOOMFILE` : optional name of the zoomned FM-file (output file). If the user does not specify this name, or if YZOOMFILE = CPGDFILE, the code builds the zoomned FM-file name as: YZOOMFILE = CPGDFILE.zYZOOMNBR.

* :code:`YZOOMNBR` : NumBeR which will be added to CPGDFILE to generate the name of the Zoomned FM-file.
