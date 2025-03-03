.. _nam_isba:

NAM_ISBA
-----------------------------------------------------------------------------

.. csv-table:: NAM_ISBA content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "NPATCH", "integer", "1"
   "NGROUND_LAYER", "integer", "1E+9"
   "CISBA", "character(LEN=3)", "3-L"
   "CPEDO_FUNCTION", "character(LEN=4)", "CH78"
   "CPHOTO", "character(LEN=3)", "NON"
   "LTR_ML", "logical", "F"
   "CALBEDO", "character(LEN=3)", "CM13"
   "XRM_PATCH", "real", "0."
   "XUNIF_CLAY", "real", "0.33"
   "YCLAY", "character(LEN=28)", ""
   "YCLAYFILETYPE", "character(LEN=6)", "ASCLLV"
   "XUNIF_SAND", "real", "0.33"
   "YSAND", "character(LEN=28)", ""
   "YSANDFILETYPE", "character(LEN=6)", "ASCLLV"
   "XUNIF_RUNOFFB", "real", "0.5"
   "YRUNOFFB", "character(LEN=28)", ""
   "YRUNOFFBFILETYPE", "character(LEN=6)", "ASCLLV"
   "XUNIF_WDRAIN", "real", "0."
   "YWDRAIN", "character(LEN=28)", ""
   "YWDRAINFILETYPE", "character(LEN=6)", "ASCLLV"
   "YCTI", "character(LEN=28)", ""
   "YCTIFILETYPE", "character(LEN=6)", ""
   "XUNIF_SOC_TOP", "real", "1.E+20"
   "XUNIF_SOC_SUB", "real", "1.E+20"
   "YSOC_TOP", "character(LEN=28)", ""
   "YSOC_SUB", "character(LEN=28)", ""
   "YSOCFILETYPE", "character(LEN=6)", ""
   "XUNIF_PERM", "real", "1.E+20"
   "YPERM", "character(LEN=28)", ""
   "YPERMFILETYPE", "character(LEN=28)", ""
   "XUNIF_PH", "real", "1.E+20"
   "YPH", "character(LEN=28)", ""
   "YPHFILETYPE", "character(LEN=28)", ""
   "XUNIF_FERT", "real", "1.E+20"
   "YFERT", "character(LEN=28), ""
   "YFERTFILETYPE", "character(LEN=28)", ""
   "LIMP_SAND", "logical", "F"
   "LIMP_CLAY", "logical", "F"
   "LIMP_CTI", "logical", "F"
   "LIMP_SOC", "logical", "F"
   "LIMP_PERM", "logical", "F"
   "XSOILGRID", "real(150)", "1.E+20"
   "LMEB", "logical", "F"
   "LLULCC", "logical", "F"


* NPATCH: number of patches used in ISBA. One patch corresponds to aggregated parameters. 12 patches correspond to separate energy budgets for all vegetation types present in ISBA. 3 patches correspond to bare soil types, low vegetation, trees. If CPHOTO equals 'NON' any number of patches between 1 and 12 is possible, for the other values of CPHOTO, 12 patches are required. The order and the signification of each patch is the following:

  * 1: no vegetation (smooth) - NO
  * 2: no vegetation (rocks) - ROCK
  * 3: permanent snow and ice - SNOW
  * 4: temperate broadleaf cold-deciduous summergreen - TEBD (TREE)
  * 5: boreal needleleaf evergreen - BONE (CONI)
  * 6: tropical broadleaf evergreen - EVER
  * 7: C3 cultures types - C3
  * 8: C4 cultures types - C4
  * 9: irrigated crops - IRR
  * 10: grassland (C3) - GRAS
  * 11: tropical grassland (C4) - TROG
  * 12: peat bogs, parks and gardens (irrigated grass) - PARK
  * 13: tropical broadleaf deciduous - TRBD (TREE)
  * 14: temperate broadleaf evergreen - TEBE (TREE)
  * 15: temperate needleleaf evergreen - TENE (CONI)
  * 16: boreal broadleaf cold-deciduous summergreen - BOBD (TREE)
  * 17: boreal needleleaf cold-deciduous summergreen - BOND (CONI)
  * 18: boreal grass - BOGR (GRASS)
  * 19: shrub - SHRB (TREE)
  
* NGROUND_LAYER: number of soil layer used in case of diffusion physics in the soil (CISBA = 'DIF'):

  * with CISBA = 2-L, NGROUND_LAYER default is 2
  * with CISBA = 3-L, NGROUND_LAYER default is 3
  * with CISBA= DIF and LECOCLIMAP, NGROUND_LAYER default is 14
  
* CISBA: type of soil discretization and physics in ISBA:

  * '2-L': force-restore method with 2 layers for hydrology
  * '3-L': force-restore method with 3 layers for hydrology
  * 'DIF': diffusion layer, with any number of layers
  
* CPEDO_FUNCTION: Pedo-transfert function for DIF. The following options are currently available:

  * "CH78": Clapp and Hornberger 1978 for BC
  * "C084": Cosby et al. 1988 for BC
  
