.. _spawning:

SPAWNING
***************************************************************************** 

:program:`SPAWNING` program performs the horizontal interpolation from one Meso-NH file into another (respectively file 1 and file 2). The grid of the file 2 must be exactly included in the grid of file 1. The file 2 can be directly used for a model run, but it contains smooth surface fields (especially the orography). It is possible to run the model with the two files with gridnesting interaction, since a iterative procedure insures the gridnesting condition on the orographies. The domain of the file 2 can be defined either:

* by namelist NAM_GRID2_SPA specification.

* with the domain of another Meso-NH file, which grid is coherent with the input file. For example this file can be a PGD file created by :program:`PREP_PGD` with a domain defined from the domain of file 1 and the same type of specifications as those in NAM_GRID2_SPA.

.. csv-table:: SPAWNING program and its corresponding namelist and function
   :header: "Executable", "Namelist", "Function"
   :widths: 30, 30, 30

   "SPAWNING", "SPAWN1.nam", "Horizontal interpolations from a Meso-NH file into another Meso-NH file, with a finer resolution and smaller domain."

The following namelists can be used in the :file:`SPAWN1.nam` file :

* :ref:`nam_blankn`
* :ref:`nam_grid2_spa`
* :ref:`nam_lunit2_spa`
* :ref:`nam_spawn_surf`  
 
.. include:: namelists/nam_blankn.rst
.. include:: namelists/nam_grid2_spa.rst
.. include:: namelists/nam_lunit2_spa.rst
.. include:: namelists/nam_spawn_surf.rst
