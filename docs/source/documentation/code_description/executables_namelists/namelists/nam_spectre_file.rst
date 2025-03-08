.. _nam_spectre_file:

NAM_SPECTRE_FILE
-----------------------------------------------------------------------------

.. csv-table:: NAM_SPECTRE_FILE content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "YINIFILE","array of character (len=NFILENAMELGTMAX)",""
   "CTYPEFILE","character (LEN=6)","'MESONH'"
   "YOUTFILE","array of character (len=NFILENAMELGTMAX)",""
   "LSTAT","logical",".FALSE."

* YINIFILE : name of the input synchronous backup file.

* CTYPEFILE : type of the input  file ('AROME ', 'MESONH')

* YOUTFILE  : prefix of the output file.

  * If the user does specify this name, the output file will be named YOUTFILE_U, YOUTFILE_V ....
  * If the user does NOT specify this name, the output file will be named spectra_YINIFILE_U, spectra_YINIFILE_V ....

* LSTAT : flag to have some statistiques on fields if .TRUE.
