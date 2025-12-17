.. _nam_paramn:

NAM_PARAMn
-----------------------------------------------------------------------------

It contains the different types of parameterizations used by the model n. They are included in the declarative module MODD_PARAMn. 

.. csv-table:: NAM_PARAMn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "CTURB","CHARACTER(LEN=4)","'NONE'"
   "CRAD","CHARACTER(LEN=4)","'NONE'"
   "CCLOUD","CHARACTER(LEN=4)","'NONE'"
   "CDCONV","CHARACTER(LEN=4)","'NONE'"
   "CSCONV","CHARACTER(LEN=4)","'NONE'"
   "CELEC","CHARACTER(LEN=4)","'NONE'"
   "CACTCCN","CHARACTER(LEN=4)","'NONE'"

* :code:`CTURB` :  type of turbulence scheme used to parameterize the transfers from unresolved scales to resolved scales.
 
  * 'NONE' : no turbulence scheme.
  * 'TKEL' : turbulence scheme with a one and a half  order closure (i.e. prognostic turbulent kinetic energy (TKE) and diagnostic mixing length). Specific options have to be set in :ref:`nam_turbn`.
   
* :code:`CRAD` :  type of radiative transfer scheme used to parameterize the effects of the solar and infrared radiations.

  * 'NONE' : then the downward surface fluxes are set to zero
  * 'TOPA' : the solar flux is equal to the one at TOP of Atmosphere. The infra-red flux is equal to 300 :math:`{\rm W.m}^{-2}`.
  * 'FIXE' : then the daily evolutions of the downward surface fluxes are prescribed. The temporal evolution is done in the routine PHYS_PARAMn by fixing the hourly value of the infrared and solar fluxes and can be modified for personal application.
  * 'ECMW' : the ECMWF radiation scheme code is used. Specific options have to be set in :ref:`nam_param_radn`.
  * 'ECRA' : the ECRAD radiation scheme code is used. Specific options have to be set in :ref:`nam_param_radn` and :ref:`nam_param_ecradn`.

* :code:`CCLOUD` : type of the microphysical scheme used to parameterize the different  water phases' transformations.

  * 'NONE' no microphysical scheme is used. You can still use water vapor if you want (LUSERV= TRUE or FALSE)
  * 'REVE' only the saturation adjustment is used to create cloud water. This liquid water is never transformed in rain water. 
  * 'KESS' a warm Kessler microphysical scheme is used. It allows  transformations between the  3 classes of water: vapor, cloud water and rain.
  * 'C2R2' a 2-moment warm microphysical scheme according to Cohard and Pinty (2000). Specific options have to be set in :ref:`nam_param_c2r2`.
  * 'KHKO' a 2-moment warm microphysical scheme for LES of Stratocumulus according to Khairoudinov and Kogan (2000). Specific options have to be set in :ref:`nam_param_c2r2`.
  * 'ICE3' a mixed microphysical scheme including ice, snow, and graupel (6 classes of hydrometeors).
  * 'LIMA' a mixed  2-moment microphysical scheme  (6 classes of hydrometeors ). Specific options have to be set in :ref:`nam_param_lima`.
  * 'ICE4' same as ICE3 but with hail (7 classes of hydrometeors).                     

* :code:`CDCONV` : type of deep convection scheme used to parameterize the effects of unresolved convective clouds.

  * 'NONE' : no convection scheme.                            
  * 'KAFR' : Kain-Fritsch-Bechtold scheme. Specific options have to be set in :ref:`nam_param_kafrn`.

* :code:`CSCONV` : type of shallow convection scheme used to parameterize the effects of unresolved shallow convective clouds.

  * 'NONE' : no convection scheme.                            
  * 'KAFR' : Kain-Fritsch-Bechtold scheme. Specific options have to be set in :ref:`nam_param_kafrn`.
  * 'EDKF' : Eddy-Diffusivity-Kain-Fritsch scheme (according to Pergaud et al., 2008). Can only be used with CTURB='TKEL'. Specific options have to be set in :ref:`nam_param_mfshalln`.

* :code:`CELEC` : type of electricity-lightning scheme used to parameterize electrification of hydrometeors

  * 'NONE' : no electricity-lightning scheme.
  * 'ELE3' : original scheme CELLS based on duplication of microphysics ICE3 code. Works only with NAM_PARAM_ICEn LRED=F, LSNOW_T=F. Specific options have to be set in :ref:`nam_elec`.
  * 'ELE4' : externalization and modernization of ELE3 with possibility to use with LIMA and ICE3 with time-splitting. Specific options have to be set in :ref:`nam_elec`.
 
.. note::
 
   With LIMA, two configurations are possible in NAM_PARAM_LIMA:
   
   * LPTSPLIT=T, NMOM_C=NMOM_R=NMOM_I=2, NMOM_S=NMOM_G=1, NMOM_H=0, and LSNOW_T=F 
   * LPTSPLIT=T, NMOM_C=NMOM_R=NMOM_I=NMOM_S=NMOM_G=2, NMOM_H=0, and LSNOW_T=F.

  With ICE3, set LRED=T and LSNOW_T=F in NAM_PARAM_ICEn.

* :code:`CACTCCN` : type of CCN activation scheme 

  * 'NONE' : no CCN activation scheme.                            
