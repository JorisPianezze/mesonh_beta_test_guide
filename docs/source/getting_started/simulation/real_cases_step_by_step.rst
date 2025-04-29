.. _real_cases:

Real cases
================================================

The general workflow for a one-domain real case simulation is :

* define the domain location and initialize the physiographic surface fields (:ref:`prep_pgd`)

* define the initial (surface and atmosphere) and atmospheric boundaries conditions (:ref:`prep_real_case`)

* start the time-integration (:ref:`mesonh`)

* (optional) compute diagnostics (:ref:`diag` and :ref:`spectra`)

This workflow is described in the following figure : 

.. figure:: real_cases_step_by_step/algorithm_real_cases.png
   :scale: 50 %
   :alt: Realistic simulation workflow without and with grid-nesting.
   
   Realistic simulation workflow

A few examples are described hereafter : 

.. toctree::
   :maxdepth: 1

   real_cases_step_by_step/one_domain_era5.rst
   real_cases_step_by_step/one_domain_mesonh.rst
   real_cases_step_by_step/two_domains_grid_nesting.rst
   
.. note::

   If you need advance settings, please go to :ref:`cases_catalogue` section.
