.. _nam_prep_isba:

NAM_PREP_ISBA
-----------------------------------------------------------------------------

.. csv-table:: NAM_PREP_ISBA content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CFILE_ISBA", "CHARACTER(LEN=28)", ""
   "CTYPE", "CHARACTER(LEN=6)", ""
   "CFILEPGD_ISBA", "CHARACTER(LEN=28)", ""
   "CTYPEPGD", "CHARACTER(LEN=6)", ""
   "XHUG_SURF", "REAL", "'NONE'"
   "XHUG_ROOT", "REAL", "'NONE'"
   "XHUG_DEEP", "REAL", "'NONE'"
   "XHUGI_SURF", "REAL", "'NONE'"
   "XHUGI_ROOT", "REAL", "'NONE'"
   "XHUGI_DEEP", "REAL", "'NONE'"
   "CFILE_HUG_SURF", "CHARACTER(LEN=28)", ""
   "CFILE_HUG_ROOT", "CHARACTER(LEN=28)", ""
   "CFILE_HUG_DEEP", "CHARACTER(LEN=28)", ""
   "CFILE_HUG", "CHARACTER", ""
   "CTYPE_HUG", "CHARACTER(LEN=6)", ""
   "XTG_SURF", "REAL", "'NONE'"
   "XTG_ROOT", "REAL", "'NONE'"
   "XTG_DEEP", "REAL", "'NONE'"
   "CFILE_TG_SURF", "CHARACTER(LEN=28)", ""
   "CFILE_TG_ROOT", "CHARACTER(LEN=28)", ""
   "CFILE_TG_DEEP", "CHARACTER(LEN=28)", ""
   "CFILE_TG", "CHARACTER(LEN=28)", ""
   "CTYPE_TG", "CHARACTER(LEN=6)", ""
   "NYEAR", "INTEGER", "'NONE'"
   "NMONTH", "INTEGER", "'NONE'"
   "NDAY", "INTEGER", "'NONE'"
   "XTIME", "REAL", "'NONE'"
   "LISBA_CANOPY", "LOGICAL", ".FALSE."
   "LEXTRAP_TG", "LOGICAL", ".FALSE."
   "LEXTRAP_WG", "LOGICAL", ".FALSE."
   "LEXTRAP_WGI", "LOGICAL", ".FALSE."
   "LEXTRAP_SN", "LOGICAL", ".FALSE."

* :code:`CFILE_ISBA` / :code:`CFILEPGD_ISBA` : name of the PREP / PGD files used to define any ISBA variable. The use of a file or prescribed value XHUG_SURF, XHUG_ROOT, XHUG_DEEP, XTG_SURF, XTG_ROOT, XTG_DEEP, CFILE_WG and CFILE_TG has priority on the data in CFILE_ISBA file.

* :code:`CTYPE` / :code:`CTYPEPGD` : type of the CFILE_ISBA / CFILEPGD_ISBA files, if the latter is provided. CTYPE / CTYPEPGD must then be given. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.

  * "GRIB ": the file type is a GRIB file, coming from any of these models:
  
    * "ECMWF ": european center forecast model
    * "ARPEGE": Arpege french forecast model
    * "AROME": AROME french forecast local model
    * "MOCAGE": Mocage french research chemistry model

  * "ASCII ": PREP/PGD Surfex ASCII file
  
  * "LFI ": PREP/PGD Surfex LFI file
  
* :code:`XHUG_SURF` : uniform prescribed value of liquid soil water index (SWI) for the surface soil layer. This prescribed value, if defined, has priority on the use of CFILE_HUG and CFILE_ISBA data.

* :code:`XHUG_ROOT` : uniform prescribed value of liquid soil water index (SWI) for the root zone soil layer(s). This prescribed value, if defined, has priority on the use of CFILE_HUG and CFILE_ISBA data.

* :code:`XHUG_DEEP` : uniform prescribed value of liquid soil water index (SWI) for the deep soil layer(s). This prescribed value, if defined, has priority on the use of CFILE_HUG and CFILE_ISBA data.

* :code:`XHUGI_SURF` : uniform prescribed value of ice soil water index (SWI) for the surface soil layer. This prescribed value, if defined, has priority on the use of CFILE_HUG and CFILE_ISBA data.

* :code:`XHUGI_ROOT` : uniform prescribed value of ice soil water index (SWI) for the root zone soil layer(s). This prescribed value, if defined, has priority on the use of CFILE_HUG and CFILE_ISBA data.

