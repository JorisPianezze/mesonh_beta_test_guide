.. _nam_diag_radiation:

NAM_DIAG - Radiation
-----------------------------------------------------------------------------

Only available if CRAD not NONE in YINIFILE.des.

* add :code:`NRAD_3D=0` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "DTHRAD", "Radiative heating/cooling rate (K/s)", "3D"
   "FLALWD", "Downward LW on FLAT surface (W/m2)", "2D"
   "DIRFLASWD", "Direct Downward SW on FLAT surface (W/m2)", "2D"
   "SCAFLASWD", "Scattered Downward SW on FLAT surface (W/m2)", "2D"
   "DIRSRFSWD", "Direct Downward SW (W/m2)", "2D"
   "CLEARCOL_TM1", "trace of cloud (-)", "2D"
   "EMIS", "emmissivity (-)", "2D"
   "ZENITH", "solar zenithal angle (RAD)", "2D"
   "AZIM", "azimuthal angle (RAD)", "2D"
   "DIR_ALB", "direct albedo(-)", "2D"
   "SCA_ALB", "scattered albedo (-)", "2D"
   "TSRAD", "radiative surface temperature (K)", "2D"

* add :code:`NRAD_3D=1` in :code:`NAM_DIAG` to store following variables (in addition to :code:`NRAD_3D=0` variables):

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "SWU", "Upward SW radiative fluxes (W/m2)", "2D"
   "SWD", "Downward SW radiative fluxes (W/m2)", "2D"
   "LWU", "Upward LW radiative fluxes (W/m2)", "2D"
   "LWD", "Downward LW radiative fluxes (W/m2)", "2D"
   "SWF_DOWN", "Downward SW radiative fluxes (W/m2)", "3D"
   "SWF_UP", "Upward SW radiative fluxes (W/m2)", "3D"
   "LWF_DOWN", "Downward LW radiative fluxes (W/m2)", "3D"
   "LWF_UP", "Upward LW radiative fluxes (W/m2)", "3D"
   "LWF_NET", "Total LW net radiative fluxes (W/m2)", "3D"
   "SWF_NET", "Total SW radiative fluxes (W/m2)", "3D"
   "DTRAD_LW", "LW radiative tendency for T (K/day)", "3D"
   "DTRAD_SW", "SW radiative tendency for T (K/day)", "3D"
   "RADSWD_VIS", "surface radiative flux in visible (W/m2)", "2D"
   "RADSWD_NIR", "surface radiative flux in near-infrared (W/m2)", "2D"
   "RADLWD", "LW surface radiative flux (W/m2)", "2D"

* add :code:`NRAD_3D=2` in :code:`NAM_DIAG` to store following variables (in addition to :code:`NRAD_3D=1,0` variables):

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "SWF_DOWN_CS", "Clear-Sky Downward SW radiative fluxes (W/m2)", "3D"
   "SWF_UP_CS", "Clear-Sky Upward SW radiative fluxes (W/m2)", "3D"
   "LWF_DOWN_CS", "Clear-Sky Downward LW radiative fluxes (W/m2)", "3D"
   "LWF_UP_CS", "Clear-Sky Upward LW radiative fluxes (W/m2)", "3D"
   "LWF_NET_CS", "Clear-Sky Total LW net radiative fluxes (W/m2)", "3D"
   "SWF_NET_CS", "Clear-Sky Total SW radiative fluxes (W/m2)", "3D"
   "DTRAD_LW_CS", "Clear-Sky LW radiative tendency for T (K/day)", "3D"
   "DTRAD_SW_CS", "Clear-Sky SW radiative tendency for T (K/day)", "3D"
   "RADSWD_NIR_CS", "Clear-Sky surface radiative flux in near-infrared (W/m2)", "2D"
   "RADLWD_CS", "Clear-Sky LW surface radiative flux (W/m2)", "2D"
 
