.. _nam_write_diag_surfn:

NAM_WRITE_DIAG_SURFN
-----------------------------------------------------------------------------

Diagnostics for to each grid cell and each tile.

.. csv-table:: NAM_WRITE_DIAG_SURFN content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LSELECT", "logical", "F"
   "CSELECT", "array of string of characters", ""
   "LPROVAR_TO_DIAG", "logical", "F"
   "LSNOWDIMNC", "logical", "F"
   "LRESETCUMUL", "logical", "F"
   
* LSELECT: if T it indicates that a selection will be used as output .

* CSELECT: array containing the list of output fields .

* LPROVAR_TO_DIAG: used to write out prognostic variables like diagnostic one, on average over all patches.

* LSNOWDIMNC: gin case of OFFLIN output files, to write the output snow fields in 2D (number of points / number of snow layers).

* LRESETCUMUL: gin OFFLINE mode, for the ISBA scheme, replaces the instantaneous fields by the averaged cumulated fields on the output writing time step. Then the cumulated fields are cumulated during the writing time steps and reset at the end of each of them.
