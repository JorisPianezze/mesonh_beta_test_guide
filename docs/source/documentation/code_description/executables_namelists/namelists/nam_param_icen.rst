.. _nam_param_icen:

NAM_PARAM_ICEn
-----------------------------------------------------------------------------

It contains the options for the mixed phase cloud parameterizations used  by the model (ICE3 or ICE4). They are included in the declarative module MODD_PARAM_ICE.

.. csv-table:: NAM_PARAM_ICEn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LWARM","LOGICAL","TRUE"
   "CPRISTINE_ICE","CHARACTER(LEN=4)","'PLAT'"
   "LSEDIC","LOGICAL","TRUE"
   "CSEDIM","CHARACTER(LEN=4)","'SPLI'"
   "LCONVHG","LOGICAL","FALSE"
   "LDEPOSC","LOGICAL","FALSE"
   "XVDEPOSC","REAL","0.02"
   "LRED","LOGICAL","TRUE"
   "LFEEDBACKT","LOGICAL","TRUE"
   "LEVLIMIT","LOGICAL","TRUE"
   "LNULLWETG","LOGICAL","TRUE"
   "LWETGPOST","LOGICAL","TRUE"
   "LNULLWETH","LOGICAL","TRUE"
   "LWETHPOST","LOGICAL","TRUE"
   "CSNOWRIMING","CHARACTER(LEN=4)","'M90 '"
   "XFRACM90","REAL","0.1"
   "NMAXITER_MICRO","INTEGER","5"
   "XMRSTEP","REAL","0.00005"
   "XTSTEP_TS","REAL","0.0"
   "LADJ_BEFORE","LOGICAL","TRUE"
   "LADJ_AFTER","LOGICAL","TRUE"
   "LCRFLIMIT","LOGICAL","TRUE"
   "XSPLIT_MAXCFL","REAL","0.8"
   "LSEDIM_AFTER","LOGICAL","FALSE"
   "CSUBG_RC_RR_ACCR","CHARACTER(LEN=80)","'NONE'"
   "CSUBG_RR_EVAP","CHARACTER(LEN=80)","'NONE'"
   "CSUBG_PR_PDF","CHARACTER(LEN=80)","'SIGM'"
   "CSUBG_AUCV_RC","CHARACTER(LEN=4)","'NONE'"
   "CSUBG_AUCV_RI","CHARACTER(LEN=80)","'NONE'"
   "CSUBG_MF_PDF","CHARACTER(LEN=80)","'TRIANGLE'"
   "LSNOW_T","LOGICAL",".FALSE."
   "LPACK_INTERP","LOGICAL","TRUE"
   "LPACK_MICRO","LOGICAL","TRUE"
   "NPROMICRO","INTEGER","0"
   "LCRIAUTI","LOGICAL","FALSE"
   "LOCND2","LOGICAL","FALSE"
   "XCRIAUTI_NAM","REAL","0.2E-4"
   "XT0CRIAUTI_NAM","REAL","(LOG10(XCRIAUTI_NAM)"
   "","","-XBCRIAUTI_NAM)/0.06"
   "XBCRIAUTI_NAM","REAL","-3.5"
   "XACRIAUTI_NAM","REAL","0.06"
   "XCRIAUTC_NAM","REAL","0.5E-3"
   "XRDEPSRED_NAM","REAL","1.0"
   "XRDEPGRED_NAM","REAL","1.0"
   "XFRMIN_NAM","REAL(40)",""

* :code:`LWARM` : When .TRUE. activates the formation of rain by the warm microphysical processes

* :code:`CPRISTINE_ICE` : Pristine ice crystal type

  * 'PLAT' : plates 
  * 'COLU' : columns
  * 'BURO' : bullet rosettes

* :code:`LSEDIC` : Cloud droplets are allowed to sediment if set to TRUE

* :code:`CSEDIM` : Sedimentation algorithm type

  * 'SPLI' : Splitting method (original one)
  * 'STAT' : Statistic method (accordingly to Bouteloup and Seity in AROME) 

* :code:`LCONVHG` : For ICE4, .TRUE. activates the reconversion of hail to graupel for low values of supercooled cloud water or hail contents.

* :code:`LDEPOSC` : TRUE to enable cloud droplet deposition

* :code:`XVDEPOSC` : Droplet deposition velocity

* :code:`LRED` : To use modified ICE3/ICE4 to reduce time step dependency

* :code:`LFEEDBACKT` :  .TRUE. when feedback on temperature is taken into account (active when LRED=T)

* :code:`LEVLIMIT` : .TRUE. when water vapour pressure is limited by saturation (active when LRED=T)

* :code:`LNULLWETG` : .TRUE. when graupel wet growth is activated with null rate (to allow water shedding) (active when LRED=T)

* :code:`LWETGPOST` : .TRUE. when graupel wet growth is activated with positive temperature (to allow water shedding) (active when LRED=T)
 
* :code:`LNULLWETH` : Same as LNULLWETG but for hail

* :code:`LWETHPOST` : Same as LWETGPOST but for hail

* :code:`CSNOWRIMING` :  Parametrization for snow riming (active when LRED=T)

  * 'OLD' : standard parametrization
  * 'M90' : Murakami 1990 formulation

* :code:`XFRACM90` : Fraction used for the Murakami 1990 formulation (active when LRED=T)

* :code:`NMAXITER_MICRO` : Maximum number of iterations for mixing ratio or time splitting (active when LRED=T)

