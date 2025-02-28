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

* Surface schemes: SURFEX 7.3, see the Geosci. Model Dev. special issue relative to SURFEX 7.2

  * General reference: V. Masson, P. Le Moigne, E. Martin, S. Faroux, A. Alias, R. Alkama, S. Belamari, A. Barbu, A. Boone, F. Bouyssel, P. Brousseau, E. Brun, J.-C. Calvet, D. Carrer, B. Decharme, C. Delire, S. Donier, K. Essaouini, A.-L. Gibelin, H. Giordani, F. Habets, M. Jidane, G. Kerdraon, E. Kourzeneva, M. Lafaysse, S. Lafont, C. Lebeaupin Brossier, A. Lemonsu, J.-F. Mahfouf, P. Marguinaud, M. Mokhtari, S. Morin, G. Pigeon, R. Salgado, Y. Seity, F. Taillefer, G. Tanguy, P. Tulet, B. Vincendon, V. Vionnet, and A. Voldoire, 2013, the SURFEXv7.2 land and ocean surface platform for coupled or offline simulation of earth surface variables and fluxes, Geosci. Model Dev., 6, 929-960. Link to paper.

  * Water surfaces:

    * Sea surface turbulent fluxes: Belamari, S., 2005 : Report on uncertainty estimates of an optimal bulk formulation for surface turbulent fluxes. MERSEA IP Deliverable, D.4.1.2, 29.
    * 1D TKE oceanic model: Gaspar, P., Y. Grégoris, and J.-M. Lefevre, 1990: A simple eddy kinetic energy model for simulations of the oceanic vertical mixing: Tests at station Papa and long‐term upper ocean study site, J. Geophys. Res., 95(C9), 16,179–16,193, doi:10.1029/JC095iC09p16179 Link to paper 

  * Urban and artifical areas: Masson V., 2000: A physically-based scheme for the urban energy budget in atmospheric models. Bound. Layer Meteor, 1994, 357-397. Link to paper

  * Soil and vegetation: Noilhan, J., and S. Planton, 1989: A simple parameterization of land surface processes for meteorological models. Mon. Wea. Rev., 117, 536-549. Link to paper 

* Land use - ECOCLIMAP: Masson, V., J.-L. Champeaux, C. Chauvin, C. Meriguet, and R. Lacaze, 2003: A global database of land surface parameters at 1 km resolution for use in meteorological and climate models, J. Climate, 16, 1261-1282. Link to paper and ECOCLIMAP-II: Faroux, S., A. T. Kaptué Tchuenté, J.-L. Roujean, V. Masson, E. Martin, and P. Le Moigne, 2013: ECOCLIMAP-II/Europe: a twofold database of ecosystems and surface parameters at 1 km resolution based on satellite information for use in land surface, meteorological and climate models. Geosci. Model Dev., 6, 563-582. Link to paper 

Part III: Physics
-----------------------------------------------------------------------------

* Radiation

  * Longwave: Mlawer, E.J., S.J. Taubman, P.D. Brown, M.J. Iacono, and S.A. Clough, 1997: Radiative transfer for inhomogeneous atmospheres: RRTM, a validated correlated-k model for the longwave. J. Geophys. Res., 102D, 16663-16682. Link to paper
  * Shortwave: Fouquart, Y., and B. Bonnel, 1980: Computations of solar heating of the earth’s atmosphere: A new parametrization. Beitr. Phys. Atmosph., 53, 35-62. 

* Turbulence scheme: Cuxart, J., Bougeault, Ph. and Redelsperger, J.L., 2000: A turbulence scheme allowing for mesoscale and large-eddy simulations. Q. J. R. Meteorol. Soc., 126, 1-30. Link to paper

* EDKF shallow convection scheme: Pergaud, J., V. Masson, S. Malardel, and F. Couvreux, 2009: A parameterization of dry thermals and shallow cumuli for mesoscale numerical weather prediction, Bound.-Layer. Meteor., 132, 83-106. Link to paper

* Convection scheme: Bechtold, P., E. Bazile, F. Guichard, P. Mascart and E. Richard, 2001: A mass flux convection scheme for regional and global models. Quart. J. Roy. Meteor. Soc., 127, 869-886. Link to paper

* Microphysical schemes for warm clouds

  * C2R2: Cohard, J.-M., and J.-P. Pinty, 2000a: A comprehensive two-moment warm microphysical bulk scheme. Part I: Description and selective tests. Q. J. R. Meteorol. Soc., 126, 1815-1842. Link to paper

  * KHKO: Geoffroy, O., 2007: Modelisation LES des precipitations dans les nuages de couche limite et parametrisation pour les GCM, Ph.D. thesis, Universite Paul Sabatier (Toulouse III). 

