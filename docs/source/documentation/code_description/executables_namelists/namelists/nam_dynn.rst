.. _nam_dynn:

NAM_DYNn
-----------------------------------------------------------------------------

It contains the specific dynamic parameters for the model n. They are included in the module MODD_DYNn. 

.. csv-table:: NAM_DYNn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XTSTEP","REAL","60.0"
   "CPRESOPT","CHARACTER(LEN=4)","'CRESI'"
   "NITR","INTEGER","4"
   "LRES","LOGICAL",".FALSE."
   "XRES","REAL","1.E-07"
   "LITRADJ","LOGICAL",".TRUE."
   "XRELAX","REAL","1.0"
   "LHORELAX_UVWTH","LOGICAL",".FALSE."
   "LHORELAX_RV","LOGICAL",".FALSE."
   "LHORELAX_RC","LOGICAL",".FALSE."
   "LHORELAX_RR","LOGICAL",".FALSE."
   "LHORELAX_RI","LOGICAL",".FALSE."
   "LHORELAX_RS","LOGICAL",".FALSE."
   "LHORELAX_RG","LOGICAL",".FALSE."
   "LHORELAX_RH","LOGICAL",".FALSE."
   "LHORELAX_TKE","LOGICAL",".FALSE."
   "LHORELAX_SV","array LOGICAL",".FALSE."
   "LHORELAX_SVC2R2","LOGICAL",".FALSE."
   "LHORELAX_SVC1R3","LOGICAL",".FALSE."
   "LHORELAX_SVLG","LOGICAL",".FALSE."
   "LHORELAX_SVCHEM","LOGICAL",".FALSE."
   "LHORELAX_SVDST","LOGICAL",".FALSE."
   "LHORELAX_SVPP","LOGICAL",".FALSE."
   "LHORELAX_SVAER","LOGICAL",".FALSE."
   "LHORELAX_SVFIRE","LOGICAL",".FALSE."
   "LVE_RELAX","LOGICAL",".FALSE."
   "LVE_RELAX_GRD","LOGICAL",".FALSE."
   "NRIMX","INTEGER","1"
   "NRIMY","INTEGER","1"
   "XRIMKMAX","REAL","1 / (100*60.)"
   "XT4DIFU","REAL","1800.0"
   "XT4DIFTH","REAL","1800.0"
   "XT4DIFSV","REAL","1800.0"
   "LOCEAN","LOGICAL",".FALSE."

* :code:`XTSTEP` : Time step in seconds. If the model is not the DAD model, XTSTEP is not taken into account but NDTRATIO in :ref:`nam_nesting`.

* :code:`CPRESOPT` : Pressure solver option. 3 choices are implemented in Meso-NH for the moment (see the Scientific documentation for more details) : 

  * 'RICHA' Richardson method preconditionned by the flat cartesian operator   
  * 'CGRAD' Generalized pre-conditioned gradient for non-symmetric problems with the same preconditioner
  * 'CRESI' Conjugate Residual method
  * 'ZRESI' Parallelized version of Conjugate Residual method

.. note::

   If the problem is flat and cartesian, then the resolution becomes exact and no iteration is performed.

* :code:`NITR` : Number of iterations for the pressure solver. The value of this parameter depends on the maximum slope of the orography in the model. This parameter cannot be set in a restarted simulation (CCONF='RESTA') because the value of the previous timestep is used to ensure reproducibility between restarted and non-restarted runs.

* :code:`LRES` : flag to change the residual divergence limit

* :code:`XRES` : Value of the residual divergence limit

* :code:`LITRADJ` : Logical to adjust the number of iterations for the  pressure solver according to the range of the residual divergence. 

* :code:`XRELAX` : Relaxation coefficient in the Richardson method (CPRESOPT='RICHA'). This value can be less than 1 only for very steep orography, in general, the optimal value is equal to 1.

* :code:`LHORELAX_UVWTH` : Flag for the horizontal relaxation applied on the outermost verticals of the model for U,V,W TH variables. 

  * .TRUE. The horizontal relaxation is applied 
  * .FALSE. The horizontal relaxation is not applied 

.. note::

   * LHORELAX_RV, LHORELAX_RC, LHORELAX_RR, LHORELAX_RI, LHORELAX_RS, LHORELAX_RG, LHORELAX_RH, LHORELAX_TKE, LHORELAX_SV, LHORELAX_SVCHEM, LHORELAX_SVC2R2, LHORELAX_SVC1R3, LHOREAX_SVLG, LHORELAX_SVDST, LHORELAX_SVPP, LHORELAX_SVAER, LHORELAX_SVELEC, LHORELAX_SVSNW, LHORELAX_SVFIRE : same as LHORELAX_UVWTH

   * It is safer to set all the LHORELAX values rather than use their default values which can be modified by the desfm file.

* :code:`LVE_RELAX` : Flag for the vertical relaxation applied to the outermost verticals of the model. 

  * .TRUE. The vertical relaxation is applied 
  * .FALSE. The vertical relaxation is not applied 

* :code:`LVE_RELAX_GRD` : Flag for the vertical relaxation applied to the lowest verticals of the model. 

  * .TRUE. The vertical relaxation is applied 
  * .FALSE. The vertical relaxation is not applied 

* :code:`NRIMX` : number of points in the lateral relaxation  in the x axis. 

* :code:`NRIMY` : number of points in the lateral relaxation  in the Y axis.

* :code:`XRIMKMAX` : maximum value (in :math:`s^{-1}`)  of the relaxation coefficient for the lateral relaxation area. This value is applied to all the outermost verticals of the domain if LHO_RELAX. 

* :code:`XT4DIFU` : characteristic time (e-folding time) of the fourth order numerical diffusion for momentum (in seconds). Associated to LNUMDIFU in :ref:`nam_dyn`.

* :code:`XT4DIFTH` : characteristic time (e-folding time)  of the numerical diffusion of fourth order for meteorological variables (in seconds). Associated to LNUMDIFTH in :ref:`nam_dyn`.

* :code:`XT4DIFSV` : characteristic time (e-folding time)  of the numerical diffusion of fourth order for scalar variables (in seconds). Associated to LNUMDIFSV in :ref:`nam_dyn`.

* :code:`LOCEAN` : flag to activate the Ocean version of Meso-NH. Pronostic variables are: Current (U and V), Vertical velocity (W), Temperature (TH), Subgrid Turbulent Kinetic Energy (TKE). Salinity (RV) can be activated with LUSERV=T. The Z-axis is directed upward (as in the atmosphere version), i.e. top of model domain corresponds to the sea surface. 

