ZOOM_PGD
*****************************************************************************

The previous condition on the orography needed when using the gridnesting technique implies that all the PGD files have to be created (with :program:`PREP_PGD` and :program:`PREP_NEST_PGD` programs) before beginning the run. However, the user is not always sure where (and when) to initialize the inner models. To avoid to set exactly the domain of inner models at the :program:`PREP_PGD` step, one solution is to make PGD file on larger domain and then, zoom it on the part of the domain of interest when known with the following program :program:`ZOOM_PGD`. Then the output PGD file is used as PGD file for the interpolations of atmospheric fields with :program:`SPAWNING` and :program:`PREP_REAL_CASE` programs.

.. csv-table:: ZOOM_PGD program and its corresponding namelist and function
   :header: "Executable", "Namelist", "Function"
   :widths: 30, 30, 30

   "ZOOM_PGD", "PRE_ZOOM1.nam", "Zoom on PGD file to make an inner domain at the same resolution"
