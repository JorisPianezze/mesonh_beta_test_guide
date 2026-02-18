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
The wind turbine code is updated from EOL-1.0 to EOL-2.0.1. The main changes are:
* New kinematic architecture with 6D harmonic floating motion;
* New controller architecture including now TABLE, JONKM, and ROSCO (new) methods;
* 3D Gaussian smearing method;
* Additional time series outputs and optimizations.

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

* :code:`LCONTROL_EOL` : true to use a controller to modify rotational speed and blade pitch angle during the run. Only for CMETH_EOL='ADR' or 'ALM'.

  * .TRUE.  activates the controller. More parameterizations are available in the EOL_CONTROL namelist.
  * .FALSE. the rotational speed and blade pitch angle are constant during the simulation (values imposed in CFARM_CSVDATA).

* :code:`LNACELLE` : true to model wind turbines nacelle. Only for CMETH_EOL='ADR' or 'ALM'.

  * .TRUE.  to simulate wind turbine nacelle.
  * .FALSE. to remove the nacelle body forces.

* :code:`LTOWER` : true to model wind turbines tower. Only for CMETH_EOL='ADR' or 'ALM'.

  * .TRUE.  to simulate wind turbine tower.
  * .FALSE. to remove the tower body forces.


* :code:`LDIA_EOL` : true to write SCADA-like variables in the diachronic file. Only for CMETH_EOL='ADR' or 'ALM'. See Sect. \ref{ss:variables_SCADA} for a list of available variables.

  * .TRUE.  write variables. They are written into subgroup 'Turbines', itself containing one subgroup for each turbine.
  * .FALSE. do not write variables.

* :code:`LFLOAT_EOL` : true to activate the floating motions and static positions. Only for CMETH_EOL='ADR' or 'ALM'.

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

Variables outputs
**********************************

List of output variables dedicated to :ref:`output_WindTurbine` are updated.

I/O
---------------------------

ACLIB: Aerosols and Chemistry Library
---------------------------


PHYEX
---------------------------

Turbulence
**********************************

.. csv-table:: NAM_TURBn new entries
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LGOGER","LOGICAL",".FALSE."
   "XSMAG","REAL","0.2"
   "LDYNMF","LOGICAL",".FALSE."
   "LTHERMMF","LOGICAL",".TRUE."
   "LBL89TOP","LOGICAL",".FALSE."
   "LBL89EXP","LOGICAL",".TRUE."

* :code:`LGOGER`: true to compute the Goger terms

* :code:`XSMAG`: dimensionless Smagorinsky constant

* :code:`LDYNMF`: true to take into account a dynamical TKE production from EDMF

* :code:`LTHERMMF`: true to take into account a buoyancy TKE production from EDMF

* :code:`LBL89TOP`: true to limit BL89/RM17 at PBL top (as in ARPEGE)

* :code:`LBL89EXP`: true to use the exposant from the BL89 paper ( which is LOG(16.)/(4.*LOG(XKARMAN)+LOG(XCED)-3.*LOG(XCMFS))). Otherwise 2./3. (False in AROME cycl 50t1)

Schallow convection
**********************************

.. csv-table:: NAM_PARAM_MFSHALLn new entries
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "CWET_MIXING","CHARACTER(LEN=4)","'PKFB'"
   "CKIC_COMPUTE","CHARACTER(LEN=4)","'KFB'"
   "CDETR_DRY_LUP","CHARACTER(LEN=4)","'SURF'"
   "LMIXTKE","LOGICAL",".FALSE."
   "XSIGMA_ENV","REAL","0"
   "LPZ_EXP_LOG","LOGICAL",".FALSE."
   "XBRIO","REAL","0"
   "XAADVEC","REAL","0"
   "LRELAX_ALPHA_MF","LOGICAL",".FALSE."


* :code:`CWET_MIXING`: type of env mixing for buoyancy sorting scheme. 'PKFB' for the original Pergaud code, 'LR01' for Lappen and Randall 2001

* :code:`CKIC_COMPUTE`: method to compute KIC: 'KFB' (PMMC09 original method, as in KFB). 'RS08' to use the Rooy and Siebesma (2008) formulation

* :code:`CDETR_DRY_LUP`: 'SURF' to use :math:`L_{UP}` at surface (PMMC09), 'UPDR' to compute :math:`L_{UP}` in updraft

* :code:`LMIXTKE`: true if mixing of TKE. Only implemented with :code:`CMF_UPDRAFT='EDKF'`

* :code:`XSIGMA_ENV`: coefficient for the environment sigma contribution in the bigaussian scheme

* :code:`LPZ_EXP_LOG`: true to use exp/log during dP/dZ conversion

* :code:`XBRIO`: coefficient to slow down :math:`w_{UP}` equation as in Rio 2010

* :code:`XAADVEC`: coefficient for advective pressure perturbation as in Jia he 2022

* :code:`LRELAX_ALPHA_MF`: true to relax the small fraction assumption


ICE3
**********************************

.. csv-table:: NAM_PARAM_ICEn new entries
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LKOGAN","LOGICAL",".FALSE."
   "LMODICEDEP","LOGICAL",".FALSE."
   "LEXCLDROP","LOGICAL",".FALSE."
   "LEXT_TEND","LOGICAL",".FALSE."

* :code:`LKOGAN`: true to use Kogan autocoversion of liquid

* :code:`LMODICEDEP`: flag for alternative deposition/evaporation of ice

* :code:`LEXCLDROP`: true to use of external cloud droplet (as from NRT aerosols)

