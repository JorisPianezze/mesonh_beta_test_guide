.. _nam_param_ecradn:

NAM_PARAM_ECRADn
-----------------------------------------------------------------------------

It contains the options for the ECRAD radiative scheme (CRAD = "ECRA" in :ref:`nam_paramn`). ECRAD version is defined in the compilation procedure by setting VERSION_ECRAD.

.. note::

   Since the version 1.4.0, ECRAD is open-source. To use ECRAD, you must link specific files found at $SRC_MESONH/src/LIB/RAD/ecrad-VERSION_ECRAD/data/ in the folder of the simulation.

.. csv-table:: NAM_PARAM_ECRADn content
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
   "CSW_SOLVER_NAME", "CHARACTER(LEN=63)", "Tripleclouds"
   "CLW_SOLVER_NAME", "CHARACTER(LEN=63)", "Tripleclouds"
   "COVERLAP_SCHEME_NAME", "CHARACTER(LEN=63)", "Exp-Ran"
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
   "NRADLP","INTEGER","1"
   "NRADIP","INTEGER","1"
   "NREG","INTEGER","3"
   "XCLOUD_FRAC_STD","REAL","1.0"
   "LSPEC_EMISS","LOGICAL",".FALSE"
   "LSPEC_ALB","LOGICAL",".FALSE."
   "SURF_TYPE","CHARACTER(LEN=4)","'SNOW'"


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

* :code:`NREG`: Number of regions, where one is clear sky and one or two are cloud (the Tripleclouds solver always assumes three regions regardless of this parameter)

* :code:`XCLOUD_INHOM_DECORR_SCALING`: Ratio of overlap decorrelation lengths for cloud inhomogeneities and boundaries

* :code:`XCLOUD_FRACTION_THRESHOLD`: Ignore clouds with fraction below this. Set to 2.5e-5 if COVERLAP_SCHEME_NAME='Exp-Ran'

* :code:`XCLOUD_FRAC_STD` : Cloud water content horizontal fractional standard deviation in a gridbox

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

* :code:`NRADLP` : liquid effective radius calculation

  * 0: ERA-15, 
  * 1: Zhang and Rossow,
  * 2: Martin (1994), 
  * 3: Martin (1994) and Woods (2000)
  * 4: use droplets mixing ratio and concentration from LIMA

* :code:`NRADIP` : ice water effective radius calculation

  * 0: 40 mum
  * 1: Liou and Ou (1994)
  * 2: Liou and Ou (1994) improved
  * 3: Sun and Rikus (1999)
  * 4: use ice crystals mixing ratio and concentration from LIMA

* :code:`LSPEC_EMISS` : flag to use an idealized (horizontally homogeneous) spectral emissivity defined by SURF_TYPE

* :code:`LSPEC_ALB` : flag to use an idealized (horizontally homogeneous) spectral albedo defined by SURF_TYPE

* :code:`SURF_TYPE` : type of surface for idealized spectral emissivity and albedo among  "VEGE", "SNOW", "OCEA", "DESE", "ZERO", "UNIT". Values are read in ECRAD data files (spectral_albedo.nc spectral_emissivity.nc (these files are in src/LIB/RAD/data_mnh). 

