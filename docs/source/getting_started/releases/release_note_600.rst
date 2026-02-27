.. _release_note_600:

MNH-V6-0-0
============================================================================

Release date : XX/XX/2026

.. contents::
   :local:
   :depth: 2

Running on GPU
----------------------------------------------------------------------------

Radiation scheme - ECRAD 1.6.1
----------------------------------------------------------------------------

ECRAD is now compiled by default. All namelist keys available in ECRAD-offline is now available with Méso-NH (see the `reference ECMWF documentation <https://confluence.ecmwf.int/download/attachments/70945505/ecrad_documentation.pdf?version=5&modificationDate=1655480733414&api=v2>`_)

.. note::

   To use ECRAD, you still must link data files found at $SRC_MESONH/src/LIB/RAD/ecrad-1.6.1/data/ in the folder of the simulation (MESONH step).

.. csv-table:: NAM_PARAM_ECRADn new entries
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "CDATADIR", "CHARACTER(LEN=511)", "."
   "LDO_SW", "LOGICAL", ".TRUE."
   "LDO_LW", "LOGICAL", ".TRUE."
   "LDO_SW_DIRECT", "LOGICAL", ".TRUE."
   "LDO_CLEAR", "LOGICAL", ".TRUE."
   "LDO_CLOUD_AEROSOL_PER_SW_G_POINT", "LOGICAL", ".TRUE."
   "LDO_CLOUD_AEROSOL_PER_LW_G_POINT", "LOGICAL", ".TRUE."
   "CGAS_MODEL_NAME", "CHARACTER(LEN=63)", "RRTMG-IFS"
   "CGAS_OPTICS_SW_OVERRIDE_FILE_NAME", "CHARACTER(LEN=511)", ""
   "CGAS_OPTICS_LW_OVERRIDE_FILE_NAME", "CHARACTER(LEN=511)", ""
   "LUSE_AEROSOLS", "LOGICAL", ".FALSE."
   "LUSE_GENERAL_AEROSOL_OPTICS", "LOGICAL", ".FALSE."
   "LDO_LW_AEROSOL_SCATTERING", "LOGICAL", ".FALSE."
   "NAEROSOL_TYPES", "INTEGER", "6"
   "NI_AEROSOL_TYPE_MAP", "INTEGER(NMAXAEROSOLTYPES)", "(1,2,3,4,5,6/)"
   "CAEROSOL_OPTICS_OVERRIDE_FILE_NAME", "CHARACTER(LEN=511)", "aerosol_ifs_rrtm_tegen.nc"
   "CLIQUID_MODEL_NAME", "CHARACTER(LEN=63)", "SOCRATES"
   "CICE_MODEL_NAME", "CHARACTER(LEN=63)", "Fu-IFS"
   "LUSE_GENERAL_CLOUD_OPTICS", "LOGICAL", ".TRUE."
   "LDO_LW_CLOUD_SCATTERING", "LOGICAL", ".TRUE."
   "CIQ_OPTICS_OVERRIDE_FILE_NAME", "CHARACTER(LEN=511)", ""
   "CICE_OPTICS_OVERRIDE_FILE_NAME", "CHARACTER(LEN=511)", ""
   "CCLOUD_TYPE_NAME", "CHARACTER(LEN=511)(:)", "mie_droplet"
   "LUSE_THICK_CLOUD_SPECTRAL_AVERAGING(:)", "LOGICAL", ".TRUE."
   "CSW_SOLVER_NAME", "CHARACTER(LEN=63)", "Tripleclouds"
   "CLW_SOLVER_NAME", "CHARACTER(LEN=63)", "Tripleclouds"
   "COVERLAP_SCHEME_NAME", "CHARACTER(LEN=63)", "Exp-Ran"
   "LUSE_BETA_OVERLAP", "LOGICAL", ".FALSE."
   "XCLOUD_INHOM_DECORR_SCALING", "REAL", "1.0"
   "XCLOUD_FRACTION_THRESHOLD", "REAL", "1.0E-6"
   "XCLOUD_MIXING_RATIO_THRESHOLD", "REAL", "1.0E-9"
   "CCLOUD_PDF_SHAPE_NAME", "CHARACTER(LEN=63)", "Gamma"
   "CCLOUD_PDF_OVERRIDE_FILE_NAME", "CHARACTER(LEN=511)", ""
   "LDO_SW_DELTA_SCALING_WITH_GASES", "LOGICAL", ".FALSE."
   "LDO_3D_EFFECTS", "LOGICAL", ".TRUE."
   "LDO_LW_SIDE_EMISSIVITY", "LOGICAL", ".TRUE."
   "CSW_ENTRAPMENT_NAME", "CHARACTER(LEN=63)", "Explicit"
   "LDO_3D_LW_MULTILAYER_EFFECTS", "LOGICAL", ".FALSE."
   "XMAX_3D_TRANSFER_RATE", "REAL", "10.0"
   "XMAX_GAS_OD_3D", "REAL", "8.0"
   "XMAX_CLOUD_OD", "REAL", "16.0"
   "LUSE_EXPM_EVERYWHERE", "LOGICAL", ".FALSE."
   "XCLEAR_TO_THICK_FRACTION", "REAL", "0.0"
   "XOVERHEAD_SUN_FACTOR", "REAL", "0.0"
   "XOVERHANG_FACTOR", "REAL", "0.0"
   "LDO_NEAREST_SPECTRAL_SW_ALBEDO", "LOGICAL", ".FALSE."
   "LDO_NEAREST_SPECTRAL_LW_EMISS", "LOGICAL", ".FALSE."
   "XSW_ALBEDO_WAVELENGTH_BOUND", "REAL(:)", "-10"
   "XLW_EMISS_WAVELENGTH_BOUND", "REAL(:)", "-10"
   "ISW_ALBEDO_INDEX", "INTEGER(:)", "0"
   "ILW_EMISS_INDEX", "INTEGER(:)", "0"
   "LDO_WEIGHTED_SURFACE_MAPPING", "LOGICAL", ".TRUE."
   "IVERBOSESETUP", "INTEGER", "3"
   "IVERBOSE", "INTEGER", "1"
   "LDO_SAVE_SPECTRAL_FLUX", "LOGICAL", ".FALSE."
   "LDO_SAVE_GPOINT_FLUX", "LOGICAL", ".FALSE."
   "LDO_SAVE_RADIATIVE_PROPERTIES", "LOGICAL", ".FALSE."


