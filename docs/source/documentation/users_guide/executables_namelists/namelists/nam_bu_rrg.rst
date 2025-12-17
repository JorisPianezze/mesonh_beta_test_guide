.. _nam_bu_rrg:

NAM_BU_RRG
-----------------------------------------------------------------------------

.. csv-table:: NAM_BU_RRG content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LBU_RRG", "LOGICAL", ".FALSE."
   "CBULIST_RRG", "ARRAY(CHARACTER)", ""

* :code:`LBU_RRG` : flag to activate budget for graupel

* :code:`CBULIST_RRG` : list of source terms

.. note::

   Description of the names to be used for the different source terms in the CBULIST_RRG array and the conditions of their availability:
   
Source terms (except water microphysical schemes)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "ALL","all available source terms (separated, water microphysics included)","no condition"
   "ASSE","time filter (Asselin)","no condition"
   "NEST","nesting","NMODEL>1"
   "VTURB","vertical turbulent diffusion","CTURB='TKEL'"
   "HTURB","horizontal turbulent diffusion","CTURB='TKEL' and CTURBDIM='3DIM'"
   "VISC","viscosity","LVISC=T and LVISC_R=T"
   "ADV","total advection","no condition"
   "FRC","forcing","LFORCING=T"
   "DIF","numerical diffusion","LNUMDIFTH=T"
   "REL","relaxation","LHORELAX_RG=T"

LIMA source terms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "NETUR","negativity correction induced by turbulence","CTURB='TKEL'"
   "SEDI","sedimentation","NMOM_I>=1 and NMOM_S>=1"
   "HONR","rain homogeneous freezing","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and LNUCL=T and NMOM_R>=1)"
   "DEPG","deposition on graupel","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "RIM","riming of cloud water","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "ACC","rain accretion on graupel","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1 and NMOM_R>=1)"
   "CMEL","conversion melting of snow","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "CFRZ","conversion freezing of rain","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "RDSF","ice multiplication process following rain contact freezing","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1 and LRDSF=T)"
   "HMG","Hallett-Mossop ice multiplication process due to graupel riming","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "WETG","wet growth of graupel","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "DRYG","dry growth of graupel","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "GMLT","graupel melting","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "WETH","wet growth of hail","LPTSPLIT=T or (NMOM_H>=1 and NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "COHG","conversion of hail to graupel","LPTSPLIT=T or (NMOM_H>=1 and NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "NEGA","negativity correction","no condition"
   "NEADV","negativity correction induced by advection","no condition"
   "NECON","negativity correction induced by condensation","no condition"

ICE3 / ICE4 source terms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "NETUR","negativity correction induced by turbulence","CTURB='TKEL'"
   "SEDI","sedimentation","no condition"
   "SFR","spontaneous freezing","no condition"
   "DEPG","deposition on graupel","no condition"
   "RIM","riming of cloud water","no condition"
   "ACC","rain accretion on graupel","no condition"
   "CMEL","conversion melting of snow","no condition"
   "CFRZ","conversion freezing of rain","no condition"
   "WETG","wet growth of graupel","no condition"
   "GHCV","graupel to hail conversion","CCLOUD='ICE4' and LRED=T and CELEC='NONE'"
   "DRYG","dry growth of graupel","no condition"
   "GMLT","graupel melting","no condition"
   "WETH","wet growth of hail","CCLOUD='ICE4'"
   "HGCV","hail to graupel conversion","CCLOUD='ICE4' and LRED=T and CELEC='NONE'"
   "DRYH","dry growth of hail","CCLOUD='ICE4' and LRED=T and CELEC='NONE'"
   "CORR","correction","LRED=T and CELEC/='ELE3'"
   "NEGA","negativity correction","no condition"
   "NEADV","negativity correction induced by advection","no condition"
   "NECON","negativity correction induced by condensation","no condition"


