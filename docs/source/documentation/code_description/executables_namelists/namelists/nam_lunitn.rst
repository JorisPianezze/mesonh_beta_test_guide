.. _nam_lunitn:

NAM_LUNITn
-----------------------------------------------------------------------------

.. csv-table:: NAM_LUNITn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CINIFILE","CHARACTER(LEN=128)","'INIFILE'"
   "CINIFILEPGD","CHARACTER(LEN=128)","' '"

* :code:`CINIFILE` : name of the initial Meso-NH file produced by :ref:`prep_ideal_case`, it will then be used as initial file in a :ref:`mesonh` simulation.

* :code:`CINIFILEPGD` : name of the PGD file if CSURF :math:`\neq` 'NONE' : 

  * If you use an input PGD file for the step :ref:`prep_ideal_case` (CPGD_FILE in :ref:`nam_real_pgd`), you must have CINIFILEPGD=CPGD_FILE.
  * If there is no input PGD, CINIFILEPGD is the name of the PGD file produced by :ref:`prep_ideal_case`.
