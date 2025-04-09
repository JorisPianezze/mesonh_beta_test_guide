.. _nam_prep_teb:

NAM_PREP_TEB
-----------------------------------------------------------------------------

This namelist information is used to initialize the "TEB " urban scheme variables: road, roof and wall temperature profiles, water intercepted by roofs and roads, snow, building internal temperature.

.. csv-table:: NAM_PREP_TEB content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XWS_ROAD", "REAL", "'NONE'"
   "XWS_ROOF", "REAL", "'NONE'"
   "CFILE_WS", "CHARACTER(LEN=28)", ""
   "CTYPE_WS", "CHARACTER(LEN=6)", ""
   "XTS_ROAD", "REAL", "'NONE'"
   "XTS_ROOF", "REAL", "'NONE'"
   "XTS_WALL", "REAL", "'NONE'"
   "XTI_BLD", "REAL", "'NONE'"
   "XHUI_BLD", "REAL", "'NONE'"
   "CROAD_DIR", "CHARACTER(LEN=4)", ""
   "CWALL_OPT", "CHARACTER(LEN=4)", ""
   "CFILE_TS", "CHARACTER(LEN=28)", ""
   "CTYPE_TS", "CHARACTER(LEN=6)", ""
   "CFILE_TEB", "CHARACTER(LEN=28)", ""
   "CTYPE", "CHARACTER(LEN=6)", ""
   "CFILEPGD_TEB", "CHARACTER(LEN=28)", ""
   "CTYPEPGD", "CHARACTER(LEN=6)", ""
   "NYEAR", "INTEGER", "'NONE'"
   "NMONTH", "INTEGER", "'NONE'"
   "NDAY", "INTEGER", "'NONE'"
   "XTIME", "REAL", "'NONE'"
   "LTEB_CANOPY", "LOGICAL", ".FALSE."
   "LATM_CANOPY", "LOGICAL", ".FALSE."
   "XTDEEP_TEB", "REAL", "1.E+20"
   "XTS_BLD", "REAL", "17+XTT"

* :code:`XWS_ROAD` : uniform prescribed value of soil water interception for the road reservoir. This prescribed value, if defined, has priority on the use of CFILE_WS and CFILE_TEB data.

* :code:`XWS_ROOF` : uniform prescribed value of soil water interception for the roof reservoir. This prescribed value, if defined, has priority on the use of CFILE_WS and CFILE_TEB data.

* :code:`CFILE_WS` : name of the file used to define the soil water reservoirs. The use of a file or prescribed value of XWS_ROAD and XWS_ROOF has priority on the data in CFILE_WS file.

* :code:`CTYPE_WS` : type of the CFILE_WS file, if the latter is provided. CTYPE_WS must then be given. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.
  
  * "GRIB ": the file type is a GRIB file, coming from any of these models:

    * "ECMWF ": european center forecast model
    * "ARPEGE": Arpege french forecast model
    * "AROME": Arome french forecast local model
    * "MOCAGE": Mocage french research chemistry model
    
* :code:`XTS_ROAD` : uniform prescribed value of temperature for road, supposed at an altitude of 0m (mean sea level altitude). The temperature is then modified for each point depending on its altitude, following a uniform vertical gradient of -6.5 K km-1. This prescribed value, if defined, has priority on the use of CFILE_TS and CFILE_TEB data.

* :code:`XTS_ROOF` : uniform prescribed value of temperature for roof, supposed at an altitude of 0m (mean sea level altitude). The temperature is then modified for each point depending on its altitude, following a uniform vertical gradient of -6.5 K km-1. This prescribed value, if defined, has priority on the use of CFILE_TS and CFILE_TEB data.

* :code:`XTS_WALL` : uniform prescribed value of temperature for wall, supposed at an altitude of 0m (mean sea level altitude). The temperature is then modified for each point depending on its altitude, following a uniform vertical gradient of -6.5 K km-1. This prescribed value, if defined, has priority on the use of CFILE_TS and CFILE_TEB data.

* :code:`XTI_BLD` : uniform prescribed value of internal building temperature. This temperature is not dependent on altitude. This prescribed value, if defined, has priority on the use of CFILE_TS and CFILE_TEB data.

* :code:`XHUI_BLD` : uniform bulding relative hum (between 0-1)

* :code:`CROAD_DIR` : TEB option for road direction:

  * "UNIF" : no specific direction
  * "ORIE" : many road ORIEntations (linked to NTEB_PATCH)
  
* :code:`CWALL_OPT` : TEB option for walls:

  * "UNIF" : uniform walls
  * "TWO" : two separated walls
  
* :code:`CFILE_TS` : name of the file used to define the soil temperature profile. The use of a file or prescribed value of XTS_ROAD, XTS_ROOF, XTS_WALL, XTI_BLD or XTI_ROAD has priority on the data in CFILE_TS file.

* :code:`CTYPE_TS` : type of the CFILE_TS file, if the latter is provided. CTYPE_TS must then be given. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.
  
  * "GRIB ": the file type is a GRIB file, coming from any of these models:
  
    * "ECMWF ": european center forecast model
    * "ARPEGE": Arpege french forecast model
    * "AROME": Arome french forecast local model
    * "MOCAGE": Mocage french research chemistry model

* :code:`CFILE_TEB` / :code:`CFILEPGD_TEB` : name of the PREP/PGD files used to define any TEB variable. The use of a file or prescribed value XWS_ROAD, XWS_ROOF, XTS_ROAD, XTS_ROOF, XTS_WALL, XTI_BLD, XTI_ROAD, CFILE_WS or CFILE_TS has priority on the data in CFILE_TEB file.

* :code:`CTYPE` / :code:`CTYPEPGD` : type of the CFILE_TEB / CFILEPGD_TEB file, if the latter is provided. CTYPE must then be given. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.
  
  * "GRIB ": the file type is a GRIB file, coming from any of these models:
  
    * "ECMWF ": european center forecast model
    * "ARPEGE": Arpege french forecast model
    * "AROME": Arome french forecast local model
    * "MOCAGE": Mocage french research chemistry model

  * "ASCII ": PREP/PGD Surfex ASCII file
  
  * "LFI ": PREP/PGD Surfex LFI file
  
* :code:`NYEAR` : year of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read).

* :code:`NMONTH` : month of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read).

* :code:`NDAY` : day of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read).

* :code:`XTIME` : time from midnight of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read). (seconds).

* :code:`LTEB_CANOPY` : activates surface boundary multi layer scheme over town.

* :code:`LATM_CANOPY` : flag to replace canopy prognostic variables by atmospheric models prognostic variables

* :code:`XTDEEP_TEB` : deep temperature for TEB soil (K). XTS_BLD corresponds to the old key XTI_ROAD (before V9)

* :code:`XTS_BLD` : soil below buildings uniform temperature (K). Default value is 17+XTT (XTT for triple point temperature = 273.16K).