* :code:`CDATADIR`: Directory containing NetCDF data files

* :code:`LDO_SW`: flag to compute shortwave fluxes

* :code:`LDO_LW`: flag to compute longwave fluxes

* :code:`LDO_SW_DIRECT`: flag to compute direct shortwave fluxes

* :code:`LDO_CLEAR`: flag to ompute clear-sky fluxes

* :code:`LDO_CLOUD_AEROSOL_PER_SW_G_POINT`: flag to ompute cloud, aerosol and surface shortwave optical properties per g-point

* :code:`LDO_CLOUD_AEROSOL_PER_LW_G_POINT`: flag to compute cloud, aerosol and surface longwave optical properties per g-point

* :code:`CGAS_MODEL_NAME`: Gas optics model: 'RRTMG-IFS', 'ECCKD' or 'Monochromatic'.

* :code:`CGAS_OPTICS_SW_OVERRIDE_FILE_NAME`: Path to alternative shortwave ecCKD gas optics file

* :code:`CGAS_OPTICS_LW_OVERRIDE_FILE_NAME`: Path to alternative longwave ecCKD gas optics file

* :code:`LUSE_AEROSOLS`: flag to represent aerosols

* :code:`LUSE_GENERAL_AEROSOL_OPTICS`: Support arbitrary spectral discretization for aerosols (not just RRTMG)

* :code:`LDO_LW_AEROSOL_SCATTERING`: Include longwave aerosol scattering?

* :code:`NAEROSOL_TYPES`: Number of aerosol types

* :code:`NI_AEROSOL_TYPE_MAP(:)`: Mapping from input aerosol types to aerosol optics NetCDF file. By default the mapping is 1: Continental background, 2: Maritime, 3: Desert, 4: Urban, 5: Volcanic active, 6: Stratospheric background. Positive integers indexe hydrophobic types, negative integers index hydrophilic types and zero indicates a type should be ignored

* :code:`CAEROSOL_OPTICS_OVERRIDE_FILE_NAME`: Path to alternative aerosol optics file

* :code:`CLIQUID_MODEL_NAME`: Liquid optics model: 'SOCRATES', 'Slingo' (1989) or 'Monochromatic'

* :code:`CICE_MODEL_NAME`: Ice optics model: 'Fu-IFS', 'Baran2016', 'Yi' or 'Monochromatic'. From Fu(1996), Fu et al. (1998), Baran et al. (2016) and Yi et al. (2013)

* :code:`LUSE_GENERAL_CLOUD_OPTICS`: Support arbitrary hydrometeor types?

* :code:`LDO_LW_CLOUD_SCATTERING`: Include longwave cloud scattering?

* :code:`CLIQ_OPTICS_OVERRIDE_FILE_NAME`: Alternative liquid optics file name

* :code:`CICE_OPTICS_OVERRIDE_FILE_NAME`: Alternative ice optics file name

* :code:`CCLOUD_TYPE_NAME(:)`: Optical property model name for each generalized hydrometeor species: 'mie_droplet', 'baum-general-habit-mixture_ice'

* :code:`LUSE_THICK_CLOUD_SPECTRAL_AVERAGING(:)`: Use thick spectral averaging?

* :code:`CSW_SOLVER_NAME`: Shortwave solver. 'Cloudless', 'Homogeneous', 'McICA', 'Tripleclouds', 'SPARTACUS'. Note that the homogeneous solver assumes cloud fills the gridbox horizontally (so ignores cloud fraction) while the cloudless solver ignores clouds completely

* :code:`CLW_SOLVER_NAME`: Longwave solver: 'Cloudless', 'Homogeneous', 'McICA', 'Tripleclouds' or 'SPARTACUS'

* :code:`COVERLAP_SCHEME_NAME`: Cloud overlap scheme: 'Max-Ran', 'Exp-Ran', 'Exp-Exp' Note that SPARTACUS and Tripleclouds only work with the Exp-Ran overlap scheme

* :code:`LUSE_BETA_OVERLAP`: Use Shonk et al . 2010  :math:`\beta` overlap parameter definition, rather than the default :math:`\alpha`

