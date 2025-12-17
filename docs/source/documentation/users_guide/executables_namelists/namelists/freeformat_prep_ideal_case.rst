.. _freeformat_prep_ideal_case:

Free-format part
-----------------------------------------------------------------------------

The free-format part of the PRE_IDEA1.nam namelist corresponds to blocks of text that are necessary when using certain options, which are described in the following sections.
Each section of the free format part must be introduced by its corresponding keyword (writen on a separated line).

Vertical grid
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

If you want to define your own vertical grid (CZGRID_TYPE = "MANUAL" in :ref:`nam_ver_grid` inside :file:`PRE_IDEA1.nam`), you must give the heights of the vertical velocity levels from the surface to the top of the domain (NKMAX + 1 values).
The corresponding keyword is **ZHAT**.

.. note::

   Example of free part of :file:`PRE_IDEA1.nam` :

   .. code-block::
                 
      &NAM_VER_GRID NKMAX       = 10,
                    YZGRID_TYPE = 'MANUAL' /

      ZHAT
      0.
      1050.
      2100.
      3250.
      4300.
      5200.
      6100.
      7000.
      8000.
      9000.
      10000.


Radiosounding case
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

For idealized simulations, it is possible to use a radiosounding to initialize the model (CIDEAL = "RSOU" in :ref:`nam_conf_pre` in :file:`PRE_IDEA1.nam`). The corresponding keyword is **RSOU** and the free format part has to be set in this order:

.. code-block::

   RSOU
   year month day time

.. note::

   * year has to be an integer (example : 1994)
   * month has to be an integer (example : 4)
   * day has to be an integer (example : 22)
   * time has to be a real in seconds (example : 36000. for 10 h)
   
.. code-block::   

   kind of radiosounding

.. note::

   Nine kind of radiosounding are possible : "STANDARD", "PUVTHVMR", "PUVTHVHU", "ZUVTHVMR", "ZUVTHVHU", "PUVTHDMR", "PUVTHDHU", "ZUVTHDMR", "ZUVTHLMR". Except for the "STANDARD":

   * the first letter represents the kind of altitude variable (P for pressure (Pa) and Z for height (m)),
   * the second and third letters represent the kind of wind variables (U for zonal wind (m/s), V for meridian wind (m/s)),
   * the fourth, fifth and sixth letters represent the kind of temperature variable (THV for virtual potential temperature (K), THD for dry potential temperature (K) and THL for liquid potential temperature (K)),
   * the seventh and eighth letters represent the kind of moist variable (HU for relative humidity (%) and MR for vapor mixing ratio (kg/kg)).

     In case of "STANDARD", the altitude variable is the pressure (Pa), the wind variables are direction and wind force (m/s), the temperature variable is the temperature (K) and the moist variable is the dew point temperature (K).

.. code-block::   

   height of the ground level (real, in meters)
   pressure at the ground level (real,in Pascal)
   temperature at ground level (real, in Kelvin)
   humidity at ground level (real, unit depends on the kind radiosounding)
   
   number of wind data levels (integer)
   altitude_level_1 first_wind_variable second_wind_variable
   altitude_level_2 first_wind_variable second_wind_variable
   ...
   altitude_level_top first_wind_variable second_wind_variable

.. note::

   Units of altitude_levels, first_wind_variable and second_wind_variable depends on the kind radiosounding you choose.

.. code-block::

   number of mass data levels (integer)
   altitude_level_2 temperature humidity additional_cloud_variable(s)
   altitude_level_3 temperature humidity additional_cloud_variable(s)
   ...
   altitude_level_top temperature humidity additional_cloud_variable(s)

.. note::

   * Number of mass data levels includes the ground level (i.e. the first level). That is why the following list starts at level 2.
   * Units of altitude_levels, temperature, humidity and additional_cloud_variable(s) depends on the kind radiosounding you choose).

.. warning::
   
   * You should make sure that the highest level of the radiosounding is located above the highest vertical level of the model.
      
   * Additional cloud variables. For the moment, this configuration works only for kind="PUVTHDMR" or "ZUVTHDMR" and L1D=.TRUE.. It is planned to compute radiation diagnostics with the :ref:`diag` program :

     * cloud mixing ratio if LUSERC=T or LUSERI=T (real, in kg/kg)
     * ice mixing ratio if LUSERI=T (real, in kg/kg)
     
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

For idealized simulations, it is possible to use a constant Brunt-Vaisala frequency, shear and humidity layers to initialize the model (CIDEAL = "CSTN" in :ref:`nam_conf_pre` in :file:`PRE_IDEA1.nam`). The corresponding keyword is **CSTN** and the free format part has to be set in this order:

