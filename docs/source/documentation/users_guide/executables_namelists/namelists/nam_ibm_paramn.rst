.. _nam_ibm_paramn:

NAM_IBM_PARAMn
-----------------------------------------------------------------------------

.. csv-table:: NAM_IBM_PARAMn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LIBM","LOGICAL",".FALSE."
   "LIBM_TROUBLE","LOGICAL",".FALSE."
   "CIBM_ADV","CHARACTER(LEN=6)","'NOTHIN'"
   "XIBM_EPSI","REAL","1.E-9"
   "XIBM_RUG","REAL","0.01"
   "XIBM_CNU","REAL","0.06"
   "NIBM_LAYER_V","INTEGER","2"
   "NIBM_LAYER_T","INTEGER","2"
   "NIBM_LAYER_R","INTEGER","2"
   "NIBM_LAYER_E","INTEGER","2"
   "NIBM_LAYER_S","INTEGER","2"
   "CIBM_MODE_INTE3_V","CHARACTER(LEN=3)","'LAI'"
   "CIBM_MODE_INTE3_T","CHARACTER(LEN=3)","'LAI'"
   "CIBM_MODE_INTE3_R","CHARACTER(LEN=3)","'LAI'"
   "CIBM_MODE_INTE3_E","CHARACTER(LEN=3)","'LAI'"
   "CIBM_MODE_INTE3_S","CHARACTER(LEN=3)","'LAI'"
   "CIBM_MODE_INTE1NV","CHARACTER(LEN=3)","'CL2'"
   "CIBM_MODE_INTE1TV","CHARACTER(LEN=3)","'CL2'"
   "CIBM_MODE_INTE1CV","CHARACTER(LEN=3)","'CL2'"
   "CIBM_MODE_INTE1_T","CHARACTER(LEN=3)","'CL2'"
   "CIBM_MODE_INTE1_R","CHARACTER(LEN=3)","'CL2'"
   "CIBM_MODE_INTE1_E","CHARACTER(LEN=3)","'CL2'"
   "CIBM_MODE_INTE1_S","CHARACTER(LEN=3)","'CL2'"
   "XIBM_RADIUS_V","REAL","2.0"
   "XIBM_RADIUS_T","REAL","2.0"
   "XIBM_RADIUS_R","REAL","2.0"
   "XIBM_RADIUS_E","REAL","2.0"
   "XIBM_RADIUS_S","REAL","2.0"
   "XIBM_POWERS_V","REAL","1.0"
   "XIBM_POWERS_T","REAL","1.0"
   "XIBM_POWERS_R","REAL","1.0"
   "XIBM_POWERS_E","REAL","1.0"
   "XIBM_POWERS_S","REAL","1.0"
   "CIBM_MODE_BOUNN_V","CHARACTER(LEN=3)","'ASY'"
   "CIBM_MODE_BOUNT_V","CHARACTER(LEN=3)","'ASY'"
   "CIBM_MODE_BOUNC_V","CHARACTER(LEN=3)","'ASY'"
   "CIBM_MODE_BOUND_T","CHARACTER(LEN=3)","'SYM'"
   "CIBM_MODE_BOUND_R","CHARACTER(LEN=3)","'SYM'"
   "CIBM_MODE_BOUND_E","CHARACTER(LEN=3)","'SYM'"
   "CIBM_MODE_BOUND_S","CHARACTER(LEN=3)","'SYM'"
   "XIBM_FORC_BOUNN_V","REAL","0.0"
   "XIBM_FORC_BOUNT_V","REAL","0.0"
   "XIBM_FORC_BOUNC_V","REAL","0.0"
   "XIBM_FORC_BOUND_T","REAL","0.0"
   "XIBM_FORC_BOUND_R","REAL","0.0"
   "XIBM_FORC_BOUND_E","REAL","0.0"
   "XIBM_FORC_BOUND_S","REAL","0.0"
   "CIBM_TYPE_BOUNT_V","CHARACTER(LEN=3)","'DIR'"
   "CIBM_TYPE_BOUNN_V","CHARACTER(LEN=3)","'DIR'"
   "CIBM_TYPE_BOUNC_V","CHARACTER(LEN=3)","'DIR'"
   "CIBM_TYPE_BOUND_T","CHARACTER(LEN=3)","'NEU'"
   "CIBM_TYPE_BOUND_R","CHARACTER(LEN=3)","'NEU'"
   "CIBM_TYPE_BOUND_E","CHARACTER(LEN=3)","'NEU'"
   "CIBM_TYPE_BOUND_S","CHARACTER(LEN=3)","'NEU'"
   "CIBM_FORC_BOUNN_V","CHARACTER(LEN=3)","'CST'"
   "CIBM_FORC_BOUNT_V","CHARACTER(LEN=3)","'CST'"
   "CIBM_FORC_BOUNC_V","CHARACTER(LEN=3)","'CST'"
   "CIBM_FORC_BOUNR_V","CHARACTER(LEN=3)","'CST'"
   "CIBM_FORC_BOUND_T","CHARACTER(LEN=3)","'CST'"
   "CIBM_FORC_BOUND_R","CHARACTER(LEN=3)","'CST'"
   "CIBM_FORC_BOUND_E","CHARACTER(LEN=3)","'CST'"
   "CIBM_FORC_BOUND_S","CHARACTER(LEN=3)","'CST'"

