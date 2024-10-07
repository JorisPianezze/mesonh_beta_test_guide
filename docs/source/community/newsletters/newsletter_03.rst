Infolettre #03
================================================

**8 octobre 2024.** Version française, English version `here <newsletter_03_english.html>`_.


Chers utilisateurs, chères utilisatrices de Méso-NH,

Voici la 3ème infolettre de notre communauté Méso-NH. Vous y trouverez un entretien avec un membre de l'équipe support de Méso-NH, les dernières nouvelles de l’équipe support et la liste des dernières publications utilisant Méso-NH.

Entretien avec `Juan Escobar <mailto:juan.escobar-munoz@cnrs.fr>`_ (CNRM)
**************************************************************************

.. image:: photo_je.jpg
  :width: 450

Juan, tu as porté Méso-NH 5-5-1 sur GPU avec Philippe. Pourrais-tu décrire de quoi il s'agit et les perspectives d'utilisation que cela ouvre ?
  Les GPU (Graphics Processing Unit) sont devenus les successeurs des supercalculateurs parallèles et vectoriels des années 2000 (comme les CRAY ou NEC). Ils possèdent des dizaines de processeurs pouvant exécuter des milliers d'instructions en parallèle, avec une bande passante mémoire bien supérieure aux CPU, tout en étant bien plus économiques et moins énergivores.

  Dès les années 2010, j’ai commencé à porter Méso-NH sur GPU grâce aux compilateurs Fortran de PGI, en utilisant la programmation par directives (ACC), qui a évolué vers le standard OpenACC. Aujourd'hui, environ 90 % des parties les plus coûteuses en calcul (advection, turbulence, microphysique à un moment et solveur de pression) sont portées sur GPU, ce qui permet d’utiliser Méso-NH pour des simulations scientifiques. Cette version a été testée lors du Grand Défi Adastra GPU avec succès, simulant des événements extrêmes sur environ 1/3 de la partition GPU d’Adastra (128 nœuds de calcul dotés au total de 1024 GPU).

Quel intérêt y a-t-il à réaliser des simulations sur les calculateurs dotés de GPU plutôt que sur ceux basés sur des CPU uniquement ?
  L'intérêt principal des GPU est leur puissance de calcul supérieure. Par exemple, sur Adastra, 338 nœuds GPU fournissent 61 Pétaflops, contre seulement 13 Pétaflops[#flops]_ pour 556 nœuds CPU. De plus, les GPU sont bien plus efficaces énergétiquement : lors du Grand Challenge Adastra, le code tournait 5 fois plus vite sur GPU tout en consommant 2 fois moins d’énergie. Cet écart va s’accentuer. Par exemple, le futur supercalculateur européen à Jülich atteindra 1 Exaflops[#flops]_ avec sa partition GPU, tandis que la partition CPU ne fournira que 50 Pétaflops, soit 0,5 % de la puissance totale.

