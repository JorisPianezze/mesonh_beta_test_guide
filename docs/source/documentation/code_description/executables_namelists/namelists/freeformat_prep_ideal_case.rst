.. _freeformat_prep_ideal_case:

Free-format part
-----------------------------------------------------------------------------

Each section of the free format part must be introduced by its corresponding keyword (writen on a separated line).
There is always a moist variable written in :file:`PRE_IDEA1.nam` file, even in idealized dry cases, for which the moist variable should be equal to zero in the :file:`PRE_IDEA1.nam` file.
The produced initial file will always contain a moist variable in 'CSTN' and 'RSOU' cases.

Vertical grid
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

keyword: **ZHAT**

If the vertical grid generation selector CZGRID_TYPE is equal to 'MANUAL', you must enter at the end of your namelist file, the heights of the vertical velocity levels. You must start from the ground level (K=2) to the model top (K=KMAX +2), thus you only have to enter KMAX + 1 values, because the level below the ground (i.e. K=1) is at the same distance from the ground ( K=2 ) as the first level above the ground ( K=3 ). Note also that the K= KMAX + 2 level represents the model top. In this case the free parameters (ZDZGRD, ZDZTOP,ZSTRGRD, ...) are not used.

Radiosounding case
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

keyword: **RSOU**

The radiosounding data are written in the free-format part of PRE_IDEA1.nam file, where the altitude variable is :

* the pressure in case KIND='STANDARD' or 'PUVTHVMR' or 'PUVTHVHU' or 'PUVTHDHU' or 'PUVTHDMR' (real, in Pascal)

* the height in case ’ZUVTHVMR’ or ’ZUVTHVHU’or ’ZUVTHDMR’ or ’ZUVTHLMR’ (real, in meters)

The first wind variable is :

* the wind direction in case KIND=’STANDARD’ (real,in degrees)

* the zonal wind in cases KIND=’PUVTHVMR’ or ’PUVTHDMR’ or ’ZUVTHDMR’ or ’ZUVTHLMR’or ’ZUVTHVHU’ or ’PUVTHDHU’ or ’ZUVTHVMR’ or ’PUVTHVHU’ (real, in m/s)

The second wind variable is :

* the wind force in case KIND=’STANDARD’ (real, in m/s)

* the meridian wind in cases KIND=’PUVTHVMR’ or ’PUVTHDMR’ or ’ZUVTHDMR’ or ’ZUVTHLMR’ or ’ZUVTHVHU’ or ’PUVTHDHU’ or ’ZUVTHVMR’ or ’PUVTHVHU’ (real, in m/s)

The temperature variable is :

* the temperature in case KIND=’STANDARD’ (real, in Kelvin)

* the virtual potential temperature in cases KIND=’PUVTHVMR’ or ’PUVTHVHU’ or ’ZUVTHVMR’ or ’ZUVTHVHU’ (real,in Kelvin)

* the dry potential temperature in cases KIND=’PUVTHDMR’ or ’PUVTHDHU’ or ’ZUVTHDMR’ (real, in Kelvin)

* the liquid potential temperature in case KIND=’ZUVTHLMR’(real, in Kelvin)

The moist variable is :

* the dew point temperature in case KIND=’STANDARD’ (real, in Kelvin)

* the vapor mixing ratio in cases KIND=’PUVTHVMR’ or ’ZUVTHDMR’ or ’ZUVTHVMR’ or ’PUVTHDMR’ (real, in Kg/Kg)

* the total water mixing ratio in case KIND= ’ZUVTHLMR (real, in Kg/Kg)

* the relative humidity in cases KIND= ’ZUVTHVHU’, or ’PUVTHDHU’ or ’PUVTHVHU’ (real, in percents)

Additional cloud variables

For the moment, this configuration works only for KIND=’PUVTHDMR’ or ’ZUVTHDMR’ and L1D=.TRUE.. It is planned to compute radiation diagnostics with the :program:`DIAG` program.

* cloud mixing ratio if LUSERC=T or LUSERI=T (real, in Kg/Kg)