.. code-block::

   CSTN
   year month day time

.. note::

   * year has to be an integer (example : 1994)
   * month has to be an integer (example : 4)
   * day has to be an integer (example : 22)
   * time has to be a real in seconds (example : 36000. for 10 h)

.. code-block::

   number of levels (integer)
   virtual potential temperature at ground level (real, in K)
   pressure at ground level (real, in Pa)
   height at all levels.
   zonal wind component at all levels
   meridian wind component at all levels
   relative humidity at all levels
   moist Brunt Vaisala frequency at all layers

.. note::

   * The first level is the ground level.
   * For moist Brunt Vaisala frequency, the number of layers is the number of levels - 1.

In this case, the level number can even be equal to 1, because the profile information is linearly interpolated on the model grid without orography (wind components, :math:`\theta_v` and humidity) before the application of the Laplace relation to deduce the pressure and the vapor mixing ratio. Thus, the layers' thicknesses are never too large to invalidate the Laplace relation. 

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

For idealized simulations a forced mode can be useful to impose the effects of a simplified large scale environment to the model solution.
This functionality works when LFORCING=.TRUE. and CIDEAL='RSOU' or 'CSTN' in :ref:`nam_conf_pre` and when LGEOSBAL =.FALSE. in :ref:`nam_vprof_pre` for inclusion of a geostrophic wind forcing in :file:`PRE_IDEA1.nam`.
All forcing fields are issued from spatial interpolation of chronological series of 1D data (provided by the user onto the model grid).

The forcing fields can be time dependent. Application of the forcing begins as soon as the date and time of the first set of forcing field given by the user, is lower or equal to the current date and time of the model run. The forcing action of the last forcing field is remanant, this is a way to impose a stationnary forcing. When the current date and time of the model run is bounded by two successive forcing fields, a simple linear interpolation in time is made. Note that an available Newtonian relaxation forcing type on [u, v] and/or [:math:`\theta`, rv] is exclusive from the other physical forcings.

The forcing information and soundings have to be added at the end of the free-format part already written for CIDEAL="CSTN" or "RSOU".
Depending of the altitude of the forcing data two keywords are available, **ZFRC** means that the altitude of the forcing data are in height scale (m) and PFRC means that the altitude of the forcing data are in pressure scale (Pa). 

The free format part has to be set in this order:

.. code-block::
   
   ZFRC or PFRC
   number of time dependent forcing (integer)
   year month day time

.. note::

   * year has to be an integer (example : 1994)
   * month has to be an integer (example : 4)
   * day has to be an integer (example : 22)
   * time has to be a real in seconds (example : 36000. for 10 h)
   
.. warning::
   
   The 1D forcing data are different from the one used to initialize the model because specific data have to be entered. The data used to define each forcing are given sequentially in the following order (one item per line):

.. code-block::

   ground height (real, m)
   ground pressure (real, Pa)
   potential temperature at ground level (real, K)
   
.. note::

   It is used later in the code to compute - if asked - a time varying sea surface temperature).

.. code-block::

   humidity (real, kg/kg) at ground level
   number of level (integer)
   altitude of level 1 list of forcing fields
   idem at level 2
   ...
   idem at level top

.. note::

   * Unit of altitudes depends on the keyword chosen ZFRC for (m) and PFRC for (Pa)
   
   * List of forcing field is :
   
     * :math:`u_{frc}` component at the corresponding level  (real, m/s)
     * :math:`v_{frc}` component at the corresponding level (real, m/s)
     * :math:`\theta_{frc}` at the corresponding level (real, K)
     * :math:`rv_{frc}` at the corresponding level (real, kg/kg)
     * :math:`w_{frc}` at the corresponding level (real, m/s)
     * :math:`(\partial\theta / \partial t)_{frc}` at the corresponding level (real, K/s)
     * :math:`(\partial rv / \partial t)_{frc}` at the corresponding level (real, 1/s)
     * :math:`(\partial u / \partial t)_{frc}` at the corresponding level (real, m/s2)
     * :math:`(\partial v / \partial t)_{frc}` at the corresponding level (real, m/s2).    

   If PFRC is the forcing type, an additional sounding is given in order to convert the pressure levels into height levels with enough accuracy. Data are organized as follows:

   * number of level (integer)
   * pressure at level 1 (real, Pa), :math:`\theta` at level 1 (real, K) and rv at level 1 (real, kg/kg).
   
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

