.. _nam_lunitn:

NAM_LUNITn
-----------------------------------------------------------------------------

.. csv-table:: NAM_LUNITn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CINIFILE","CHARACTER(LEN=128)","'INIFILE'"
   "CINIFILEPGD","CHARACTER(LEN=128)","' '"

* :code:`CINIFILE` : name of the initial FM-file produced by :program:`PREP_IDEAL_CASE`, it will then be used as initial file in a :program:`MESONH` simulation.

* :code:`CINIFILEPGD` : name of the PGD file if CSURF :math:`\neq` 'NONE' : 

  * If you use an input PGD file for the step :program:`PREP_IDEAL_CASE` (CPGD_FILE in NAM_REAL_PGD), you must have CINIFILEPGD=CPGD_FILE.
  * If there is no input PGD, CINIFILEPGD is the name of the PGD file produced by :program:`PREP_IDEAL_CASE`.