.. [#flops] Pétaflops = millions de milliards d'opérations de calcul par seconde. 1 Exaflop = 1000 Pétaflops.

Y a-t-il des situations qui se prêtent particulièrement bien à l'utilisation de Méso-NH 5-5-1 sur GPU ?
  Les GPU sont adaptés aux simulations massivement parallèles, comme les Giga-LES, où les grilles de calcul contiennent des milliards de points. Par exemple, lors du Grand Challenge Adastra GPU, nous avons utilisé des grilles de 2,14 milliards de points (4096x4096x128) pour des simulations à 100 mètres de résolution.

  Les GPU permettent aussi de réaliser un grand nombre de simulations simultanées sur des configurations plus petites. Par exemple, sur Adastra, nous avons simulé 350 jours de météo en Corse avec une grille de 256x256x70 points à 1 km de résolution, en utilisant 1 nœud GPU par simulation. Grâce à cette approche, l’ensemble des simulations a été réalisé en seulement 3 jours.

Quelles recommandations ferais-tu aux utilisateur.trices qui souhaiteraient simuler sur GPU ?
  Il faut se rapprocher de nous, Support Méso-NH, pour mettre le pied à l'étrier sur GPU. Au niveau utilisation du code il n'y a pas de différence fondamentale pour quelqu'un qui a déjà fait tourner Méso-NH sur Supercalculateur à base de CPU, à Météo-France ou au GENCI. La version GPU actuelle est basé sur MNH-551, donc il faut utiliser cette version d'abord sur CPU pour 'calibrer' ses simulations, et ensuite passer sur GPU.

  Il faut bien sûr de préférence utiliser les paramétrisations déjà portées sur GPUs, pour avoir un gain de performance. Toutefois, cela n'est pas obligatoire dans un premier temps, car le code peut être compilé pour être bit-reproductible tout en tournant en partie sur CPU et en partie sur GPU.

Quelles sont les limites pour l'instant de ce portage de Méso-NH ? les perspectives ?
  Actuellement, seule une partie du code a été portée sur GPU, et dans la version MNH-5-5-1, donc il faut faire des simulations avec cette version MNH-55X du code.

  Avec l'introduction de PHYEX, dans les versions MNH-5-6-X et MNH-5-7-X, une partie du travail de portage sur GPU réalisé a été perdu (notamment la turbulence, ICE3 et la condensation sous maille). Toutefois, Quentin Rodier et Sebastien Riette au CNRM, ont en charge le portage de PHYEX sur GPU en utilisant la méthodologie choisie par Météo-France, soit la technique des DSL (Domain Specific Language). Pour ce faire, ils ont développé un pré-compilateur en python, `pyft_tool <https://github.com/UMR-CNRM/pyft>`_, permettant des transformations semi-automatiques du code pour le porter sur GPUs. La librairie transforme le code à la volée avant la compilation sur GPU, ce qui permet d'avoir un code source un peu plus allégé.

  Phillippe Wautelet et moi-même collaborons avec eux, en apportant notre expertise GPU et OpenACC pour rajouter les fonctionnalités nécessaires à cet outil pyft pour transformer le code de PHYEX dans MNH-56X et l'adapter aux GPUs. Parmi ces fonctionnalités, on retrouve les 'outils faits main' pour le portage de Méso-NH sur GPU, comme le rajout automatique d'appel à des fonctions mathématiques bit-reproductibles, le rajout automatique des appels aux routines MPPDB_CHECK permettant la vérification "au fil de l'eau" de l'identité des calculs sur GPU et CPU, la gestion optimisée de la mémoire pour les tableaux, l'expansion de l'array syntax en boucle imbriquée, etc.

  La version MNH-5-6 + PHYEX sur GPU est en bonne voie, et devrait être intégrée 'rapidement' (avant la fin d'année ;-) ) dans la toute dernière version MNH-57X. Il sera ensuite question de porter d'autres parties du code comme par exemple la convection peu profonde et LIMA.

.. note::

   Si vous aussi vous souhaitez expliquer un développement que vous avez mis en place dans Méso-NH, ou une méthode d’analyse que vous partagez à la communauté, n’hésitez pas à me le signaler par `mail <mailto:thibaut.dauhut@univ-tlse3.fr>`_.

    
    
Les nouvelles de l’équipe support
************************************






    
Version 5.7.1 (en cycle de validation)
  - Les bugfixs des contributeurs sont en cours de test. Sortie au plus tard fin septembre 2024.
  - En cours d'intégration : seules les données sur le domaine physique seront écrites par défaut. Les mailles non-physiques sur les bords sont automatiquement retirées. Il en est de même pour les couches d'absorptions supérieure et éventuellement inférieure. En cas de besoin, toutes ces mailles peuvent néanmoins être sauvegardées.
  - En cours d'intégration : la possibilité de faire des écritures par boîtes (sous-domaines) dans les sorties fréquentes. Chaque boîte pourra contenir sa liste propre de champs à écrire en plus d'une liste commune.

Version 5.8
  Un appel à contribution sera lancée en novembre. Toutes les contributions prêtes pour décembre 2024, c'est-à-dire testées et livrées avec un (nouveau) cas test, seront prises pour intégration.
 
Développement en cours
  - Chimie/aérosols : le projet ACCALMIE a commencé à restructurer la chimie et les aérosols dans les modèles de Météo-France (ARPEGE, MOCAGE, AROME, MESO-NH) pour externaliser la chimie et les aérosols. La bibliothèque s'appellera ACLIB (Aerosols and Chemistry LIBrary). Le travail est en cours, les routines impactées seront nombreuses notamment à l’intérieur de ch_monitorn.f90, les ch_* et tous les *aer*.
  - ECRAD v 1.6.1 (actuellement opérationnel dans AROME et ARPEGE/IFS) sera branchée à MésoNH. ECRAD deviendra le schéma de rayonnement par défaut dans la 5.8 après validation.
  - Version 6.0 : le développement de la prochaine version majeure a commencé par la montée de version de la branche GPU (MNH-55X-dev-OPENACC-FFT) phasée sur la 5.6 dans un premier temps sans PHYEX. Cette nouvelle branche MNH-56X-dev-OPENACC-FFT-unlessPHYEX tourne sur GPU sur quelques tests. Des tests de performance sur les architectures avec GPU (AMD et Nvidia) ont été réalisés, mais cette branche n’a pas encore été validée sur CPU. Les directives OpenACC sont en cours de portage (manuel) dans PHYEX.
  - Outils : ajouts de fonctionnalités dans la librairie Python Fortran Tool pour gérer automatiquement certaines transformations du code source de Méso-NH pour produire du code qui tourne sur GPU.
  - Entrées/Sorties : plusieurs stratégies pour réduire encore la quantité de données dans les sorties fréquentes (*outputs*) sans impacter négativement leur qualité sont en cours de réflexion. Par exemple, l'utilisation de seuils pour filtrer certains champs, de retirer une constante (i.e. pour des pressions ou des températures), de pouvoir sélectionner les paramètres de compression champ par champ... Tout cela nécessitera des changements internes assez importants.

.. note::
  Si vous avez des besoins, idées, améliorations à apporter, bugs à corriger ou suggestions concernant les entrées/sorties, `Philippe Wautelet <mailto:philippe.wautelet@cnrs.fr>`_ est preneur. Sinon, vous serez limités par son imagination et ses priorités du moment ;)

Stage Méso-NH
  - Le prochain stage aura lieu du 12 au 15 novembre 2024. Planning `ici <http://mesonh.aero.obs-mip.fr/mesonh57/MesonhTutorial>`_
  - Date limite d'inscription : 1er novembre
  - Inscription par mail à `Quentin Rodier <mailto:quentin.rodier@meteo.fr>`_

Autres nouvelles
  - PHYEX: la physique externalisée se dote à présent d'un pilote logiciel hors-ligne (*driver offline*) en python. Il permet de lancer les paramétrisations ICE3, TURB, EKDF et ICE_ADJUST individuellement en 1D ou 3D.
  - La demande récurrente de labellisation par l'INSU de notre code communautaire a été déposée en mai 2024, parmi les nouveautés : une estimation de l’empreinte environnementale du service "code communautaire Méso-NH" (pas de la communauté utilisatrice) à 8 tonnes équivalent CO2 par an, et l’obligation du service à intégrer une infrastructure de recherche. Une demande a été faite auprès de CLIMERI-France.

Nouvelles de SURFEX
  - SURFEX : la réunion annuelle du comité de pilotage a eu lieu le 27 mai 2024. Les présentations sont disponibles `ici <https://www.umr-cnrm.fr/surfex/spip.php?article55>`_.
  - Le `futur d'Ecoclimap <https://www.umr-cnrm.fr/surfex/IMG/pdf/surfex_steeringcommittee-27052024-physio.pdf>`_
  - Migration vers GitHub, utilisation de fourches (*forks*) pour les responsables d'intégration (Quentin R. pour Méso-NH).
  - Contribution à SURFEX à une date fixée par requête d'intégration (*Pull-Request*) avec mise à jour de la documentation obligatoire.


Dernières publications utilisant Méso-NH
****************************************************************************************

Boundary layer processes & Complex terrain meteorology
  - Impact of surface turbulent fluxes on the formation of roll vortices in a Mediterranean windstorm [`Lfarh et al., 2024 <https://doi.org/10.22541/essoar.169774560.07703883/v1>`_]
  - The Pyrenean Platform for Observation of the Atmosphere: Site, long-term dataset and science [`Lothon et al., 2024 <https://doi.org/10.5194/amt-2024-10>`_]
  - Irrigation strongly influences near-surface conditions and induces breeze circulation: Observational and model-based evidence [`Lunel et al., 2024 <https://doi.org/10.1002/qj.4736>`_]

Fire meteorology
  - Triggering pyro-convection in a high-resolution coupled fire–atmosphere simulation [`Couto et al., 2024 <https://doi.org/10.3390/fire7030092>`_]
  - Exploring the atmospheric conditions increasing fire danger in the Iberian Peninsula [`Purificação et al., 2024 <https://doi.org/10.1002/qj.4776>`_]

Microphysics
  - A full two-moment cloud microphysical scheme for the mesoscale non-hydrostatic model Meso-NH v5-6 [`Taufour et al., 2024 <https://doi.org/10.5194/egusphere-2024-946>`_]

Sea spray & Cyclogenesis over Mediterranean sea
  - Study of the atmospheric transport of sea-spray aerosols in a coastal zone using a high-resolution model [`Limoges et al., 2024 <https://doi.org/10.3390/atmos15060702>`_]
  -  The crucial representation of deep convection for the cyclogenesis of medicane Ianos [`Pantillon et al., 2024 <https://doi.org/10.5194/egusphere-2024-1105>`_]

Urban meteorology
  - Urban influence on convective precipitation in the Paris region: Hectometric ensemble simulations in a case study [`Forster et al., 2024 <https://doi.org/10.1002/qj.4749>`_]
  - The heat and health in cities (H2C) project to support the prevention of extreme heat in cities [`Lemonsu et al., 2024 <https://doi.org/10.1016/j.cliser.2024.100472>`_]


PhD theses
  - De l'impact des aérosols sur le cycle de vie des nuages stratiformes au sud de l'Afrique de l'Ouest [`Delbeke <https://theses.fr/s295025>`_, Université de Toulouse, 2024]
  - Impact des surfaces urbanisées sur la convection en région parisienne : observations et simulations numériques hectométriques [`Forster <https://theses.fr/s302779>`_, Université de Toulouse, 2024]



.. note::

   Si vous souhaitez partager avec la communauté le fait qu’un de vos projets utilisant Méso-NH a été financé ou toute autre communication sur vos travaux (notamment posters et présentations *disponibles en ligne*), n’hésitez pas à m’écrire. A l’occasion de la mise en place de ces infolettres, je suis également preneur de vos avis sur le format proposé.

Bonnes simulations avec Méso-NH !

A bientôt,

Thibaut Dauhut et toute l’équipe Méso-NH: Philippe Wautelet, Quentin Rodier, Didier Ricard, Joris Pianezze, Juan Escobar et Jean-Pierre Chaboureau
