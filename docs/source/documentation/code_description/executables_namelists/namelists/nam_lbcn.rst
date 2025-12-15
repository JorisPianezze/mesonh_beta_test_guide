.. _nam_lbcn:

NAM_LBCn
-----------------------------------------------------------------------------

It contains the parameters needed to specify the lateral boundary conditions for the model n. They are included in the declarative module MODD_LBCn.

.. csv-table:: NAM_LBCn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "CLBCX","ARRAY(2*CHARACTER(LEN=4))","2*'CYCL'"
   "CLBCY","ARRAY(2*CHARACTER(LEN=4))","2*'CYCL'"
   "XCPHASE","REAL","20.0"
   "XCPHASE_PBL","REAL","0.0"
   "XCARPKMAX","REAL","XUNDEF"
   "XPOND","REAL","1.0"

* :code:`CLBCX` : represent the type of lateral boundary condition at the left and right boundaries along x (CLBCX(1) and CLBCX(2) respectively). The possible values are : 

  * 'CYCL' : for cyclic boundary conditions (in this case CLBCX(1)=CLBCX(2)='CYCL')
  * 'OPEN' : for open boundary condition (Sommerfeld equation for the normal velocity)
  * 'WALL' : for wall boundary condition (zero normal velocity)
  
* :code:`CLBCY` : array containing 2 elements: they represent the type of lateral boundary condition at the left and right boundaries along y (CLBCY(1) and CLBCY(2) respectively). The possible values are identical to those for CLBCX. 

* :code:`XCPHASE` : imposed phase velocity of the outgoing gravity waves. This phase velocity can be  used in the Sommerfeld equation which gives the temporal evolution of the normal velosity at the open lateral boundary.  

* :code:`XCPHASE_PBL` : imposed phase velocity of the outgoing gravity waves in the PBL. 

* :code:`XCARPKMAX` : maximum value (in :math:`s^{-1}`)  of the relaxation coefficient used to relaxe the normal wind in the Carpenter equation for open lbc conditions. If not specified, XCARPKMAX=1/(10.* XTSTEP), that is the advised value, is imposed.

* :code:`XPOND` : relaxation coefficient for LBC.
