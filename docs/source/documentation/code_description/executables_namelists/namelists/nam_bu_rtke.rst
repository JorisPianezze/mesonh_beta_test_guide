.. _nam_bu_rtke:

NAM_BU_RTKE
-----------------------------------------------------------------------------

.. csv-table:: NAM_BU_RTKE content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LBU_RTKE", "LOGICAL", ".FALSE."
   "CBULIST_RTKE", "ARRAY(CHARACTER)", ""

* :code:`LBU_RTKE` : flag to activate budget for turbulent kinetic energy

* :code:`CBULIST_RTKE` : list of source terms

.. note::

   Description of the names to be used for the different source terms in the CBULIST_RTKE array and the conditions of their availability:

.. csv-table::
   :header: "Name", "Description", "Condition(s)"
   :widths: 30, 30, 30
   
   "ALL","all available source terms (separated)","no condition"
   "ASSE","time filter (Asselin)","no condition"
   "ADV","total advection","no condition"
   "FRC","forcing","LFORCING=T"
   "DIF","numerical diffusion","LNUMDIFTH=T"
   "REL","relaxation","LHORELAX_TKE=T"
   "DRAG","drag force","LDRAGTREE=T"
   "DRAGB","drag force due to buildings","LDRAGBLDG=T"
   "DP","dynamic production","no condition"
   "TP","thermal production","no condition"
   "DISS","dissipation of TKE","no condition"
   "TR","turbulent transport","no condition"


