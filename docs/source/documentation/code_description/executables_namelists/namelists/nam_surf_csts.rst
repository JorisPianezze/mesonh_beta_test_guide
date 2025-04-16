.. _nam_surf_csts:

NAM_SURF_CSTS
----------------------------------------------------------------------------- 

.. csv-table:: NAM_SURF_CSTS content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XEMISSN", "REAL", "1.0 /0.99"
   "XANSMIN", "REAL", "0.5"
   "XANSMAX", "REAL", "0.85"
   "XAGLAMIN", "REAL", "0.8"
   "XAGLAMAX", "REAL", "0.85"
   "XALBWAT", "REAL", "0.135/0.065"
   "XALBCOEF_TA96", "REAL", "0.037"
   "XALBSCA_WAT", "REAL", "0.06"
   "XEMISWAT", "REAL", "0.98/0.96"
   "XALBWATICE", "REAL", "0.85/0.40"
   "XEMISWATICE", "REAL", "1.0/0.97"
   "XHGLA", "REAL", "33.3"
   "XWSNV", "REAL", "5.0"
   "XCFFV", "REAL", "4.0"
   "XZ0SN", "REAL", "0.001"
   "XZ0HSN", "REAL", "0.0001"
   "XTAU_SMELT", "REAL", "300.0"
   "XALBSEAICE", "REAL", "0.85/0.71"
   "XZ0FLOOD", "REAL", "0.0002"
   "XALBWATSNOW", "REAL", "0.85/0.60"
   "XTAU_LW", "REAL", "0.5"

* :code:`XEMISSN` : snow emissivity (default depends of LREPROD_OPER flag)

* :code:`XANSMIN` : minimum value for snow albedo

* :code:`XANSMAX` : maximum value for snow albedo

* :code:`XAGLAMIN` : minimum value for permanent snow/ice albedo

* :code:`XAGLAMAX` : maximum value for permanent snow/ice albedo

* :code:`XALBWAT` : water direct albedo (default depends of LREPROD_OPER flag)

* :code:`XALBCOEF_TA96` : coefficient used in th computation of albedo if ’TA96’ option selected

* :code:`XALBSCA_WAT` : water diffuse albedo

* :code:`XEMISWAT` : water emissivity (default depends of LREPROD_OPER flag)

* :code:`XALBWATICE` : water ice albedo (default depends of LREPROD_OPER flag)

* :code:`XEMISWATICE` : sea ice emissivity (default depends of LREPROD_OPER flag)

* :code:`XHGLA` : Height of aged snow in glacier case (allows Pn=1)

* :code:`XWSNV` : Coefficient for calculation of snow fraction over vegetation

* :code:`XZ0SN` : roughness length of pure snow surface (m)

* :code:`XZ0HSN` : roughness length for heat of pure snow surface (m)

* :code:`XTAU_SMELT` : snow melt timescale with D95 (s): needed to prevent time step dependence of melt when snow fraction < unity.

* :code:`XCFFV` : Coefficient for calculation of floodplain fraction over vegetation

* :code:`XALBSEAICE` : sea ice albedo (default depends of LREPROD_OPER flag)

* :code:`XZ0FLOOD` : flood z0

* :code:`XALBWATSNOW` : snow albedo over water bodies or lakes (default depends of LREPROD_OPER flag)

* :code:`XTAU_LW` : Extinction coefficient for view factor for long-wave radiation
