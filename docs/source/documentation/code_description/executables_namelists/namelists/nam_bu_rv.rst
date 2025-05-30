.. _nam_bu_rv:

NAM_BU_RV
-----------------------------------------------------------------------------

.. csv-table:: NAM_BU_RV content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LBU_RV", "LOGICAL", ".FALSE."
   "CBULIST_RV", "ARRAY(CHARACTER)", ""

* :code:`LBU_RV` : flag to activate budget for v-wind

* :code:`CBULIST_RV` : list of source terms

.. note::

   Description of the names to be used for the different source terms in the CBULIST_RV array and the conditions of their availability:

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "ALL","all available source terms (separated)","no condition"
   "ASSE","time filter (Asselin)","no condition"
   "NEST","nesting","NMODEL>1"
   "VISC","viscosity","LVISC=T and LVISC_UVW=T"
   "ADV","total advection","no condition"
   "FRC","forcing","LFORCING=T"
   "NUD","nudging","LNUDGING=T"
   "CURV","curvature","L1D=F and LCARTESIAN=F"
   "COR","Coriolis","LCORIO=T"
   "DIF","numerical diffusion","LNUMDIFU=T"
   "REL","relaxation","LHORELAX_UVWTH=T or LVE_RELAX=T or LVE_RELAX_GRD=T"
   "DRAG","drag force","LDRAGTREE=T"
   "DRAGEOL","drag force due to wind turbine","LMAIN_EOL=T"
   "DRAGB","drag force due to buildings","LDRAGBLDG=T"
   "HTURB","horizontal turbulent diffusion","CTURB='TKEL' and CTURBDIM='3DIM'"
   "VTURB","vertical turbulent diffusion","CTURB='TKEL'"
   "MAFL","mass flux","CSCONV='EDKF'"
   "PRES","pressure","no condition"
