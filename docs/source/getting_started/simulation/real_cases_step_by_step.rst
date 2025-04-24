.. _real_cases:

Real cases
================================================

The general workflow for real case simulation is :

* define the domain location and initialize the surface fields (:ref:`prep_pgd`)

* define initial and boundary conditions (:ref:`prep_real_case`)

* launch the simulation (:ref:`mesonh`)

* compute diagnostics (:ref:`diag` and :ref:`spectra`)

This workflow is describe in the following figure : 

.. figure:: real_cases_step_by_step/algorithm_real_cases.png
   :scale: 50 %
   :alt: General algorithm for real case's simulation with no nesting and grid-nesting.
   
   General algorithm for real case's simulation with no nesting and grid-nesting.

Some basic example are describe hereafter : 

.. toctree::
   :maxdepth: 1

   real_cases_step_by_step/one_domain_era5.rst
   real_cases_step_by_step/one_domain_mesonh.rst
   real_cases_step_by_step/two_domains_grid_nesting.rst
   
.. note::

   If you need advance settings, please go to :ref:`cases_catalogue` section.