* :code:`LEXT_TEND`: true to use external tendencies during the time-splitting

* :code:`CSUBG_MF_PDF`: new option 'BIGA'. Current available options are 'NONE' or 'TRIANGLE' (see :ref:`nam_param_icen`)


LIMA
**********************************

.. csv-table:: NAM_PARAM_LIMA new entries
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LICE3","LOGICAL",".FALSE."
   "LSIGMOIDE_G","LOGICAL",".FALSE."
   "LSIGMOIDE_NG","LOGICAL",".FALSE."
   "XSIGMOIDE_G","LOGICAL","1E8"
   "XMVDMIN_G","LOGICAL","125E-6"
   "LCRIAUTI","LOGICAL",".FALSE."
   "XPSH_MAX_RDSF", "REAL", "0.2"
   "XT0CRIAUTI","LOGICAL","(LOG10(XCRIAUTI)-XBCRIAUTI)/0.06"
   "XCRIAUTI","REAL","0.2E-4"
   "XCRIAUTC","REAL","0.5E-3"
   "XACRIAUTI","REAL","0.06"
   "XBCRIAUTI","REAL","-3.5"
   "CSUBG_PR_PDF","CHARACTER(LEN=4)","'SIGM'"
   "CSUBG_AUCV_RC","CHARACTER(LEN=4)","'NONE'"
   "CSUBG_AUCV_RI","CHARACTER(LEN=4)","'NONE'"
   "LCRYSTAL_SHAPE","LOGICAL",".FALSE."
   "NNB_CRYSTAL_SHAPE", "INTEGER", "1"
   "HTYPE_CRYSTAL", "CHARACTER(LEN=4)(:)","NNB_CRYSTAL_SHAPE * ''"
   "LICE_ISC", "LOGICAL", ".FALSE."
   "LINITORILAM", "LOGICAL", ".FALSE."
   "LINTERP_CAMS", "LOGICAL", ".FALSE."

* :code:`LICE3`: Use to mimic the ICE3 scheme. If set to .TRUE., some parameters are set :

::
  
  NMOM_C=1  
  NMOM_R=1  
  NMOM_I=1
  NMOM_S=1
  NMOM_G=1
  NMOM_H=MIN(NMOM_H,1)
  NMOD_CCN=0
  NMOD_IFN=0
  LMURAKAMI=.TRUE.
  LKESSLERAC=.TRUE.
  XALPHAR=1.
  XNUR=1.

* :code:`LSIGMOIDE_G`: true to limit graupel growth by XSIGMOIDE_G

* :code:`XSIGMOIDE_G`: sigmoide parameter for graupel growth limitation

* :code:`LSIGMOIDE_NG`: true to force lambda to be < lambda(Dmin)

* :code:`XMVDMIN_G`: minimum MVD for graupel growth lim or lambda(Dmin) calculation

* :code:`LCRIAUTI`: true to compute XACRIAUTI and XBCRIAUTI (from XCRIAUTI and XT0CRIAUTI). If false, XT0CRIAUTI is computed from XCRIAUTI and XBCRIAUTI.

* :code:`XPSH_MAX_RDSF`: shattering probability normal distribution maximum

* :code:`XT0CRIAUTI`: threshold temperature for the ice->snow autoconversion threshold

* :code:`XCRIAUTI`: ?

* :code:`XACRIAUTI`: ?

* :code:`XBCRIAUTI`: ?

* :code:`CSUBG_PR_PDF`: PDF for subgrid precipitation. Options are the same as in :ref:`nam_param_icen`.

* :code:`CSUBG_AUCV_RC`: type of subgrid rc->rr autoconversion method. Options are the same as in :ref:`nam_param_icen`.

* :code:`CSUBG_AUCV_RI`: type of subgrid ri->rs autoconversion method. Options are the same as in :ref:`nam_param_icen`.

* :code:`LCRYSTAL_SHAPE`: true to enable several ice crystal shapes. It can only be used if :code:`LPTSPLIT=T`.

* :code:`NNB_CRYSTAL_SHAPE`: number of ice crystal shapes ; taken into account if :code:`LCRYSTAL_SHAPE=T`. For the moment, only 4 ice crystal shapes are allowed.

* :code:`HTYPE_CRYSTAL_SHAPE`: ice crystal shapes if :code:`LCRYSTAL_SHAPE=T`. Can be set to YPLA, YCOL, YBUR or YDRO.

* :code:`LICE_ISC`: true to enable self collection of ice crystals

* :code:`LINITORILAM`: true to initialize CCN and IF by ORILAM

* :code:`LINTERP_CAMS`: true to interpolate CAMS data at each time step (from Large-Scale fields)


Condensation
**********************************

.. csv-table:: NAM_NEBn new entry
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LCONDBORN","LOGICAL",".FALSE."

* :code:`LCONDBORN` : true to limit condensation

Ocean-Atmosphere-Wave coupling
---------------------------

Diagnostics
---------------------------

Passive pollutants
---------------------------
* :code:`LPASPOLDUST = FALSE`: emit dust aerosols 
* :code:`NMODEL_PP = 1`: model number where passive pollutants are emitted. 

WRF and ICON init and forcing
---------------------------
* HRRR-WRF: Initializing and forcing Méso-NH with daily operational model HRRR is now possible. More info in :ref:`extracthrrr`

SURFEX
---------------------------

Cleaning
---------------------------

External libraries and tools
---------------------------
* ECCODES updated to 2.41