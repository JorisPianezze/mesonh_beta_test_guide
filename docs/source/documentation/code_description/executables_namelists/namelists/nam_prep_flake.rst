.. _nam_prep_flake:

NAM_PREP_FLAKE
-----------------------------------------------------------------------------

This namelist information is used to initialize the "FLAKE" sea scheme temperature.
   
.. csv-table:: NAM_PREP_FLAKE content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XTS_UNIF", "REAL", ""
   "XUNIF_T_SNOW", "REAL", "MIN(273.15,XTS_WATER)"
   "XUNIF_T_ICE", "REAL", "MIN(273.15,XTS_WATER)"
   "XUNIF_T_WML", "REAL", "MIN(273.15,XTS_WATER)"
   "XUNIF_T_BOT", "REAL", "TS_WATER or 277.15 if TS_WATER ≤ 273.15"
   "XUNIF_T_B1", "REAL", "TS_WATER-0.1 or 277.05 if TS_WATER ≤ 273.15"
   "XUNIF_CT", "REAL", "0.5"
   "XUNIF_H_SNOW", "REAL", "0.0"
   "XUNIF_H_ICE", "REAL", "0.0 or 0.01 if XTS_WATER XTS_WATER ≤ 273.15"
   "XUNIF_H_ML", "REAL", "XWATER_DEPTH or XWATER_DEPTH/2 if TS_WATER ≤ 273.15"
   "XUNIF_H_B1", "REAL", "0.0"
   "CFILE_FLAKE", "CHARACTER(LEN=28)", "CFILE in NAM_PREP_SURF_ATM"
   "CTYPE", "CHARACTER(LEN=6)", "CFILETYPE in NAM_PREP_SURF_ATM"
   "CFILEPGD_FLAKE", "CHARACTER(LEN=28)", "CFILEPGD in NAM_PREP_SURF_ATM"
   "CTYPEPGD", "CHARACTER(LEN=6)", "CFILEPGDTYPE in NAM_PREP_SURF_ATM"
   "LCLIM_LAKE", "LOGICAL", ".FALSE."
   "NYEAR", "INTEGER", ""
   "NMONTH", "INTEGER", ""
   "NDAY", "INTEGER", ""
   "XTIME", "REAL", ""
   "LWAT_SBL", "LOGICAL", ".FALSE."
   
* :code:`XTS_UNIF` : uniform prescribed value of water surface temperature supposed at an altitude of 0m (mean sea level altitude). The temperature is then modified for each point depending on its altitude, following a uniform vertical gradient of -6.5 K km-1. This prescribed value, if defined, has priority on the use of CFILE_FLAKE data.

* :code:`XUNIF_T_SNOW` : surface temperature of snow (K)

* :code:`XUNIF_T_ICE` : surface temperature at the ice-atmosphere or at the ice-snow interface (K)

* :code:`XUNIF_T_WML`: mixed-layer temperature (K)

* :code:`XUNIF_T_BOT`: water temperature at the bottom of the lake (K)

* :code:`XUNIF_T_B1`: temperature at the bottom of the upper layer of sediments (K)

* :code:`XUNIF_CT`: shape factor (thermocline)

* :code:`XUNIF_H_SNOW`: snow layer thickness (m)

* :code:`XUNIF_H_ICE`: ice layer thickness (m)

* :code:`XUNIF_H_ML`: thickness of the mixed-layer (m)

* :code:`XUNIF_H_B1`: thickness of the upper level of the active sediments (m)

* :code:`CFILE_FLAKE` / :code:`CFILEPGD_FLAKE` : name of the PREP and PGD files used to define the Sea surface Temperature. The use of a file or prescribed value XTS_WATER_UNIF has priority on the data in CFILE_FLAKE file.

* :code:`CTYPE` / :code:`CTYPEPGD` : type of the CFILE_FLAKE / CFILEPGD_FLAKE files, if the latter is provided. CTYPE / CTYPEPGD must then be given. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.
  * "GRIB ": the file type is a GRIB file, coming from any of these models:

     * "ECMWF ": european center forecast model
     * "ARPEGE": Arpege french forecast model
     * "AROME": AROME french forecast local model
     * "MOCAGE": Mocage french research chemistry model

  * "ASCII": Surfex PREP / PGD ASCII file
  * "LFI ": Surfex PREP / PGD LFI file

* :code:`LCLIM_LAKE` : to use the climatological lake database to initialise FLAKE pronostic variables.  Needs to link with LAKE_LTA_NEW.nc.

* :code:`NYEAR` : year of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read).

* :code:`NMONTH` : month of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read).

* :code:`NDAY` : day of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read).

* :code:`XTIME` : time from midnight of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read). (seconds).

* :code:`LWAT_SBL` : activates surface boundary multi layer scheme over inland water.