* Microphysical schemes for atmospheric ice

  * ICE3: Pinty, J.-P. and P. Jabouille, 1998: A mixed-phase cloud parameterization for use in mesoscale non-hydrostatic model: simulations of a squall line and of orographic precipitations. Proc. Conf. of Cloud Physics, Everett, WA, USA, Amer. Meteor. soc., Aug. 1999, 217 - 220. Paper and Caniaux, G., J.-L. Redelsperger and J.-P. Lafore, 1994: A numerical study of the stratiform region of a fast-moving squall line. Part I. General description, and water and heat budgets. J. Atmos. Sci., 51, 2046-2074. Link to paper

  * ICE4: Lascaux, F., E. Richard, and J.-P. Pinty, 2006: Numerical simulations of three MAP IOPs and the associated microphysical processes. Quart. J. Roy. Meteor. Soc., 132, 1907-1926. Link to paper

  * LIMA: Vié, B., J.-P. Pinty, S. Berthet, and M. Leriche, 2016: LIMA (v1.0): a quasi two-moment microphysical scheme driven by a multimodal population of cloud condensation and ice freezing nuclei, Geosci. Model Dev., 9, 567-586. Link to paper 

* Sub-grid condensation schemes

  * Warm phase: Bougeault, P. 1981: Modeling the trade-wind cumulus boundary layer. Part I: testing the ensemble cloud relations against numerical data, J. Atmos. Sci., 38, 2414-2428, 1981 Link to paper and Bougeault, P., 1982: Cloud-ensemble relations based on the gamma probability distribution for the higher-order models of the planetary boundary layer, J. Atmos. Sci., 39, 2691-2700. Link to paper

  * Ice phase and convective clouds: Chaboureau J.-P., and P. Bechtold, 2002: A simple cloud parameterization derived from cloud resolving model data: Diagnostic and prognostic applications. J. Atmos. Sci., 59, 2362- 2372. Link to paper and Chaboureau J.-P., and P. Bechtold, 2005: Statistical representation of clouds in a regional model and the impact on the diurnal cycle of convection during Tropical Convection, Cirrus and Nitrogen Oxides (TROCCINOX). J. Geophys. Res., 110, D17103, doi:10.1029/2004JD005645. Link to paper 

* Electrical scheme: Barthe, C., M. Chong, J.-P. Pinty, C. Bovalo, and J. Escobar, CELLS v1.0: updated and parallelized version of an electrical scheme to simulate multiple electrified clouds and flashes over large domains, Geosci. Model Dev., 5, 167-184, 2012. Link to paper 

Part IV: Chemistry and Aerosols
-----------------------------------------------------------------------------

* Basics for the chemistry and aerosols

  * Chemical scheme RACM: Stockwell R.W., Kirchner F., Kuhn M., Seefeld S., 1997: A new mechanism for regional atmospheric chemistry modeling, J. Geophys. Res., 102(D22), 25847-25879. Link to paper

  * Chemical scheme ReLACS: Crassier, V., K. Suhre, P. Tulet, and R. Rosset, 2000: Development of a reduced chemical scheme for use in mesoscale meteororological models. Atm. Env., 34, 2633–2644. Link to paper

  * Chemical scheme CACM: Griffin, R. J., D. Dabdub, and J. H. Seinfeld, 2002: Secondary organic aerosol, 1, Atmospheric chemical mechanism for production of molecular constituents, J. Geophys. Res., 107(D17), 4332, doi:10.1029/2001JD000541. Link to paper

  * Equilibrium between gases and aerosols for inorganic ARES: Binkowki, F and U. Shankar, 1995: The regional particulate model: 1. Model description and preliminary results, J. Geophys. Res., 100(D12), 26191-26209, doi:10.1029/95JD02093. Link to paper

  * Equilibrium between gases and aerosols for inorganic ISORROPIA: Nenes, A., C. Pilinis, and S. Pandis, 1998: A new thermodynamic model for inorganic multicomponent atmospheric aerosols, Aquat. Geochem., 4, 123-152, doi:10.1029/95JD02093. Link to paper

  * Equilibrium between gases and aerosols for inorganic EQSAM: Metzger, S., F. Dentener, S. Pandis, and J. Lelieveld, 2002: Gas/aerosols partitioning: 1. A computationally efficient model. J. Geophys. Res., 107, ACH 16–1, doi:10.1029/2001JD001102. Link to paper

  * Equilibrium between gases and aerosols for organic Pun: Pun, B. K., R. J. Griffin, C. Seigneur, and J. H. Seinfeld, 2002: Secondary organic aerosols 2. Thermodynamic model for gas/particle partitioning of molecular constituents. J. Geophys. Res., 107, AAC 4–1–AAC 4–15, doi:10.1029/2001JD000542. Link to paper

  * Equilibrium between gases and aerosols for organic MPMPO: Griffin, R. J., K. Nguyen, D. Dabdub, and J. H. Seinfeld, 2003: A coupled hydrophobic-hydrophilic model for predicting secondary organic aerosols formation. J. Atmos. Chem., 44, 171–190, doi:10.1023/A:1022436813699. Link to paper 

