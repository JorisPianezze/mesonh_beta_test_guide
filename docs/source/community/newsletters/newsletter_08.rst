Infolettre #08
================================================

**8 janvier 2025.** Version française, English version `here <newsletter_03_english.html>`_.


Chers utilisateurs, chères utilisatrices de Méso-NH,

Voici ci-dessous la 8ème infolettre de notre communauté. Vous y trouverez un entretien avec deux dévelopeur.euses de Méso-NH, les dernières nouvelles de l’équipe support et la liste des dernières publications utilisant Méso-NH.

Entretien avec `Quentin Libois <quentin.libois@meteo.fr>`_ et Sophia Schaefer (CNRM)
*************************************************************************************************************************************

|pic1|     |pic2|

.. |pic1| image:: photo_ql.jpg
  :width: 250

.. |pic2| image:: photo_ss.jpg
  :width: 230

Quentin, tu as inclus en 2017 la possibilité d'utiliser le code ecRad pour la représentation du rayonnement dans Méso-NH, et Sophia, tu as contribué à mettre à jour la nouvelle version d'ecRad dans la prochaine version de Méso-NH avec Quentin Rodier. Pourriez-vous résumer ce que permet l'utilisation de ce code ?
  ecRad est le code de transfert radiatif utilisé dans IFS (Integrated Forecasting System, le modèle atmosphérique global de l’ECMWF, le Centre Européen pour les Prévisions Météorologiques à Moyen Terme). C'est avant tout un code à l'état-de-l'art qui permet d'utiliser des développements récents tant pour la résolution de l'équation du transfert radiatif (prise en compte des hétérogénéités sous-maille des nuages, paramétrisation des effets 3D sous-maille) que pour les propriétés optiques des aérosols et des nuages. A l'origine il s'appuyait sur les propriétés optiques des gaz telles que fournies par RRTM (Rapid Radiative Transfer Model) mais, depuis la version 1.6, il propose de nouvelles propriétés via l'option ecckd qui le rend particulièrement rapide. Son aspect modulaire le rend facile d'accès, tant pour son utilisation que pour contribuer à son développement. La conception modulaire permet de faire varier individuellement certaines parties du code, de tester l’impact de ces modifications et d'optimiser les réglages pour différentes applications.

Pourquoi vaut-il mieux utiliser ecRad qu’une autre représentation du rayonnement (par ex. celle nommée ECMWF dans Méso-NH) ?
  ecRad dispose d'un grand nombre d'options (hypothèse d'hétérogénéité sous-maille des nuages, recouvrement vertical des fractions nuageuses, propriétés optiques des gaz, aérosols et hydrométéores, etc.) qui permettent d'explorer simplement la sensibilité du transfert radiatif à ces options ou de prendre en compte des processus qui ne pouvaient pas l'être auparavant (prise en compte de la diffusion pour le rayonnement infrarouge thermique, effets 3D, prise en compte de différents types d'hydrométéores liquides et glacés). Aujourd'hui il est aussi plus rapide et plus précis que l'option historique nommée ECMWF dans Méso-NH. De manière générale ecRad peut faire tout ce que proposait l'option historique, mais bien plus encore, et le code est également plus facile à utiliser et à modifier.

Dans quel cas ecRad est-il recommandé ?
  Il n'y a a priori aucun cas où ecRad n'est pas recommandé. En fonction des applications, différentes options d'ecRad peuvent être recommandées (par exemple, différents solveurs de rayonnement).

Quelles recommandations feriez-vous aux utilisateur.ices ?
  Le rayonnement reste une composante assez mal connue des utilisateur.ices de Méso-NH. Pourtant une simulation peut être très sensible au choix des options de rayonnement. Nous encourageons les utilisateur.ices à estimer la sensibilité de leurs simulations à des paramètres clés tels que l'hypothèse de recouvrement vertical ou l'hétérogénéité sous-maille. Noter aussi que l'estimation du rayon effectif des hydrométéores peut fortement impacter les propriétés optiques d'un nuage, et en conséquence le bilan d'énergie et le cycle de vie d'un nuage. Pour le solveur de rayonnement, l'option par défaut est actuellement McICA, mais pour les cas LES ou à colonne unique, Tripleclouds est une meilleure option (puisqu'elle n'introduit pas de bruit stochastique).

