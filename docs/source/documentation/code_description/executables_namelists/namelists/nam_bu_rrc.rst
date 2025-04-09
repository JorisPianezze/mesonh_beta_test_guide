.. _nam_bu_rrc:

NAM_BU_RRC
-----------------------------------------------------------------------------

.. csv-table:: NAM_BU_RRC content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LBU_RRC", "LOGICAL", ".FALSE."
   "CBULIST_RRC", "ARRAY(CHARACTER)", ""

* :code:`LBU_RRC` : flag to activate budget for cloud mixing ratio

* :code:`CBULIST_RRC` : list of source terms

Description of the names to be used for the different source terms in the CBULIST_RRC array and the conditions of their availability:

Source terms (except water microphysical schemes)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30

   "ALL","all available source terms (separated,water microphysics included)","no condition"
   "ASSE","time filter (Asselin)","no condition"
   "NEST","nesting","NMODEL>1"
   "VISC","viscosity","LVISC=T and LVISC_R=T"
   "ADV","total advection","no condition"
   "FRC","forcing","LFORCING=T"
   "DIF","numerical diffusion","LNUMDIFTH=T"
   "REL","relaxation","LHORELAX_RC=T"
   "DCONV","KAFR convection","CDCONV='KAFR' or CSCONV='KAFR'"
   "HTURB","horizontal turbulent diffusion","CTURB='TKEL' and CTURBDIM='3DIM'"
   "VTURB","vertical turbulent diffusion","CTURB='TKEL'"
   "DEPOTR","tree droplet deposition","LDRAGTREE=T and LDEPOTREE=T"

LIMA source terms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "ACCR","accretion of cloud droplets","LPTSPLIT=T or (NMOM_C>=1 and NMOM_R>=1)"
   "AUTO","autoconversion into rain","LPTSPLIT=T or (NMOM_C>=1 and NMOM_R>=1)"
   "SEDI","sedimentation of cloud","NMOM_C>=1 and LSEDC=T"
   "DEPO","surface droplet deposition","NMOM_C>=1 and LDEPOC=T"
   "RIM","riming of cloud water","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "WETG","wet growth of graupel","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "DRYG","dry growth of graupel","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "IMLT","melting of ice","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1)"
   "BERFI","Bergeron-Findeisen","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1)"
   "HENU","CCN activation nucleation","NMOM_C>=1 and LACTI=T and NMOD_CCN>0 and (LPTSPLIT=F or LSUBG_COND=F)"
   "WETH","wet growth of hail","LPTSPLIT=T or (NMOM_H>=1 and NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "HINC","heterogeneous nucleation by contact","NMOM_I>=1 and LNUCL=T"
   "HONC","droplet homogeneous freezing","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and LNUCL=T)"
   "CEDS","adjustment to saturation","no condition"
   "REVA","evaporation of rain drops","LPTSPLIT=T or (NMOM_C>=1 and NMOM_R>=1)"
   "R2C1","rain to cloud change after sedimentation","LPTSPLIT=T and NMOM_C>=1 and NMOM_R>=1"
   "CVRC","rain to cloud change after other microphysical processes","LPTSPLIT=T"
   "NEGA","negativity correction","no condition"
   "NETUR","negativity correction induced by turbulence","CTURB='TKEL'"
   "NEADV","negativity correction induced by advection","no condition"
   "NECON","negativity correction induced by condensation","no condition"
   "CORR2","supplementary correction inside LIMA splitting","LPTSPLIT=T"

ICE3 / ICE4 source terms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "ACCR","accretion of cloud droplets","NMOM_C>=1"
   "AUTO","autoconversion into rain","NMOM_C>=1"
   "SEDI","sedimentation of cloud","LSEDIC=T"
   "DEPO","surface droplet deposition","LDEPOSC=T and CELEC='NONE'"
   "HON","homogeneous nucleation","no condition"
   "RIM","riming of cloud water","no condition"
   "WETG","wet growth of graupel","no condition"
   "DRYG","dry growth of graupel","no condition"
   "IMLT","melting of ice","no condition"
   "BERFI","Bergeron-Findeisen","no condition"
   "DEPI","condensation/deposition on ice","LRED=F or ( LRED=T and LADJ_AFTER=T) or CELEC/='NONE'"
   "CMEL","collection by snow and conversion into rain with T>XTT on ice","LRED=T and CELEC/='ELE3'"
   "DRYH","dry growth of hail","CCLOUD='ICE4' and LRED=T and CELEC='NONE'"
   "ADJU","adjustement to saturation","LRED=T and LADJ_BEFORE=T and CELEC/='ELE3'"
   "WETH","wet growth of hail","CCLOUD='ICE4'"
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
   
   "ACCR","accretion of cloud droplets","NMOM_R>=1"
   "AUTO","autoconversion into rain","NMOM_R>=1"
   "SEDI","sedimentation of cloud","LSEDC=T"
   "DEPO","surface droplet deposition","LDEPOC=T"
   "COND","vapor condensation or cloud water evaporation","no condition"
   "HENU","CCN activation nucleation","LSUPSAT=F or (CACTCCN='ABRK' and (LORILAM=T or LDUST=T or LSALT=T))"
   "NEGA","negativity correction","no condition"
   "NETUR","negativity correction induced by turbulence","CTURB='TKEL'"
   "NEADV","negativity correction induced by advection","no condition"
   "NECON","negativity correction induced by condensation","no condition"

KESS source terms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "ACCR","accretion of cloud droplets","no condition"
   "AUTO","autoconversion into rain","no condition"
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