* :code:`XMRSTEP` : Maximum mixing ratio step for mixing ratio splitting (active when LRED=T)

* :code:`XTSTEP_TS` : Approximative time step for time-splitting (0 for no time-splitting) (active when LRED=T)

* :code:`LADJ_BEFORE` : .TRUE. when an adjustment before rain_ice call is performed (active when LRED=T)

* :code:`LADJ_AFTER` : .TRUE. when an adjustment after rain_ice call is performed (equal to T when LRED=F)

* :code:`LSNOW_T` : Switch to activate the representation of snow proposed by Wurtz et al. 2023 which improves the extension and cloud composition of anvils in convective systems.

* :code:`LPACK_INTERP` : to save computation time, some mycrophysical processes (especially collections) are tabulated. If this key is .TRUE., the input variables for the interpolations are packed to limit the computation to the necessary points; otherwise, the interpolations are performed everywhere.

* :code:`LPACK_MICRO` : the microphysics input variables are packed to perform the computation only on points with hydrometeors; otherwise, computations are performed everywhere..

* :code:`LCRFLIMIT` : .TRUE. to limit rain contact freezing to possible heat exchange (active when LRED=T)

* :code:`XSPLIT_MAXCFL` : Maximum CFL number allowed for SPLIT scheme (active when LRED=T)

* :code:`LSEDIM_AFTER` : sedimentation done before (.FALSE.) or after (.TRUE.) microphysics (active when LRED=T)

* :code:`CSUBG_AUCV_RC` : Type of subgrid :math:`r_c` - :math:`r_r` autoconversion scheme.

  * 'NONE'
  * 'SIGM' for Redelsperger and Sommeria (1982) scheme using :math:`\overline{s'r'_{c}}` (if LSUBG_COND is set to TRUE and only with the mixed phase for the moment)
  * 'CLFR' from the convective cloud fraction given by EDKF  (if CSCONV='EDKF' only)
  * 'PDF' for subgrid warm precipitation (not only autoconversion) according to Turner et al. (2012). Only if LRED=TRUE.
  * 'ADJU' to use a diagnostic computed in the saturation adjustment when CCONDENS is set to GAUS.

* :code:`CSUBG_AUCV_RI` : Type of subgrid :math:`r_i` - :math:`r_s` autoconversion scheme.

  * 'NONE' for considering a homogeneous cloud over the entire grid-cell
  * 'CLFR' for considering a homogeneous cloud over its cloud fraction
  * 'ADJU' to use a diagnostic computed in the saturation adjustment when CCONDENS is set to GAUS.

* :code:`CSUBG_MF_PDF` : PDF used to diagnose autoconversion from the shallow convection cloud.

  * 'NONE' for considering a homogeneous cloud over its fraction.
  * 'TRIANGLE' to use a triangular PDF.

* :code:`CSUBG_RC_RR_ACCR` : Subgrid :math:`r_c`-:math:`r_r` accretion

  * 'NONE' : cloud and rain occupy the entire grid cell of the model
  * 'PRFR' : the cloud is concentrated on the cloud fraction and the rain on the rain fraction

* :code:`CSUBG_RR_EVAP` : Subgrid rr evaporation

  * 'NONE' : rain occupies the entire grid cell and evaporation can only occur on grid cells that are completely free of clouds
  * 'CLFR' : rain occupies the entire grid cell and evaporation can only occur on the clear sky part of the grid cell
  * 'PRFR' : same as CLFR but rain is concentrated on the rain fraction

* :code:`CSUBG_PR_PDF` : PDF for subgrid precipitation

  * 'SIGM' : use of the Redelsperger and Sommeria (1986) PDF 
  * 'HLCRECTPDF' : rectangular PDF
  * 'HLCTRIANGPDF' : triangular PDF
  * 'HLCQUADRAPDF' : second order quadratic PDF
  * 'HLCISOTRIPDF' : isocele triangular PDF

* :code:`NPROMICRO` :  size of cache-blocking bloc (0 to deactivate)

* :code:`LCRIAUTI` : True to compute XACRIAUTI and XBCRIAUTI (from XCRIAUTI and XT0CRIAUTI); False to compute XT0CRIAUTI (from XCRIAUTI and XBCRIAUTI)

* :code:`LOCND2` :  flag to switch on the OCND2 scheme that separates liquid and ice (full documentation here\footnote{https://hirlam.github.io/HarmonieSystemDocumentation/dev/ForecastModel/OCDN2/})
 
* :code:`XCRIAUTI_NAM` : minimum value for the ice :math:`\rightarrow` snow autoconversion threshold

* :code:`XT0CRIAUTI_NAM` :  threshold temperature for the ice :math:`\rightarrow` snow autoconversion threshold

* :code:`XBCRIAUTI_NAM` : B parameter for the ice :math:`\rightarrow` snow autoconversion 10**(aT+b) law

* :code:`XACRIAUTI_NAM` : A parameter for the ice :math:`\rightarrow` snow autoconversion 10**(aT+b) law

* :code:`XCRIAUTC_NAM` : threshold for liquid cloud :math:`\rightarrow` rain autoconversion (kg/m**3)

* :code:`XRDEPSRED_NAM` : tuning factor of sublimation of snow

* :code:`XRDEPGRED_NAM` : tuning factor of sublimation of graupel

* :code:`XFRMIN_NAM` : parameters to modify melt and growth of graupels 