For 2D idealized simulation, an advective forcing can be used to impose effects to the model solution. This functionality works when L2D_ADV_FRC=.TRUE. in :ref:`nam_conf_pre` in :file:`PRE_IDEA1.nam`. The advecting forcings mimic the latidudinal humidity and temperature advection not taken into account in a 2D model. The forcing information and soundings have to be added at the end of the free-format part already written for CIDEAL="CSTN" or "RSOU". The corresponding keyword is **ZFRC_ADV** and the free format part has to be set in this order:

.. code-block::

   ZFRC_ADV
   number of forcing files
   type of forcing : ZADV2D for Z levels or PADV2D for pressure levels
   number vertical levels for the file
   date of first forcing : year (integer) month (integer) day (integer) time (real, seconds)
   name of the file with horizontal mean profile of theta, rv
   name of the advective forcing file

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

For 2D idealized simulation, a relaxation forcing can be used to impose effects to the model solution. This functionality works when L2D_REL_FRC=.TRUE.  in :ref:`nam_conf_pre` in :file:`PRE_IDEA1.nam`. The relaxation forcing allows the relax the model fields towards a 2D climatology for temperature and humidity. The forcing information and soundings have to be added at the end of the free-format part already written for CIDEAL="CSTN" or "RSOU". The corresponding keyword is **ZFRC_REL** and the free format part has to be set in this order:

.. code-block::

   ZFRC_REL
   number of forcing files
   type of forcing : ZREL2D for Z levels or PREL2D for pressure levels
   number vertical levels for the file
   date of first forcing : year (integer) month (integer) day (integer) time (real, seconds)
   name of the file with horizontal mean profile of theta, rv
   name of the advective forcing file

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

You can prescribe your own orography when CZS = "DATA" in :ref:`nam_conf_pre` in :file:`PRE_IDEA1.nam`. Only the orography corresponding to the computational domain must be provided in the free format part. For 3D orography, data are read like if it was a map (the first line is the Northern border and the first data is the North-West corner) with one line per Y-axis increment.  The corresponding keyword is **ZSDATA**.

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

For oceanic version of Meso-NH, the initial and forcing profiles of the ocean are written in the free-format part of PRE_IDEA1.nam file, where the altitude variable is the depth. To follow usual convention for ocean data, the 1D profiles are given starting from the surface (positive value). The corresponding keyword is **RSOU** and the profile and forcing information are written in the following order :

.. code-block::

   RSOU
   year month day time

.. note::

   * year has to be an integer (example : 1994)
   * month has to be an integer (example : 4)
   * day has to be an integer (example : 22)
   * time has to be a real in seconds (example : 36000. for 10 h)

.. code-block::

   kind of data used for the profile

.. note::

   Two kind are possible :
   
   * KIND="IDEALOCE" : data written in PRE_IDEA1.nam
   * KIND="STANDOCE" : data written in a NetCDF file (See set_rsou.f90 for details)

The following format is valid for KIND="IDEALOCE" :

.. code-block::

   atmospheric pressure at the surface (real, in Pascal)
   
.. warning::

   The surface corresponds to the top domain of the oceanic model.
   
.. code-block::
      
   sea surface temperature at the surface (real, in K)
   sea surface salinity at the surface (real, in g/kg)
   
   number of sea current levels (integer)
   level 1 : depth (real, m)  u-current (real, m/s)  v-current (real, m/s)
   level 2 : depth (real, m)  u-current (real, m/s)  v-current (real, m/s)
   level ...

   number of mass data levels (integer).
   level 2 : depth (real, m)  temperature (real, K), salinity (real, g/kg)
   level 3 : depth (real, m)  temperature (real, K), salinity (real, g/kg)
   level ...

   number of time-varying forcing (integer). 
 
.. warning::

   The data used to define each forcing are given sequentially in the following order (one item per line):
   
.. code-block::
   
   year month day time

.. note::

   * year has to be an integer (example : 1994)
   * month has to be an integer (example : 4)
   * day has to be an integer (example : 22)
   * time has to be a real in seconds (example : 36000. for 10 h)

.. code-block::
   
   u-stress (real, m2/s2)
   v-stress (real, m2/s2)
   heat turbulent flux (real, W/m2)
   radiative flux (real, W/m2)

.. note::

   * Surface fluxes are positive when going upward (from the ocean to the atmosphere).
   
   * In the KIND="STANDOCE" initial 1D profiles and surface fluxes(t) are read from 2 netcdf files (See set_rsou.f90 for details)
