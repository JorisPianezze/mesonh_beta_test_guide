.. _nam_ibm_lsf:

NAM_IBM_LSF
-----------------------------------------------------------------------------

.. csv-table:: NAM_IBM_LSF content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LIBM_LSF","LOGICAL",".FALSE."
   "CIBM_TYPE","CHARACTER(LEN=4)","'NONE'"
   "NIBM_SMOOTH","INTEGER","1"
   "XIBM_SMOOTH","REAL","0.0001"

* :code:`LIBM_LSF` : Flag to calculate LevelSet Function (the minimum distance to the obstacles) or not.

  * .TRUE.: The LevelSet Function is calculated.
  * .FALSE.: The LevelSet Function is not calculated.

* :code:`CIBM_TYPE` : The way the obstacles are described.

  * 'NONE': No obstacles.
  * 'IDEA': Idealised ellipsoide or parallelepiped obstacles that are described in the additional namelist :file:`ibm_idea.nam`.
  * 'GENE': Generic user defined obstacles in .obj format.

* :code:`NIBM_SMOOTH` : The number of iterations for smoothing the LevelSet Function. In the case a considerable smoothing shall be done, it is recommended to use NIBM_SMOOTH=10.

* :code:`XIBM_SMOOTH` : The characteristic length scale used for smoothing the LevelSet Function. It is recommended to use a value of XIBM_SMOOTH close to the grid size.
