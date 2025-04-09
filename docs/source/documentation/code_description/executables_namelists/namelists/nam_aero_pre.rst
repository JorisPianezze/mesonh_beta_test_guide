.. _nam_aero_pre:

NAM_AERO_PRE
-----------------------------------------------------------------------------

.. csv-table:: NAM_AERO_PRE content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LORILAM","LOGICAL",".FALSE."
   "LDUST","LOGICAL",".FALSE."
   "LSALT","LOGICAL",".FALSE."
   "LINITPM","LOGICAL",".FALSE."
   "XINIRADIUSI","REAL","0.05"
   "XINIRADIUSJ","REAL","0.2"
   "XINISIGI","REAL","1.8"
   "XINISIGJ","REAL","2.0"
   "XN0IMIN","REAL","10.0"
   "XN0JMIN","REAL","1.0"
   "CRGUNIT","CHARACTER","'NUMB'"
   "NMODE_DST","INTEGER","3"
   "XN0MIN","REAL","1.e3, 1.e1, 1.e-2"
   "XINIRADIUS","REAL","0.044, 0.3215, 1.575"
   "XINISIG","REAL","2.0, 1.78, 1.85"
   "CRGUNITD","CHARACTER","'NUMB'"
   "NMODE_SLT","INTEGER","3"
   "XN0MIN_SLT","REAL","1.e4, 1.e2, 1.e-1"
   "XINIRADIUS_SLT","REAL","0.14, 1.125, 7.64"
   "XINISIG_SLT","REAL","1.9, 2., 2."
   "CRGUNITS","CHARACTER","'MASS'"
   "CCLOUD","CHARACTER","'NONE'"
   "NMOD_CCN","INTEGER","1"
   "NMOD_IFN","INTEGER","1"
   "LDSTCAMS","LOGICAL",".FALSE."
   "LSLTCAMS","LOGICAL",".FALSE."

* :code:`LORILAM` : flag to activate chemical aerosol initialization (only if LCH_INIT_FIELD=T in NAM_CH_MNHCn_PRE).

* :code:`LDUST` : flag to activate passive dust initialization.

* :code:`LSALT` : flag to activate passive sea salt initialization.

* :code:`LINITPM` : flag to activate primary aerosol initialization (Black and Organic carbon) from concentration of CO (only if LORILAM=T in NAM_CH_MNHCn_PRE).

* :code:`XINIRADIUSI` : initial mean radius of aitken mode in :math:`\mu m`  (only if LORILAM=T in NAM_AERO_PRE).

* :code:`XINIRADIUSJ` : initial mean radius of accumulation mode in :math:`\mu m` (only if LORILAM=T in NAM_AERO_PRE).

* :code:`XINISIGI` : initial standard deviation of aitken  mode (only if LORILAM=T in NAM_AERO_PRE).

* :code:`XINISIGJ` : initial standard deviation of accumulation  mode (only if LORILAM=T in NAM_AERO_PRE).

* :code:`XN0IMIN` : minimum number concentration of aitken mode (only if LORILAM=T in NAM_AERO_PRE).

* :code:`XN0JMIN` : minimum number concentration of accumulation mode (only if LORILAM=T in NAM_AERO_PRE).

* :code:`CRGUNIT` : definition of XINIRADIUSI and XINIRADIUSJ : mean radius can be in mass ('MASS') or in number ('NUMB') (only if LORILAM=T in NAM_AERO_PRE).

* :code:`NMODE_DST` : number of DUST mode (between  1 and 3 and only if LDUST=T in NAM_AERO_PRE).

* :code:`XN0MIN` : minimum number concentration of the NMODE_DST in particles by :math:`m^3` (only if LDUST=T in NAM_AERO_PRE).

* :code:`XINIRADIUS` : initial mean radius of the NMODE_DST modes in :math:`\mu m` (only if LDUST=T in NAM_AERO_PRE). 

* :code:`XINISIG` : initial standard deviation of the NMODE_DST modes (only if LDUST=T in NAM_AERO_PRE). 

* :code:`CRGUNITD` : definition of XINIRADIUS : mean radius can be in mass ('MASS') or in number ('NUMB') (only if LDUST=T in NAM_AERO_PRE).

* :code:`NMODE_SLT` : number of SALT mode in :math:`\mu m` (between 1 and 3 and only if LSALT=T in NAM_AERO_PRE).

* :code:`XN0MIN_SLT` : minimum number concentration of the NMODE_SLT in particles by :math:`m^3` (only if LSALT=T in NAM_AERO_PRE).

* :code:`XINIRADIUS_SLT` : initial mean radius of the NMODE_SLT modes (only if LSALT=T in NAM_AERO_PRE).

* :code:`XINISIG_SLT` : initial standard deviation of the NMODE_SLT modes (only if LSALT=T in NAM_AERO_PRE).

* :code:`CRGUNITS` : definition of XINIRADIUS_SLT :  mean radius can be in mass ('MASS') or in number ('NUMB') (only if LSALT=T in NAM_AERO_PRE).

* :code:`CCLOUD` : microphysics scheme (only 'LIMA' possible) to use with aerosols coupling

* :code:`NMOD_CCN` : number of CCN modes

* :code:`NMOD_IFN` : number of IFN modes

* :code:`LDSTCAMS` : flag to activate initialization of dust aerosols from CAMS file.

* :code:`LSLTCAMS` : flag to activate initialization of sea-salt aerosols from CAMS file.