* :code:`XCLOUD_INHOM_DECORR_SCALING`: Ratio of overlap decorrelation lengths for cloud inhomogeneities and boundaries

* :code:`XCLOUD_FRACTION_THRESHOLD`: Ignore clouds with fraction below this. Set to 2.5e-5 if COVERLAP_SCHEME_NAME='Exp-Ran'

* :code:`XCLOUD_MIXING_RATIO_THRESHOLD`: Ignore clouds with total mixing ratio below this

* :code:`CCLOUD_PDF_SHAPE_NAME`: Cloud water PDF shape: 'Gamma' or 'Lognormal'

* :code:`CCLOUD_PDF_OVERRIDE_FILE_NAME`: Name of NetCDF file of alternative cloud PDF look-up table

* :code:`LDO_SW_DELTA_SCALING_WITH_GASES`: Apply delta-Eddington scaling to particle-gas mixture, rather than particles only (see Hogan and Bozzo, 2018)

* :code:`LDO_3D_EFFECTS`: Represent cloud edge effects when SPARTACUS solver selected; note that this option does not affect entrapment, which is also a 3D effect

* :code:`LDO_LW_SIDE_EMISSIVITY`: Represent effective emissivity of the side of clouds (Schafer et al., 2016)

* :code:`CSW_ENTRAPMENT_NAME`: Entrapment model (Hogan et al. 2019): 'Zero', 'Edge-only', 'Explicit', 'Non-fractal' or 'Maximum'.   

* :code:`LDO_3D_LW_MULTILAYER_EFFECTS`: Maximum entrapment for longwave radiation?

* :code:`XMAX_3D_TRANSFER_RATE`: Maximum rate of lateral exchange between regions in one layer, for stability of matrix exponential (where the default means that as little as e−10 of the radiation could remain in a region)

* :code:`XMAX_GAS_OD_3D`: 3D effects ignored for spectral intervals where gas optical depth of a layer exceeds this, for stability

* :code:`XMAX_CLOUD_OD`: Maximum in-cloud optical depth, for stability

* :code:`LUSE_EXPM_EVERYWHERE`: Use matrix-exponential method even when 3D effects not important, such as clear-sky layers and parts of the spectrum where the gas optical depth is large?

* :code:`XCLEAR_TO_THICK_FRACTION`: Fraction of cloud edge interfacing directly to the most optically thick cloudy region

* :code:`XOVERHEAD_SUN_FACTOR`: Minimum tan-squared of solar zenith angle to allow some ‘direct’ radiation from overhead sun to pass through cloud sides (0.06 used by Hogan et al., 2016)

* :code:`XOVERHANG_FACTOR`: A detail of the entrapment representation described by Hogan et al. (2019)

* :code:`LDO_NEAREST_SPECTRAL_SW_ALBEDO`: Surface shortwave albedos may be supplied in their own spectral intervals: do we select the nearest to each band of the gas optics scheme, rather than using a weighted average?

* :code:`LDO_NEAREST_SPECTRAL_LW_EMISS`: same as :code:`LDO_NEAREST_SPECTRAL_SW_ALBEDO` for longwave emissivity

* :code:`XSW_ALBEDO_WAVELENGTH_BOUND(:)`: Vector of the wavelength bounds (m) delimiting the shortwave albedo intervals

* :code:`XLW_EMISS_WAVELENGTH_BOUND(:)`: Vector of the wavelength bounds (m) delimiting the longwave emissivity intervals

* :code:`ISW_ALBEDO_INDEX(:)`: Vector of indices mapping albedos to wavelength intervals

* :code:`ILW_EMISS_INDEX(:)`: Vector of indices mapping emissivities to wavelength intervals

* :code:`LDO_WEIGHTED_SURFACE_MAPPING`: Planck-weighted surface mapping?

* :code:`IVERBOSESETUP`: Setup verbosity level. 1=warning, 2=info, 3=progress, 4=detailed, 5=debug

* :code:`IVERBOSE`: Execution verbosity level

* :code:`LDO_SAVE_SPECTRAL_FLUX`: Save flux profiles in each band

* :code:`LDO_SAVE_GPOINT_FLUX`: Save flux profiles in each g-point

* :code:`LDO_SAVE_RADIATIVE_PROPERTIES`: Write intermediate NetCDF file(s) of properties sent to solver (radiative_properties*.nc)?


The following namelists are renamed or replaced:

* :code:`NSWSOLVER` is replaced by  :code:`CSW_SOLVER_NAME`

* :code:`NLWSOLVER` is replaced by  :code:`CLW_SOLVER_NAME`

* :code:`NLIQOPT` is replaced by :code:`CLIQUID_MODEL_NAME`

* :code:`NICEOPT` is replaced by :code:`CICE_MODEL_NAME`

* :code:`NOVLP` is replaced by  :code:`COVERLAP_SCHEME_NAME`

* :code:`NLWSCATTERING` is replaced by :code:`LDO_LW_AEROSOL_SCATTERING` and :code:`LDO_LW_CLOUD_SCATTERING`

* :code:`NAERMACC` is replaced by :code:`NAEROSOL_TYPES`


