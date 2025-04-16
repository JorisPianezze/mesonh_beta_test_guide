.. _nam_surf_slt:

NAM_SURF_SLT
----------------------------------------------------------------------------- 

.. csv-table:: NAM_SURF_SLT content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CEMISPARAM_SLT", "CHARACTER(LEN=5)", "'Vig01'"

* "CEMISPARAM_SLT": One-line sea salt emission parameterization type. This namelist gives the distribution of emitted sea salt of SURFEX. For Each paramterization type, a geometric standard deviation and a median radius is given. See the code init_sltn.f90 (MesoNH) or init_sltn.mnh (AROME, ALADIN) for values associated to these parameterizations. Note that if the defaut value is change, it is necessary to uses the same modes in the sea initialisation in the atmospheric model. It concerns the value of XINIRADIUS_SLT (initial radius), XINISIG_SLT (standard deviation) and CRGUNITS (mean radius definition) to have the same aerosol size distribution emitted and in the atmosphere. It is possible to do it directly in the fortran code (modd_salt.mnh in case of aladin/arome, modd_salt.f90 for Meso-NH) or for Meso-NH only, change the values of these variables in :ref:`nam_aero_conf` (:ref:`prep_real_case` or :ref:`prep_ideal_case`).
