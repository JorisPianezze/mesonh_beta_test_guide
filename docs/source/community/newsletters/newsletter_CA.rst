Infolettre #CA
================================================

**X xxxxx 2025.** Version française, English version `here <newsletter_03_english.html>`_.


Chers utilisateurs, chères utilisatrices de Méso-NH,

Voici ci-dessous la Xème infolettre de notre communauté. Vous y trouverez un entretien avec la développeuse d'un outil utile aux utilisateurs.trices de Méso-NH, les dernières nouvelles de l’équipe support et la liste des dernières publications utilisant Méso-NH.

Entretien avec `Clotilde Augros <mailto:clotilde.augros@meteo.fr>`_ (CNRM)
************************************************************************************

Clotilde, tu as développé un simulateur radar qui peut tourner à partir des sorties de Méso-NH. Pourrais-tu résumer ce que fait ce module ?
  Ce code, appelé **operadar** (Augros et al., 2016, David et al. 2025) prend les variables du modèle en entrée (contenus, concentrations en hydrométéores, température, altitude, pression) et calcule en chaque point de grille du modèle les variables radar (réflectivité Zh, réflectivité différentielle Zdr, phase différentielle spécifique Kdp, coefficient de corrélation ρhv) à partir de la lecture de tables de coefficients de rétrodiffusion calculées en bande S, C, X (en cours de préparation : Ka, W).

  La méthode de diffusion utilisée est la méthode de la matrice T (Waterman, 1965) qui représente les hydrométéores comme des sphéroïdes aplatis. 

  Cet outil implémenté en python est indépendant du code de MesoNH. Il a été développé en “offline” de sorte à pouvoir être utilisé à la fois avec Méso-NH ou AROME. Ainsi, des améliorations réalisées à l’occasion de travaux s’appliquant à AROME peuvent ensuite être utilisée pour MésoNH et vice versa. 

Pourquoi vaut-il mieux utiliser ce module que l'autre simulateur radar inclus dans les diagnostics de Méso-NH ?
  ll existe aussi deux versions “online” du simulateur radar dans Meso-NH, implémentées dans la partie DIAG.

  - la première version de simulateur radar de MésoNH (NVERSION_RAD=1, Richard et al, 2003) permet de calculer les variables radar dans la géométrie du modèle (grille 3D), en appliquant l’approximation de Rayleigh pour le calcul de la diffusion, qui reste valide tant que la taille des hydrométéores est très petite devant la taille de la longueur d’onde λ. Pour des radars en bande S (λ~10 cm), cette hypothèse est valide pour tous les hydrométéores sauf la grêle. Pour des radars en bande C (λ~5 cm), on sort du cadre de cette hypothèse si on simule des pluies intenses avec de grosses gouttes d’eau (~8 mm).

  - une deuxième version (NVERSION_RAD=2, Caumont et al, 2006, Augros et al 2016) a été implémentée dans MésoNH en fortran pour inclure différentes méthodes de diffusion, dont la diffusion de la matrice T (Waterman, 1965) qui permet de simuler la diffusion pour des hydrométéores aplatis y compris lorsqu’on sort du régime de Rayleigh (soit pour la pluie intense dès la bande C, ou pour la grêle, ou pour des bandes de fréquence plus faibles: K, Ka, Ku, W). Mais : cette deuxième version n’a pas été maintenue depuis 2018. 

  Les besoins de cet opérateur d’observation radar pour l’évaluation de simulations AROME également, ont conduit à privilégier le développement d’une version offline pour la recherche compatible à la fois avec AROME et MésoNH, et donc plus facile à maintenir et à faire évoluer de manière collaborative (operadar: https://github.com/UMR-CNRM/operadar)
  Le module offline operadar permet de calculer dans la géométrie du modèle les variables radar à la fois avec la méthode de diffusion T-matrice, mais aussi avec l’approximation de Rayleigh.   Des options bien plus avancées que dans les versions online de MesoNH sont disponibles:

  - prise en compte de l’oscillation des hydrométéores (important pour simuler les variables polarimétriques dans la grêle) 

  - différents choix de formulation des constantes diélectriques

  - version plus avancée de la représentation de la fonte et de la phase mixte (via l'espère graupel qu'on "convertit" en graupel fondant lorsqu'elle co-existe avec de l'eau de pluie, y compris à des températures négatives). Ce module a permis de simuler avec succès les colonnes de Zdr (qui traduisent la présence de grosses gouttes d’eau liquide à température négative au sein des courants ascendants des orages, Kumjian et al, 2014) avec AROME et le schéma LIMA (David et al., 2025)

  - le code utilise explicitement la concentration lorsque celle-ci est pronostique (2-moments), pour calculer les variables radars intégrées sur la distribution de taille
Les comparaisons entre simulations et observations montrent une très bonne représentation des variables Zh, Zdr et Kdp dans la pluie avec le schéma microphysique LIMA (David et al. 2025) sur plus de 30 cas d’orage simulés avec AROME.




Références
  - Comparisons between S, C, and X band polarimetric radar observations and convective-scale simulations of HyMeX first special observing period [`Augros et al., 2016 <https://doi.org/10.1002/qj.2572>`_]
  - Improved Simulation of Thunderstorm Characteristics and Polarimetric Signatures with LIMA 2-Moment Microphysics in AROME [`David et al., 2025 <https://doi.org/10.5194/egusphere-2025-685>`_]
  - The Anatomy and Physics of ZDR Columns: Investigating a Polarimetric Radar Signature with a Spectral Bin Microphysical Model [`Kumjian et al., 2014 <https://doi.org/10.1175/jamc-d-13-0354.1>`_]
  - High-resolution numerical simulations of the convective system observed in the Lago Maggiore area on 17 September 1999 (MAP IOP 2a) [`Richard et al., 2003 <https://doi.org/10.1256/qj.02.50>`_]
  - Matrix formulation of electromagnetic scattering [`Waterman, 1965 <https://doi.org/10.1109/PROC.1965.4058>`_]

.. note::

  Si vous aussi vous souhaitez expliquer un développement que vous avez mis en place dans Méso-NH, ou une méthode d’analyse que vous partagez à la communauté, n’hésitez pas à me le signaler par `mail <mailto:thibaut.dauhut@univ-tlse3.fr>`_.

    
    
Les nouvelles de l’équipe support
************************************



Version 6


Développements en cours et récents


Dépôt Méso-NH sur forge logicielle 


Stage Méso-NH


.. note::
  Si vous avez des besoins, idées, améliorations à apporter, bugs à corriger ou suggestions concernant les entrées/sorties, `Philippe Wautelet <mailto:philippe.wautelet@cnrs.fr>`_ est preneur.


Dernières publications utilisant Méso-NH
****************************************************************************************



.. note::

   Si vous souhaitez partager avec la communauté le fait qu’un de vos projets utilisant Méso-NH a été financé ou toute autre communication sur vos travaux (notamment posters et présentations *disponibles en ligne*), n’hésitez pas à m’écrire. A l’occasion de la mise en place de ces infolettres, je suis également preneur de vos avis sur le format proposé.

Bonnes simulations avec Méso-NH !

A bientôt,

Thibaut Dauhut et toute l’équipe Méso-NH : Philippe Wautelet, Quentin Rodier, Didier Ricard, Joris Pianezze, Juan Escobar et Jean-Pierre Chaboureau
