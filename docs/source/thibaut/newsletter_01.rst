Newsletter     #01
================================================

Chers utilisateurs, chères utilisatrices de Méso-NH,

Voici la 1ère infolettre de notre communauté Méso-NH. Vous y trouverez un entretien avec un développeur de Méso-NH, les dernières nouvelles de l’équipe support et la liste des dernières publications utilisant Méso-NH.

.. image:: photo_bv.jpg
  :width: 300


Entretien avec `Benoît Vié <mailto:benoit.vie@meteo.fr>`_ (CNRM) au sujet de LIMA pour la représentation de la microphysique à deux moments
*******************************************************************************************************************

Benoît, tu as fortement contribué à LIMA pour la représentation à deux moments de la microphysique dans Méso-NH. Pourrais-tu résumer ce que fait cette option ?
  Oui, j'ai dépoussiéré LIMA qui dormait dans un tiroir du LAERO après la thèse de Sarah Berthet avec Jean-Pierre Pinty ! C'est un des schémas microphysiques disponibles dans Meso-NH, qui s'occupe donc de prévoir la formation des nuages et des précipitations. Comme ICE3 dont il s'inspire largement, la composition nuageuse est décomposée en grandes catégories d'hydrométéores (gouttelettes, pluie, petits cristaux, neige, graupel et grêle). Mais la nouveauté de LIMA, c'est de prévoir le nombre d'hydrométéores de chaque type, en plus de leur masse totale. Cela permet de mieux estimer leur taille et de mieux représenter l'ensemble des processus (condensation/évaporation, collisions...) qui dirigent leur évolution. LIMA représente aussi les interactions aérosols-nuages, en s'appuyant sur une population d'aérosols pronostique réaliste pour déterminer le nombre d'hydrométéores. LIMA est ainsi le schéma microphysique de Méso-NH le plus à même de prévoir avec précision la composition nuageuse, son évolution et la formation des précipitations.

Pourquoi vaut-il mieux utiliser LIMA qu’une autre représentation de la microphysique ?
  L'apport de LIMA se traduit généralement par de meilleures prévisions ou simulations. Ainsi, il a déjà été montré par exemple que LIMA est plus performant pour la prévision du brouillard, et produit des systèmes convectifs plus réalistes en comparaison à des observations radar, notamment parce qu'il est capable de représenter des grosses gouttes de pluie et gère mieux l'évaporation des précipitations sous le nuage. Donc, que ce soit pour de la prévision ou de l'étude de processus, n'hésitez pas à l'essayer !

Dans quel cas cette option est-elle recommandée?
  En fait, quel que soit le système nuageux qui vous intéresse, il est probable que LIMA soit le bon choix ! D'autant plus que LIMA est maintenant très modulaire et qu'il est possible de choisir le niveau de complexité souhaité en fonction du sujet d'étude.

Quelles recommandations ferais-tu aux utilisateurs.trices ? 
  Le meilleur conseil est de ne pas hésiter à demander conseil, justement ! LIMA peut être utilisé très simplement, en mettant CCLOUD="LIMA" dans votre namelist, avec des réglages par défaut qui devraient donner une bonne base de travail. Néanmoins, le vrai potentiel de LIMA s'exprimera si sa configuration est adaptée au cas d'étude. Il est par exemple souvent important de bien définir la population d'aérosols que LIMA utilisera pour former des gouttelettes et des cristaux pour obtenir les meilleurs résultats, et parfois même nécessaire d'activer également les schémas d'émission d'aérosols. Au delà de LIMA, Meso-NH dispose maintenant d'un ensemble de paramétrisations cohérent (pour les aérosols, la microphysique, le rayonnement, l'électricité...) et il est facile de se perdre parmi toutes les options disponibles, donc, je le répète : n'hésitez pas à nous demander des conseils !

Quelles sont les limites ? Dans quel cas cette option est-elle plutôt à éviter ?
  Il est inutile d'activer LIMA si ... vous simulez un cas de couche limite sèche très stable ! Plus sérieusement, nous travaillons sur deux biais encore importants de LIMA : la sous-estimation des concentrations en petits cristaux, que l'on corrige en ajoutant des processus de formation secondaire de glace qui manquaient jusqu'à maintenant et ne sont pas encore complètement validés, et la sous-estimation de l'eau liquide surfondue, que l'on a bon espoir d'améliorer en s'appuyant sur des campagnes de mesure récentes. Mais il n'y a pas mieux que LIMA dans Meso-NH... jusqu'à ce qu'un schéma bin y soit ajouté !


*Si vous aussi vous souhaitez expliquer un développement que vous avez mis en place dans Méso-NH, ou une méthode d’analyse que vous partagez à la communauté, n’hésitez pas à me le signaler par* `mail <mailto:thibaut.dauhut@aero.obs-mip.fr>`_.

Les nouvelles de l’équipe support
***********************************

<peut contenir :  ce que vous avez mis au point ces derniers mois (disons depuis les journées des utilisateurs) et qq mots sur vos plans à venir. Merci de renseigner ce que vous souhaitez y écrire sur ce framapad (il y a qq idées en plus, notamment sur les bugs que vous auriez vus passés, en bas du pad) : https://mypads2.framapad.org/p/nouvelles-de-l-equipe-support-2024-03-9831oz9o2 >

La liste des publications utilisant Méso-NH parues dernièrement (depuis le début 2024)
****************************************************************************************

Air-sea interactions
------------------------

The wave-age-dependent stress parameterisation (WASP) for momentum and heat turbulent fluxes at sea in SURFEX v8.1
  Bouin, M.-N., C. Lebeaupin Brossier, S. Malardel, A. Voldoire, and C. Sauvage. Geosci. Model Dev., 17, 117-141, 2024. [ `http <https://doi.org/10.5194/gmd-17-117-2024>`_ ]