* :code:`LIBM` : Flag to activate Immersed Boundary Method (IBM) or not. 

  * .TRUE.: Immersed Boundary Method is activated.
  * .FALSE.: Immersed Boundary Method is not activated.
  
.. warning::

   In their current version, IBM can only be used in combination with flat terrain (LFLAT=.TRUE.), cartesian coordinates (LCARTESIAN=.TRUE.), and near-neutral atmospheric conditions. It is furthermore recommended to use IBM in combination with the WENO5 or WENO3 momentum advection scheme.

* :code:`LIBM_TROUBLE` : Flag to deal with too small obstacles or too small space in between obstacles (underresolved obstacles). Recommended is to filter the  obstacles during the preprocessing and not to use LIBM_TROUBLE=.TRUE..

  * .TRUE.: Flag to deal with too small obstacles is activated.
  * .FALSE.: Flag to deal with too small obstacles is not activated.

* :code:`CIBM_ADV` : How to deal with the Immersed Boundary Conditions in the Runge Kutta time stepping. Recommended is 'LOWORD'.

  * 'NOTHIN': Nothing special is done - One ghost cell technique forcing is used per time step and the same advection scheme (WENO or CENTERED) is used close to the obstacles than in the rest of the model domain.
  * 'LOWORD': Low order - One ghost cell technique forcing is used per time step and a lower order advection scheme (WENO3 instead of WENO5 or CEN2 instead of CEN4) is used close to the obstacles.
  * 'FORCIN': Forcing - The ghost cell technique is used at all intermediate time steps of the Runge Kutta scheme.
  * 'FREEZE': Freeze - A quasi-static approach for the Immersed Boundary Conditions is used at the intermediate time steps of the Runge Kutta scheme.

* :code:`XIBM_EPSI` : Very small REAL number value to be used in computations related to the Immersed Boundary Method.
  
* :code:`XIBM_RUG` : Aerodynamical roughness length [m] of obstacles. A constant value is used for all obstacles.
  
* :code:`XIBM_CNU` : Parameter in the IBM wall model.

* :code:`NIBM_LAYER_V,T,R,E,S` : Number of ghost point layers for wind velocity components, potential temperature,mixing ratio of water vapour, subgrid turbulekinetic energy, mixing ratio of scalar variables.

* :code:`CIBM_MODE_INTE3_V,T,R,E,S` : Method for 3D interpolation to calculate the values of wind velocity, potential temperature,mixing ratio of water vapour,subgrid turbulent kinetic energy, mixing ratio of scalar variables at mirror, image1, and image2 points.

  * 'LAI': Inverse distance weighting.
  * 'LAM': Modified distance weighting.

* :code:`CIBM_MODE_INTE1_NV,TV,CV` : Method for 1D interpolation to calculate the value of velocity normal,tangential,tangential to the obstacles at ghost points.

  * 'CL1': Lagrange Polynomials - 1 point.
  * 'CL2': Lagrange Polynomials - 2 points.
  * 'CL3': Lagrange Polynomials - 3 points.

