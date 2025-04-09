.. _nam_diag_file:

NAM_DIAG_FILE
-----------------------------------------------------------------------------

.. csv-table:: NAM_DIAG_FILE content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "YINIFILE","ARRAY(CHARACTER(LEN=128))",""
   "YINIFILEPGD","ARRAY(CHARACTER(LEN=128))",""
   "YSUFFIX","ARRAY(CHARACTER(LEN=5))","_DIAG"


* :code:`YINIFILE` : name of the input synchronous backup files.

* :code:`YINIFILEPGD` : name of the PGD file associated to YINIFILE.

* :code:`YSUFFIX` : suffix appended to input file name to form output file name.
