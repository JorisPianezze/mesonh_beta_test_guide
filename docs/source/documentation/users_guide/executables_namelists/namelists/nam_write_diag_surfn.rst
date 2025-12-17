.. _nam_write_diag_surfn:

NAM_WRITE_DIAG_SURFN
-----------------------------------------------------------------------------

.. warning::

   This namelist comes from SURFEX 9.0.0 user guide https://www.umr-cnrm.fr/surfex/IMG/pdf/surfex_tecdoc.pdf.

Diagnostics for to each grid cell and each tile.

.. csv-table:: NAM_WRITE_DIAG_SURFN content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LSELECT", "LOGICAL", ".FALSE."
   "CSELECT", "ARRAY(CHARACTER)", ""
   "LPROVAR_TO_DIAG", "LOGICAL", ".FALSE."
   "LSNOWDIMNC", "LOGICAL", ".FALSE."
   "LRESETCUMUL", "LOGICAL", ".FALSE."
   
* :code:`LSELECT` : if T it indicates that a selection will be used as output.

* :code:`CSELECT` : array containing the list of output fields.

* :code:`LPROVAR_TO_DIAG` : used to write out prognostic variables like diagnostic one, on average over all patches.

* :code:`LSNOWDIMNC` : in case of OFFLIN output files, to write the output snow fields in 2D (number of points / number of snow layers).

* :code:`LRESETCUMUL` : in OFFLINE mode, for the ISBA scheme, replaces the instantaneous fields by the averaged cumulated fields on the output writing time step. Then the cumulated fields are cumulated during the writing time steps and reset at the end of each of them.
