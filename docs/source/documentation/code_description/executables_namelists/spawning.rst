SPAWNING
***************************************************************************** 

This program performs the horizontal interpolation from one MESO-NH file into another (re-
spectively file 1 and file 2). The grid of the file 2 must be exactly included in the grid of file 1.
The file 2 can be directly used for a model run, but it contains smooth surface fields (especially
the orography). It is possible to run the model with the two files with gridnesting interaction,
since a iterative procedure insures the gridnesting condition on the orographies.
The domain of the file 2 can be defined either:
1. by namelist NAM_GRID2_SPA specification.
2. with the domain of another FM file, which grid is coherent with the input file. For example
this file can be a PGD file created by PREP_PGD with a domain defined from the domain
of file 1 and the same type of specifications as those in NAM_GRID2_SPA (see above)

.. csv-table:: SPAWNING program and its corresponding namelist and function
   :header: "Executable", "Namelist", "Function"
   :widths: 30, 30, 30

   "SPAWNING", "SPAWN1.nam", "Horizontal interpolations from a Meso-NH file
into another Meso-NH file, with a finer resolution and smaller domain."

