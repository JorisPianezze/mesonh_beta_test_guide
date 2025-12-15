Infolettre #SSQL
================================================

**X xxxxx 2025.** Version française, English version `here <newsletter_03_english.html>`_.


Chers utilisateurs, chères utilisatrices de Méso-NH,

Voici ci-dessous la Xème infolettre de notre communauté. Vous y trouverez un entretien avec deux dévelop'heur.euses de Méso-NH, les dernières nouvelles de l’équipe support et la liste des dernières publications utilisant Méso-NH.

Entretien avec `Quentin Libois <quentin.libois@meteo.fr>`_ (CNRM) et `Sophia Schaefer <sophia.schaefer@meteo.fr>`_ (CNRM)
*************************************************************************************************************************************


Quentin, tu as inclus en 2017 la possibilité d'utiliser le code ecRad pour la représentation du rayonnement dans Méso-NH et, Sophia, tu as contribué à mettre à jour la nouvelle version d'ecRad dans la prochaine version de Méso-NH avec Quentin Rodier. Pourriez-vous résumer ce que permet l'utilisation de ce code ?
  ecRad est le code de transfert radiatif utilisé dans IFS (Integrated Forecasting System, le modèle atmosphérique global de l’ECMWF, le Centre européen pour les prévisions météorologiques à moyen terme). C'est avant tout un code à l'état-de-l'art qui permet d'utiliser des développements récents tant pour la résolution de l'équation du transfert radiatif (prise en compte des hétérogénéités sous-maille des nuages, paramétrisation des effets 3D sous-maille) que pour les propriétés optiques des aérosols et des nuages. A l'origine il s'appuyait sur les propriétés optiques des gaz telles que fournies par RRTM (Rapid radiative transfer model) mais, depuis la version 1.6, il propose de nouvelles propriétés via l'option ecckd qui le rend particulièrement rapide. Son aspect modulaire le rend facile d'accès, tant pour son utilisation que pour contribuer à son développement.
  La conception modulaire permet à l'utilisateur de faire varier individuellement certaines parties du code, de tester l’impact de ces modifications et d'optimiser les réglages pour différentes applications.

Pourquoi vaut-il mieux utiliser ecRad qu’une autre représentation du rayonnement (par ex. celle nommée ECMWF dans Méso-NH) ?
  ecRad dispose d'un grand nombre d'options (hypothèse d'hétérogénéité sous-maille des nuages, recouvrement vertical des fractions nuageuses, propriétés optiques des gaz, aérosols et hydrométéores, etc.) qui permettent d'explorer simplement la sensibilité du transfert radiatif à ces options ou de prendre en compte des processus qui ne pouvaient pas l'être auparavant (prise en compte de la diffusion pour le rayonnement infrarouge thermique, effets 3D, prise en compte de différents types d'hydrométéores liquides et glacés). Aujourd'hui il est aussi plus rapide et plus précis que l'option historique nommée ECMWF dans Méso-NH. De manière générale ecRad peut faire tout ce que proposait l'option historique, mais bien plus encore, et le code est également plus facile à utiliser et à modifier.

Dans quel cas ecRad est-il recommandé ?
  Il n'y a a priori aucun cas où ecRad n'est pas recommandé. En fonction des applications, différentes options d'ecRad peuvent être recommandées (par exemple, différents solveurs de rayonnement).

Quelles recommandations feriez-vous aux utilisateurs.trices ?
  Le rayonnement reste une composante assez mal connue des utilisateur.trices de Méso-NH. Pourtant une simulation peut être très sensible au choix des options de rayonnement. Nous encourageons les utilisateur.trices à estimer la sensibilité de leurs simulations à des paramètres clés tels que l'hypothèse de recouvrement vertical ou l'hétérogénéité sous-maille. Noter aussi que l'estimation du rayon effectif des hydrométéores peut fortement impacter les propriétés optiques d'un nuage, et en conséquence le bilan d'énergie et le cycle de vie d'un nuage. Il est important que l'estimation du rayon effectif et l'option choisie pour les propriétés optiques des hydrométéores soient cohérentes. Pour le solveur de rayonnement, l'option par défaut pour les modèles opérationnels est actuellement McICA, mais pour les cas LES ou à colonne unique, Tripleclouds peut être une meilleure option (puisqu'elle n'introduit pas de bruit stochastique).

Quelles sont les limites ? Dans quel cas cette option est-elle plutôt à éviter ?
  ecRad demeure un modèle deux-flux basé sur l'hypothèse plan-parallèle et suppose donc des colonnes indépendantes. En conséquence ses performances demeurent limitées à haute résolution spatiale lorsque les transferts radiatifs horizontaux entre colonnes adjacentes deviennent importants. Une option pour traiter cet effet 3D pourrait être incluse à l'avenir. Mais ecRad n'en demeure pas moins la meilleure option disponible aujourd'hui dans Méso-NH.


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