* ice mixing ratio if LUSERI=T (real, in Kg/Kg)

You should make sure that the levels are dense enough so that the Laplace relation, which gives the thickness between successive levels, can be applied. The radiosounding information is written in the file in the following order :

* YEAR (integer, exemple : 1994), MONTH (integer, exemple : 4), DAY (integer, exemple : 22), TIME (real, in seconds, exemple : 36000 for 10 h)

* KIND of data used for the radiosounding (string of 8 charcaters) Nine kind of data are possible : ’STANDARD’, ’PUVTHVMR’, ’PUVTHVHU’, ’ZUVTHVMR’, ’ZUVTHVHU’, ’PUVTHDMR’, ’PUVTHDHU’, ’ZUVTHDMR’, ’ZUVTHLMR’.

Except for the STANDARD kind :

* the first letter of KIND represents the kind of altitude variable (P for pressure and Z for height),

* the second and third letters represent the kind of wind variables (U for zonal wind, V for meridian wind),

* the fourth, fifth and sixth letters represent the kind of temperature variable (THV for virtual potential temperature, THHD for dry potential temperature and THL for liquid potential temperature),

* the seventh and eighth letters represent the kind of moist variable (HU for relative humidity and MR for vapor mixing ratio).

(In case of STANDARD kind, the altitude variable is the pressure, the wind variables are direction and wind force, the temperature variable is the temperature and the moist variable is the due point temperature. )

* HEIGHT of GROUND LEVEL (real, in meters)

* PRESSURE at GROUND LEVEL (real,in Pascal)

* a TEMPERATURE variable at GROUND LEVEL (real, in Kelvin)

* a MOIST variable at GROUND LEVEL

* NUMBER of WIND data LEVELS (integer)

* level 1 : ALTITUDE variable , first WIND variable, second WIND variable at wind level 1 (the lowest wind-level).

* level 2 : ALTITUDE variable, first WIND variable, second WIND variable.

uppermost wind level : ALTITUDE variable, first WIND variable, second WIND variable.

* NUMBER of mass data LEVELS (integer) Note that this number includes the ground level (i.e. the first level). That is why the following list starts at level 2.

* level 2 : ALTITUDE variable, TEMPERATURE variable, MOIST variable, additional cloud variable(s) (the mass level 1 is at ground).

* level 3 : ALTITUDE variable, TEMPERATURE variable, MOIST variable, additional cloud variable(s) .

* uppermost mass level: ALTITUDE variable, TEMPERATURE variable, MOIST variable, additional cloud variable(s).
You should make sure that the highest level of the radiosounding is located above the highest vertical level of the model.

.. note::

   Example of free part of :file:`PRE_IDEA1.nam` :
   
   .. code-block::

      RSOU
      1990 10 3 72000.
      'STANDARD'
      200.
      100240.
      287.5
      276.
      2
      85000. 20. 10.
      70000. 30. 10.
      3
      90000. 280. 275.
      60000. 271. 269.

Constant moist Brunt-Vaisala case
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

keyword: **CSTN**

Data of the vertical profile are written in the free-format part of PRE_IDEA1.nam file in the following order :

* YEAR (integer, example : 1994), MONTH (integer, example : 4), DAY (integer, example : 22), TIME (real, in seconds, example : 36000. for 10 h)

* NUMBER of LEVELS (integer)

* VIRTUAL POTENTIAL TEMPERATURE at GROUND LEVEL (i.e at the first level) (real,in Kelvin)

* PRESSURE at GROUND LEVEL (i.e at the first level) (real, in Pascal)

* HEIGHT at all levels. the first level is the ground level

* ZONAL WIND COMPONENT at all levels (the first level is the ground level)

* MERIDIAN WIND COMPONENT at all levels (the first level is the ground level)

* RELATIVE HUMIDITY at all levels (the first level is the ground level)

* MOIST BRUNT VAISALA FREQUENCY at all layers (the number of layers is the number of levels - 1)

