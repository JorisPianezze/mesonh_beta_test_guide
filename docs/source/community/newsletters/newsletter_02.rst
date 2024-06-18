Infolettre #02
================================================

**3 juillet 2024.** Version française, English version `here <newsletter_01_english.html>`_.

 

Chers utilisateurs, chères utilisatrices de Méso-NH,

Voici la 2ème infolettre de notre communauté Méso-NH. Vous y trouverez un entretien avec une développeuse de Méso-NH, les dernières nouvelles de l’équipe support et la liste des dernières publications utilisant Méso-NH.

Entretien avec `Fleur Couvreux <mailto:fleur.couvreux@meteo.fr>`_ (CNRM)
**************************************************************************

.. image:: photo_fleur_couvreux.jpg
  :width: 300

Fleur, tu as développé la possibilité d'inclure des traceurs passifs à décroissance radioactive dans Méso-NH. Pourrais-tu résumer ce que fait cette option ?
  Cette option a initialement été développée pour identifier les structures cohérentes, à savoir les thermiques, ces panaches ascendants qui contribuent fortement au transport vertical dans les couches limites convectives, dans des simulations LES. Une fois les structures identifiées on peut quantifier leur contribution au transport vertical de chaleur, d’humidité et de quantité de mouvement.

  On peut activer sans modifier le code jusqu’à trois traceurs passifs. Le 1er est émis avec un flux constant en surface, le 2eme est émis juste en dessous de la base des nuages, il a été implémenté pour estimer les échanges entre la couche sous-nuageuse et l’intérieur des nuages, voire la couche de transition. Le 3e est émis juste au-dessus du sommet moyen des nuages et permet d’estimer les échanges au sommet des nuages. Si on est en condition de ciel clair, on peut choisir d’émettre le traceur 3 au sommet de la couche limite et choisir comment déterminer cette hauteur de couche limite[#namelist]_. Les trois traceurs subissent une décroissance radioactive pour éviter une accumulation de leur concentration, avec un temps de vie fixé à 15 min par défaut mais qui peut être modifié en nameliste. 

.. [#namelist] NFINDTOP=1 détermination de la hauteur de couche limite comme la zone de maximum de gradient de température potentielle 
   NFINDTOP=2 détermination de la hauteur de couche limite en utilisant le niveau où la température potentielle virtuelle dépasse celle moyenne des niveaux sous-jacents plus un seuil

Dans quel cas cette option est-elle recommandée?
  Cette option est recommandée dans les simulations LES en conditions idéalisées lorsqu’on veut documenter les structures cohérentes de la couche limite. De nombreux diagnostiques sont déjà codés qui permettent de faire une analyse conditionnelle de ces structures et sortir un ensemble de champs (moyenne, fraction couverte, moment d’ordre 2) en diagnostiquant les structures ayant une anomalie positive de concentration de traceurs et une anomalie positive de vitesse verticale et potentiellement un contenu en eau liquide non nul dans la couche nuageuse.

Quelles recommandations ferais-tu aux utilisateurs.trices ?
  Il est important de vérifier que les valeurs par défaut conviennent à l’utilisateur notamment  l’altitude d’émission sous la base et au-dessus du sommet des nuages pour les traceurs 2 et 3, le taux de décroissance et le seuil contrôlant l’échantillonnage conditionnel. Pour plus de détails, n’hesitez pas à me contacter ou à vous reporter au papier Couvreux et al 2010.

Quelles sont les limites ? Dans quel cas cette option est-elle plutôt à éviter ? 
  Attention à la mise en place des diagnostics en cas d’hétérogénéités de surface (ou de relief), l’émission des traceurs fonctionne tel quel et peut déjà être utilisé pour identifier les structures mais les calculs de diagnostics statistiques de l’analyse conditionnelle sont à adapter. Il est sans doute plus adapté dans ce cas de faire une analyse des champs 3D à partir des fichiers *OUT* plutôt que de modifier l’analyse conditionnelle. Pour cela, il faut tout d’abord bien s’assurer que les concentrations des traceurs sont sorties dans les fichiers OUT (cf. la procédure pour rajouter des variables dans les sorties fréquétentes, à appliquer à SVT). A posteriori, il est important de s'assurer d'avoir des statistiques spatiales ou temporelles qui convergent bien. Vous pouvez contacter Nathan Philippot ou Hugo Jacquet qui utilisent les traceurs  en présence d’hétérogénéités de surface respectivement de relief ou de température de surface de la mer.



Références
  - Couvreux, F., F. Hourdin and C. Rio, 2010: Resolved versus parametrized boundary-layer plumes. Part I: a parametrization-oriented conditional sampling in Large-Eddy simulations. Boundary Layer Meteorology. 134, Iss 3, 441-458 DOI 10.1007/s10546-009-9456-5
  - Brient F., Couvreux F, Villefranque N, Rio C, Honnert R, 2019: Object-oriented identification of coherent structures in large-eddy simulations: importance of downdrafts in stratocumulus Geophysical Research Letters, 46, 1-11, https://doi.org/10.1029/2018GL081499
  - Brient F, Couvreux F, Rio C, Honnert R, 2024: Coherent subsiding structures in large eddy simulations of atmospheric boundary layers,  QJRMS, https://doi.org/10.1002/qj.4625

.. note::

   Si vous aussi vous souhaitez expliquer un développement que vous avez mis en place dans Méso-NH, ou une méthode d’analyse que vous partagez à la communauté, n’hésitez pas à me le signaler par `mail <mailto:thibaut.dauhut@aero.obs-mip.fr>`_.

Les nouvelles de l’équipe support
************************************

.. warning::

   A changer entièrement

Version 5.7.0
  - La version 5.7 ... 
  - A noter également : ...

Version 5.7.1 (en développement)
  - ...
 
Développement en cours
  - ...
  - Version 6.0 : ...
  - SURFEX :  ...
  - ECRAD ...
  - Outils ...

Développement en cours de réflexion
  - ...

Autres nouvelles
  - ...


Dernières publications utilisant Méso-NH
****************************************************************************************

.. warning::

   A changer entièrement, inclure poster de Hugo

Air-sea interactions
  - The wave-age-dependent stress parameterisation (WASP) for momentum and heat turbulent fluxes at sea in SURFEX v8.1 [`Bouin et al., 2024 <https://doi.org/10.5194/gmd-17-117-2024>`_]
  - A numerical study of ocean surface layer response to atmospheric shallow convection: impact of cloud shading, rain and cold pool [`Brilouet et al., 2024 <https://doi.org/10.1002/qj.4651>`_]

Boundary layer processes
  - Coherent subsiding structures in large eddy simulations of atmospheric boundary layers Brient [`Brient et al., 2024 <https://doi.org/10.1002/qj.4625>`_]
  - Breakdown of the velocity and turbulence in the wake of a wind turbine – Part 1: Large-eddy-simulation study [`Jézéquel et al., 2024a <https://doi.org/10.5194/wes-9-97-2024>`_]
  - Breakdown of the velocity and turbulence in the wake of a wind turbine – Part 2: Analytical modeling [`Jézéquel et al., 2024b <https://doi.org/10.5194/wes-9-119-2024>`_]
  - Impact of surface turbulent fluxes on the formation of convective rolls in a Mediterranean windstorm [`Lfarh et al., 2024 <https://doi.org/10.22541/essoar.169774560.07703883/v1>`_]
  - The Marinada fall wind in the eastern Ebro sub-basin: Physical mechanisms and role of the sea, orography and irrigation [`Lunel et al., 2024 <http://dx.doi.org/10.5194/egusphere-2024-495>`_]

Lightnings and Fire meteorology
  - Numerical investigation of the Pedrógão Grande pyrocumulonimbus using a fire to atmosphere coupled model [`Couto et al., 2024 <https://doi.org/10.1016/j.atmosres.2024.107223>`_]
  - 3D Monte-Carlo simulations of lightning optical waveforms and images observable by on-board operational instruments [`Rimboud et al., 2024 <http://dx.doi.org/10.1016/j.jqsrt.2024.108950>`_]

Aerosols and their interactions with clouds and dynamics:
  - Fractional solubility of iron in mineral dust aerosols over coastal Namibia: a link to marine biogenic emissions? [`Desboeufs et al., 2024 <https://doi.org/10.5194/acp-24-1525-2024>`_]
  - Cyclogenesis in the tropical Atlantic: First scientific highlights from the Clouds-Atmospheric Dynamics-Dust Interactions in West Africa (CADDIWA) field campaign [`Flamant et al., 2024a <https://doi.org/10.1175/BAMS-D-23-0230.1>`_]
  - The radiative impact of biomass burning aerosols on dust emissions over Namibia and the long-range transport of smoke observed during AEROCLO-sA [`Flamant et al., 2024b <https://doi.org/10.5194/egusphere-2023-2371>`_]

Extreme precipitations
  - Impact of urban land use on mean and heavy rainfall during the Indian summer monsoon [`Falga and Wang, 2024 <https://doi.org/10.5194/acp-24-631-2024>`_]

Chemistry and atmospheric composition:
  - Measurement Report: Bio-physicochemistry of tropical clouds at Maïdo (Réunion Island, Indian Ocean): overview of results from the BIO-MAÏDO campaign [`Leriche et al., 2024 <https://doi.org/10.5194/egusphere-2023-1362>`_]
  - Measurement Report: Insights into the chemical composition of molecular clusters present in the free troposphere over the Southern Indian Ocean: observations from the Maïdo observatory (2150 m a.s.l., Reunion Island) [`Salignat et al., 2024 <https://doi.org/10.5194/acp-24-3785-2024>`_]




.. note::

   Si vous souhaitez partager avec la communauté le fait qu’un de vos projets utilisant Méso-NH a été financé ou toute autre communication sur vos travaux (notamment posters et présentations disponibles en ligne), n’hésitez pas à m’écrire. A l’occasion de la mise en place de ces infolettres, je suis également preneur de vos avis sur le format proposé.

Bonnes simulations avec Méso-NH !

A bientôt,

Thibaut Dauhut et toute l’équipe Méso-NH: Philippe Wautelet, Quentin Rodier, Didier Ricard, Joris Pianezze, Juan Escobar et Jean-Pierre Chaboureau
