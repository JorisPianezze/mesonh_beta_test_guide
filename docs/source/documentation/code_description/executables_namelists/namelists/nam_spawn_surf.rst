.. _nam_spawn_surf:

NAM_SPAWN_SURF
-----------------------------------------------------------------------------

.. csv-table:: NAM_SPAWN_SURF content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LSPAWN_SURF","LOGICAL",".TRUE."
   
* :code:`LSPAWN_SURF` : flag to  perform or not the interpolation of all the surface fields (both physiographic and prognostic fields).

  * .TRUE. : the interpolations are made
  * .FALSE. : the interpolations are not made and therefore no surface field will be present in the output spawned file. 
