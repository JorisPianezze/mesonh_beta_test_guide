Infolettre #02
================================================

**3 juillet 2024.** Version française, English version `here <newsletter_01_english.html>`_.

 

Chers utilisateurs, chères utilisatrices de Méso-NH,

Voici la 2ème infolettre de notre communauté Méso-NH. Vous y trouverez un entretien avec une développeuse de Méso-NH, les dernières nouvelles de l’équipe support et la liste des dernières publications utilisant Méso-NH.

Entretien avec `Benoît Vié <mailto:benoit.vie@meteo.fr>`_ (CNRM)
*****************************************************************

.. image:: photo_bv.jpg
  :width: 300

Fleur, tu as développé la possibilité d'inclure des traceurs passifs à décroissance radioactive dans Méso-NH. Pourrais-tu résumer ce que fait cette option ?
  Cette option a initialement été développée pour identifier les structures cohérentes, à savoir les thermiques, ces panaches ascendants qui contribuent fortement au transport vertical dans les couches limites convectives, dans des simulations LES. Une fois les structures identifiées on peut quantifier leur contribution au transport vertical de chaleur, d’humidité et de quantité de mouvement.
  On peut activer sans modifier le code jusqu’à trois traceurs passifs. Le 1er est émis avec un flux constant en surface, le 2eme est émis juste en dessous de la base des nuages, il a été implémenté pour estimer les échanges entre la couche sous-nuageuse et l’intérieur des nuages, voire la couche de transition. Le 3e est émis juste au-dessus du sommet moyen des nuages et permet d’estimer les échanges au sommet des nuages. Si on est en condition de ciel clair, on peut choisir d’émettre le traceur 3 au sommet de la couche limite et choisir comment déterminer cette hauteur de couche limite*. Les trois traceurs subissent une décroissance radioactive pour éviter une accumulation de leur concentration, avec un temps de vie fixé à 15 min par défaut mais qui peut être modifié en nameliste. 

Dans quel cas cette option est-elle recommandée?
  Cette option est recommandée dans les simulations LES en conditions idéalisées lorsqu’on veut documenter les structures cohérentes de la couche limite. De nombreux diagnostiques sont déjà codés qui permettent de faire une analyse conditionnelle de ces structures et sortir un ensemble de champs (moyenne, fraction couverte, moment d’ordre 2) en diagnostiquant les structures ayant une anomalie positive de concentration de traceurs et une anomalie positive de vitesse verticale et potentiellement un contenu en eau liquide non nul dans la couche nuageuse.

Quelles recommandations ferais-tu aux utilisateurs.trices ?
  Il est important de vérifier que les valeurs par défaut conviennent à l’utilisateur notamment  l’altitude d’émission sous la base et au-dessus du sommet des nuages pour les traceurs 2 et 3, le taux de décroissance et le seuil contrôlant l’échantillonnage conditionnel. Pour plus de détails, n’hesitez pas à me contacter ou à vous reporter au papier Couvreux et al 2010.

Quelles sont les limites ? Dans quel cas cette option est-elle plutôt à éviter ? 
  Attention à la mise en place des diagnostics en cas d’hétérogénéités de surface (ou de relief), l’émission des traceurs fonctionne tel quel et peut déjà être utilisé pour identifier les structures mais les calculs de diagnostics statistiques de l’analyse conditionnelle sont à adapter. Il est sans doute plus adapté dans ce cas de faire une analyse des champs 3D à partir des fichiers *OUT* plutôt que de modifier l’analyse conditionnelle. Pour cela, il faut tout d’abord bien s’assurer que les concentrations des traceurs sont sorties dans les fichiers OUT (cf. la procédure pour rajouter des variables dans les sorties fréquétentes, à appliquer à SVT). A posteriori, il est important de s'assurer d'avoir des statistiques spatiales ou temporelles qui convergent bien. Vous pouvez contacter Nathan Philippot ou Hugo Jacquet qui utilisent les traceurs  en présence d’hétérogénéités de surface respectivement de relief ou de température de surface de la mer.

*
  NFINDTOP=1 détermination de la hauteur de couche limite comme la zone de maximum de gradient de température potentielle si NFINDTOP=2 détermination de la hauteur de couche limite en utilisant le niveau où la température potentielle virtuelle dépasse celle moyenne des niveaux sousjacents plus un seuil

Références
  Couvreux, F., F. Hourdin and C. Rio, 2010: Resolved versus parametrized boundary-layer plumes. Part I: a parametrization-oriented conditional sampling in Large-Eddy simulations. Boundary Layer Meteorology. 134, Iss 3, 441-458 DOI 10.1007/s10546-009-9456-5

Brient F., Couvreux F, Villefranque N, Rio C, Honnert R, 2019: Object-oriented identification of coherent structures in large-eddy simulations: importance of downdrafts in stratocumulus Geophysical Research Letters, 46, 1-11, https://doi.org/10.1029/2018GL081499

Brient F, Couvreux F, Rio C, Honnert R, 2024: Coherent subsiding structures in large eddy simulations of atmospheric boundary layers,  QJRMS, https://doi.org/10.1002/qj.4625

.. note::

   Si vous aussi vous souhaitez expliquer un développement que vous avez mis en place dans Méso-NH, ou une méthode d’analyse que vous partagez à la communauté, n’hésitez pas à me le signaler par `mail <mailto:thibaut.dauhut@aero.obs-mip.fr>`_.

Les nouvelles de l’équipe support
***********************************