Wind turbine - EOL 2.0.1
----------------------------------------------------------------------------
The wind turbine code is updated from EOL-1.0 to EOL-2.0.1. The main changes are:
* New kinematic architecture with 6D harmonic floating motion;
* New controller architecture including now TABLE, JONKM, and ROSCO (new) methods;
* 3D Gaussian smearing method;
* Additional time series outputs and optimizations.

&NAM_EOL
****************************************************************************

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
****************************************************************************

:code:`NNB_BLAELT` is renamed :code:`NNB_RADELT` 

&NAM_EOL_CONTROL
****************************************************************************
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
****************************************************************************
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
****************************************************************************

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
****************************************************************************

List of output variables dedicated to :ref:`output_WindTurbine` are updated.


I/O
----------------------------------------------------------------------------

Group :file:`/SURFEX`
****************************************************************************

In the netCDF files, the majority of the fields related to SURFEX are now stored in a group named :file:`/SURFEX`.
The exceptions are grid coordinates, grid dimensions and some orographic fields.
A group can be seen as a folder in which several fields can be stored.
This allows to better organize the content of the file and to avoid name conflicts with other fields (there was some collisions).
The group :file:`/SURFEX` is created at the root of the file.


Compression enabled by default
****************************************************************************

Compression is now enabled by default for all written netCDF files.

As a reminder, compression for all files is enabled or disabled via the ``LIO_COMPRESS`` parameter in the ``&NAM_CONFIO`` namelist.

**Note:** if ``LIO_COMPRESS = .TRUE.``, the parameters ``LIO_COMPRESS_ALGO`` and ``LIO_COMPRESS_LEVEL`` take precedence over those in the ``NAM_BACKUP`` and ``NAM_OUTPUT`` namelists (however, no impact if compression is imposed per variable in the outputs).


Zstandard (zstd) compression
****************************************************************************

The Zstandard compression library (zstd) is now available as a compression algorithm for netCDF files.
It is the default compression algorithm for all floating-point variables if compression is activated.
If the variable type is different (other than floating-point numbers, e.g., integers), it is automatically forced to DEFLATE (zlib).

Description
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Zstandard is a lossless library. It is open-source and developed by Facebook.
It is widely used and is supported by many tools and libraries (e.g., Python...).
It provides a better compression ratio than zlib/DEFLATE and is much faster for both compression and decompression.

More information about zstd can be found on the following links:

- `GitHub - facebook/zstd <https://github.com/facebook/zstd/>`_
- `Zstandard Documentation <https://facebook.github.io/zstd/>`_
- A manual is aloso available in the sources


Constraints
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

- Not available everywhere (especially the development part). Therefore, it is bundled with Meso-NH.
- Not hardcoded in HDF5 but is used as a plugin. Therefore, it is necessary to set the ``HDF5_PLUGIN_PATH`` environment variable. This variable is automatically set when loading the Meso-NH environment (:file:`profile-*` files)
- Need to provide the plugin sources (outside of HDF5)
- Not necessarily supported/compiled in all NetCDF tools (but is present for NetCDF with recent Python)
- Only works for floating-point numbers


Namelists
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

- ``&NAM_CONFIO``: ``CIO_COMPRESS_ALGO = 'ZSTD'`` (overrides ``CBAK/COUT_COMPRESS_ALGO`` if ``LIO_COMPRESS=T``)
- ``&NAM_BACKUP``: ``CBAK_COMPRESS_ALGO(m) = 'ZSTD'``
- ``&NAM_OUTPUT``: ``COUT_COMPRESS_ALGO(m) = 'ZSTD'``

Allowed values: ``ZSTD``, ``DEFLATE``, or ``NONE``.

- By default, the compression algorithm is ``ZSTD`` (instead of ``DEFLATE`` previously).
- For non-floating-point numbers, if compression is activated and set to ``ZSTD``, it is automatically forced to ``DEFLATE``.
- Compression algorithm per model (not possible per variable or per box) (possible in theory, but the interest seems negligible).
- If the algorithm is forced to ``NONE``, compression is disabled, including lossy compression.
- Allowed compression levels: -99 to 22.

Performance
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

Example:

- Modified test case 004_Reunion (resolution x4: 288x320x50)
- 5 3D fields in real64 in outputs: UT, VT, WT, THT, PABST
- 10 time steps with 10 backups and 10 outputs
- Runs on a standard PC
- gfortran 14.2.0, compiled with -O2.

.. csv-table:: Performance Comparison
   :header: "#processes", "Compression Algorithm", "Compression Level", "I/O Time", "Total Time", "File Size"
   :widths: 10, 20, 15, 15, 15, 15

   1,None,,40.9 s,405.6 s,9.8 GiB
   1,Deflate,4,150.8 s,514.3 s,3.6 GiB
   1,Zstd,4,32.3 s,399.0 s,3.6 GiB
   1,Zstd,22,1084.5 s,1465.8 s,3.5 GiB
   4,None,,41.6 s,293.2 s,9.8 GiB
   4,Deflate,4,152.8 s,406.6 s,3.6 GiB
   4,Zstd,-4,37.6 s,294.4 s,3.6 GiB
   4,Zstd,4,40.8 s,292.4 s,3.6 GiB
   4,Zstd,22,1059.4 s,1387.9 s,3.5 GiB

Conclusions:

