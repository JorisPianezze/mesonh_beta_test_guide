.. _nam_ch_solvern:

NAM_CH_SOLVERn
-----------------------------------------------------------------------------

.. csv-table:: NAM_CH_SOLVERn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CSOLVER","CHARACTER(LEN=32)","'EXQSSA'"
   "NSSA","INTEGER","0"
   "NSSAINDEX","ARRAY(INTEGER)","1000*0"
   "XRTOL","REAL","0.001"
   "XATOL","REAL","0.1"
   "NRELAB","INTEGER","2"
   "NPED","INTEGER","1"
   "NMAXORD","INTEGER","5"
   "LPETZLD","LOGICAL",".TRUE."
   "CMETHOD","CHARACTER(LEN=1)","N"
   "CNORM","CHARACTER(LEN=1)","A"
   "NTRACE","INTEGER","0"
   "XALPHA","REAL","0.5"
   "XSLOW","REAL","100.0"
   "XFAST","REAL","0.1"
   "NQSSAITER","INTEGER","1"
   "XDTMIN","REAL","0.1"
   "XDTMAX","REAL","600.0"
   "XDTFIRST","REAL","10.0"

* :code:`CSOLVER` : type of numerical method used to resolve the ode system of coupling differential equations for chemistry (chemistry solver). for the description of each method, see the associated  ch\_routine. rosenbrock'method are gouped in mode\_RBK90\_Integrator routine. possible values are: 

  * 'SIS'
  * 'LINSSA'
  * 'CRANCK'
  * 'QSSA'
  * 'EXQSSA'
  * 'ROS1'
  * 'ROS2'
  * 'ROS3'
  * 'ROS4'
  * 'RODAS3'
  * 'RODAS4'
  * 'ROSENBROCK': default method ROS1 with ROSENBROCK

* :code:`NSSA` : number of variables to be treated as "steady state".

* :code:`NSSAINDEX` : index set of steady state variables.

* :code:`XRTOL` : relative tolerance for SVODE and D02EAF, D02EBF, D02NBF methods.

* :code:`XATOL` : absolute tolerance for SVODE and D02NBF.

* :code:`NRELAB` : choose relative error for NAG's D02EBF solver:

  * 1 : for correct decimal places
  * 2 : for correct significant digits
  * 0 : for a mixture

* :code:`NPED` : calculation parameter of the Jacobian matric for SVODE and NAG's D02EBF/D02NBF solvers:

  * 1 : for analytical Jacobian (using subroutine CH_JAC)
  * 0 : for numerical Jacobian

* :code:`NMAXORD` : maximum order for the BDF method (0<NMAXORD<=5) for NAG's D02NBF solver.

* :code:`LPETZLD` : switch to activate Petzold local error test (recommended) for NAG's D02NBF solver.

* :code:`CMETHOD` : method to use non-linear system for NAG's D02NBF solver.

  * 'N' or 'D' : modified Newton iteration
  * 'F' : functional iteration

* :code:`CNORM` : type of norm to be used for NAG's D02NBF solver.

  * 'A' or 'D' : averaged L2 norm
  * 'M' : maximum norm

* :code:`NTRACE` : level of output from D02NBF solver:

  * -1 : no output
  * 0 : only warnings are printed
  * >= 1 : details on Jacobian entries, nonlinear iteration and time integration are given 

* :code:`XALPHA` : the Cranck-Nicholson parameter (0,1).

* :code:`XSLOW` : slow species, lifetime > XSLOW * timestep for EXQSSA and QSSA methods.

* :code:`XFAST` : fast species, lifetime < XFAST * timestep for EXQSSA and QSSA methods.

* :code:`NQSSAITER` : number of iterations in QSSA method.

* :code:`XDTMIN` : minimal allowed timestep for EXQSSA.

* :code:`XDTMAX` : maximal allowed timestep for EXQSSA.

* :code:`XDTFIRST` : timestep for first integration step of EXQSSA.

