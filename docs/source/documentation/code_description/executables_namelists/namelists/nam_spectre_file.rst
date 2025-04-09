.. _nam_spectre_file:

NAM_SPECTRE_FILE
-----------------------------------------------------------------------------

.. csv-table:: NAM_SPECTRE_FILE content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "YINIFILE","ARRAY(CHARACTER(LEN=128))",""
   "CTYPEFILE","CHARACTER(LEN=6)","'MESONH'"
   "YOUTFILE","ARRAY(CHARACTER(LEN=128))",""
   "LSTAT","LOGICAL",".FALSE."

* :code:`YINIFILE` : name of the input synchronous backup file.

* :code:`CTYPEFILE` : type of the input  file ('AROME ', 'MESONH')

* :code:`YOUTFILE` : prefix of the output file.

  * If the user does specify this name, the output file will be named YOUTFILE_U, YOUTFILE_V ....
  * If the user does NOT specify this name, the output file will be named spectra_YINIFILE_U, spectra_YINIFILE_V ....

* :code:`LSTAT` : flag to have some statistiques on fields if .TRUE.
