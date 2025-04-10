.. _nam_bu_rw:

NAM_BU_RW
-----------------------------------------------------------------------------

.. csv-table:: NAM_BU_RW content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LBU_RW", "LOGICAL", ".FALSE."
   "CBULIST_RW", "ARRAY(CHARACTER)", ""

* :code:`LBU_RW` : flag to activate budget for w-wind

* :code:`CBULIST_RW` : list of source terms

.. note::

   Description of the names to be used for the different source terms in the CBULIST_RW array and the conditions of their availability:

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
   "CURV","curvature","L1D=F and LCARTESIAN=F and LTHINSHELL=F"
   "COR","Coriolis","LCORIO=T and LTHINSHELL=F"
   "DIF","numerical diffusion","LNUMDIFU=T"
   "REL","relaxation","LHORELAX_UVWTH=T or LVE_RELAX=T or LVE_RELAX_GRD=T"
   "HTURB","horizontal turbulent diffusion","CTURB='TKEL' and CTURBDIM='3DIM'"
   "VTURB","vertical turbulent diffusion","CTURB='TKEL'"
   "GRAV","gravity","no condition"
   "PRES","pressure","no condition"
   "DRAGEOL","drag force due to wind turbine","LMAIN_EOL=T"