In this case, the level number can even be equal to 1, because the profile information is linearly interpolated on the model grid without orography (wind components, :math:`\theta_v` and humidity) before the application of the Laplace relation to deduce the pressure and the vapor mixing ratio. Thus, the layers’ thicknesses are never too large to invalidate the Laplace relation. 

.. note::

   Example of free part of :file:`PRE_IDEA1.nam` :

   .. code-block::
   
      CSTN
      2006 06 06 21600.
      5
      287.5
      100240.
      200. 1000. 1500. 3000. 4000.
      10. 20. 25. 30. 35.
      2. 10. 12.5 11.5 15.
      80. 84. 85. 79. 87.
      0.01 0.014 0.015 0.016

The forced version
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

keyword: **ZFRC** or **PFRC**

For idealized simulations a forced mode can be useful to impose the effects of a simplified large scale environment to the model solution. This functionality works (LFORCING=.TRUE. in module MODD_CONF) when CIDEAL=’RSOU’ or ’CSTN’ (see 5.2.10 and 5.3) and only in the case LGEOSBAL =.FALSE. for inclusion of a geostrophic wind forcing. All forcing fields are issued from spatial interpolation of chronological series of 1D data (provided by the user onto the model grid). They are prepared during the prep_ideal_case sequence and are stored in the Meso-NH files for further use in case of RESTART model run.

The forcing fields can be time dependent. Application of the forcing begins as soon as the date and time of the first set of forcing field given by the user, is lower or equal to the current date and time of the model run. The forcing action of the last forcing field is remanant, this is a way to impose a stationnary forcing. When the current date and time of the model run is bounded by two successive forcing fields, a simple linear interpolation in time is made. Note that an available Newtonian relaxation forcing type on [u, v] and/or [:math:`\theta`, rv] is exclusive from the other physical forcings.

The forcing information and soundings have to be added at the end of the free-format part already written for CIDEAL=’CSTN’ or ’RSOU’. First, the type of forcing and the number of time dependent forcing are given:

* keyword forcing type (character*4)

  * ZFRC means that the altitude of the forcing data are in height scale (meters).
  * PFRC means that the altitude of the forcing data are in pressure scale (Pascal).
  
* number of time dependent forcing (integer)

The 1D forcing data are different from the one used to initialize the model because specific data have to be entered. The data used to define each forcing are given sequentially in the following order (one item per line):

* date and time of the forcing in the format: year (integer), month (integer), day (integer) and time of the day (real, s).

* ground height (real, m)

* ground pressure (real, Pa)

:math:`\theta_d` (real, K) at ground level (Nota: it is used later in the code to compute - if asked - a
time varying sea surface temperature).

* rv (real, kg/kg) at ground level

* number of level (integer)

* height of level1 (real, m) if ZFRC or pressure at level1 (real, Pa) if PFRC, uf rc component at level1 (real, m/s), vf rc component at level1 (real, m/s), :math:`\theta f` rc at level1 (real, K), rv f rc at level1 (real, kg/kg), wf rc at level1 (real, m/s), (:math:`\partial\theta/\partial t`)f rc at level1 (real, K s) and (:math:`\partial rv/\partial t`)f rc at level1 (real, 1/s). (:math:`\partial u/\partial t`)f rc at level1 (real, m/s2). (:math:`partial v/ \partial t`)f rc at level1 (real, m/s2). 

* idem at level2

* ...

* idem at levelN

If PFRC is the forcing type, an additional sounding is given in order to convert the pressure
levels into height levels with enough accuracy. Data are organized as follows:

* number of level (integer)

* pressure at level1 (real, Pa), :math:`theta` at level1 (real, K) and rv at level1 (real, kg/kg).

This operation is repeated until the previous number of sounding is reached.

.. note::

   Example of free part of :file:`PRE_IDEA1.nam` :
   
   .. code-block::
   
      ZFRC
      1
      1983 07 01 0.
      0
      1000000
      284.5
      0.008
      6
      5. -7.0 0.0 281.10 0.00540 -0.00000 0. 0. 0. 0.
      15. -7.0 0.0 281.10 0.00540 -0.00000 0. 0. 0. 0.
      1095. -7.0 0.0 280.75 0.00540 -0.00300 0. 0. 0. 0.
      1145. -7.0 0.0 290.60 0.00190 -0.00300 0. 0. 0. 0.
      3000. -7.0 0.0 304.15 0.00190 -0.00300 0. 0. 0. 0.
      9000. -7.0 0.0 346.15 0.00190 -0.00300 0. 0. 0. 0.

