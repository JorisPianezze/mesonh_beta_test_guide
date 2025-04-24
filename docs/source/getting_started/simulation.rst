Simulation
============================================================================

Principle
*****************************************************************************

In Meso-NH, simulations can be divived in two categories:
   
* :ref:`ideal_cases` category corresponds to simulations which are initialized with an idealized atmosphere, typically with a radiosonding. In this kind of simulation you can use 1D, 2D or 3D grid on cartesian or conformal projections.
   
* :ref:`real_cases` category corresponds to simulations which are initialized with large-scale 3d atmospheric fields (IFS, ARPEGE, AROME, GFS, etc.).

For both catergories, you will have to use several :ref:`executables_and_namelists` to prepare, run and compute diagnostics of your simulation. To deepns Meso-NH's functionality please go to the following tutorials. 

Some basic tutorial
*****************************************************************************

Both categories are described in the following sections :

.. toctree::
   :maxdepth: 2

   simulation/ideal_cases_step_by_step.rst
   simulation/real_cases_step_by_step.rst
