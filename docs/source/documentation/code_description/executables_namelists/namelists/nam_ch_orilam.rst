.. _nam_ch_orilam:

NAM_CH_ORILAM
-----------------------------------------------------------------------------

This namelist is used to activate ORILAM chemical aerosols (lognormal distribution for Aitken and accumulation mode). This parameterization include coagulation (intra and inter modal), nucleation,  sedimentation, condensation/adsorption of gas phase. This parameterization need to be run together with gas chemical phase (namelist :ref:`nam_ch_mnhcn`). For correct representation, it is recommended to have severals compounds as HNO3 (nitric acid), H2SO4 (or SULF; sulphates), NH3 (ammonium) and CO (carbon monoxyde) in the chemical scheme. 

.. csv-table:: NAM_CH_ORILAM content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LORILAM","LOGICAL",".FALSE."
   "LVARSIGI","LOGICAL",".FALSE."
   "LVARSIGJ","LOGICAL",".FALSE."
   "LSEDIMAERO","LOGICAL",".FALSE."
   "XINIRADIUSI","REAL","0.01"
   "XINIRADIUSJ","REAL","0.5"
   "CRGUNIT","CHARACTER(LEN=4)","'MASS'"
   "XINISIGI","REAL","1.60"
   "XINISIGJ","REAL","1.60"
   "XN0IMIN","REAL","10.0"
   "XN0JMIN","REAL","1.0"
   "XCOEFRADIMAX","REAL","10.0"
   "XCOEFRADJMAX","REAL","10.0"
   "XCOEFRADIMIN","REAL","0.1"
   "XCOEFRADJMIN","REAL","0.1"
   "CMINERAL","CHARACTER(LEN=5)","'NONE'"
   "CORGANIC","CHARACTER(LEN=5)","'NONE'"
   "CNUCLEATION","CHARACTER(LEN=80)","'MAATTANEN'"
   "LCONDENSATION","LOGICAL",".TRUE."
   "LCOAGULATION","LOGICAL",".TRUE."
   "LMODE_MERGING","LOGICAL",".FALSE."

* :code:`LORILAM` : flag to activate chemical aerosol (only if LUSECHEM = .TRUE.).

* :code:`LVARSIGI` : flag to activate variable standard deviation for mode I (Aitken).

* :code:`LVARSIGJ` : flag to activate variable standard deviation for mode J (accumulation).

* :code:`LSEDIMAERO` : flag to activate aerosol sedimentation.

* :code:`XINIRADIUSI` : flag for  the initialization of mean radius mode I (Aitken mode) of the distribution (in micrometers). 

* :code:`XINIRADIUSJ` : flag for the initialization of mean radius mode J (accumulation mode) of the distribution (in micrometers). 

* :code:`CRGUNIT` : type of mean radius given in namelist. Default is for a mass spectral distribution; XINIRADIUSI and XINIRADIUSJ have been converted into a  mean radius in number. IF CRGUNIT :math:`\neq` 'MASS' then the mean radius need to be given for a number spectral distribution (no conversion).  

* :code:`XINISIGI` : value of standard deviation for mode I (Aitken mode).  

* :code:`XINISIGJ` : value of standard deviation for mode J (accumulation mode).  

* :code:`XCOEFRADIMAX` : factor to compute maximum value of mean radius mode I (Aitken mode). :math:`R_i^{max} =  XCOEFRADIMAX . XINIRADIUSI`

* :code:`XCOEFRADJMAX` : factor to compute maximum value of mean radius mode J (accumulation mode). :math:`R_j^{max} =  XCOEFRADJMAX . XINIRADIUSJ`

* :code:`XCOEFRADIMIN` : same as XCOEFRADIMAX but for the minimum value.

* :code:`XCOEFRADJMIN` : same as XCOEFRADIMAX but for the minimum value.

* :code:`CMINERAL` : type of parameterization for mineral gas/particle balance. Possible values are:

  * 'ARES' : ARES parameterization (non vectorized)
  * 'NARES': neuronal network of ARES (vectorized)
  * 'ISPIA': ISORROPIA parameterization (non vectorized)
  * 'TABUL': tabulation of ISORROPIA  (vectorized)
  * 'EQSAM': EQSAM parameterization (vectorized) 

* :code:`CORGANIC` : type of parameterization for organic gas/particle balance. To activate organic parameterization it is necessary to use a chemical scheme capable forming secondary organic aerosol (i.e. RELACS2 or CACM). Possible values are:

  * 'PUN' : PUN parameterization 
  * 'MPMPO': MPMPO (non vectorized) 

* :code:`CNUCLEATION` : type of parameterization for nucleation's parametrization. Four options are available:

  * 'NONE' : no nucleation
  * 'KULMALA' : based on Kulmala et al. 1998
  * 'VEHKAMAKI' : based on Vehkamäki et al. 2002
  * 'MAATTANEN' : based on Määttänen et al. 2018

* :code:`LCONDENSATION` : flag to activate the condensation processes.

* :code:`LCOAGULATION` : flag to activate the intra and inter coagulation processes.

* :code:`LMODE_MERGING` : flag to activate the mode merging. 

* Convective scavenging is activated with LCH_CONV_SCAV in :ref:`nam_ch_mnhcn`.
   