* :code:`XHUGI_DEEP` : uniform prescribed value of ice soil water index (SWI) for the deep soil layer(s). This prescribed value, if defined, has priority on the use of CFILE_HUG and CFILE_ISBA data.

* :code:`CFILE_HUG_SURF` : name of the file used to define the liquid soil water index (SWI) for the surface soil layer.

* :code:`CFILE_HUG_ROOT` : name of the file used to define the liquid soil water index (SWI) for the root zone soil layer(s).

* :code:`CFILE_HUG_DEEP` : name of the file used to define the liquid soil water index (SWI) for the deep soil layer(s).

* :code:`CFILE_HUG` : name of the file used to define the soil water profiles. 

.. warning::

   The use of a file or prescribed value of XHUG_SURF, XHUG_ROOT and XHUG_DEEP has priority on the data in CFILE_HUG file.

* :code:`CTYPE_HUG` : type of the CFILE_HUG file, if the latter is provided. CTYPE_HUG must then be given. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.

  * "GRIB ": the file type is a GRIB file, coming from any of these models:

    * "ECMWF ": european center forecast model
    * "ARPEGE": Arpege french forecast model
    * "AROME": AROME french forecast local model
    * "MOCAGE": Mocage french research chemistry model

  * "ASCII / LFI ": PREP file from Surfex
  
  * "ASCLLV": ASCII latlonval file (one file for each depth)
  
  * "NETCDF": netcdf standard file (one variable by depth)
  
* :code:`XTG_SURF` : uniform prescribed value of temperature for the surface soil layer, supposed at an altitude of 0m (mean sea level altitude). The temperature is then modified for each point depending on its altitude, following a uniform vertical gradient of -6.5 K km-1. This prescribed value, if defined, has priority on the use of CFILE_TG and CFILE_ISBA data.

* :code:`XTG_ROOT` : uniform prescribed value of temperature for the root zone soil layer(s), supposed at an altitude of 0m (mean sea level altitude). The temperature is then modified for each point depending on its altitude, following a uniform vertical gradient of -6.5 K km-1. This prescribed value, if defined, has priority on the use of CFILE_TG and CFILE_ISBA data.

* :code:`XTG_DEEP` : uniform prescribed value of temperature for the deep soil layer(s), supposed at an altitude of 0m (mean sea level altitude). The temperature is then modified for each point depending on its altitude, following a uniform vertical gradient of -6.5 K km-1. This prescribed value, if defined, has priority on the use of CFILE_TG and CFILE_ISBA data.

* :code:`CFILE_TG_SURF` : name of the file used to define the surface soil temperature profile.

* :code:`CFILE_TG_ROOT` : name of the file used to define the root zone soil temperature profile.

* :code:`CFILE_TG_DEEP` : name of the file used to define the deep soil temperature profile.

* :code:`CFILE_TG` : name of the file used to define the soil temperature profile. The use of a file or prescribed value of XTG_SURF, XTG_ROOT and XTG_DEEP has priorityon the data in CFILE_TG file.

* :code:`CTYPE_TG` : type of the CFILE_TG file, if the latter is provided. CTYPE_TG must then be given. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.

  * "GRIB ": the file type is a GRIB file, coming from any of these models:
  
    * "ECMWF ": european center forecast model
    * "ARPEGE": Arpege french forecast model
    * "AROME": AROME french forecast local model
    * "MOCAGE": Mocage french research chemistry model
    
  * "ASCII / LFI ": PREP file from Surfex

  * "ASCLLV": ASCII latlonval file (one file for each depth)
  
  * "NETCDF": netcdf standard file (one variable by depth)
  
* :code:`NYEAR` : year of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read).

* :code:`NMONTH` : month of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read).

* :code:`NDAY` : day of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read).

* :code:`XTIME` : time from midnight of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read). (seconds).

* :code:`LISBA_CANOPY` : activates surface boundary multi layer scheme over vegetation.

* :code:`LEXTRAP_TG` : extrapolate TG points where LSM < 0.5 (buffer only)

* :code:`LEXTRAP_WG` : extrapolate WG points where LSM < 0.5 (buffer only)

* :code:`LEXTRAP_WGI` : extrapolate WGI points where LSM < 0.5 (buffer only)

* :code:`LEXTRAP_SN` : extrapolate SNOW (SWE/depth) points where LSM < 0.5 (buffer only)
