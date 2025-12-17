.. _nam_bu_rri:

NAM_BU_RRI
-----------------------------------------------------------------------------

.. csv-table:: NAM_BU_RRI content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LBU_RRI", "LOGICAL", ".FALSE."
   "CBULIST_RRI", "ARRAY(CHARACTER)", ""

* :code:`LBU_RRI` : flag to activate budget for non-precipitating ice

* :code:`CBULIST_RRI` : list of source terms

.. note::

   Description of the names to be used for the different source terms in the CBULIST_RRI array and the conditions of their availability:

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
   "DIF","numerical diffusion","LNUMDIFTH=T"
   "REL","relaxation","LHORELAX_RI=T"
   "DCONV","KAFR convection","CDCONV='KAFR' or CSCONV='KAFR'"
   "HTURB","horizontal turbulent diffusion","CTURB='TKEL' and CTURBDIM='3DIM'"
   "VTURB","vertical turbulent diffusion","CTURB='TKEL'"


LIMA source terms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "SEDI","sedimentation of cloud","NMOM_I>=1 and LSEDI=T"
   "HIN","heterogeneous ice nucleation","NMOM_I=1"
   "HIND","heterogeneous nucleation by deposition","NMOM_I>=1 and LNUCL=T"
   "HINC","heterogeneous nucleation by contact","NMOM_I>=1 and LNUCL=T"
   "HONH","haze homogeneous nucleation","NMOM_I>=1 and LNUCL=T and LHHONI=T and NMOD_CCN>0"
   "HONC","droplet homogeneous freezing","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and LNUCL=T)"
   "CNVI","conversion of snow to cloud ice","LPTSPLIT=T or (NMOM_I>=1 and NMOM_S>=1)"
   "CNVS","conversion of pristine ice to snow","LPTSPLIT=T or (NMOM_I>=1 and NMOM_S>=1)"
   "AGGS","aggregation of snow","LPTSPLIT=T or (NMOM_I>=1 and NMOM_S>=1)"
   "IMLT","melting of ice","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1)"
   "BERFI","Bergeron-Findeisen","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1)"
   "HMS","Hallett-Mossop ice multiplication process due to snow riming","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "HMG","Hallett-Mossop ice multiplication process due to graupel riming","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "CIBU","ice multiplication process due to ice collisional breakup","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1 and LCIBU=T)"
   "CFRZ","conversion freezing of rain","LPTSPLIT=T or (NMOM_I>=1 and NMOM\_C>=1 and NMOM_S>=1)"
   "RDSF","ice multiplication process following rain contact freezing","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1 and LRDSF=T)"
   "DEPI","condensation/deposition on ice","LPTSPLIT=T"
   "WETG","wet growth of graupel","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "DRYG","dry growth of graupel","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "WETH","wet growth of hail","LPTSPLIT=T or (NMOM_H>=1 and NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
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
   
   "SEDI","sedimentation of cloud","no condition"
   "HIN","heterogeneous ice nucleation","no condition"
   "HON","homogeneous nucleation","no condition"
   "AGGS","aggregation of snow","no condition"
   "AUTS","autoconversion of ice","no condition"
   "IMLT","melting of ice","no condition"
   "BERFI","Bergeron-Findeisen","no condition"
   "CFRZ","conversion freezing of rain","no condition"
   "WETG","wet growth of graupel","no condition"
   "DRYG","dry growth of graupel","no condition"
   "WETH","wet growth of hail","CCLOUD='ICE4'"
   "DRYH","dry growth of hail","CCLOUD='ICE4' and LRED=T and CELEC='NONE'"
   "DEPI","condensation/deposition on ice","LRED=F or ( LRED=T and LADJ_AFTER=T) or CELEC/='NONE'"
   "CORR","correction","LRED=T and CELEC/='ELE3'"
   "ADJU","adjustment to saturation","LRED=T and LADJ_BEFORE=T and CELEC/='ELE3'"
   "NEGA","negativity correction","no condition"
   "NETUR","negativity correction induced by turbulence","CTURB='TKEL'"
   "NEADV","negativity correction induced by advection","no condition"
   "NECON","negativity correction induced by condensation","no condition"



