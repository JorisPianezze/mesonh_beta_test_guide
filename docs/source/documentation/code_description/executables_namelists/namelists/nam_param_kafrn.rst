.. _nam_param_kafrn:

NAM_PARAM_KAFRN
-----------------------------------------------------------------------------

.. csv-table:: NAM_PARAM_KAFRN content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XDTCONV","REAL","MAX(300.0,XTSTEP)"
   "NICE","INTEGER","1"
   "LREFRESH_ALL","LOGICAL",".TRUE."
   "LCHTRANS","LOGICAL",".FALSE."
   "LDOWN","LOGICAL",".TRUE."
   "LSETTADJ","LOGICAL",".FALSE."
   "XTADJD","REAL","3600"
   "XTADJS","REAL","10800"
   "LDIAGCONV","LOGICAL",".FALSE."
   "NENSM","INTEGER","0"

* :code:`XDTCONV` : timestep for the call of the convective scheme. Maximum value is 300s. 

* :code:`NICE` : flag to include ice proceses in convection scheme ( 1 = yes, 0 = no ice ).

* :code:`LREFRESH_ALL` : flag to refresh convective columns at every call of the convection scheme.

* :code:`LCHTRANS` : flag to take into account the convective transport for scalar variables (chemical variables, passive pollutants, ...). Can only be used with the options CDCONV='KAFR'.

* :code:`LDOWN` : flag to use downdrafts in deep convection.

* :code:`LSETTADJ` : flag to allow user to define adjustment time.

* :code:`XTADJD` : deep convective adjustment time (if LSETTADJ=TRUE).

* :code:`XTADJS` : shallow convective adjustment time (if LSETTADJ=TRUE).

* :code:`LDIAGCONV` : flag to store diagnostic variables in module MODD_DEEP_CONVECTIONn (CAPE, deep and shallow convective cloud top and base levels, up-and downdraft mass fluxes).

* :code:`NENSM` : number of additional convective ensemble members for deep convection (for the moment limited to 3).
