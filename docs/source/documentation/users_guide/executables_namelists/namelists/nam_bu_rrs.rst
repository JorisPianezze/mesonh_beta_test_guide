.. _nam_bu_rrs:

NAM_BU_RRS
-----------------------------------------------------------------------------

.. csv-table:: NAM_BU_RRS content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LBU_RRS", "LOGICAL", ".FALSE."
   "CBULIST_RRS", "ARRAY(CHARACTER)", ""

* :code:`LBU_RRS` : flag to activate budget for snow

* :code:`CBULIST_RRS` : list of source terms

.. note::

   Description of the names to be used for the different source terms in the CBULIST_RRS array and the conditions of their availability:

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
   "REL","relaxation","LHORELAX_RS=T"

LIMA source terms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "NETUR","negativity correction induced by turbulence","CTURB='TKEL'"
   "SEDI","sedimentation","NMOM_I>=1 and NMOM_S>=1"
   "CNVI","conversion of snow to cloud ice","LPTSPLIT=T or (NMOM_I>=1 and NMOM_S>=1)"
   "DEPS","deposition on snow","LPTSPLIT=T or (NMOM_I>=1 and NMOM_S>=1)"
   "CNVS","conversion of pristine ice to snow","LPTSPLIT=T or (NMOM_I>=1 and NMOM_S>=1)"
   "AGGS","aggregation of snow","LPTSPLIT=T or (NMOM_I>=1 and NMOM_S>=1)"
   "RIM","riming of cloud water","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "HMS","Hallett-Mossop ice multiplication process due to snow riming","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "CIBU","ice multiplication process due to ice collisional breakup","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1 and LCIBU=T)"
   "ACC","accretion of rain on snow","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1 and NMOM_R>=1)"
   "CMEL","conversion melting of snow","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "WETG","wet growth of graupel","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "DRYG","dry growth of graupel","LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "WETH","wet growth of hail","LPTSPLIT=T or (NMOM_H>=1 and NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
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
   "DEPS","deposition on snow","no condition"
   "AGGS","aggregation of snow","no condition"
   "AUTS","autoconversion of ice","no condition"
   "RIM","riming of cloud water","no condition"
   "ACC","accretion of rain on snow","no condition"
   "CMEL","conversion melting of snow","no condition"
   "WETG","wet growth of graupel","no condition"
   "DRYG","dry growth of graupel","no condition"
   "WETH","wet growth of hail","CCLOUD='ICE4'"
   "DRYH","dry growth of hail","CCLOUD='ICE4' and LRED=T and CELEC='NONE'"
   "CORR","correction","LRED=T and CELEC/='ELE3'"
   "NEGA","negativity correction","no condition"
   "NEADV","negativity correction induced by advection","no condition"
   "NECON","negativity correction induced by condensation","no condition"