Quelles sont les limites ? Dans quel cas cette option est-elle plutôt à éviter ?
  ecRad demeure un modèle deux-flux basé sur l'hypothèse plan-parallèle et suppose donc des colonnes indépendantes. En conséquence ses performances demeurent limitées pour des configurations où le soleil est bas sur l'horizon, et à haute résolution spatiale lorsque les transferts radiatifs horizontaux entre colonnes adjacentes deviennent importants. Une option pour traiter ces transferts inter-colonnes pourrait être incluse à l'avenir. Malgré cette limite, ecRad n'en demeure pas moins la meilleure option disponible aujourd'hui dans Méso-NH.


.. note::

  Si vous aussi vous souhaitez expliquer un développement que vous avez mis en place dans Méso-NH, ou une méthode d’analyse que vous partagez à la communauté, n’hésitez pas à me le signaler par `mail <mailto:thibaut.dauhut@univ-tlse3.fr>`_.

    
    
Les nouvelles de l’équipe support
************************************

Version 6
  - La préparation de la version 6.0.0 est en cours, sa sortie est imminente.
  - La mise à jour de PHYEX (de Méso-NH/PHYEX à PHYEX-offline, puis le rétro-phasage) dans Méso-NH est en cours.
  - Le support pour l'écriture des fichiers LFI est terminé.
  - Dans les fichiers netCDF les variables SURFEX seront à présent séparées dans un groupe spécifique.
  - L'appel à RTTOV14 a été intégré pour l'étape de diagnostic et pour le calcul en ligne, l'appel à RTTOV13 a été enlevé.
  - Les dernières optimisations du portage GPU sur différentes machines (cartes GPU AMD MI250X et MI300A sur Adastra) et APU NVIDIA ont été intégrées à la branche ``MNH-60-branch``.
  - La dernière version du code d'éolienne (EOL-v2) et une mise à jour du couplage LIMA-ECRAD-aérosols ont été intégré à la branche ``MNH-60-branch``.

Développements en cours et récents
  - Des tests de Méso-NH en simple précision sont en cours sur tous les cas tests éligibles. Le passage en simple précision par défaut n'est pas encore acté et sera probablement repoussé à la 6.1.
  - Quelques mises à jour de la documentation ont été réalisées et le futur site technique de Méso-NH permettra de retrouver cette documentation.

Stage Méso-NH
  - Le prochain stage Méso-NH est programmé du 10 au 13 mars 2026.
  - Le stage se déroulera en hybride et en anglais.
  - Envoyez un email à `Quentin Rodier <mailto:quentin.rodier@meteo.fr>`_ pour informations et inscriptions.

.. note::
  Si vous avez des besoins, idées, améliorations à apporter, bugs à corriger ou suggestions concernant les entrées/sorties, `Philippe Wautelet <mailto:philippe.wautelet@cnrs.fr>`_ est preneur.


Dernières publications utilisant Méso-NH
****************************************************************************************



.. note::

   Si vous souhaitez partager avec la communauté le fait qu’un de vos projets utilisant Méso-NH a été financé ou toute autre communication sur vos travaux (notamment posters et présentations *disponibles en ligne*), n’hésitez pas à m’écrire. A l’occasion de la mise en place de ces infolettres, je suis également preneur de vos avis sur le format proposé.

Bonnes simulations avec Méso-NH !

A bientôt,

Thibaut Dauhut et toute l’équipe Méso-NH : Philippe Wautelet, Quentin Rodier, Didier Ricard, Joris Pianezze, Juan Escobar et Jean-Pierre Chaboureau
