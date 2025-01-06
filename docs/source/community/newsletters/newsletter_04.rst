Infolettre #04
================================================

**10 janvier 2025.** Version française, English version `here <newsletter_03_english.html>`_.


Chers utilisateurs, chères utilisatrices de Méso-NH,

Nous vous souhaitons tout d'abord une très bonne année 2025 ! Riche en découvertes grâce à vos simulations Méso-NH :)

Voici ci-dessous la 4ème infolettre de notre communauté. Vous y trouverez un entretien avec un développeur de Méso-NH, les dernières nouvelles de l’équipe support et la liste des dernières publications utilisant Méso-NH.

Entretien avec `Robert Schoetter <mailto:robert.schoetter@meteo.fr>`_ (CNRM)
************************************************************************************

.. image:: photo_robert-s.jpg
  :width: 200

Robert, tu as développé le couplage à plusieurs niveaux entre Méso-NH et SURFEX-TEB, le module de SURFEX qui représente les interactions entre les villes et l'atmosphère. Pourrais-tu résumer ce qui a motivé ce développement ?
  Le couplage à plusieurs niveaux a été développé pour représenter le fait que les bâtiments sont immergés dans l'atmosphère. Ceci contraste avec le couplage classique entre Méso-NH et TEB pour lequel les toits des bâtiments sont au niveau du sol de Méso-NH. Avec le couplage classique, la rue-canyon de TEB se situe en-dessous du sol, donc un volume d'air artificiel est introduit et il n'y a pas d'advection de ce volume d'air entre différents points de grille. Ceci est particulièrement problématique pour des villes hétérogènes avec des bâtiments de grande hauteur car les échanges horizontaux ne peuvent se faire que via l'air au-dessus des bâtiments.

Comment fonctionne le couplage à plusieurs niveaux ?
  Avec le couplage à plusieurs niveaux, les variables météorologiques issues de tous les niveaux de Méso-NH qui intersectent les bâtiments sont transmis à SURFEX-TEB. Dans TEB ils sont utilisés comme forçage météorologique du toit, des murs et du sol. Dans Méso-NH, l'effet des bâtiments sur l'écoulement est considéré avec une approche de coefficient de traînée sur tous les niveaux qui intersectent les bâtiments. Les flux de chaleur sensible et latent depuis le sol, les murs et le toit vers l'atmosphère sont convertis en tendances de température potentielle et de rapport de mélange de vapeur d'eau sur tous les niveaux verticaux qui intersectent ces facettes urbaines.

Pourquoi conseilles-tu d'utiliser ce développement ? 
  Le couplage à plusieurs niveaux a initialement été développé pour les villes avec des bâtiments de grande hauteur. Mais il peut être utile pour n'importe quelle ville car il permet d'augmenter la résolution verticale de Méso-NH et notamment de simuler de manière prognostique les variables à 2 m tout en prenant en compte le bâti urbain. Il suffit pour cela de choisir une résolution verticale de 4 m proche de la surface.

Quelles sont les éventuelles limites ? Dans quel cas ce couplage est-il plutôt à éviter ?
  Des limites de cette approche ont été mises en évidence pour les villes entourées de forêts car certaines paramétrisations dans le modèle de végétation ISBA ne donnent pas de bons résultats avec une résolution verticale aussi fine. Il existe aussi des limites théoriques de l'approche de coefficient de traînée pour des villes très denses (par exemple plus de 50% de la surface des mailles occupé par des bâtiments) qui pourraient entraîner des biais. On néglige aussi le fait qu'une partie du volume des mailles de Méso-NH ne soit pas de l'air mais des bâtiments ce qui pourrait également induire des imprécisions pour des villes denses.

.. note::

   Si vous aussi vous souhaitez expliquer un développement que vous avez mis en place dans Méso-NH, ou une méthode d’analyse que vous partagez à la communauté, n’hésitez pas à me le signaler par `mail <mailto:thibaut.dauhut@univ-tlse3.fr>`_.

    
    
Les nouvelles de l’équipe support
************************************

Version 5.7.1 (sortie le 4 septembre)
  - Liste des bugfixs
  - Notez que tous les cas tests 

Version 5.8
  Un appel à contribution sera lancée en décembre. 

Développements en cours et récents
  - Chimie/aérosols
  - Version 6.0
  - Outils
  - Forge logicielle
  - Site vitrine
  - Couplage

Ménage des fichiers en sortie
  - les fichiers .des inutiles (car vides) ne seront plus écrits.
  - les fichiers de statistiques détaillées des performances du solveur de pression ne sont plus écrits.
  - le fichier file_for_xtransfer a également disparu (ainsi que quelques morceaux de code devenus inutiles).
  - le fichier OUTPUT_LISTING0 est conservé sauf s'il est vide 
Stage Méso-NH
  - Le prochain stage aura lieu du 12 au 15 novembre 2024. Planning `ici <http://mesonh.aero.obs-mip.fr/mesonh57/MesonhTutorial>`_
  - Date limite d'inscription : 1er novembre
  - Inscription par mail à `Quentin Rodier <mailto:quentin.rodier@meteo.fr>`_

.. note::
  Si vous avez des besoins, idées, améliorations à apporter, bugs à corriger ou suggestions concernant les entrées/sorties, `Philippe Wautelet <mailto:philippe.wautelet@cnrs.fr>`_ est preneur.


Dernières publications utilisant Méso-NH
****************************************************************************************

Marine atmospheric boundary layer
  - Adjustment of the marine atmospheric boundary-layer to the North Brazil Current during the EUREC4A-OA experiment [`Giordani et al., 2024 <https://doi.org/10.1016/j.dynatmoce.2024.101500>`_]

Drone measurements of cumulus
  - Experimental UAV flights to collect data within cumulus clouds [`Hattenberger et al., 2024 <https://doi.org/10.1109/TFR.2024.3478216>`_]

PhD theses
  - Amélioration de la prise en compte du givrage par la modélisation et la prévision météorologique pour l'exploitation des parcs éoliens [`Dupont, Université de Toulouse, 2024 <https://theses.fr/s305624>`_]
  - Etude de l'évolution de la couche limite atmosphérique et des nuages de pente sur l'île de la Réunion [`El Gdachi, Université de La Réunion, 2024 <https://theses.fr/s311244>`_]
  - Interactions entre irrigation, couche limite atmosphérique et vents de méso-échelle en région semi-aride : observations et modélisation [`Lunel, Université de Toulouse, 2024 <https://theses.fr/s304370>`_]

.. note::

   Si vous souhaitez partager avec la communauté le fait qu’un de vos projets utilisant Méso-NH a été financé ou toute autre communication sur vos travaux (notamment posters et présentations *disponibles en ligne*), n’hésitez pas à m’écrire. A l’occasion de la mise en place de ces infolettres, je suis également preneur de vos avis sur le format proposé.

Bonnes simulations avec Méso-NH !

A bientôt,

Thibaut Dauhut et toute l’équipe Méso-NH : Philippe Wautelet, Quentin Rodier, Didier Ricard, Joris Pianezze, Juan Escobar et Jean-Pierre Chaboureau
