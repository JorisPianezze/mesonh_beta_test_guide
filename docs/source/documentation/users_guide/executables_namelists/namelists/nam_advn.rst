.. _nam_advn:

NAM_ADVn
-----------------------------------------------------------------------------

It contains the different advection schemes for dynamic variables (u,v and w), scalar meteorological variables (temperature, water substances, TKE) and tracers used by the model n. 

.. csv-table:: NAM_ADVn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CUVW_ADV_SCHEME","CHARACTER(LEN=6)","'CEN4TH'"
   "CMET_ADV_SCHEME","CHARACTER(LEN=6)","'PPM_01'"
   "CSV_ADV_SCHEME","CHARACTER(LEN=6)","'PPM_01'"
   "CTEMP_SCHEME","CHARACTER(LEN=4)","'RKC4'"
   "NWENO_ORDER","INTEGER","3"
   "LSPLIT_CFL","LOGICAL",".TRUE."
   "LSPLIT_WENO","LOGICAL",".TRUE."
   "XSPLIT_CFL","REAL","0.8"
   "LCFL_WRIT","LOGICAL",".FALSE."

* :code:`CUVW_ADV_SCHEME` : Advection scheme used for horizontal and vertical velocities. The following options are possible : 

  * 'WENO_K' : WENO odd ordered advection scheme
  * 'CEN2ND' : 2nd order advection scheme CENtred on space and time
  * 'CEN4TH' : 4th order advection scheme CENtred on space and time

* :code:`CMET_ADV_SCHEME` : Advection scheme used for the following METeorological variables: temperature, water substances and TKE. The following options are possible : 

  * 'PPM_00' : PPM advection scheme without constraint
  * 'PPM_01' : Monotonic version of PPM. It is POSITIVE definite.

* :code:`CSV_ADV_SCHEME` : Advection scheme used for the tracer variables. The same options as CMET_ADV_SCHEME can be used.

.. note::
  
   Note that if LLG=T in NAM_CONF, CSV_ADV_SCHEME must be equal to CMET_ADV_SCHEME.

* :code:`CTEMP_SCHEME` : Temporal scheme for momentum advection (the rest of the model is in Forward In Time). The following options are possible :

  * 'LEFR' : Leap-Frog scheme (only for CEN4TH or CEN2ND wind schemes)
  * 'RKC4' : Runge-Kutta centred 4th order (recommended for CEN4TH)
  * 'RK53' : Runge-Kutta 5 steps 3th order  (recommended for WENO5 and WENO3)
  * 'RK33' : Runge-Kutta 3 steps 3th order 
  * 'RK21' : Runge-Kutta 2 steps 1st order 

* :code:`NWENO_ORDER` : Order of WENO scheme for CUVW_ADV_SCHEME. For the moment, the 3rd order and the 5th order are available.

* :code:`LSPLIT_CFL` : Flag to split PPM advection as a function of CFL

* :code:`XSPLIT_CFL` : Allowed CFL maximum value for LSPLIT_CFL=T.  

* :code:`LSPLIT_WRITE` : Flag to store CFL fields on every output synchronous file.

* :code:`LSPLIT_WENO` : Flag to split WENO momentum advection
