.. _nam_bu_rrv:

NAM_BU_RRV
-----------------------------------------------------------------------------

.. csv-table:: NAM_BU_RRV content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LBU_RRV", "LOGICAL", ".FALSE."
   "CBULIST_RRV", "ARRAY(CHARACTER)", ""

* :code:`LBU_RRV` : flag to activate budget for vapor

* :code:`CBULIST_RRV` : list of source terms

.. note::

   Description of the names to be used for the different source terms in the CBULIST_RRV array and the conditions of their availability:

Source terms (except water microphysical schemes)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "ALL","all available source terms (separated, water microphysics included)","no condition"
   "ASSE","time filter (Asselin)","no condition"
   "NEST","nesting","NMODEL>1"
   "VISC","viscosity","LVISC=T and LVISC_R=T"
   "ADV","total advection","no condition"
   "FRC","forcing","LFORCING=T"
   "2DADV","advective forcing","L2D_ADV_FRC=T"
   "2DREL","relaxation forcing","L2D_REL_FRC=T"
   "NUD","nudging","LNUDGING=T"
   "DIF","numerical diffusion","LNUMDIFTH=T"
   "REL","relaxation","LHORELAX_RV=T"
   "DCONV","KAFR convection","CDCONV='KAFR' or CSCONV='KAFR'"
   "DRAGB","vapor released by buildings","LDRAGBLDG=T"
   "BLAZE","Blaze fire model","LBLAZE=T"
   "HTURB","horizontal turbulent diffusion","CTURB='TKEL' and CTURBDIM='3DIM'"
   "VTURB","vertical turbulent diffusion","CTURB='TKEL'"
   "MAFL","mass flux","CSCONV='EDKF'"
   "SNSUB","blowing snow sublimation","LBLOWSNOW=T and LSNOWSUBL=T"

LIMA source terms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "HENU","heterogeneous nucleation","NMOM_C>=1 and LACTI=T and NMOD_CCN>0 and (LPTSPLIT=F or LSUBG_COND=F)"
   "REVA","rain evaporation","LPTSPLIT=T or (NMOM_C>=1 and NMOM_R>=1)"
   "HIN","heterogeneous ice nucleation","NMOM_IMM=1"
   "HIND","heterogeneous nucleation by deposition","NMOM_I>=1 and LNUCL=T"
   "HONH","haze homogeneous nucleation","NMOM_I>=1 and LNUCL=T and LHHONI=T and NMOD_CCN>0"
   "DEPS","deposition on snow","LPTSPLIT=T or (NMOM_I>=1 and NMOM_S>=1)"
   "DEPI","condensation/deposition on ice","LPTSPLIT=T"
   "DEPG","deposition on graupel","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "DEPH","deposition on hail","LPTSPLIT=T or NMOM_H>=1"
   "CEDS","adjustment to saturation","no condition"
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
   
   "REVA","rain evaporation","NMOM_C>=1"
   "HIN","heterogeneous ice nucleation","no condition"
   "DEPS","deposition on snow","no condition"
   "DEPG","deposition on graupel","no condition"
   "DEPH","deposition on hail","CCLOUD='ICE4'"
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


