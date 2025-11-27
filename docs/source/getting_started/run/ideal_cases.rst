.. _ideal_cases:

Ideal cases
================================================

The general workflow for ideal case simulation is :

* initialize the surface fields : idealised (:ref:`prep_ideal_case`) or realistic (:ref:`prep_pgd`)

* specify an horizontally uniform atmosphere from a profile (:ref:`prep_ideal_case`)

* specify atmospheric vertical forcings (:ref:`prep_ideal_case`)

* (optional) add a perturbation (:ref:`prep_ideal_case`)

* start the time-integration (:ref:`mesonh`)

* (optional) compute diagnostics (:ref:`diag` and :ref:`spectra`)

This workflow is describe in the following figure : 

.. figure:: ideal_cases/algorithm_ideal_cases.png
   :scale: 50 %
   :alt: Ideal simulation workflow
   
   Ideal simulation workflow

A few examples are described hereafter : 

.. toctree::
   :maxdepth: 1

   ideal_cases/1D/1D.rst
   ideal_cases/2D/2D.rst
   ideal_cases/3D_ideal_surface/3D_ideal_surface.rst
   ideal_cases/3D_real_surface/3D_real_surface.rst

.. note::

   If you need advance settings, please go to :ref:`cases_catalogue` section.
