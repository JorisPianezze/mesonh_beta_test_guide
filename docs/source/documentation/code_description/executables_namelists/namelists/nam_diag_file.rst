.. _nam_diag_file:

NAM_DIAG_FILE
-----------------------------------------------------------------------------

.. csv-table:: NAM_DIAG_FILE content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "YINIFILE","array of character (len=NFILENAMELGTMAX)",""
   "YINIFILEPGD","array of character (len=NFILENAMELGTMAX)",""
   "YSUFFIX","character (len=5)","_DIAG"


* YINIFILE : name of the input synchronous backup files.

* YINIFILEPGD : name of the PGD file associated to YINIFILE.

* YSUFFIX : suffix appended to input file name to form output file name.