A numerical study of ocean surface layer response to atmospheric shallow convection: impact of cloud shading, rain and cold pool,
  Brilouet, P.-E., J.-L. Redelsperger, M.-N. Bouin, F. Couvreux, and N. Villefranque. Quart. J. Roy. Meteor. Soc., n/a, accepted, 2024. [ http ]


Boundary layer
-------------------

Coherent subsiding structures in large eddy simulations of atmospheric boundary layers
  Brient, F., F. Couvreux, C. Rio, and R. Honnert. Quart. J. Roy. Meteor. Soc., n/a, in press, 2024. [ http ]

Breakdown of the velocity and turbulence in the wake of a wind turbine – Part 1: Large-eddy-simulation study
  Jézéquel, E., F. Blondel, and V. Masson. Wind Energ. Sci., 9, 97–117, 2024a. [ http ]

Breakdown of the velocity and turbulence in the wake of a wind turbine – Part 2: Analytical modeling
  Jézéquel, E., F. Blondel, and V. Masson. Wind Energ. Sci., 9, 119–139, 2024b. [ http ]

Impact of surface turbulent fluxes on the formation of convective rolls in a Mediterranean windstorm
  Lfarh, W., F. Pantillon, and J.-P. Chaboureau. J. Geophys. Res., n/a, submitted, 2024. [ http ]


Fire
-----

Numerical investigation of the Pedrógão Grande pyrocumulonimbus using a fire to atmosphere coupled model
  Couto, F. T., J.-B. Filippi, R. Baggio, C. Campos, and R. Salgado. Atmos. Res., 299, 107223, 2024. [ http ]

Dust
------

Fractional solubility of iron in mineral dust aerosols over coastal Namibia: a link to marine biogenic emissions?
  Desboeufs, K., P. Formenti, R. Torres-Sánchez, K. Schepanski, J.-P. Chaboureau, H. Andersen, J. Cermak, S. Feuerstein, B. Laurent, D. Klopper, A. Namwoonde, M. Cazaunau, S. Chevaillier, A. Feron, C. Mirande-Bret, S. Triquet, and S. J. Piketh. Atmos. Chem. Phys., 24, 1525–1541, 2024. [ http ]


Cyclogenesis in the tropical Atlantic: First scientific highlights from the Clouds-Atmospheric Dynamics-Dust Interactions in West Africa (CADDIWA) field campaign
  Flamant, C., J.-P. Chaboureau, J. Delanoë, M. Gaetani, C. Jamet, C. Lavaysse, O. Bock, M. Borne, Q. Cazenave, P. Coutris, J. Cuesta, L. Menut, C. Aubry, A. Benedetti, P. Bosser, S. Bounissou, C. Caudoux, H. Collomb, T. Donal, G. Febvre, T. Fehr, A. H. Fink, P. Formenti, N. Gomes Araujo, P. Knippertz, E. Lecuyer, M. Neves Andrade, C. G. Ngoungué Langué, T. Jonville, A. Schwarzenboeck, and A. Takeishi. Bull. Amer. Meteo. Soc., n/a, in press, 2024a. [ http ]

The radiative impact of biomass burning aerosols on dust emissions over Namibia and the long-range transport of smoke observed during AEROCLO-sA
  Flamant, C., J.-P. Chaboureau, M. Gaetani, K. Schepanski, and P. Formenti. Atmos. Chem. Phys., n/a, submitted, 2024b. [ http ]



Extreme precipitation
-----------------------

Impact of urban land use on mean and heavy rainfall during the Indian summer monsoon
  Falga, R., and C. Wang. Atmos. Chem. Phys., 24, 631–647, 2024. [ http ]

Chemistery
-----------

Measurement Report: Bio-physicochemistry of tropical clouds at Maïdo (Réunion Island, Indian Ocean): overview of results from the BIO-MAÏDO campaign
  Leriche, M., P. Tulet, L. Deguillaume, F. Burnet, A. Colomb, A. Borbon, C. Jambert, V. Duflot, S. Houdier, J.-L. Jaffrezo, M. Vaïtilingom, P. Dominutti, M. Rocco, C. Mouchel-Vallon, S. El Gdachi, M. Brissy, M. Fathalli, N. Maury, B. Verreyken, C. Amelynck, N. Schoon, V. Gros, J.-M. Pichon, M. Ribeiro, E. Pique, E. Leclerc, T. Bourrianne, A. Roy, E. Moulin, J. Barrie, J.-M. Metzger, G. Péris, C. Guadagno, C. Bhugwant, J.-M. Tibere, A. Tournigand, E. Freney, K. Sellegri, A.-M. Delort, P. Amato, M. Joly, J.-L. Baray, P. Renard, A. Bianco, A. Réchou, and G. Payen. Atmos. Chem. Phys., n/a, in discussion, 2024. [ http ]

Measurement Report: Insights into the chemical composition of molecular clusters present in the free troposphere over the Southern Indian Ocean: observations from the Maïdo observatory (2150 m a.s.l., Reunion Island)
  Salignat, R., M. Rissanen, S. Iyer, J.-L. Baray, P. Tulet, J.-M. Metzger, J. Brioude, K. Sellegri, and C. Rose. Atmos. Chem. Phys., n/a, in discussion, 2024. [ http ]




*Si vous souhaitez partager avec la communauté le fait qu’un de vos projets utilisant Méso-NH a été financé ou toute autre communication sur vos travaux (notamment posters et présentations disponibles en ligne), n’hésitez pas à m’écrire. A l’occasion de la mise en place de ces infolettres, je suis également preneur de vos avis.*

Bonnes simulations avec Méso-NH !

A bientôt,

Thibaut
pour l’équipe support
