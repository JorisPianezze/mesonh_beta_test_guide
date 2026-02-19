.. _nam_eol:

NAM_EOL
-----------------------------------------------------------------------------

For now, simulations of wind turbine have been tested and validated only in ideal cases. 

.. csv-table:: NAM_EOL content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LMAIN_EOL","LOGICAL",".FALSE."
   "NMODEL_EOL","INTEGER","1"
   "CMETH_EOL","CHARACTER(LEN=4)","'ADNR'"
   "CSMEAR","CHARACTER(LEN=4)","'3LIN'"
   "XKERNEL_RATIO","REAL","2."  
   "LCONTROL_EOL", "LOGICAL", ".FALSE." 
   "LNACELLE", "LOGICAL", ".FALSE." 
   "LTOWER", "LOGICAL", ".FALSE."
   "LDIA_EOL", "LOGICAL", ".TRUE."
   "LFLOAT_EOL", "LOGICAL", ".FALSE." 
 
* :code:`LMAIN_EOL` : flag to model wind turbines

  * .TRUE. to simulate wind turbines.
  * .FALSE. to forget about them.

* :code:`NMODEL_EOL` : model number where the wind turbines are included (if nested models). If NMODEL_EOL :math:`\neq 1` (n :math:`\neq 1`), the namelists :ref:`nam_eol_alm`, :ref:`nam_eol_adr` and :ref:`nam_eol_adnr`  have also to be set in EXSEGn.nam

* :code:`CMETH_EOL` : aerodynamic method for wind turbine simulations

  * 'ADNR' to use the  Non-Rotating Actuator Disc method.
  * 'ADR' to use the  Rotating Actuator Disc method.
  * 'ALM' to use the Actuator Line Method.

* :code:`CSMEAR` : smearing method of the aerodynamic forces field

  * 'NULL' : no smearing.
  * '1LIN' : 1D linear smearing method.
  * '3LIN' : 3D linear smearing method.
  * '3DGA' : 3D gaussian kernel. Note that this can increase the computational cost of the simulation. This mode is only available for ALM and ADR (not ADNR).

* :code:`XKERNEL_RATIO` : ratio of the kernel size in the 3D Gaussian smearing to the mesh size.

* :code:`LCONTROL_EOL` : flag to use a controller to modify rotational speed and blade pitch angle during the run. Only for CMETH_EOL='ADR' or 'ALM'.

  * .TRUE.  activates the controller. More parameterizations are available in the EOL_CONTROL namelist.
  * .FALSE. the rotational speed and blade pitch angle are constant during the simulation (values imposed in CFARM_CSVDATA).

* :code:`LNACELLE` : flag to model wind turbines nacelle. Only for CMETH_EOL='ADR' or 'ALM'.

  * .TRUE.  to simulate wind turbine nacelle.
  * .FALSE. to remove the nacelle body forces.

* :code:`LTOWER` : flag to model wind turbines tower. Only for CMETH_EOL='ADR' or 'ALM'.

  * .TRUE.  to simulate wind turbine tower.
  * .FALSE. to remove the tower body forces.


* :code:`LDIA_EOL` : flag to write SCADA-like variables in the diachronic file. Only for CMETH_EOL='ADR' or 'ALM'. See Sect. \ref{ss:variables_SCADA} for a list of available variables.

  * .TRUE.  write variables. They are written into subgroup 'Turbines', itself containing one subgroup for each turbine.
  * .FALSE. do not write variables.

* :code:`LFLOAT_EOL` : flag to activate the floating motions and static positions. Only for CMETH_EOL='ADR' or 'ALM'.

  * .FALSE. do not use floating DOF.
  * .TRUE.  use floating DOFs. Each turbine written in CFARM_CSVDATA must have a last column which contains the name of the CSV field containing the prescribed motions. A mean value for static position as well as an amplitude, frequency and phase for dynamic motion can be given as follows:

.. csv-table:: LFLOAT content
   :header: "Motion", "Mean [m or rad]", "Amplitude [m or rad]", "Frequency [Hz]", "Phase [rad]"
   :widths: 20, 20, 20, 20, 20
   
   "Surge", "0.00000", "0.0000", "0.000", "0.000"
   "Sway",  "0.00000", "0.0000", "0.000", "0.000"
   "Heave", "10.0000", "0.0000", "0.000", "0.000"
   "Roll", "0.00000",  "0.0000", "0.000", "0.000"
   "Pitch", "0.08727", "0.0349", "0.200", "0.000"
   "Yaw", "0.00000",   "0.0000", "0.000", "0.000"

Note that filling the table with 0.000 will lead to the same behavior as if LFLOAT_EOL = .FALSE. This can be useful if some turbines are floating and some are not.