* Atmospheric chemistry

  * Chemistry module: Tulet, P, V. Crassier, F. Solmon, D. Guedalia, R. Rosset, 2003: Description of the Mesoscale Nonhydrostatic Chemistry model and application to a transboundary pollution episode between northern France and southern England, J. Geophys. Res., 108(D1), 4021, doi:10.1029/2000JD000301 Link to paper

  * Dry deposition: Wesely, M., Parametrizations of surface resistance to gaseous dry deposition in regional scale, numerical models, Atmos. Environ., 23, 12931304, 1989. Link to paper

  * Photolysis rates: Madronich, S., 1987: Photodissociation in the atmosphere: 1. Actinic flux and the effects of ground reflections and clouds. J. Geophys. Res., 92, D8, 9740–9752. Link to paper 

* Clouds and chemistry

  * Scavenging by convective precipitations: Mari C., D.J. Jacob, P. Bechtold, 2000: Transport and scavenging of soluble gases in a deep convective cloud, J. Geophys. Res. 105, 22255-22263. Link to paper

  * Lightning produced NOx: Mari, C., J.-P. Chaboureau, J.-P. Pinty, J. Duron, P. Mascart, J.-P. Cammas, F. Gheusi, T. Fehr, H. Schlager, A. Roiger, H. Lichtenstein, and P. Stock, Regional lightning NOx sources during the TROCCINOX experiment, Atmos. Chem. Phys., 6, 5559-5572, 2006. Link to paper

  * Cloud chemistry module: Leriche, M., J.-P. Pinty, C. Mari and D. Gazen, A cloud chemistry module for the 3-D cloud resolving mesoscale model Meso-NH with application to idealized cases, Geosci. Model Dev., 6, 1275-1298, 2013. Link to paper 

* Aerosols

  * Dust aerosols and sea salt: Grini, A., P. Tulet, and L. Gomes, 2006: Dusty weather forecasts using the MesoNH mesoscale atmospheric model. J. Geophys. Res., 111, D19205, doi:10.1029/2005JD007007. Link to paper

  * ORILAM module: Tulet, P, V. Crassier, F. Cousin, K. Shure, R. Rosset, 2005: ORILAM, A three moment lognormal aerosol scheme for mesoscale atmospheric model. On-line coupling into the Meso-NH-C model and validation on the Escompte campaign,J. Geophys. Res., 110, D18201, doi:10.1029/2004JD005716. Link to paper

  * ORILAM-SOA module: Tulet P., A. Grini, R.J. Griffin, S. Petitcol, 2006: ORILAM-SOA: A computationally efficient model for predicting secondary organic aerosols in 3D atmospheric models. J. Geophys. Res., 111, D23208, doi:10.1029/2006JD007152. Link to paper 

Part V: Diagnostics
-----------------------------------------------------------------------------

* Kinetic energy spectra: Ricard, D., C. Lac, S. Riette, R. Legrand, and A. Mary, Kinetic energy spectra characteristics of two convection-permitting limited-area models AROME and Meso-NH, Quart. J. Roy. Meteor. Soc., 139, 1327-1341, 2013. Link to paper

* GPS zenith delay: Brenot, H., V. Ducrocq, A. Walpersdorf, C. Champollion, and O. Caumont, 2006: GPS zenith delay sensitivity evaluated from high-resolution numerical weather prediction simulations of the 8-9th September 2002 flash flood over southeastern France. J. Geophys. Res., 111, doi:10.1029/2004JD005726 Link to paper

* Radar products

  * Grid-point radar diagnostics: Richard, E., S. Cosma, P. Tabary, J.-P. Pinty, and M. Hagen, 2003: High-resolution numerical simulations of the convective system observed in the Lago Maggiore area on 17 September 1999 (MAP IOP 2a). Quart. J. Roy. Meteor. Soc., 129, 543-563. Link to paper

  * Radar diagnostics on Plan Position Indicators (PPI): Caumont, O., V. Ducrocq, G. Delrieu, M. Gosset, J.-P. Pinty, J. Parent du Chatelet, H. Andrieu, Y. Lemaitre, and G. Scialom, 2006: A radar simulator for high-resolution nonhydrostatic models, J. Atmos. Ocean. Tech., 23, 1049-1067. Link to paper 

* Satellite diagnostics: Saunders, R., M. Matricardi, P. Brunel, S. English, P. Bauer, U. O'Keeffe, P. Francis and P. Rayer, 2005: RTTOV-8 science and validation report. NWP SAF Report, 41 pages, Tech. rep. and Chaboureau, J.-P., N. Söhne, J.-P. Pinty, I. Meirold-Mautner, E. Defer, C. Prigent, J.-R. Pardo, M. Mech, and S. Crewell, A midlatitude cloud database validated with satellite observation, J. Appl. Meteorol. Clim., 47, 1337-1353, 2008 Link to paper