* :code:`CIBM_MODE_INTE1_T,R,E,S` : Method for 1D interpolation to calculate the value of potential temperature,mixing ratio of water vapour,subgrid turbulent kinetic energy,mixing ratio of scalar variables at ghost points.
  
  * 'CL1': Lagrange Polynomials - 1 point.
  * 'CL2': Lagrange Polynomials - 2 points.
  * 'CL3': Lagrange Polynomials - 3 points.

* :code:`XIBM_RADIUS_V,T,R,E,S` : Radius (in number of grid points) for modified distance weighting ('LAM') of wind velocity components,potential temperature, mixing ratio of water vapour,subgrid turbulent kinetic energy,mixing ratio of scalar variables.

* :code:`XIBM_POWERS_V,T,R,E,S` : Exponent to be used in inverse ('LAI') or modified distance weighting ('LAM') of wind velocity components,potential temperature, mixing ratio of water vapour,subgrid turbulent kinetic energy,mixing ratio of scalar variables.
       
* :code:`CIBM_MODE_BOUNN,T,C_V` : The way the value at the ghost point for wind velocity normal,tangential,tangential to the obstacles is calculated based on the value at the image point and the value at the interface.

  * 'SYM': Symmetrical: VALUE_GHOST = VALUE_IMAGE.
  * 'ASY': Asymmetrical: VALUE_GHOST = -VALUE_IMAGE + 2.*VALUE_INTERFACE.
  * 'CST': Constant: VALUE_GHOST = VALUE_INTERFACE.

* :code:`CIBM_MODE_BOUND_T,R,E,S` : The way the value at the ghost point for potential temperature,mixing ratio of water vapour,subgrid turbulent kinetic energy,mixing ratio of scalar variables is calculated based on the value at the image point and the value at the interface.

  * 'SYM': Symmetrical: VALUE_GHOST = VALUE_IMAGE.
  * 'ASY': Asymmetrical: VALUE_GHOST = -VALUE_IMAGE + 2.*VALUE_INTERFACE.
  * 'CST': Constant: VALUE_GHOST = VALUE_INTERFACE.

* :code:`XIBM_FORC_BOUNN,T,C_V` : The value of the boundary condition for wind velocity normal,tangential,tangential to the obstacles specified at the interface. 
  
* :code:`XIBM_FORC_BOUND_T,R,E,S` : The value of the boundary condition for potential temperature,water vapour mixing ratio,subgrid turbulent kinetic energy,mixing ratio of scalar variables specified at the interface. 

* :code:`CIBM_TYPE_BOUNN,T,C_V` : The type of boundary condition for wind velocity normal,tangential,tangential to the obstacles.

  * 'DIR': Dirichlet boundary condition - the value of the boundary condition is the value of the parameter.
  * 'NEU': Neumann boundary condition - the value of the boundary condition is the gradient of the parameter.
  * 'ROB': Robin boundary condition - linear combination between Dirichlet and Neumann.

* :code:`CIBM_TYPE_BOUND_T,R,E,S` : The type of boundary condition for potential temperature,mixing ratio of water vapour,subgrid turbulent kinetic energy,mixing ratio of scalar variables.  

  * 'DIR': Dirichlet boundary condition - the value of the boundary condition is the value of the parameter.
  * 'NEU': Neumann boundary condition - the value of the boundary condition is the gradient of the parameter.
  * 'ROB': Robin boundary condition - linear combination between Dirichlet and Neumann.

* :code:`CIBM_FORC_BOUNN,T,C_V` : The way to calculate the value at the interface for wind velocity normal,tangential,tangential to the obstacles.

  * 'CST': VALUE_INTERFACE is taken.
  * 'WN1': A wall model is activated between the first layer image point and the interface.
  * 'WN3': A wall model is activated between the second layer image point and the interface.

* :code:`CIBM_FORC_BOUND_T,R,E,S` : The way to calculate the value at the interface for potential temperature,mixing ratio of water vapour,subgrid turbulent kinetic energy,mixing ratio of scalar variables.

  * 'CST': VALUE_INTERFACE is taken.
  * 'WN1': A wall model is activated between the first layer image point and the interface.
  * 'WN3': A wall model is activated between the second layer image point and the interface.

* :code:`CIBM_FORC_BOUNR_V` : Parameter for the interpolation when performing the change of basis (u,v,w) to (n,t,c) of the wind vector close to the obstacles.

  * 'CST': Interpolation in the direction of the first image layer.
  * 'LIN': Linear evolution between first and second image layer.

