Scientific & References
=============================================================================

Scientific
*****************************************************************************

* :download:`Meso-NH - Part I : Dynamics <scientific/scidoc_p1.pdf>`
* :download:`Meso-NH - Part II : Model Setup <scientific/scidoc_p2.pdf>`
* :download:`Meso-NH - Part III : Physics <scientific/scidoc_p3.pdf>`
* :download:`Meso-NH - Part IV : Chemistry and Aerosols <scientific/scidoc_p4.pdf>`
* :download:`Meso-NH - Part V : Budget and Diagnostics <scientific/scidoc_p5.pdf>`
* `SURFEX <https://www.umr-cnrm.fr/surfex/spip.php?rubrique11>`_

References
*****************************************************************************

General references
-----------------------------------------------------------------------------

* **version >= 5.4:** Overview of the Meso-NH model version 5.4 and its applications :cite:p:`lac_overview_2018`.

* **version < 5.4:** The Meso-NH Atmospheric Simulation System. Part I: Adiabatic formulation and control simulations :cite:p:`lafore_meso-nh_1998`

Part I: Dynamics
-----------------------------------------------------------------------------

* **Grid-nesting:** High-resolution non-hydrostatic simulations of flash-flood episodes with grid-nesting and ice-phase parametrization :cite:p:`stein_high-resolution_2000`

* **Parallelization:** Parallelization of the French meteorological mesoscale model Meso-NH :cite:p:`amestoy_parallelization_1999`

* **Large parallel computing capability:** Seamless Meso-NH modeling over very large grids :cite:p:`pantillon_seamless_2010`

Part II: Model Setup
-----------------------------------------------------------------------------

* **Surface scheme (SURFEX):**

  * **General reference:** 

    * **version >= 8.0:** SURFEX v8.0 interface with OASIS3-MCT to couple atmosphere with hydrology, ocean, waves and sea-ice models, from coastal to global scales :cite:p:`voldoire_surfex_2017`  
    * **version < 8.0:** The SURFEXv7.2 land and ocean surface platform for coupled or offline simulation of earth surface variables and fluxes :cite:p:`masson_surfexv7.2_2013`

  * **Water surfaces:**

    * **Sea surface turbulent fluxes:** Report on uncertainty estimates of an optimal bulk formulation for surface turbulent fluxes :cite:p:`belamari_report_2005`
    * **1D TKE oceanic model:** A simple eddy kinetic energy model for simulations of the oceanic vertical mixing: Tests at station Papa and long‐term upper ocean study site :cite:p:`gaspar_simple_1990`

  * **Urban and artifical areas:** A physically-based scheme for the urban energy budget in atmospheric models :cite:p:`masson_physically-based_2000`

  * **Soil and vegetation:** A simple parameterization of land surface processes for meteorological models :cite:p:`noilhan_simple_1989`

  * **Land use - ECOCLIMAP-II/Europe:** A twofold database of ecosystems and surface parameters at 1 km resolution based on satellite information for use in land surface, meteorological and climate models :cite:p:`faroux_ecoclimap-iieurope_2013`

Part III: Physics
-----------------------------------------------------------------------------

* **Radiation:**

  * **Longwave:** Radiative transfer for inhomogeneous atmospheres: RRTM, a validated correlated-k model for the longwave :cite:p:`mlawer_radiative_1997`
  * **Shortwave:** Computations of solar heating of the earth's atmosphere: A new parametrization :cite:p:`FOUQUARTY1980`

* **Turbulence scheme:** A turbulence scheme allowing for mesoscale and large-eddy simulations :cite:p:`cuxart_turbulence_2000`

* **EDKF shallow convection scheme:** A parameterization of dry thermals and shallow cumuli for mesoscale numerical weather prediction :cite:p:`pergaud_parameterization_2009`

* **Convection scheme:** A mass flux convection scheme for regional and global models :cite:p:`bechtold_massflux_2001`

* **Microphysical schemes for warm clouds:**

  * **C2R2:** A comprehensive two-moment warm microphysical bulk scheme. Part I: Description and selective tests :cite:p:`cohard_comprehensive_2000`

  * **KHKO:** Modelisation LES des precipitations dans les nuages de couche limite et parametrisation pour les GCM :cite:p:`geoff2007`

* **Microphysical schemes for atmospheric ice:**

  * **ICE3:**
  
    * A mixed-phase cloud parameterization for use in mesoscale non-hydrostatic model: simulations of a squall line and of orographic precipitations :cite:p:`pinty_mixed-phase_1998`
    * A numerical study of the stratiform region of a fast-moving squall line. Part I. General description, and water and heat budgets :cite:p:`caniaux_numerical_1994`

  * **ICE4:** Numerical simulations of three MAP IOPs and the associated microphysical processes :cite:p:`lascaux_numerical_2006`

  * **LIMA:** LIMA (v1.0): a quasi two-moment microphysical scheme driven by a multimodal population of cloud condensation and ice freezing nuclei :cite:p:`vie_lima_2016`

