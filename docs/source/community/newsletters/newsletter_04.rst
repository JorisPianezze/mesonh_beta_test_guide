Infolettre #04
================================================

**10 janvier 2025.** Version française, English version `here <newsletter_03_english.html>`_.


Chers utilisateurs, chères utilisatrices de Méso-NH,

Nous vous souhaitons tout d'abord une très bonne année 2025 ! Riche en découverte grâce à vos futures simulations :)

Voici ci-dessous la 4ème infolettre de notre communauté. Vous y trouverez un entretien avec un développeur de Méso-NH, les dernières nouvelles de l’équipe support et la liste des dernières publications utilisant Méso-NH.

Entretien avec `Robert S <mailto:email@cnrs.fr>`_ (CNRM)
************************************************************************************

.. image:: photo_je.jpg
  :width: 450

Juan, tu as porté Méso-NH 5-5-1 sur GPU avec Philippe. Pourrais-tu décrire de quoi il s'agit et les perspectives d'utilisation que cela ouvre ?
  rep

  rep suite

Quel intérêt y a-t-il à réaliser des simulations sur les calculateurs dotés de GPU plutôt que sur ceux basés sur des CPU uniquement ?
  rep [#flop1]_ rep [#flop2]_ de la puissance totale.

.. [#flop1] Pétaflops = millions de milliards d'opérations de calcul par seconde. 
.. [#flop2] 1 Exaflop = 1000 Pétaflops.

Y a-t-il des situations qui se prêtent particulièrement bien à l'utilisation de Méso-NH 5-5-1 sur GPU ?
  rep

  rep suite

Quelles recommandations ferais-tu aux utilisateur.trices qui souhaiteraient simuler sur GPU ?
  rep

  rep

Quelles sont les limites pour l'instant de ce portage de Méso-NH ? les perspectives ?
  rep

  rep

  rep

  rep

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
  - Amélioration de la prise en compte du givrage par la modélisation et la prévision météorologique pour l'exploitation des parcs éoliens [`Dupont <https://theses.fr/s305624>`_, Université de Toulouse, 2024]
  - Etude de l'évolution de la couche limite atmosphérique et des nuages de pente sur l'île de la Réunion [`El Gdachi <https://theses.fr/s311244>`_, Université de La Réunion, 2024]
  - Interactions entre irrigation, couche limite atmosphérique et vents de méso-échelle en région semi-aride : observations et modélisation [`Lunel <https://theses.fr/s304370>`_, Université de Toulouse, 2024]

.. note::

   Si vous souhaitez partager avec la communauté le fait qu’un de vos projets utilisant Méso-NH a été financé ou toute autre communication sur vos travaux (notamment posters et présentations *disponibles en ligne*), n’hésitez pas à m’écrire. A l’occasion de la mise en place de ces infolettres, je suis également preneur de vos avis sur le format proposé.

Bonnes simulations avec Méso-NH !

A bientôt,

Thibaut Dauhut et toute l’équipe Méso-NH : Philippe Wautelet, Quentin Rodier, Didier Ricard, Joris Pianezze, Juan Escobar et Jean-Pierre Chaboureau
