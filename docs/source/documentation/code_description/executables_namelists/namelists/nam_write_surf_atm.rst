.. _nam_write_surf_atm:

NAM_WRITE_SURF_ATM
----------------------------------------------------------------------------- 

.. csv-table:: NAM_WRITE_SURF_ATM content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LNOWRITE_CANOPY", "LOGICAL", ".FALSE."
   "LNOWRITE_TEXFILE", "LOGICAL", ".FALSE."
   "LSPLIT_PATCH", "LOGICAL", ".TRUE."

* :code:`LNOWRITE_CANOPY` : if T, do not write canopy prognostic variables in initial/restart or LBC files

* :code:`LNOWRITE_TEXFILE` : if T, do not fill class_cover_data.tex file during the model setup

* :code:`LSPLIT_PATCH` : T by default, setting FALSE it writes output fields 2D, with the dimension PATCH, like before.
