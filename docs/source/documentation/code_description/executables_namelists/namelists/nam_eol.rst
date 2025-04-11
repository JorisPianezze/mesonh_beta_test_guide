.. _nam_eol:

NAM_EOL
-----------------------------------------------------------------------------

For now, simulations of wind turbine have been tested and validated only in ideal cases. 

.. csv-table:: NAM_EOL content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LMAIN_EOL","LOGICAL",".FALSE."
   "CMETH_EOL","CHARACTER(LEN=4)","'ADNR'"
   "CSMEAR","CHARACTER(LEN=4)","'3LIN'"
   "NMODEL_EOL","INTEGER","1"

* :code:`LMAIN_EOL` : flag to model wind turbines

  * .TRUE. to simulate wind turbines.
  * .FALSE. to forget about them.

* :code:`CMETH_EOL` : aerodynamic method for wind turbine simulations

  * 'ADNR' to use the  Non-Rotating Actuator Disc method.
  * 'ADR' to use the  Rotating Actuator Disc method.
  * 'ALM' to use the Actuator Line Method.

* :code:`CSMEAR` : smearing method of the aerodynamic forces field

  * 'NULL' : no smearing.
  * '1LIN' : 1D linear smearing method.
  * '3LIN' : 3D linear smearing method.

* :code:`NMODEL_EOL` : model number where the wind turbines are included (if nested models). If NMODEL_EOL=:math:`n\neq1`, the namelists :ref:`nam_eol_alm`, :ref:`nam_eol_adr` and :ref:`nam_eol_adnr`  have to be set in EXSEGn.nam
