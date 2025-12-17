.. _nam_2d_frc:

NAM_2D_FRC
-----------------------------------------------------------------------------

.. csv-table:: NAM_2D_FRC content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "L2D_ADV_FRC","LOGICAL",".FALSE."
   "L2D_REL_FRC","LOGICAL",".FALSE."
   "XRELAX_HEIGHT_BOT","REAL","0.0"
   "XRELAX_HEIGHT_TOP","REAL","30000.0"
   "XRELAX_TIME","REAL","864000.0"

* :code:`L2D_ADV_FRC` : flag to activate advecting forcing (2D simulations), using files passed through namelist :file:`PRE_IDEA1.nam`

* :code:`L2D_REL_FRC` : flag to activate relaxation forcing (2D simulations), using files passed through namelist :file:`PRE_IDEA1.nam`

* :code:`XRELAX_HEIGHT_BOT` : lower limit of relaxation (m)

* :code:`XRELAX_HEIGHT_TOP` : upper limit of relxation (m)

* :code:`XRELAX_TIME` : relaxation timsescale (s)

