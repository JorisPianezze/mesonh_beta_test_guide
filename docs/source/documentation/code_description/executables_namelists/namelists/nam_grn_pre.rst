.. _nam_grn_pre:

NAM_GRn_PRE
-----------------------------------------------------------------------------

.. csv-table:: NAM_GRn_PRE content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CSURF", "CHARACTER(LEN=4)", "'NONE'"

* :code:`CSURF` : ground selector.

  * 'NONE' no surface scheme will be activated during the future MesoNH simulation, we therefore do not need any surface parameters. All the namelists of the externalized surface will be ignored.
  * 'EXTE' the externalized surface is used. See the SURFEX documentation for more details.
