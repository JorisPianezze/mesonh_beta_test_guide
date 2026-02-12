.. _release_note_600:

MNH-V6-0-0
============================================================================

Release date : XX/XX/2026

.. contents::
   :local:
   :depth: 2

Running on GPU
---------------------------

Radiation scheme
---------------------------

Wind turbine - EOL 2.0.1
---------------------------
The wind turbine code is updated from EOL-1.0 to EOL-2.0.1. The main changes are 

&NAM_EOL
**********************************

.. csv-table:: NAM_EOL new keys
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "XKERNEL_RATIO","REAL","2."  
   "LCONTROL_EOL", "LOGICAL", ".FALSE." 
   "LNACELLE", "LOGICAL", ".FALSE." 
   "LTOWER", "LOGICAL", ".FALSE."
   "LDIA_EOL", "LOGICAL", ".TRUE."
   "LFLOAT_EOL", "LOGICAL", ".FALSE." 


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

* :code:`CSMEAR` : smearing method of the aerodynamic forces field. New entry:

  * '3DGA' : 3D gaussian kernel. Note that this can increase the computational cost of the simulation. This mode is only available for ALM and ADR (not ADNR).

&NAM_EOL_ALM
**********************************

:code:`NNB_BLAELT` is renamed :code:`NNB_RADELT` 

&NAM_EOL_CONTROL
**********************************
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


&NAM_EOL_TOWNAC
**********************************
Parametrization of the turbine's tower and nacelle. In the current implementation, the tower is represented by a cylinder with NNB_TOWELT sections and the nacelle by a disk of radius R\_r (defined in the data\_turbine.csv file). Drag forces are deduced from these geometrical shapes. 
The user can modify the modified drag coefficient. These drag forces are smeared the same way as the body forces of the blades.

.. csv-table:: NAM_EOL_TOWAC content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "NNB_TOWELT", "INTEGER", "84"       
   "XCD_NAC", "REAL", "0.68"
   "XCD_TOW", "REAL", "4.0"       

* :code:`NEMITTING_ROT`: number of rotor that emit tracers. We recommend to limit this number to the number of wind turbines for which the wake meandering will be studied. Having too many additional variables will reduce the code's performance.

* :code:`NNB_TOWELT`: number of elements to add a drag to the tower. We recommend having at least one element per cell size.

* :code:`XCD_NAC`: modified drag coefficient of the nacelle. 

* :code:`XCD_TOW`: modified drag coefficient of the tower.

.. _nam_eol_tracers:

&NAM_EOL_TRACERS
**********************************

.. csv-table:: NAM_EOL_TRACERS content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "NEMITTING_ROT", "INTEGER", "1"       
   "NNB_EMITTING_ROT", "INTEGER(:)", "(1,0,0,..)"
   "XTRAC_DIST", "REAL", "120"       
   "XTRAC_RAD", "REAL", "-60"      

* :code:`NEMITTING_ROT`: number of rotor that emit tracers. We recommend to limit this number to the number of wind turbines for which the wake meandering will be studied. Having too many additional variables will reduce the code's performance.

* :code:`NNB_EMITTING_ROT`: list of size NEMITTING_ROT which indicates the indices of tracked turbines. 

* :code:`XTRAC_DIST`: Distance (in meters) in the hub frame between the rotor hub and the centre of the emitting disk (positive is upstream, negative is downstream).

* :code:`XTRAC_RAD`: Radius (in meters) of the emitting disk.


I/O
---------------------------

ACLIB: Aerosols and Chemistry Library
---------------------------


PHYEX
---------------------------

Turbulence
**********************************

Schallow convection
**********************************

LIMA
**********************************

Ocean-Atmosphere-Wave coupling
---------------------------

Diagnostics
---------------------------

Passive pollutants
---------------------------
* :code:`LPASPOLDUST = FALSE`: emit dust aerosols 
* :code:`NMODEL_PP = 1`: model number where passive pollutants are emitted. 

Atmospheric coupling
---------------------------
* HRRR-WRF: Coupling with daily operational model HRRR is now possible. More info in :ref:`extracthrrr`

SURFEX
---------------------------

Cleaning
---------------------------

External libraries and tools
---------------------------
* ECCODES updated to 2.41