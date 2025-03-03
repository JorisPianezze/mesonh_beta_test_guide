MESONH
***************************************************************************** 

The MESONH user will specify some free parameters of the run by fixing their new values in
the NAMELISTs of the file EXSEG$n.nam.
When more than one model is present, each model needs its own MESONH file to be
initialized and its own EXSEG$n.nam file to fix the free-parameters (note that a lot of physical
free-parameters depends on the mesh and therefore vary with the model number).
The input files are read by the program in order to realize the initialization and the eventual
coupling of the MESONH model with a large-scale model ( CEP, Arpège. . . ).
The output files are of two types:
• synchronous files for a given instant of the run. They contain the prognostic fields and
eventually, additional records for supplementary diagnostic fields at the same instant. The
file name ends by 00n with n>0
• a diachronic file for the temporal series of prognostic or diagnostic fields. The file name
ends by 000

.. csv-table:: MESONH program and its corresponding namelist and function
   :header: "Executable", "Namelist", "Function"
   :widths: 30, 30, 30

   "MESONH", "EXSEG1.nam", "Launch simulation"

