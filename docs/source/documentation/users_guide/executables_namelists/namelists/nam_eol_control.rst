.. _nam_eol_control:

NAM_EOL_CONTROL
-----------------------------------------------------------------------------
Parametrization of the turbine's controller. Default data are given for a typical IEA15MW wind turbine controlled with a velocity table. 
To use with LCONTROL_EOL=.TRUE. in NAM_EOL.

.. csv-table:: NAM_EOL_CONTROL content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 40, 30
   
   "CMETH_OPS", "CHARACTER(LEN=9)", "TABLE    "
   "CCONTROL_CSVDATA", "CHARACTER(LEN=NFILENAMELGTMAX)", "data_TABLE.csv"
   "XCON_AVG_PERIOD", "REAL", "10."
   "XCON_DIST_VEL", "REAL", "240."
   "XCON_RAD_VEL", "REAL", "120."

* :code:`CMETH_OPS`: method for operational state control

  * 'TABLE': the rotational velocity and blade pitch angle are linearly interpolated from a table given in CCONTROL_CSVDATA. The inflow velocity used to interpolate is defined as the mean wind on a virtual disk defined by XCON_DIST_VEL and XCON_RAD_VEL and over a time period XCON_AVG_PERIOD.
  * 'JONKM': use the 'baseline' controller such as proposed in the Ph.D. thesis of JM Jonkman. The pitch control is a PID and the rotational speed is controlled through a mechanical equilibrium based on the 5-region model. This method requires a lot of mechanical data from the turbine, that are given to Meso-NH through the table CCONTROL_CSVDATA.
  * 'ROSCO': Reference Open-Source Controller is a wind turbine controller developed by NREL (National Renewable Energy Laboratory). It allows a minimal rotor speed control, which is applicable to large wind turbines such as the IEA 15 MW reference turbine. In this implementation, only Mode 1 of the generator torque control mode type has been considered. Controller information can be found in the ROSCO Controller setup file named DISCON.IN, which is specific for each turbine. These files are available open-source from the ROSCO repository for canonical (reference) turbines. The file CCONTROL_CSVDATA contains theses datas.
  * 'NONE': No operational control method applied. Constant values from CFARM_CSVDATA will be used. Intended for testing purposes only.

* :code:`CCONTROL_CSVDATA`: Data necessary for the turbine controller. Its definition varies as a function of the chosen control method:

  * 'TABLE': Meso-NH will expect four columns: Turbine Name, Velocity (in m/s), Rotational velocity (in rad/s) and Blade pitch angle (in rad). 
  Take care of the sign of the variables (use the same convention as in the CSV file data_farm.csv, described in namelist :code:`CFARM_CSVDATA` in :ref:`nam_eol_alm`.
  There can be as much lines as known operating points by the user, but it should be sorted in increasing velocity as the following example:

.. code-block::

   Turbine name, Velocity [m/s], Rotational vel [rad/s], Pitch [rad]
   NREL5MW,         3.0,              -0.734,             -0.00000 
   NREL5MW,         4.0,              -0.755,             -0.00000 
   ...,             ...,                 ...,             ... 
   NREL5MW,        19.8,              -1.266,             -0.299684

* :code:`CCONTROL_CSVDATA`

  * 'JONKM': the user must put the 17 parameters needed for this model in columns, and one line for each type of turbine. The columns are (again, take care of the units!):
 
.. csv-table::
   :header: "Parameter", "Units"
   :widths: 60, 40

   "Turbine name", ""
   "Filter frequency", "rad.s-1"
   "Drivetrain Inertia", "kg.m²"
   "Gearbox Ratio", ""
   "Gearbox efficiency", ""
   "Cut-in gen speed", "rad.s-1"
   "Region 2 start gen speed", "rad.s-1"
   "Region 2 start end speed", "rad.s-1"
   "Rated rotor speed", "rad.s-1"
   "Cut-in gen torque", "N.m"
   "Rated gen torque", "N.m"
   "Min blade pitch angle", "rad"
   "Max blade pitch angle", "rad"
   "Torque controller gain", ":math:`N.m/(rad.s^{-1})^2`"
   "Pitch controller global gain", ""
   "Pitch proportional gain", "s"
   "Pitch integral gain", ""

* :code:`CCONTROL_CSVDATA`

  * 'ROSCO': if a ROSCO-type controller is chosen, the user must put the 25 parameters needed for this model in columns, and one line for each type of turbine. The columns are described in the following table with the correspondence with DISCON.IN file generated with the ROSCO repository https://github.com/NREL/ROSCO.

.. csv-table::
   :header: "Parameter", "Units", ""
   :widths: 60, 20, 20

   "Turbine name", "", ""
   "Pitch to switch to rng 3", "rad", "" 
   "Rated Generator speed", "rad/s",  ":math:`VS_{RefSpd}`" 
   "Min. Generator speed Rng 2", "rad/s",  ":math:`VS_{MinOMSpd}`"
   "Generator torque constant in rng 2", ":math:`N.m/(rad.s^{-1})^2`",  ":math:`VS_{Rgn2K}` convert from :math:`Nm/rpm^2`"
   "Prop. Gain gen PI torque controller", "",  ":math:`VS_{KP}`"
   "Int. Gain gen PI torque controller", "s",  ":math:`VS_{KI}`"
   "Above Rated generator torque PI sat.", "Nm",  ":math:`VS_{ArSatTq}`"
   "Min generator torque", "Nm",  ":math:`VS_{MinTq}`"
   "Wind Turbine rated power", "W",  ":math:`VS_{RtPwr}`"
   "Generator efficiency", "%",  ":math:`VS_{GenEff}`"
   "Max. torque generator", "Nm",  ":math:`VS_{MaxTq}`"
   "Gearbox ratio", "",  ":math:`WE_{GearboxRatio}`"
   "Rotor inertia", "kg m²", ""
   "Corner freq. LPF", "rad/s",  ":math:`F_{LPFCornerFreq}`"
   "Damping coef.", "",  ":math:`F_{LPFDamping}`"
   "Prop. Gain pitch poly coeff. a", ":math:`s.rad^{-2}`",  "fit :math:`PC_{GS_{KP}}`"
   "Prop. Gain pitch poly coeff. B", "s/rad",  "fit :math:`PC_{GS_{KP}}`"
   "Prop. Gain pitch poly coeff. C", "s",  "fit :math:`PC_{GS_{KP}}`"
   "Int. Gain pitch poly coeff. a", ":math:`rad.s^{-2}`",  "fit :math:`PC_{GS_{KI}}`"
   "Int. Gain pitch poly coeff. B", ":math:`rad.s^{-1}`",  "fit :math:`PC_{GS_{KI}}`"
   "Int. Gain pitch poly coeff. C", "",  "fit :math:`PC_{GS_{KI}}`"
   "Pitch control generator Rated speed", ":math:`rad.s^{-1}`",  ":math:`PC_{RefSpd}`"
   "Max. Physical pitch", "rad",  ":math:`PC_{MaxPit}`"
   "File name table Min. Pitch Vs Rotor Torque", ".csv", ""

* :code:`XCON_AVG_PERIOD`: used if CMETH_OPS = 'TABLE'. Time period (in seconds) used for the averaging of the upstream wind.

* :code:`XCON_DIST_VEL`: used if CMETH_OPS = 'TABLE'. Distance (in meters) in the hub frame between the hub and the center of the virtual disk used to sample the velocity (positive is upstream, negative is downstream).  

* :code:`XCON_RAD_VEL`: used if CMETH_OPS = 'TABLE'. Radius (in meters) of the virtual disk used to sample velocity.