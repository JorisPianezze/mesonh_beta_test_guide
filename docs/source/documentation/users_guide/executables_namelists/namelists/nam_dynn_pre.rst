.. _nam_dynn_pre:

NAM_DYNn_PRE
-----------------------------------------------------------------------------

.. csv-table:: NAM_DYNn_PRE content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CPRESOPT","CHARACTER(LEN=5)","'CRESI'"
   "NITR","INTEGER","4"
   "XRELAX","REAL","1.0"
   "LRES","LOGICAL",".FALSE."
   "XRES","REAL","1.E-07"

* :code:`CPRESOPT` :  gives the type of pressure solver used for the elliptic equation ('RICHA', 'CGRAD', 'CRESI', 'ZRESI').  This equation is solved in order to ensure the anelastic  constraint for the initial wind field. Note that the solver is applied even for the 'FLAT' case when the Earth spericity is taken into account.

* :code:`NITR` : number of  iterations used for the resolution of the elliptic equation (solver = "CPRESOPT").

* :code:`XRELAX` : relaxation factor used by the Richardson method (CPRESOPT = "RICHA").

* :code:`LRES` : flag to change the residual divergence limit

* :code:`XRES` : Value of the residual divergence limit