The advective forcing
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

keyword: **ZFRC_ADV**

For 2D idealized simulation, an advective forcing can be used to impose effects to the model solution. This functionality works (L2D_ADV_FRC=.TRUE. in MODD_CONF) only in 2D cases. The advecting forcings mimic the latidudinal humidity and temperature advection not taken into account in a 2D model.

The forcing information and soundings have to be added at the end of the free-format part already written for CIDEAL=’CSTN’ or ’RSOU’. They are set in the following order :

* ZFRC_ADV : keyword for advective forcing

* number of forcing files

* type of forcing : ZADV2D for Z levels or PADV2D for pressure levels

* number vertical levels for the file

* Date of first forcing : YYYY MM DD T (secondes)

* name of the file with horizontal mean profile of theta, rv

* name of the advective forcing file

.. note::

   Example of free part of :file:`PRE_IDEA1.nam` :
   
   .. code-block::

      ZFRC_ADV
      1
      ZADV2D
      52
      1997 07 15 00000.
      "mean_atm_07.dat"
      "frc_ideal_7_70km.dat"
 
The relaxation forcing
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

keyword: **ZFRC_REL**

For 2D idealized simulation, a relaxation forcing can be used to impose effects to the model solution. This functionality works (L2D_REL_FRC=.TRUE. in MODD_CONF) only in 2D cases. The relaxation forcing allows the relax the model fields towards a 2D climatology for temperature and humidity.

The forcing information and soundings have to be added at the end of the free-format part already written for CIDEAL=’CSTN’ or ’RSOU’. They are set in the following order :

* ZFRC_REL : keyword for advective forcing

* number of forcing files

* type of forcing : ZREL2D for Z levels or PREL2D for pressure levels

* number vertical levels for the file

* Date of first forcing : YYYY MM DD T (secondes)

* name of the file with horizontal mean profile of theta, rv

* name of the advective forcing file

.. note::

   Example of free part of :file:`PRE_IDEA1.nam` :
   
   .. code-block::
  
      ZFRC_REL
      1
      ZREL2D
      52
      1997 07 15 00000.
      "mean_atm_07.dat"
      "frc_ideal_7_70km.dat"

Discretized orography
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

keyword: **ZSDATA**

Only the orography corresponding to the computational domain must be provided in the free format part. For 3D orography, data are read like if it was a map (the first line is the Northern border and the first data is the North-West corner) with one line per Y-axis increment.

.. note::

   Example of free part of :file:`PRE_IDEA1.nam` :
   
   .. code-block::

      ZSDATA
      30. 30. 35. 50. 30. 30.
      30. 59.5 133.3 100.2 136.7 100.
      35. 89.5 183.3 200.2 299.7 170.5
      50. 112.5 193.0 210.2 206.7 120.
      40. 82.5 153.0 180.5 156.7 100.3
      
The ocean version
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

keyworkd: **RSOU**

For oceanic version of Meso-NH, the initial and forcing profiles of the ocean are written in the free-format part of PRE_IDEA1.nam file, where the altitude variable is the depth. To follow usual convention for ocean data, the 1D profiles are given starting from the surface (positive value). The profile and forcing information are written in the following order :

* YEAR (integer, exemple : 1994), MONTH (integer, exemple : 4), DAY (integer, exemple: 22), TIME (real, in seconds, exemple : 36000 for 10 h)

* KIND of data used for the profile. Two kind are possible : KIND=’IDEALOCE’ (data written in PRE_IDEA1.nam) or KIND=’STANDOCE’ (data written in a NetCDF file).

The following format is valid for KIND=’IDEALOCE’.

* ATMOSPHERIC PRESSURE at the surface which is the top domain of the oceanic model (real, in Pascal)

