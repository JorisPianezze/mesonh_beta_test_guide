.. _nam_bu_rrr:

NAM_BU_RRR
-----------------------------------------------------------------------------

.. csv-table:: NAM_BU_RRR content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LBU_RRR", "LOGICAL", ".FALSE."
   "CBULIST_RRR", "ARRAY(CHARACTER)", ""

* :code:`LBU_RRR` : flag to activate budget for rain water

* :code:`CBULIST_RRR` : list of source terms

.. note::

   Description of the names to be used for the different source terms in the CBULIST_RRR array and the conditions of their availability:

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
   "REL","relaxation","LHORELAX_RR=T"

LIMA source terms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "SEDI","sedimentation of rain drops","NMOM_C>=1 and NMOM_R>=1"
   "AUTO","autoconversion into rain","LPTSPLIT=T or (NMOM_C>=1 and NMOM_R>=1)"
   "ACCR","accretion of cloud droplets","LPTSPLIT=T or (NMOM_C>=1 and NMOM_R>=1)"
   "REVA","rain evaporation","LPTSPLIT=T or (NMOM_C>=1 and NMOM_R>=1)"
   "HONR","rain homogeneous freezing","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and LNUCL=T and NMOM_R>=1)"
   "ACC","accretion of rain on aggregates","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1 and NMOM_R>=1)"
   "CFRZ","conversion freezing of rain","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "WETG","wet growth of graupel","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "DRYG","dry growth of graupel","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "GMLT","graupel melting","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "CVRC","rain to cloud change after other microphysical processes","LPTSPLIT=T"
   "HMLT","melting of hail","LPTSPLIT=T or (NMOM_H>=1 and NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "WETH","wet growth of hail","LPTSPLIT=T or (NMOM_H>=1 and NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "R2C1","rain to cloud change after sedimentation","LPTSPLIT=T and NMOM_C>=1 and NMOM_R>=1"
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
   
   "SEDI","sedimentation of rain drops","no condition"
   "AUTO","autoconversion into rain","NMOM_C>=1"
   "ACCR","accretion of cloud droplets","NMOM_C>=1"
   "REVA","rain evaporation","NMOM_C>=1"
   "ACC","accretion of rain on aggregates","no condition"
   "CMEL","collection of droplets by snow and conversion into rain","LRED=T and CELEC/='ELE3'"
   "CFRZ","conversion freezing of rain","no condition"
   "WETG","wet growth of graupel","no condition"
   "DRYG","dry growth of graupel","no condition"
   "GMLT","graupel melting","no condition"
   "WETH","wet growth of hail","CCLOUD='ICE4'"
   "DRYH","dry growth of hail","CCLOUD='ICE4' and LRED=T and CELEC='NONE'"
   "HMLT","melting of hail","CCLOUD='ICE4'"
   "SFR","spontaneous freezing","no condition"
   "CORR","correction","LRED=T and CELEC/='ELE3'"
   "NEGA","negativity correction","no condition"
   "NEADV","negativity correction induced by advection","no condition"
   "NECON","negativity correction induced by condensation","no condition"

C2R2 / KHKO source terms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "SEDI","sedimentation of rain drops","no condition"
   "AUTO","autoconversion into rain","NMOM_R>=1"
   "ACCR","accretion of cloud droplets","NMOM_R>=1"
   "REVA","rain evaporation","NMOM_R>=1"
   "NEGA","negativity correction","no condition"
   "NETUR","negativity correction induced by turbulence","CTURB='TKEL'"
   "NEADV","negativity correction induced by advection","no condition"
   "NECON","negativity correction induced by condensation","no condition"

KESS source terms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "SEDI","sedimentation of rain drops","no condition"
   "AUTO","autoconversion into rain","no condition"
   "ACCR","accretion of cloud droplets","no condition"
   "REVA","rain evaporation","no condition"
   "NEGA","negativity correction","no condition"
   "NEADV","negativity correction induced by advection","no condition"
   "NECON","negativity correction induced by condensation","no condition"

   
