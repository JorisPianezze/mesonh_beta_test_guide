.. _nam_real_pgd:

NAM_REAL_PGD
-----------------------------------------------------------------------------

.. csv-table:: NAM_REAL_PGD content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CPGD_FILE","CHARACTER(LEN=128)",""
   "LREAD_ZS","LOGICAL",".FALSE."
   "LREAD_GROUND_PARAM","LOGICAL",".FALSE."

* :code:`CPGD_FILE` : name of the physiographic data file containing the ground data fields. The file must be generated by the :program:`PRE_PGD` program.

.. note::

   * For a purely ideal case, the CPGD_FILE variable may be deleted from the namelist or set to its default value '  '. 
   
   * The horizontal grid will be read in the PGD file and therefore, the mesh increments XDELTAX and XDELTAY are no more used.

* :code:`LREAD_GROUND_PARAM` : Flag to use or not the surface cover types (COVERnnn) and all other physiographic fields (except orographic ones) read in the PGD file.

  * .TRUE. to read the data in the PGD file 
  * .FALSE. to use XUNIF_COVER idealized homogeneous values given in the namelist NAM_COVER (from the externalized surface) and scratch the PGD_FILE  data
  
* :code:`LREAD_ZS` : Flag to use or not the orography parameters read in the PGD file.

  * .TRUE. to use the data read in the PGD_FILE 
  * .FALSE. to use an idealized orography given in the namelist NAM\_GRIDH\_PRE and scratch the PGD_FILE  data