Version 5.7.0
  - La version 5.7 a été développée, évaluée et validée de septembre à décembre 2023. Plus d'infos `ici <http://mesonh.aero.obs-mip.fr/mesonh57/BooksAndGuides?action=AttachFile&do=view&target=update_from_masdev56_to_570.pdf>`_. 
  - A noter également : pour l’étape DIAG, le bogue LGXT dans compute_r00 a été corrigé, des variables supplémentaires (vent, nuages, aérosols, …) du temps courant ont été ajoutées, les valeurs négatives ont été changées par XFILLVALUE.

Version 5.7.1 (en développement)
  - Tous les cas tests ont été ajoutés dans un commit de la branche MNH-57-branch.
  - Les noms de fichiers seront plus flexibles (CEXP et CSEG pouvant aller jusqu'à 32 caractères, modifiable au besoin).
  - Le nombre de fichiers de couplage ne sera plus limité (était de 24, maintenant à 1000 et extensible si nécessaire).
  - La gestion de tous les fichiers a été réorganisée en interne. Par exemple, on ne stockera plus dès le début la totalité de la liste des fichiers de reprise (*backups*) et de sorties fréquentes (*outputs*). Le gain en espace mémoire n'est pas du tout négligeable lorsque le nombre de backups et d'outputs est important surtout si les I/O parallèles sont activées. Pour cela, il faut spécifier les instants d'écriture avec les options en fréquence dans les namelists (ie utiliser XBAK_TIME_FREQ et non XBAK_TIME).
  - La compression (sans pertes) sera possible pour tous les fichiers écrits (au format netCDF).
  - Pour les trajectoires lagrangiennes (programme DIAG), les champs seront maintenant stockés dans des variables 4D (x, y, z, t) et non plus dans des variables différentes pour chaque instant (fichier plus lisible et moins de *post-processing* à réaliser).
  - Les fichiers de reprise (*backups*) pourront être écrits avec diminution de la précision des nombres en virgule flottante (attention : option dangereuse).
  - Même fonctionnalité pour les fichiers écrits par DIAG.
  - Pour l’étape DIAG : il sera possible d'écrire directement XT_traj, RV_traj (PW).

Développement en cours
  - Chimie/aérosols : un projet a commencé à restructurer la chimie et les aérosols dans les modèles de Météo-France (ARPEGE, MOCAGE, AROME, MESO-NH) pour externaliser la chimie et les aérosols. Le travail est en cours, les routines impactées seront nombreuses notamment à l'intérieur de ch_monitorn.f90, les ch_* et tous les *aer*.
  - Version 6.0 : le développement de la prochaine version majeure a commencé par la montée de version de la branche GPU (MNH-55X-dev-OPENACC-FFT) phasée sur la 5.6 dans un premier temps sans PHYEX. Cette nouvelle branche MNH-56X-dev-OPENACC-FFT-unlessPHYEX tourne sur GPU sur quelques tests. Des tests de performance sur les architectures avec GPU (AMD et Nvidia) ont été réalisés, mais cette branche n’a pas encore été validée sur CPU. Les directives OpenACC sont en cours de portage (manuel) dans PHYEX.
  - SURFEX :  les modifications des fichiers dans SURFEX sont remontées au dépôt de SURFEX-offline officiel pour la prochaine version 9.2.
  - ECRAD va prochainement faire peau neuve : suppression de la version (non open-source) 1.0.1, branchement d'une version plus récente.
  - Outils : ajouts de fonctionnalités dans la librairie `Python Fortran Tool <https://github.com/UMR-CNRM/pyft>`_ pour gérer automatiquement certaine transformation du code source de Méso-NH pour produire du code qui tourne sur GPU.
  - Une nouvelle mise en page du site et de la documentation est en cours de test sur des parties spécifiques.
  - Une note pour l'utilisation de l'outil d'extraction développé par Jean Wurtz est en cours de préparation.
  - Une comparaison de Méso-NH avec d'autres modèles concurrents en termes de performance est en cours.

Développement en cours de réflexion
  - Dans les sorties fréquentes (*outputs*) la possibilité d'écrire des champs sur des sous-domaines plutôt que sur toute la grille est actuellement à l'étude.

Autres nouvelles
  - Le stage Méso-NH s'est bien déroulé avec 11 stagiaires de différents établissements (ONERA, Université de Lille, Université de Corse, LAERO, SUPAERO et CNRM) du 4 au 7 mars 2024. Le prochain stage aura lieu du 12 au 15 novembre 2024.
  - Paul Boumendil, doctorant CNRM/IFPEN propose un tutoriel pour utiliser des bases de données à résolution métrique pour la description des couverts de surface avec Méso-NH/SURFEX. Pour obtenir une résolution précise du type de surface en utilisant ECOCLIMAP, il a utilisé Geoclimate pour récupérer les données de type de surface d'OpenStreetMap, puis il a associé à chaque type de sol une COVER d'ECOCLIMAP. La carte est ensuite rasterisée et enregistrée au format "Lat Lon Cover" pour être utilisée en entrée lors de l'étape de PREP de Méso-NH. Un tutoriel ainsi qu'un exemple de cette utilisation d'ECOCLIMAP seront bientôt disponibles sur le site de Méso-NH. En attendant il est disponible `ici <https://github.com/QuentinRodier/tuto-MNH-HighResCover/blob/main/Tutorial.ipynb>`_.


Dernières publications utilisant Méso-NH
****************************************************************************************

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