* **Sub-grid condensation schemes:**

  * **Warm phase:**
  
    * Modeling the trade-wind cumulus boundary layer. Part I: testing the ensemble cloud relations against numerical data :cite:p:`bougeault_modeling_1981`
    * Cloud-ensemble relations based on the gamma probability distribution for the higher-order models of the planetary boundary layer :cite:p:`bougeault_cloud-ensemble_1982`

  * **Ice phase and convective clouds:**
  
    * A simple cloud parameterization derived from cloud resolving model data: Diagnostic and prognostic applications :cite:p:`chaboureau_simple_2002`
    * Statistical representation of clouds in a regional model and the impact on the diurnal cycle of convection during Tropical Convection, Cirrus and Nitrogen Oxides (TROCCINOX) :cite:p:`chaboureau_statistical_2005`

* **Electrical scheme:** CELLS v1.0: updated and parallelized version of an electrical scheme to simulate multiple electrified clouds and flashes over large domains :cite:p:`barthe_cells_2012`

Part IV: Chemistry and Aerosols
-----------------------------------------------------------------------------

* **Basics for the chemistry and aerosols:**

  * **Chemical scheme RACM:** A new mechanism for regional atmospheric chemistry modeling, J. Geophys. Res., 102(D22), 25847-25879. Link to paper :cite:p:`stockwell_new_1997`

  * **Chemical scheme ReLACS:** Development of a reduced chemical scheme for use in mesoscale meteororological models. Atm. Env., 34, 2633–2644. Link to paper :cite:p:`crassier_development_2000`

  * **Chemical scheme CACM:** Secondary organic aerosol, 1, Atmospheric chemical mechanism for production of molecular constituents, J. Geophys. Res., 107(D17), 4332, doi:10.1029/2001JD000541. Link to paper :cite:p:`griffin_secondary_2002`

  * **Equilibrium between gases and aerosols for inorganic ARES:** The regional particulate model: 1. Model description and preliminary results :cite:p:`binkowski_regional_1995`

  * **Equilibrium between gases and aerosols for inorganic ISORROPIA:** A new thermodynamic model for inorganic multicomponent atmospheric aerosols :cite:p:`nenes_isorropia_1998`

  * **Equilibrium between gases and aerosols for inorganic EQSAM:** Gas/aerosols partitioning: 1. A computationally efficient model :cite:p:`metzger_gasaerosol_2002`

  * **Equilibrium between gases and aerosols for organic Pun:** Secondary organic aerosols 2. Thermodynamic model for gas/particle partitioning of molecular constituents :cite:p:`pun_secondary_2002`

  * **Equilibrium between gases and aerosols for organic MPMPO:** A coupled hydrophobic-hydrophilic model for predicting secondary organic aerosols formation :cite:p:`griffin_coupled_2003`

* **Atmospheric chemistry:**

  * **Chemistry module:** Description of the Mesoscale Nonhydrostatic Chemistry model and application to a transboundary pollution episode between northern France and southern England :cite:p:`tulet_description_2003`

  * **Dry deposition:** Parametrizations of surface resistance to gaseous dry deposition in regional scale, numerical models :cite:p:`wesely_parameterization_1989`

  * **Photolysis rates:** Photodissociation in the atmosphere: 1. Actinic flux and the effects of ground reflections and clouds :cite:p:`madronich_photodissociation_1987`

* **Clouds and chemistry:**

  * **Scavenging by convective precipitations:** Transport and scavenging of soluble gases in a deep convective cloud :cite:p:`mari_transport_2000`

  * **Lightning produced NOx:** Regional lightning NOx sources during the TROCCINOX experiment :cite:p:`mari_regional_2006`

  * **Cloud chemistry module:** A cloud chemistry module for the 3-D cloud resolving mesoscale model Meso-NH with application to idealized cases :cite:p:`leriche_cloud_2013`

* **Aerosols:**

  * **Dust aerosols and sea salt:** Dusty weather forecasts using the MesoNH mesoscale atmospheric model :cite:p:`grini_dusty_2006`

  * **ORILAM module:** ORILAM, A three moment lognormal aerosol scheme for mesoscale atmospheric model. On-line coupling into the Meso-NH-C model and validation on the Escompte campaign :cite:p:`tulet_orilam_2005`

  * **ORILAM-SOA module:** ORILAM-SOA: A computationally efficient model for predicting secondary organic aerosols in 3D atmospheric models :cite:p:`tulet_orilamsoa_2006`

Part V: Diagnostics
-----------------------------------------------------------------------------

* **Kinetic energy spectra:** Kinetic energy spectra characteristics of two convection-permitting limited-area models AROME and Meso-NH :cite:p:`ricard_kinetic_2013`

* **GPS zenith delay:** GPS zenith delay sensitivity evaluated from high-resolution numerical weather prediction simulations of the 8-9th September 2002 flash flood over southeastern France :cite:p:`brenot_gps_2006`

* **Radar products:**

  * **Grid-point radar diagnostics:** High-resolution numerical simulations of the convective system observed in the Lago Maggiore area on 17 September 1999 (MAP IOP 2a) :cite:p:`richard_highresolution_2003`

  * **Radar diagnostics on Plan Position Indicators (PPI):** A radar simulator for high-resolution nonhydrostatic models :cite:p:`caumont_radar_2006`

* **Satellite diagnostics:** A midlatitude cloud database validated with satellite observation :cite:p:`chaboureau_midlatitude_2008`
