.. _nam_lbcn_pre:

NAM_LBCn_PRE
-----------------------------------------------------------------------------

.. csv-table:: NAM_LBCn_PRE content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CLBCX","ARRAY(2 CHARACTERS(LEN=4))","2*'CYCL'"
   "CLBCY","ARRAY(2 CHARACTERS(LEN=4))","2*'CYCL'"

* :code:`CLBCX` : represent the type of lateral boundary condition at the left and right boundaries along x (CLBCX(1) and CLBCX(2) respectively). Possible values are :

  * 'CYCL' : for cyclic boundary condition
  * 'OPEN' : for open boundary condition
  * 'WALL' : for rigid wall boundary condition
  
.. note::

   * It should be note that CLBCX(1) or CLBCY(1) refers to the lowest index values ( IIB , IJB for X and Y directions) and CLBCX(2) or CLBCY(2) to the highest index values (IIE  and IJE). 
   
   * The same boundary conditions must be used for the MESO-NH run itself} (see EXSEG1.nam namelist)
   
   * Note also that CYCLIC conditions are not possible with a PGD file (CPGD_FILE different to '  ' in NAM_REAL_PGD).

* :code:`CLBCY` : same as CLBCX but for the left and right boundaries along y (CLBCY(1) and CLBCY(2) respectively). They are strings of 4 characters.
