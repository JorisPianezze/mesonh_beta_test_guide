.. _nam_param_mfshalln:

NAM_PARAM_MFSHALLn
-----------------------------------------------------------------------------

It contains the options retained for the EDKF shallow convection scheme used by the model n (CSCONV = "EDKF" in :ref:`nam_paramn`). Contrary to the "KAFR" scheme, "EDKF" can only be called at every time step. 

.. csv-table:: NAM_PARAM_MFSHALLn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "XIMPL_MF","REAL","1"
   "CMF_UPDRAFT","CHARACTER(LEN=4)","'EDKF'"
   "CMF_CLOUD","CHARACTER(LEN=4)","'DIRE'"
   "CWET_MIXING","CHARACTER(LEN=4)","'PKFB'"
   "CKIC_COMPUTE","CHARACTER(LEN=4)","'KFB'"
   "CDETR_DRY_LUP","CHARACTER(LEN=4)","'SURF'"
   "LMIXUV","LOGICAL","TRUE"
   "LMIXTKE","LOGICAL","FALSE"
   "LMF_FLX","LOGICAL","FALSE"
   "XALP_PERT","REAL","0.3"
   "XABUO","REAL","1.0"
   "XBENTR","REAL","1.0"
   "XBDETR","REAL","0.0"
   "XCMF","REAL","0.065"
   "XENTR_MF","REAL","0.035"
   "XCRAD_MF","REAL","50.0"
   "XENTR_DRY","REAL","0.55"
   "XDETR_DRY","REAL","10.0"
   "XDETR_LUP","REAL","1.0"
   "XKCF_MF","REAL","2.75"
   "XKRC_MF","REAL","1.0"
   "XTAUSIGMF","REAL","600.0"
   "XPRES_UV","REAL","0.5"
   "XALPHA_MF","REAL","2.0"
   "XSIGMA_MF","REAL","20.0"
   "XSIGMA_ENV","REAL","0.0"
   "XFRAC_UP_MAX","REAL","0.33"
   "XA1","REAL","2.0/3.0"
   "XB","REAL","0.002"
   "XC","REAL","0.012"
   "XBETA1","REAL","0.9"
   "XR","REAL","2.0"
   "LTHETAS_MF","LOGICAL",".FALSE."
   "LGZ","LOGICAL",".FALSE."
   "XGZ","REAL","1.83"
   "LVERLIMUP","LOGICAL",".TRUE."
   "LPZ_EXP_LOG","LOGICAL",".FALSE."
   "XBRIO","REAL","0"
   "XAADVEC","REAL","0"
   "LRELAX_ALPHA_MF","LOGICAL",".FALSE."


* :code:`XIMPL_MF` : degree of implicitness                                                        

* :code:`CMF_UPDRAFT` : type of Mass Flux Scheme ('EDKF', 'RHCJ' or 'NONE' )

* :code:`CMF_CLOUD` : type of statistical cloud ('DIRE' for the direct calculation of the cloud fraction as a function of the updraft fraction or 'STAT' given by the subgrid condensation scheme)

* :code:`CWET_MIXING` : type of env mixing for buoyancy sorting scheme ('PKFB' for the original Pergaud code, 'LR01' for :cite:t:`lappen_toward_2001`)

* :code:`CKIC_COMPUTE` : method to compute KIC ('KFB' to use the PMMC09 original method, like in KFB, 'RS08' to use the :cite:t:`de_rooy_simple_2008` formulation) 

* :code:`CDETR_DRY_LUP` : upward length to use in the dry detrainement ('SURF' to use :math:`L_{UP}` at surface (original PMMC09 :cite:t:`pergaud_parameterization_2009`),
 'UPDR' to compute :math:`L_{UP}` in updraft)
 
* :code:`LMIXUV` : flag to take into account the mixing on momentum      

* :code:`LMIXTKE` : flag to mix the prognostic variable TKE by updrafts. Only implemented with :code:`CMF_UPDRAFT='EDKF'`

* :code:`LMF_FLX` : flag to compute and store the mass fluxes on every synchronous output  file

* :code:`XALP_PERT` : coefficient for the perturbation of theta_l and r_t at the first level of the updraft

* :code:`XABUO` : coefficient of the buoyancy term in the w_up equation

* :code:`XBENTR` : coefficient of the entrainment term in the w_up equation

* :code:`XBDETR` : coefficient of the detrainment term in the w_up equation

* :code:`XCMF` : coefficient for the mass flux at the first level of the updraft (closure)

* :code:`XENTR_MF` : entrainment constant (m/Pa)

* :code:`XCRAD_MF` : cloud radius in cloudy part

* :code:`XENTR_DRY` : coefficient for entrainment in dry part

* :code:`XDETR_DRY` : coefficient for detrainment in dry part

* :code:`XDETR_LUP` : coefficient for detrainment in dry part

* :code:`XKCF_MF` : coefficient for cloud fraction

* :code:`XKRC_MF` : coefficient for convective rc

* :code:`XPRES_UV` : coefficient for pressure term in wind mixing

* :code:`XALPHA_MF` : coefficient for cloudy fraction

* :code:`XSIGMA_MF` : coefficient for sigma computation for the updraft (bi-Gaussian scheme)

* :code:`XSIGMA_ENV` : coefficient for sigma computation for the environment (bi-Gaussian scheme)

* :code:`XFRAC_UP_MAX` : maximum Updraft fraction

* :code:`XA1` : Tuning variable for RHCJ10 updraft 

* :code:`XB` : Tuning variable for RHCJ10 updraft

* :code:`XC` : Tuning variable for RHCJ10 updraft

* :code:`XBETA1` : Tuning variable for RHCJ10 updraft

* :code:`XR` : Aspect ratio of updraft

* :code:`LTHETAS_MF` : True to compute ThetaS from ThetaL

* :code:`LGZ` : flag to turn on the reduction of the mass-flux surface closure with the resolution. Must be used in the turbulence grey-zone (~500 meters horizontal resolution)

* :code:`XGZ` : parameter for the reduction the surface closure of the Mass-Flux thermal plume if LGZ = TRUE.

* :code:`LVERLIMUP` : flag to allow a smooth vertical decrease of the mass-flux as soon as the updraft reaches a specific altitude, instead of a sharp limit of 0.

* :code:`LPZ_EXP_LOG`: true to use exp/log during dP/dZ conversion to respect hydrostatic approximation to interpolate z and p between two half-level and full-level points,
 false to use linear interpolation (old interpolation, not recommended)

* :code:`XBRIO` : coefficient to slow down wup equa like :cite:t:`rio_resolved_2010`

* :code:`XAADVEC` : coefficient for advective pressure perturbation like :cite:t:`he_improved_2020`

* :code:`LRELAX_ALPHA_MF`: true to relax the small fraction assumption
