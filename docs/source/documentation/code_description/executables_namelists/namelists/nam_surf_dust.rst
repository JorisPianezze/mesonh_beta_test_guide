.. _nam_surf_dust:

NAM_SURF_DUST
----------------------------------------------------------------------------- 

.. csv-table:: NAM_SURF_DUST content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CEMISPARAM_DST", "CHARACTER(LEN=5)", "'AMMA'"
   "CVERMOD", "CHARACTER(LEN=6)", "'NONE'"
   "XFLX_MSS_FDG_FCT", "REAL", "12.0e-4"
   
* :code:`CEMISPARAM_DST` : One-line dust emission parameterization type. This namelist gives the distribution of emitted dust of SURFEX. For Each paramterization type, a geometric standard deviation and a median radius is given. Moreover , the repatition of mass flux could be derive from the friction velocity (case of "AMMA" or "EXPLI") or imposed (case of "Dal87", "alf98", "She84" or "PaG77". See the code init_dstn.f90 (Meso-NH) or init_dstn.mnh (AROME, ALADIN) for values associated to these parameterizations. Note that if the defaut value is change, it is necessary to uses the same modes in the dust initialisation in the atmospheric model. It concerns the value of XINIRADIUS (initial radius), XINISIG (standard deviation) and CRGUNITD (mean radius definition) to have the same aerosol size distribution emitted and in the atmosphere. It is possible to do it directly in the fortran code (modd_dust.mnh in case of aladin/arome, modd_dust.f90 for Meso-NH) or for Meso-NH only, change the values of these variables in :ref:`nam_aero_conf` (:ref:`prep_real_case` or :ref:`prep_ideal_case`).

* :code:`CVERMOD` : New parameterization of the dust emission formulation. In development, not recommended to uses it in this version.

* :code:`XFLX_MSS_FDG_FCT` : Value of the :math:`\alpha` factor representing the ratio of the vertical mass flux over the horizontal mass flux in the saltation layer (use only If CVERMOD=’NONE’). This :math:`\alpha` factor depend on the size distribution of the aerosol consider in the model.
