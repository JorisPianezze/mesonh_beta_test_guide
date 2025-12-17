.. _nam_bu_rrh:

NAM_BU_RRH
-----------------------------------------------------------------------------

.. csv-table:: NAM_BU_RRH content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LBU_RRH", "LOGICAL", ".FALSE."
   "CBULIST_RRH", "ARRAY(CHARACTER)", ""

* :code:`LBU_RRH` : flag to activate budget for hail

* :code:`CBULIST_RRH` : list of source terms

.. note::

   Description of the names to be used for the different source terms in the CBULIST_RRH array and the conditions of their availability:
   
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
   "SEDI","sedimentation","NMOM_I>=1 and NMOM_H>=1"
   "DEPH","deposition on hail","NMOM_H>=1"
   "WETG","wet growth of graupel","NMOM_H>=1 and (LPTSPLIT=T or (NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1))"
   "HMLT","melting of hail","LPTSPLIT=T or (NMOM_H>=1 and NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "WETH","wet growth of hail","LPTSPLIT=T or (NMOM_H>=1 and NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "COHG","conversion of hail to graupel","LPTSPLIT=T or (NMOM_H>=1 and NMOM_I>=1 and NMOM_C>=1 and NMOM_S>=1)"
   "NEGA","negativity correction","no condition"
   "NEADV","negativity correction induced by advection","no condition"
   "NECON","negativity correction induced by condensation","no condition"

ICE4 source terms
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "NETUR","negativity correction induced by turbulence","CTURB='TKEL'"
   "SEDI","sedimentation","no condition"
   "GHCV","graupel to hail conversion","LRED=T and CELEC='NONE'"
   "WETG","wet growth of graupel","LRED=F or CELEC/='NONE'"
   "WETH","wet growth of hail","no condition"
   "HGCV","hail to graupel conversion","LRED=T and CELEC='NONE'"
   "DRYH","dry growth of hail","LRED=T and CELEC='NONE'"
   "HMLT","melting of hail","no condition"
   "CORR","correction","LRED=T and CELEC='NONE'"
   "NEGA","negativity correction","no condition"
   "NEADV","negativity correction induced by advection","no condition"
   "NECON","negativity correction induced by condensation","no condition"

   