* CPHOTO:type of photosynthesis physics. The following options are currently available:

  * "NON": none is used. Jarvis formula is used for plant transpiration.
  * "AST": ISBA-AGS with offensive/defensive stress, without evolving Leaf Area Index
  * "NIT": ISBA-AGS with nitrogen, with evolving Leaf Area Index
  * "NCB": ISBA-AGS with nitrogen, with evolving Leaf Area Index and wood, soil, roots biomass

* LTR_ML: to activate new radiative transfert calculation, only if CPHOTO/=NON.

* CALBEDO: type of bare soil albedo. The following options are currently available

  * "DRY ": dry bare soil albedo
  * "WET ": wet bare soil albedo
  * "MEAN": albedo for bare soil half wet, half dry
  * "EVOL": albedo of bare soil evolving with soil humidity
  * "CM13": albedo by cover and vegetation type processed from satellite data
  
* XRM_PATCH: threshol to remove little fractions of patches

* XUNIF_CLAY: uniform prescribed value of clay fraction.

* YCLAY: clay fraction data file name.

* YCLAYFILETYPE: type of clay data file ('DIRECT', 'BINLLF', 'BINLLV', 'ASCLLV')

* XUNIF_SAND: uniform prescribed value of sand fraction.

* YSAND: sand fraction data file name.

* YSANDFILETYPE: type of sand data file ('DIRECT', 'BINLLF', 'BINLLV', 'ASCLLV')

* XUNIF_RUNOFFB: uniform prescribed value of subgrid runoff coefficient.

* YRUNOFFB: subgrid runoff coefficient data file name.

* YRUNOFFBFILETYPE: type of subgrid runoff data file ('DIRECT', 'BINLLF', 'BINLLV', 'ASCLLV')

* XUNIF_WDRAIN: uniform prescribed value of subgrid drainage.

* YWDRAIN: subgrid drainage data file name.

* YWDRAINFILETYPE: type of subgrid drainage data file ('DIRECT', 'BINLLF', 'BINLLV', 'ASCLLV')

* YCTI: topographic indices file name.

* YCTIFILETYPE: type of topographic file ('DIRECT', 'BINLLF', 'BINLLV', 'ASCLLV')

* XUNIF_SOC_TOP: uniform prescribed value of topsoil organic carbon (used only in CSOC=SGH in NAM_ISBAn)

* XUNIF_SOC_SUB: uniform prescribed value of subsoil organic carbon (used only in CSOC=SGH in NAM_ISBAn)

* YSOC_TOP: organic carbon topsoil data file name (used only in CSOC=SGH in NAM_ISBAn).

* YSOC_SUB: organic carbon subsoil data file name (used only in CSOC=SGH in NAM_ISBAn).

* YSOCFILETYPE: type of organic matter data file ('DIRECT', 'BINLLF', 'BINLLV', 'ASCLLV') (used only in CSOC=SGH in NAM_ISBAn)

* XUNIF_PERM: uniform value of permafrost distribution (used only if CISBA=DIF)

* YPERM: file name for permafrost distribution (used only if CISBA=DIF)

* YPERMFILETYPE: permafrost distribution data file type('DIRECT', 'BINLLF', 'BINLLV', 'ASCLLV') (used only if CISBA=DIF)

* XUNIF_PH: uniform value of soil pH (used only if LCH_NO_FLUX=T)

* YPH: file name for soil pH (used only if LCH_NO_FLUX=T)

* YPHFILETYPE: soil pH data file type ('DIRECT', 'BINLLF', 'BINLLV', 'ASCLLV') (used only if LCH_NO_FLUX=T)

* XUNIF_FERT: uniform value of soil fertilization rate (kgN/ha/h) (used only if LCH_NO_FLUX=T)

* YFERT: file name for soil fertilisation rate (kgN/ha/h) (used only if LCH_NO_FLUX=T)

* YFERTFILETYPE: soil fertilisation rate file type (kgN/ha/h)('DIRECT', 'BINLLF', 'BINLLV', 'ASCLLV') (used only if LCH_NO_FLUX=T)

* LIMP_SAND: reads sand fraction in an existing PGD file

* LIMP_CLAY: reads clay fraction in an existing PGD file

* LIMP_CTI: reads topographic indices in an existing PGD file

* LIMP_SOC: reads organic carbon in an existing PGD file

* LIMP_PERM: reads permafrost distribution in an existing PGD file
* XSOILGRID: uniform soil depth grid for CISBA=DIF. Default with CISBA=DIF and LECOCLIMAP is (/0.01,0.04,0.10,0.20,0.40,0.60,0.80,1.00,1.50,2.00,3.00,5.00,8.00,12.0/)

* LMEB: Flag to activate MEB (please note that by default, MEB uses the TR_LM radiation scheme, so when LMEB=T, LTR_ML=T automatically)

* LLULCC: land-use land cover change scheme activation key
