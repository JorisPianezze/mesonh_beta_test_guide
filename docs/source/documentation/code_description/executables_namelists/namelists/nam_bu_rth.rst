.. _nam_bu_rth:

NAM_BU_RTH
-----------------------------------------------------------------------------

.. csv-table:: NAM_BU_RTH content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LBU_RTH", "LOGICAL", ".FALSE."
   "CBULIST_RTH", "ARRAY(CHARACTER)", ""

* :code:`LBU_RTH` : flag to activate budget for potential temperature

* :code:`CBULIST_RTH` : list of source terms

.. note::

   Description of the names to be used for the different source terms in the CBULIST_RTH array and the conditions of their availability:
   
Source terms (except water microphysical schemes)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "ALL","all available source terms (separated, water microphysics included)","no condition"
   "ASSE","time filter (Asselin)","no condition"
   "NEST","nesting","NMODEL>1"
   "VISC","viscosity","LVISC=T and LVISC_TH=T"
   "OCEAN","radiative tendency due to SW penetrating ocean","LOCEAN .AND. (.NOT. LCOUPLES)"
   "ADV","total advection","no condition"
   "FRC","forcing","LFORCING=T"
   "2DADV","advective forcing","L2D_ADV_FRC=T"
   "2DREL","relaxation forcing","L2D_REL_FRC=T"
   "NUD","nudging","LNUDGING=T"
   "PREF","reference pressure","L1D=F and number of moist variables > 0"
   "DIF","numerical diffusion","LNUMDIFTH=T"
   "REL","relaxation","LHORELAX_UVWTH=T or LVE_RELAX=T or LVE_RELAX_GRD=T"
   "RAD","radiation","CRAD/='NONE'"
   "DCONV","KAFR convection","CDCONV='KAFR' or CSCONV='KAFR'"
   "BLAZE","Blaze fire model","LBLAZE=T"
   "DRAGB","heat released by buildings","LDRAGBLDG=T"
   "HTURB","horizontal turbulent diffusion","CTURB='TKEL' and CTURBDIM='3DIM'"
   "VTURB","vertical turbulent diffusion","CTURB='TKEL'"
   "DISSH","dissipation","CTURB='TKEL'"
   "MAFL","mass flux","CSCONV='EDKF'"
   "SNSUB","blowing snow sublimation","LBLOWSNOW=T and LSNOWSUBL=T"

LIMA source terms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "SEDI","heat transport by hydrometeors sedimentation","LPTSPLIT=T"
   "HENU","heterogeneous nucleation","NMOM_C>=1 and LACTI=T and NMOD_CCN>0 and (LPTSPLIT=F or LSUBG_COND=F)"
   "REVA","rain evaporation","LPTSPLIT=T or (NMOM_C>=1 and NMOM_R>=1)"
   "HIN","heterogeneous ice nucleation","NMOM_I=1"
   "HIND","heterogeneous nucleation by deposition","NMOM_I>=1 and LNUCL=T"
   "HINC","heterogeneous nucleation by contact","NMOM_I>=1 and LNUCL=T"
   "HONH","haze homogeneous nucleation","NMOM_I>=1 and LNUCL=T and LHHONI=T and NMOD_CCN>0"
   "HONC","droplet homogeneous freezing","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and LNUCL=T)"
   "HONR","rain homogeneous freezing","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and LNUCL=T and NMOM_R>=1)"
   "DEPS","deposition on snow","LPTSPLIT=T or (NMOM_I>=1 and NMOM_S>=1)"
   "DEPI","condensation/deposition on ice","LPTSPLIT=T"
   "DEPG","deposition on graupel","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "DEPH","deposition on hail","LPTSPLIT=T or NMOM_H>=1"
   "IMLT","melting of ice","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1)"
   "BERFI","Bergeron-Findeisen","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1)"
   "RIM","riming of cloud water","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "ACC","accretion of rain on aggregates","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1 and NMOM_R>=1)"
   "CFRZ","conversion freezing of rain","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "WETG","wet growth of graupel","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "DRYG","dry growth of graupel","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "GMLT","graupel melting","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "WETH","wet growth of hail","LPTSPLIT=T or (NMOM_H>=1 and NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "HMLT","melting of hail","LPTSPLIT=T or (NMOM_H>=1 and NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "CEDS","adjustment to saturation","no condition"
   "NEGA","negativity correction","no condition"
   "NETUR","negativity correction induced by turbulence","CTURB='TKEL'"
   "NEADV","negativity correction induced by advection","no condition"
   "NECON","negativity correction induced by condensation","no condition"

ICE3 / ICE4 source terms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "REVA","rain evaporation","NMOM_C>=1"
   "HIN","heterogeneous ice nucleation","no condition"
   "HON","homogeneous nucleation","no condition"
   "SFR","spontaneous freezing","no condition"
   "DEPS","deposition on snow","no condition"
   "DEPG","deposition on graupel","no condition"
   "DEPH","deposition on hail","CCLOUD='ICE4'"
   "IMLT","melting of ice","no condition"
   "BERFI","Bergeron-Findeisen","no condition"
   "RIM","riming of cloud water","no condition"
   "ACC","accretion of rain on aggregates","no condition"
   "CFRZ","conversion freezing of rain","no condition"
   "WETG","wet growth of graupel","no condition"
   "DRYG","dry growth of graupel","no condition"
   "GMLT","graupel melting","no condition"
   "WETH","wet growth of hail","CCLOUD='ICE4'"
   "DRYH","dry growth of hail","CCLOUD='ICE4' and LRED=T and CELEC='NONE'"
   "HMLT","melting of hail","CCLOUD='ICE4'"
   "ADJU","adjustment to saturation","LRED=T and LADJ_BEFORE=T and CELEC/='ELE3'"
   "DEPI","condensation/deposition on ice","LRED=F or ( LRED=T and LADJ_AFTER=T) or CELEC/='NONE'"
   "CORR","correction","LRED=T and CELEC/='ELE3'"
   "NEGA","negativity correction","no condition"
   "NETUR","negativity correction induced by turbulence","CTURB='TKEL'"
   "NEADV","negativity correction induced by advection","no condition"
   "NECON","negativity correction induced by condensation","no condition"

C2R2 / KHKO source terms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "HENU","heterogeneous nucleation","LSUPSAT=F or (CACTCCN='ABRK' and (LORILAM=T or LDUST=T or LSALT=T))"
   "REVA","rain evaporation","NMOM_R>=1"
   "COND","vapor condensation or cloud water evaporation","no condition"
   "NEGA","negativity correction","no condition"
   "NETUR","negativity correction induced by turbulence","CTURB='TKEL'"
   "NEADV","negativity correction induced by advection","no condition"
   "NECON","negativity correction induced by condensation","no condition"

KESS source terms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "REVA","rain evaporation","no condition"
   "COND","vapor condensation or cloud water evaporation","no condition"
   "NEGA","negativity correction","no condition"
   "NETUR","negativity correction induced by turbulence","CTURB='TKEL'"
   "NEADV","negativity correction induced by advection","no condition"
   "NECON","negativity correction induced by condensation","no condition"

REVE source terms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "COND","vapor condensation or cloud water evaporation","no condition"


