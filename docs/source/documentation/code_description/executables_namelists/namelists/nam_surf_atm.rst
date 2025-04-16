.. _nam_surf_atm:

NAM_SURF_ATM
----------------------------------------------------------------------------- 

.. csv-table:: NAM_SURF_ATM content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XCISMIN", "REAL", "6.7E-5"
   "XVMODMIN", "REAL", "0.0"
   "LALDTHRES", "LOGICAL", ".FALSE."
   "LDRAG_COEF_ARP", "LOGICAL", ".FALSE."
   "LALDZ0H", "LOGICAL", ".FALSE."
   "LNOSOF", "LOGICAL", ".TRUE."
   "LSLOPE", "LOGICAL", ".FALSE."
   "LCPL_GCM", "LOGICAL", ".FALSE."
   "XEDB", "REAL", "5.0"
   "XEDC", "REAL", "5.0"
   "XEDD", "REAL", "5.0"
   "XEDK", "REAL", "1.0"
   "XUSURIC", "REAL", "1.0"
   "XUSURID", "REAL", "0.035"
   "XUSURICL", "REAL", "4.0"
   "XVCHRNK", "REAL", "0.015"
   "XVZ0CM", "REAL", "0.0"
   "XDELTA_MAX", "REAL", "1.0"
   "XRIMAX", "REAL", "0.2"
   "LVERTSHIFT", "LOGICAL", ".FALSE."
   "LVZIUSTAR0_ARP", "LOGICAL", ".FALSE."
   "LRRGUST_ARP", "LOGICAL", ".FALSE."
   "XVZIUSTAR0", "REAL", "0.0"
   "XRZHZ0M", "REAL", "1.0"
   "XRRSCALE", "REAL", "1.15E-4"
   "XRRGAMMA", "REAL", "0.8"
   "XUTILGUST", "REAL", "0.125"
   "LCPL_ARP", "LOGICAL", ".FALSE."
   "LQVNPLUS", "LOGICAL", ".FALSE."
   "LVSHIFT_LW", "LOGICAL", ".FALSE."
   "LVSHIFT_PRCP", "LOGICAL", ".FALSE."
   "XCO2UNCPL", "REAL", "'none'"
   "LARP_PN", "LOGICAL", ".FALSE."
   "LCO2FOS", "LOGICAL", ".FALSE."
   
* :code:`LALDTHRES` : flag to set a minimum wind and shear like done in Arpege model.

* :code:`XCISMIN` : minimum wind shear to compute turbulent exchange coefficient (used only if LALDTHRES)

* :code:`XVMODMIN` : minimum wind speed to compute turbulent exchange coefficient (used only if LALDTHRES)

* :code:`LDRAG_COEF_ARP` : to use drag coefficient computed like in Arpege models

* :code:`LALDZ0H` : to take into account orography in heat roughness length

* :code:`LNOSOF` : no parameterization of subgrid orography effects on atmospheric forcing

* :code:`LSLOPE` : If True, correct parameterization of incoming radiations for homogeneous explicit slopes. If True, LNOSOF=F.

* :code:`LCPL_GCM` : flag used to red/write precipitation forcing from/into the erstart file for ARPEGE run

* :code:`XEDB`, :code:`XEDC`, :code:`XEDD`, :code:`XEDK` : coefficients used in Richardson critical numbers computation

* :code:`XUSURIC`, :code:`XUSURID`, :code:`XUSURICL` : Richardson critical numbers

* :code:`XVCHRNK`, :code:`XVZ0CM` : Charnock's constant and minimal neutral roughness length over sea (formulation of roughness length over sea)

* :code:`XDELTA_MAX` : maximum fraction of the foliage covered by intercepted water for high vegetation

* :code:`XRIMAX` : limitation of Richardson number in drag computation

* :code:`LVERTSHIFT` : vertical shifth from atmospheric orography to surface orography

* :code:`LVZIUSTAR0_ARP` : flag to activate arpege formulation for zoh over sea

* :code:`LRRGUST_ARP` : flag to activate the correction of CD, CH, CDN due to moist gustiness

* :code:`XVZIUSTAR0` : arpege formulation for zoh over sea

* :code:`XRZHZ0M` : arpege formulation for zoh over sea

* :code:`XRRSCALE` : arpege formulation for zoh over sea

* :code:`XRRGAMMA` : arpege formulation for zoh over sea

* :code:`XUTILGUST` : correction of CD, CH, CDN due to moist gustiness

* :code:`LCPL_ARP` : activate arpege formulation for Cp and L

* :code:`LQVNPLUS` : An option for the resolution of the surface temperature equation (Arpege)

* :code:`LVSHIFT_LW` : flag to activate/deactivate vertical shift for LongWave radiations

* :code:`LVSHIT_PRCP` : flag to activate/deactivate vertical shift for Precip

* :code:`XCO2UNCPL` : key for decoupling between CO2 employed for photosynthesis and radiative CO2 (in ppmv).

* :code:`LARP_PN` : Activate ARPEGE PN values for Cv and TAU_ICE

* :code:`LCO2FOS` : if activated, add fossil fuel emissions to natural CO2 emissions from ISBA