- zlib/DEFLATE is expensive
- Zstd is much faster than zlib
- Zstd compresses as well as zlib
- A very high compression level is costly in CPU but does not provide significant disk space gains (in this case, at least)
- Zstd can be faster than no compression (compression faster than writing to disk)


Removal of LFI support (in writing)
****************************************************************************

Files in LFI format are no longer supported for writing (but still supported for reading).


Storage of Meso-NH version numbers
****************************************************************************

Meso-NH version numbers are no longer stored in fields but in netCDF attributes.

- Removed fields:

  - ``MNHVERSION``
  - ``MASDEV``
  - ``BUGFIX``
  - ``BIBUSER``

- Added attributes:

  - ``MNH_VERSION`` (array of 3 integers)
  - ``MNH_VERSION_STR``: Version in text format (e.g., "6.0.0" or "6.0.0 myversion")
  - ``MNH_VERSION_USER``: Only if ``CBIBUSER`` is not empty


Other changes
****************************************************************************

- CF Conventions

  - Updated to version 1.12 (from 1.10)
  - Added quantization variables (``quantization_info_*``) that provide characteristics of lossy compression and quantization
  - Added quantization attributes and ``quantization_nsb/nsd`` required by CF 1.12 conventions for variables reduced with this approach

- Removal of backward compatibility for files of versions of Meso-NH < 5


ACLIB: Aerosols and Chemistry Library
----------------------------------------------------------------------------

ACLIB (Aerosols and Chemistry LIBrary) is an external repository which contains the aerosols and chemistry core codes from Méso-NH, MOCAGE and ARPEGE/IFS. 
The main objective of building such library is exposing a single interface to access every existing routines at the CNRM relating to aerosols physics 
and chemistry. The aerosols and chemistry code of MOCAGE and ARPEGE/IFS are now available in Méso-NH (and vice-versa). ACLIB is also plugged into AROME.