* add :code:`NRAD_3D=3` in :code:`NAM_DIAG` to store following variables (in addition to :code:`NRAD_3D=2,1,0` variables):

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30  
   
   "PLAN_ALB_VIS", "planetary albedo in visible (-)", "[2D]"
   "PLAN_ALB_NIR", "planetary albedo in near-infrared (-)", "[2D]"
   "PLAN_TRA_VIS", "planetary transmission in visible (-)", "[2D]"
   "PLAN_TRA_NIR", "planetary transmission in near-infrared (-)", "[2D]"
   "PLAN_ABS_VIS", "planetary absorption in visible (-)", "[2D]"
   "PLAN_ABS_NIR", "planetary absorption in near-infrared (-)", "[2D]"

* add :code:`NRAD_3D=4` in :code:`NAM_DIAG` to store following variables (in addition to :code:`NRAD_3D=3,2,1,0` variables):

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30  
   
   "EFNEB_UP", "upward equivalent emissivity (Morcrette scheme)(-)", "3D"
   "EFNEB_DOWN", "downward equivalent emissivity (-)", "3D"
   "FLWP", "liquid water path (g/m2)", "3D"
   "FIWP", "ice water path (g/m2)", "3D"
   "EFRADL", "cloud liquid water effective radius (:math:`mu` m)", "3D"
   "EFRADI", "cloud ice effective radius (:math:`mu` m)", "3D"
   "SW_NEB", "effective cloud fraction (-)", "3D"
   "RRTM_LW_NEB", "effective cloud fraction (-)", "3D"
   "OTH_VIS", "cloud optical thickness (-)", "3D"
   "OTH_NI1", "cloud optical thickness (-)", "3D"
   "OTH_NI2", "cloud optical thickness (-)", "3D"
   "OTH_NI3", "cloud optical thickness (-)", "3D"
   "SSA_VIS", "cloud single scattering albedo (-)", "3D"
   "SSA_NI1", "cloud single scattering albedo (-)", "3D"
   "SSA_NI2", "cloud single scattering albedo (-)", "3D"
   "SSA_NI3", "cloud single scattering albedo (-)", "3D"
   "ASF_VIS", "cloud asymetry factor (-)", "3D"
   "ASF_NIR1", "cloud asymetry factor (-)", "3D"
   "ASF_NIR2", "cloud asymetry factor (-)", "3D"
   "ASF_NIR3", "cloud asymetry factor (-)", "3D"
   "ODAER_VIS", "", "3D"
   "ODAER_NIR1", "", "3D"
   "ODAER_NIR2", "", "3D"
   "ODAER_NIR3", "", "3D"
   "SSAAER_VIS", "", "3D"
   "SSAAER_NIR1", "", "3D"
   "SSAAER_NIR2", "", "3D"
   "SSAAER_NIR3", "", "3D"
   "GAER_VIS", "", "3D"
   "GAER_NIR1", "", "3D"
   "GAER_NIR2", "", "3D"
   "GAER_NIR3", "", "3D"

* add :code:`NRAD_3D=5` in :code:`NAM_DIAG` to store following variables (in addition to :code:`NRAD_3D=4,3,2,1,0` variables):

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30  

   "O3CLIM", "climatological ozone content (Pa/Pa)", "3D"
   "CUM_AER_LAND", "cumulated optical thickness of the different aerosols from the top of the domain", "3D"
   "CUM_AER_SEA", "cumulated optical thickness of the different aerosols from the top of the domain", "3D"
   "CUM_AER_DES", "cumulated optical thickness of the different aerosols from the top of the domain", "3D"
   "CUM_AER_URB", "cumulated optical thickness of the different aerosols from the top of the domain", "3D"
   "CUM_AER_VOL", "cumulated optical thickness of the different aerosols from the top of the domain", "3D"
   "CUM_AER_STRB", "cumulated optical thickness of the different aerosols from the top of the domain", "3D"