* SEA SURFACE TEMPERATURE at the surface (real, in Kelvin)

* SEA SURFACE SALINITY at the surface (real, in g/kg)

* NUMBER of SEA CURRENT levels (integer)

* level 1 : DEPTH HEIGHT variable (real, meters) , U-CURRENT (real, m/s), V-CURRENT at CURRENT level (real, m/s)
* level 2 : DEPTH HEIGHT variable (real, meters) , U-CURRENT (real, m/s), V-CURRENT at CURRENT level (real, m/s)
* level ...

* NUMBER of mass data LEVELS (integer).

* level 2 : DEPTH HEIGHT variable (real, meters), WATER TEMPERATURE (real, Kelvin), SALINITY at mass level (real, g/kg)

* level 3 : DEPTH HEIGHT variable (real, meters), WATER TEMPERATURE (real, Kelvin), SALINITY at mass level (real, g/kg)

* level ...

* NUMBER of time-varying FORCING (integer). The data used to define each forcing are given sequentially in the following order (one item per line):

* YEAR (integer, exemple : 1994), MONTH (integer, exemple : 4), DAY (integer, exemple : 22), TIME (real, in seconds, exemple : 36000 for 10 h)

* U-STRESS (real, m2/s2)

* V-STRESS (real, m2/s2)

* HEAT TURBULENT FLUX (real, W/m2)

* RADIATIVE FLUX (real, W/m2)

Surface fluxes are positive when going upward (from the ocean to the atmosphere) In the KIND=’STANDOCE’: initial 1D profiles and surface fluxes(t) are read from 2 netcdf files (See set_rsou.f90 for details)
 
Example of PRE_IDEA1.nam :
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The selected case is the following:

* 2D mountain

* one moist layer atmosphere

This file contains the information necessary to generate the initial conditions for a quasihydrostatic flow, in the weakly non-linear regime, with a regular vertical grid.

Example of :file:`PRE_IDEA1.nam` :

.. code-block::

   &NAM_DIMn_PRE NIMAX=128, NJMAX=1 /
   &NAM_VER_GRID NKMAX=32, YZGRID_TYPE = ’FUNCTN’, ZDZGRD=500., ZDZTOP=500.,
   ZZMAX_STRGRD=1000. , ZSTRGRD=0., ZSTRTOP= 0.,
   &NAM_CONFn LUSERV=.TRUE., NSV_USER = 0 /
   &NAM_GRID_PRE XLAT0 = 48.25 , XLON0 = 0.,
   XRPK = 0. , XBETA = 0.,
   XLONORI = 48.25, XLATORI = 0. /
   &NAM_CONF_PRE LCARTESIAN=.TRUE., LBOUSS=.FALSE.,
   CIDEAL=’CSTN’, CZS=’BELL’,
   LPERTURB= .FALSE., NVERB=1 /
   &NAM_GRIDH_PRE XDELTAX=5.E2 , XDELTAY=5.E2,
   XHMAX=500., XAX=10.E3, XAY=10.E3, NIZS=64, NJZS=2,
   NEXPX = 1, NEXPY=1 /
   &NAM_LUNITn CINIFILE=’HYD2D’,CINIFILEPGD=’HYD2D_PGD’ /
   &NAM_DYNn_PRE CPRESOPT =’RICHA’, NITR=4, XRELAX=1.0 /
   &NAM_LBCn_PRE CLBCX(1)=’OPEN’, CLBCX(2)=’OPEN’,
   CLBCY(1)=’OPEN’, CLBCY(2)=’OPEN’ /
   &NAM_VPROF_PRE CTYPELOC=’IJGRID’, NILOC=10, NJLOC=2,
   CFUNU=’ZZZ’, CFUNV=’ZZZ’,
   LGEOSBAL=.FALSE. /
   &NAM_GRn_PRE CSURF=’EXTE’ /
   &NAM_CH_MNHCn_PRE LUSECHEM = F /
   CSTN
   2
   285.
   100000.
   0. 20000.
   10. 10.
   0. 0.
   40. 40.
   0.01
   