The library comes with a new way to set-up parameters with aerosols and gas species: it uses tables in a :file:`.csv`` format which makes easier to define each 
parameter for individual aerosols more easily than re-compiling the code (i.e. modd_dust.f90 to change parameters of the log-normal distribution).
Pre-defined configurations of these tables are provided by each host-models in order to ease the use of their own schemes in different host models.

.. note::

   In Méso-NH, the code of ARPEGE and MOCAGE is now available but have not been adapted nor tested yet. 
   Using these codes needs scientific adaptation with Méso-NH objects and can be done with a scientific coordination of ACLIB team (ACLIB referee for Méso-NH: quentin.rodier@meteo.fr)

Tree structure
****************************************************************************
The ACLIB sources can be found here:

   .. treeview::
   
      - :dir:`folder` |MNH_directory_extract_current|/src/ACLIB
      
        - :dir:`folder` aer

          - :dir:`folder` scav
          - :dir:`folder` sedim
          - :dir:`folder` suflux
          - :dir:`folder` transfo
          - :dir:`folder` diag
          
        - :dir:`folder` chem
        - :dir:`folder` aux

* aer: main interface :file:`aer_aclib.f90`, main initialization of aerosols propreties from the csv data :file:`init_aer_aclib.f90` and definition of the 
  variables in :file:`modd_param_aer_aclib.f90`
* aer/scav: scavenging codes of all models, including Méso-NH ones (e.g. :file:`aer_wet_dep_kmt_warm.f90`)
* aer/sedim: sedimentation codes of all models, including Méso-NH ones (e.g. :file:`sedim_dslt.f90`)
* aer/suflux: dry deposition and emission of other models than SURFEX. For Méso-NH, it is still through SURFEX.
* aer/transfo: secondary transformations of aerosols corresponding to ORILAM scheme in Méso-NH (:file:`ch_orilam.f90`)
* aer/diag: diagnostics: not pluggd to Méso-NH
* chem: main interface :file:`chem_aclib.f90` with all main chemistry code and solvers. For Méso-NH, :file:`BASIC.f90`, the main :file:`ch_*.f90` routines 
  and :file:`ch_aer_*.f90` routines for ORILAM scheme. MOCAGE solvers are :file:`mocage_*.f90` routines and ARPEGE ones are :file:`acch_*.f90`
* aux: auxilliary routines that are not used only in one specific folder but necessary to compile each codes in all host models.



Interfaces and implementation in Méso-NH
****************************************************************************

Aerosols
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

   .. treeview::
   
      - :dir:`folder` |MNH_directory_extract_current|/src/MNH
      
        - :dir:`file` ini_modeln.f90

          - CALL INIT_AER_ACLIB: init of aerosols properties and read of csv data
        
        - :dir:`file` modeln.f90
            
            - CALL AER_ACLIB 
      - :dir:`folder` |MNH_directory_extract_current|/src/ACLIB/aer/aer_aclib.f90

               - CALL AER_ACLIB_EMIS
               - CALL AER_ACLIB_DRYDEP
               - CALL AER_ACLIB_SEDIM
               - CALL AER_ACLIB_SCAV
               - CALL AER_ACLIB_TRANSFO
               - CALL AER_ACLIB_DIAGS


**Sedimentation**

   .. treeview::
   
      - :dir:`folder` |MNH_directory_extract_current|/src/ACLIB/aer/sedim
      
        - :dir:`file` aer_aclib_sedim.f90

          - CALL SEDIM: sedimentation in MOCAGE
          - CALL TACTIC_SEDIMNT: sedimentation in ARPEGE
          - CALL SEDIM_DSLT: sedimentation in Méso-NH for DUST and SALT
          - CALL CH_AER_SEDIM_n: sedimentation in Méso-NH for aerosols of ORILAM

.. note::

   The routines of sedimentation from dust and salt are merged from MNH-V6-0-0

**Scavenging**

   .. treeview::
   
      - :dir:`folder` |MNH_directory_extract_current|/src/ACLIB/aer/scav
      
        - :dir:`file` aer_aclib_scav.f90

          - CALL WETSCAV: scavenging in MOCAGE
          - CALL TACTIC_SCAV: sedimscavengingentation in ARPEGE
          - CALL AER_WET_DEP_KMT_WARM: scavenging in Méso-NH for DUST and SALT

.. note::

   The routines of scavenging of ORILAM aerosols are not in ACLIB.

**Transformations (secondary in-organic aerosols)**

   .. treeview::
   
      - :dir:`folder` |MNH_directory_extract_current|/src/ACLIB/aer/transfo
      
        - :dir:`file` aer_aclib_transfo.f90

          - CALL MOCAERO: MOCAGE transfo
          - CALL TACTIC_CGROWTH, _SO2SO4, _NO3NH4 : ARPEGE transfo
          - CALL CH_ORILAM: Méso-NH ORILAM

The routine of ORILAM-Méso-NH are not in ACLIB/aer/transfo but in ACLIB/chem because it can not be used without the chemistry module


Aerosols of ORILAM
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

The sedimentation, scavenging and dry deposition of ORILAM aerosols have been externalized from the chemistry, it is now in a new routine
:file:`ch_aer_ext_orilam.f90`:

   .. treeview::
   
      - :dir:`folder` |MNH_directory_extract_current|/src/MNH
        
        - :dir:`file` modeln.f90
            
            - CALL CH_AER_EXT_ORILAM 

               - CALL MNH_TO_AER_ACLIB
            
                  - CALL AER_ACLIB
            
                     - CALL CH_AER_SEDIM_n

               - CALL CH_AER_WET_DEP_n
               - CALL CH_AER_DEPOS

Chemistry solver
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

For the chemistry solver, a new interface :file:`chem_aclib.f90` contains the call to the chemistry monitors:

   .. treeview::
   
      - :dir:`folder` |MNH_directory_extract_current|/src/MNH
      
        - :dir:`file` modeln.f90

          - CALL INIT_CHEM_MODEL: init of other chemistries
          - CALL MNH_TO_CHEM_ACLIB
            
            - CALL CHEM_ACLIB 
      - :dir:`file` |MNH_directory_extract_current|/src/ACLIB/chem/chem_aclib.f90

               - CALL CH_MONITOR_n: Méso-NH chemistry monitor
               - CALL CHEM_SUGAR: MOCAGE monitor
               - CALL ACCHEM: ARPEGE monitor

Note that the init of Méso-NH chemistry is not yet moved to init_chem_model.
               
.. note::

   In the interfaces CHEM_ACLIB and MNH_TO_CHEM_ACLIB, the arguments are written with explicit dimensions because Méso-NH and MOCAGE are using 2 dimensions for
   latitudes and longitudes whereas ARPEGE uses only 1 dimension (lat/lon are packed). The pack/unpack operations are done correctly at the execution if the arrays are contiguous.

The use of the extra interface MNH_TO_CHEM_ACLIB is necessary for diagnostics allocated with different dimensions regarding the host model.

ACLIB custom types
****************************************************************************

To ease the use of ACLIB in each host models, new custom types have been created:

* for individual aerosols and gas species, :code:`YCHEMS` and :code:`YAEROSOLS` regroup the definition of each individual chemical species and aerosols.

* for general parameters for aerosols and chemistry schemes :code:`YPAER_ACLIB` and :code:`YPCHEM_ACLIB` are defined.

* for diagnostics, :code:`YAEROUT_ACLIB` and :code:`YCHEMOUT_ACLIB` are defined (not yet used in Meso-NH).

* for general constants used in ACLIB, :code:`CST_ACLIB` is defined. 

.. csv-table:: ACLIB objects
   :header: "Object name", "Definition", "Initialization", "Data source"
   :widths: 25, 25, 25, 25

   "YCHEMS","chem/modd_param_chem_aclib.f90","chem/init_chem_aclib.f90", "Table_chem_species_aclibn.csv (`example <https://src.koda.cnrs.fr/mesonh/mesonh-code/-/blob/MNH-60-branch/examples/test_cases/012_dust/003_run/Table_aer_general_aclib1.csv?ref_type=heads>`_)"
   "YPCHEM_ACLIB","chem/modd_param_chem_aclib.f90","chem/init_chem_aclib.f90", "Table_chem_general_aclibn.csv (`example <https://src.koda.cnrs.fr/mesonh/mesonh-code/-/blob/MNH-60-branch/examples/test_cases/012_dust/003_run/Table_aer_species_aclib1.csv?ref_type=heads>`_)"
   "YAEROSOLS","aer/modd_param_aer_aclib.f90","aer/init_aer_aclib.f90", "Table_aer_species_aclibn.csv (`example <https://src.koda.cnrs.fr/mesonh/mesonh-code/-/blob/MNH-60-branch/examples/test_cases/011_KW78CHEM/002_mesonh/Table_chem_general_aclib1.csv?ref_type=heads>`_)"
   "YPAER_ACLIB","aer/modd_param_aer_aclib.f90","aer/init_aer_aclib.f90", "Table_aer_species_aclibn.csv (`example <https://src.koda.cnrs.fr/mesonh/mesonh-code/-/blob/MNH-60-branch/examples/test_cases/011_KW78CHEM/002_mesonh/Table_chem_species_aclib1.csv?ref_type=heads>`_)"
   "CST_ACLIB","aux/modd_cst_aclib.f90","aer/init_cst_aclib.f90", ""


