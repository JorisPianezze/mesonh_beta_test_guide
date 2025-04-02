Newsletter #05
================================================

**4 April 2025.** English version, version française `ici <newsletter_05.html>`_.


Dear Meso-NH users,

This is the 5th newsletter from our Meso-NH community. You'll find an interview with the developer of a useful tool for Meso-NH users, the latest news from the support team and a list of the latest publications using Meso-NH.

Interview with `Najda Villefranque <mailto:najda.villefranque@meteo.fr>`_ (CNRM)
*************************************************************************************

.. image:: photo_nv.jpg
  :width: 250


.. note::

   A longer version of the interview, with more details, is available `here <https://mesonh-beta-test-guide.readthedocs.io/en/latest/community/newsletters/newsletter_05_extended.html>`_.


Najda, you've developed a 3D radiation simulator that can be applied to 3D fields derived from Meso-NH simulations. Could you summarize what this program does?
  `htrdr <https://www.meso-star.com/projects/htrdr/htrdr.html>`_ is a free software program based on Monte Carlo methods that simulates the trajectory of a large number of photons to solve atmospheric radiative transfer. It takes as input a 3D description of the atmosphere, typically output from Meso-NH simulations, as well as a description of surfaces (e.g. of a city like `here <https://web.lmd.jussieu.fr/~nvillefranque/pages/teapot_city>`_ but we can obviously also prescribe a flat surface). Photons interact with hydrometeors, aerosols, gases and surfaces through absorption/emission and scattering/reflection phenomena. The distribution of photons on virtual sensors positioned in the scene by the user gives an estimate of the intensity of radiation on these sensors.

What applications do you recommend using htrdr for?
  htrdr is the ideal reference calculation software for accurately determining radiative quantities, whether solar (SW) or thermal (LW), in map form or horizontally integrated. It is particularly useful for estimating the radiative effect of clouds or aerosols, studying their impact as a function of their properties, and evaluating the parameterizations of large-scale models. htrdr also serves as a target for calibrating these parameterizations in idealized cases, where observations are lacking. In short, htrdr is to radiation what Meso-NH is to atmospheric dynamics! 

  htrdr can also be used to produce computer-generated images, using techniques similar to those used by Disney for their films. These simulations can be used to visualize a 3D Meso-NH field as a photo or film, or to synthesize satellite-like images, useful for designing or evaluating inversion algorithms.

Why is it better to use htrdr than other equivalent programs? 
  The advantages of Monte Carlo methods, such as those used by htrdr, are their precision (taking into account detailed processes, absence of bias), their flexibility (notably over spatial and spectral integration domains) and their theoretical insensitivity to the complexity of the virtual scenes in which photons propagate. Unlike other codes, htrdr uses tools derived from graphics research, making computation time independent of the amount of data to be processed, and extended to volume data by |villefranque_etal|. This means that a high-resolution simulation over detailed terrain will take no longer than a low-resolution simulation over flat ground. What's more, htrdr is a continuously developing software, used and enriched by various communities, making it a living, evolving tool.

What recommendations would you make to users?
    I'd recommend that they don't hesitate to contact me (or Robert Schoetter, who's also an htrdr expert!) if they want to get to grips with the software. Although `documentation <https://www.meso-star.com/projects/htrdr/man/man1/htrdr-atmosphere.1.html>`_ and `training material <https://mattermost.lmd.ipsl.fr/g3t-rayonnement/channels/htrdr>`_ are available online, prior discussion helps to ensure that htrdr meets specific needs. It can also help choose appropriate configurations and options, and guide users through input and output. It's also an opportunity to discuss radiation physics, even if the scientific question is not directly related to radiative transfer. Don't hesitate, because in real life, radiation is a lot more fun than you might think (laughs)!

What are its limitations?
  The main drawback of htrdr is the computation time, which can be limiting in the presence of highly scattering clouds. Although this is not technically limiting for users accustomed to large simulations, it is important to note that it consumes a lot of energy. For initial tuning, it is advisable to run simulations with a small number of photons to obtain a first estimate, even if it is noisy. There are also limits to the physical modeling of the transfer, such as the approximation of the diffusion phase function of hydrometeors and aerosols. However, these limitations can be overcome with time and further research. In short, htrdr is a powerful and scalable tool, capable of meeting new needs through future developments. Finally, I'd like to point out that to date htrdr is essentially diagnostic software, to be used *off-line* on simulation outputs produced elsewhere, with or without radiation. One of my research perspectives is to couple htrdr with Meso-NH to be able to run atmospheric simulations including 3D radiation resolution.

.. |villefranque_etal| raw:: html

   <a href="https://agupubs.onlinelibrary.wiley.com/doi/full/10.1029/2018MS001602" target="_blank">Villefranque et al. (2019)</a>

.. note::

   If you too would like to explain a development you've implemented in Meso-NH, or an analysis method you share with the community, please don't hesitate to let me know by `mail <mailto:thibaut.dauhut@univ-tlse3.fr>`_.
