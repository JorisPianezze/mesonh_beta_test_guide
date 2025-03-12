.. _nam_param_kafrn:

NAM_PARAM_KAFRN
-----------------------------------------------------------------------------

.. csv-table:: NAM_PARAM_KAFRN content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XDTCONV","real","MAX(300.0,XTSTEP)"
   "NICE","integer","1"
   "LREFRESH_ALL","logical","TRUE"
   "LCHTRANS","logical","FALSE"
   "LDOWN","logical","TRUE"
   "LSETTADJ","logical","FALSE"
   "XTADJD","real","3600"
   "XTADJS","real","10800"
   "LDIAGCONV","logical","FALSE"
   "NENSM","integer","0"

* XDTCONV : timestep for the call of the convective scheme. Maximum value is 300s. 

* NICE : flag to include ice proceses in convection scheme ( 1 = yes, 0 = no ice ).

* LREFRESH_ALL : flag to refresh convective columns at every call of the convection scheme.

* LCHTRANS: flag to take into account the convective transport for scalar variables (chemical variables, passive pollutants\ldots). Can only be used with the options CDCONV='KAFR'.

* LDOWN : flag to use downdrafts in deep convection.

* LSETTADJ : flag to allow user to define adjustment time.

* XTADJD : deep convective adjustment time (if LSETTADJ=TRUE).

* XTADJS : shallow convective adjustment time (if LSETTADJ=TRUE).

* LDIAGCONV : flag to store diagnostic variables in module MODD_DEEP_CONVECTIONn: (CAPE, deep and shallow convective cloud top and base levels, up-and downdraft mass fluxes).

* NENSM : number of additional convective ensemble members for deep convection (for the moment limited to 3).