CSV input parameters
****************************************************************************
To ease the use of ACLIB within different host models, a common input parameters format has been designed using csv tables (see the list in the previous section).

For aerosols, :file:`Table_aer_general_aclibn.csv`, with :code:`n`` the Méso-NH domain number, defines general options such as the number of total aerosols/modes used,
the number of families (dust, salt, etc) and the code wanted for each processus (sedimentation, scavenging, deposition, emission, and transformation). 

The same general csv table is for chemical species.

For a smooth transition from the classic FORTRAN Méso-NH namelist to csv format, a new namelist is available

.. csv-table:: NAM_ACLIB new entries
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LUSEAERTABLE","LOGICAL",".FALSE."
   "LUSECHEMTABLE","LOGICAL",".FALSE."

* :code:`LUSEAERTABLE`: true to use :file:`Table_aer_general_aclibn.csv` to read namelist input instead of the traditional namelist for **some** aerosols general parameters

* :code:`LUSECHEMTABLE`: true to use :file:`Table_chem_general_aclibn.csv` to read namelist input instead of the traditional namelist for **some** chemistry general parameters

.. note::

   By default, :file:`Table_aer_general_aclibn.csv` and :file:`Table_chem_general_aclibn.csv` are ignored (not read). Traditional Méso-NH namelist is used.

.. note::

   The Table_aer_species_aclibn.csv are always read, so using NAM_DUST, NAM_SALT or NAM_CH_ORILAM must be carefully cross-checked with the Tables!

   The Table_chem_species_aclibn.csv are not read/implemented yet.

How to code in ACLIB ?
****************************************************************************
ACLIB is shared with other models. Specific rules must be followed:

* Use explicit dimensions in variable declaration

* Do not add Méso-NH specific modules/variables into ACLIB, but add variables through the interfaces instead. 
  If a new specific module is needed, make sure that this module is Méso-NH agnostic (not dependent of other Méso-NH specific modules that would be incompatible with other host models)

* Use dedicated ACLIB custom types as it is implemented (e.g. use CST_ACLIB for constants and not MODD_CST from MesoNH world)

* Internal routines in :file:`src/ACLIB` must be agnostic from parallelization as much as possible to ease future use of cross-codes in different host models.

PHYEX
----------------------------------------------------------------------------

Turbulence
****************************************************************************

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

Shallow convection
****************************************************************************

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


* :code:`CWET_MIXING` : type of env mixing for buoyancy sorting scheme ('PKFB' for the original Pergaud code, 'LR01' for :cite:t:`lappen_toward_2001`)

* :code:`CKIC_COMPUTE` : method to compute KIC ('KFB' to use the PMMC09 original method, like in KFB, 'RS08' to use the :cite:t:`de_rooy_simple_2008` formulation) 

* :code:`CDETR_DRY_LUP` : upward length to use in the dry detrainement ('SURF' to use :math:`L_{UP}` at surface (original PMMC09 :cite:t:`pergaud_parameterization_2009`),
  'UPDR' to compute :math:`L_{UP}` in updraft)

* :code:`LMIXTKE` : flag to mix the prognostic variable TKE by updrafts. Only implemented with :code:`CMF_UPDRAFT='EDKF'`

* :code:`XSIGMA_ENV`: coefficient for the environment sigma contribution in the bigaussian scheme

* :code:`LPZ_EXP_LOG`: true to use exp/log during dP/dZ conversion to respect hydrostatic approximation to interpolate z and p between two half-level and full-level points,
  false to use linear interpolation (old interpolation, not recommended)

* :code:`XBRIO` : coefficient to slow down wup equa like :cite:t:`rio_resolved_2010`

* :code:`XAADVEC` : coefficient for advective pressure perturbation like :cite:t:`he_improved_2020`

* :code:`LRELAX_ALPHA_MF`: true to relax the small fraction assumption


ICE3
****************************************************************************

.. csv-table:: NAM_PARAM_ICEn new entries
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LKOGAN","LOGICAL",".FALSE."
   "LMODICEDEP","LOGICAL",".FALSE."
   "LEXCLDROP","LOGICAL",".FALSE."
   "LEXT_TEND","LOGICAL",".FALSE."

* :code:`LKOGAN`: true to use Kogan autocoversion of liquid

* :code:`LMODICEDEP`: flag for alternative deposition/evaporation coefficients of water vapor on ice, snow and graupel

* :code:`LEXCLDROP`: true to use of external cloud droplet concentration (as from near-real time aerosols) instead of constant values on land/sea masks. Only
  useable in HARMONIE-AROME and not yet Meso-NH

* :code:`LEXT_TEND`: true to use external tendencies during the time-splitting

* :code:`CSUBG_MF_PDF`: new option 'BIGA'. Current available options are 'NONE' or 'TRIANGLE' (see :ref:`nam_param_icen`)


LIMA
****************************************************************************

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
****************************************************************************

.. csv-table:: NAM_NEBn new entry
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LCONDBORN","LOGICAL",".FALSE."

* :code:`LCONDBORN` : true to limit condensation: reduce the distribution width  with respect to te total water content to avoid condensate too much water vapor not present 

Ocean-Atmosphere-Wave coupling
----------------------------------------------------------------------------

* Bug Fix: Resolved an issue with the rotation of sea surface currents, ensuring accurate transformation from lon/lat to x/y grid coordinates when using oceanic/wave coupling. 

Diagnostics
----------------------------------------------------------------------------

Passive pollutants
----------------------------------------------------------------------------

* :code:`LPASPOLDUST`: emit dust aerosols instead of passive scalar

* :code:`NMODEL_PP`: model number where passive pollutants are emitted

WRF and ICON init and forcing
----------------------------------------------------------------------------

* HRRR-WRF: Initializing and forcing Méso-NH with daily operational model HRRR is now possible. More info in :ref:`extracthrrr`
* ICON-EU: Initializing and forcing Méso-NH with daily operational model ICON-EU is now possible. More info in :ref:`extracticon`

SURFEX
----------------------------------------------------------------------------

Other namelist changes
----------------------------------------------------------------------------

&NAM_CONF
****************************************************************************

- ``CINIT_LG``: the ``FMOUT`` option has been renamed to ``BACKUP``.


&NAM_PARAM_RADN
****************************************************************************

Renaming parameters for CEFRADL and CEFRADI:

- CEFRADL: the ``C2R2`` option has been renamed to ``2MOM``
- CEFRADI: the ``C3R5`` option has been renamed to ``2MOM``


&NAM_OUTPUT
****************************************************************************

An additional dimension (the first one) has been added to all ``&NAM_OUTPUT`` parameters to indicate the time series number of outputs.

For now, this new dimension is always set to 1. This will allow to have several time series of outputs with different frequencies and/or variables in the future (e.g., one time series every 15 minutes with a selection of 3D fields, and one time series every minute with surface fields).


Cleaning and restructuration
----------------------------------------------------------------------------

- The :file:`src/LIB/SURCOUCHE` directory has been removed. It contained source files par parallelization and for I/O. They all have been moved to the :file:`src/MNH/parallel` and :file:`src/MNH/io` directories.
- Subdirectories in the :file:`src/MNH` directory have been created. The :file:`src/MNH` directory contained a lot of files with different functionalities.
  To better organize the code, several subdirectories have been created and files have been moved.
  This is only a first step and more restructuring will be done in the future.
- The :file:`MY_RUN` directory has been renamed to :file:`examples`.
- The :file:`MY_RUN/KTEST` directory has been renamed to :file:`examples/test_cases`.
- The other :file:`examples/*` (formerly :file:`MY_RUN/*`) subdirectories are now lowercase. This does not apply to the test case directories, which keep their original name (usually in capital letters).


- The :file:`bin_tools` directory has been removed. It contained executables that are no longer supported and that do not work on current machines.
- The :file:`LIBTOOLS` directory has been removed. It contained mostly old tools and libraries that are no longer supported.
- The :file:`src/include` directory has been removed. Only the ISORROPIA chemistry model has been kept and moved to the :file:`src/LIB/ISORROPIA` directory.
- The :file:`LFI2CDF` tool has been renamed to :file:`CDF2CDF` and moved to :file:`MNH/`.
- Configuration files, rules for compilation, examples of jobs... for obsolete machines and architectures have been removed.
- The :file:`grib_api` library has been removed. It is no longer maintained (since 2017) and does not work with recent GRIB files. It is replaced by the ECCODES library.
- The :file:`src/ARCH_SRC` directory has been cleaned. Obsolete sources have been removed.


External libraries and tools
----------------------------------------------------------------------------

.. update to 2.41 already done in MNH 5.7.2 * ECCODES updated to 2.41


Miscellaneous changes
----------------------------------------------------------------------------

Balloons: improved vertical position calculation
****************************************************************************

- Reduced time step to improve numerical stability if necessary:

  - Originally, max 1 second
  - Now, if the speed is too high, it tries 0.1 second
  - If still too high, a forced crash occurs

- Recalculates air density and vertical speed at each intermediate time step (changes significantly if the time step is large and/or the balloon moves quickly)

Microphysics: removol of C1R3 and C3R5 schemes
****************************************************************************

The C1R3 and C3R5 microphysics schemes have been removed from the code.
These schemes were not maintained, not documented, and not used in any example test case.

Default namelist changes
----------------------------------------------------------------------------
* ECRAD: the shortwave and longwave solver was SPARTACUS by default which is very costly and not suitable for very high resolution LES. Now :code:`CSW_SOLVER_NAME='Tripleclouds'` and :code:`CLW_SOLVER_NAME='Tripleclouds'`