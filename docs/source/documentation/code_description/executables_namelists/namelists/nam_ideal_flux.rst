.. _nam_ideal_flux:

NAM_IDEAL_FLUX
----------------------------------------------------------------------------- 

.. csv-table:: NAM_IDEAL_FLUX content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "NFORCF", "INTEGER", "2 (:math:`\leq` 48)"
   "NFORCT", "INTEGER", "2 (:math:`\leq` 48)"
   "XTIMEF", "REAL(NFORCF)", "0"
   "XTIMET", "REAL(NFORCT)", "0"
   "XSFTH", "REAL(NFORCF)", "0.0"
   "CSFTQ", "CHARACTER(LEN=7)", "'kg/m2/s'"
   "XSFTQ", "REAL(NFORCF)", "0.0"
   "XSFCO2", "REAL(NFORCF)", ""
   "CUSTARTYPE", "CHARACTER(LEN=5)", "'Z0'"
   "XUSTAR", "REAL(NFORCF)", "0.0"
   "XZ0", "REAL", "0.01"
   "XALB", "REAL", ""
   "XEMIS", "REAL", "1.0"
   "XTSRAD", "REAL(NFORCT)", "XTT=273.15K"
   
* :code:`NFORCF` : number of surface forcing instants for fluxes since the beginning of the run. The default value is NFORC=2.

* :code:`NFORCT` : number of surface forcing instants for radiative temperature since the beginning of the run. The default value is NFORC=2.

* :code:`XTIMEF` : times of forcing for fluxes (from beginning of run)

* :code:`XTIMET` : times of forcing for temperature (from beginning of run)

* :code:`XSFTH` : hourly data of heat surface flux (W/m2)

* :code:`CSFTQ` : Unit for the evaporation flux (kg/m2/s) or (W/m2)

* :code:`XSFTQ` : hourly data of water vapor surface flux

* :code:`XSFCO2` : hourly data of CO2 surface flux (kgC02/kg air * m/s)

* :code:`CUSTARTYPE` : type of computation for friction

* :code:`XUSTAR` : hourly data of friction (m2/s2)

* :code:`XZ0` : roughness length (m)

* :code:`XALB` : albedo (-)

* :code:`XEMIS` :emissivity (-)

* :code:`XTSRAD` : radiative temperature (K)   
