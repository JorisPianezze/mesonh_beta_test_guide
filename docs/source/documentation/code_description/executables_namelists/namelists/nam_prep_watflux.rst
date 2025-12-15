.. _nam_prep_watflux:

NAM_PREP_WATFLUX
-----------------------------------------------------------------------------

.. warning::

   This namelist comes from SURFEX 9.0.0 user guide https://www.umr-cnrm.fr/surfex/IMG/pdf/surfex_tecdoc.pdf.

This namelist information is used to initialize the "WATFLX" sea scheme temperature.

.. csv-table:: NAM_PREP_WATFLUX content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XTS_WATER_UNIF", "REAL", ""
   "CFILE_WATFLX", "CHARACTER(LEN=28)", ""
   "CTYPE", "CHARACTER(LEN=6)", ""
   "CFILEPGD_WATFLX", "CHARACTER(LEN=28)", ""
   "CTYPEPGD", "CHARACTER(LEN=6)", ""
   "NYEAR", "INTEGER", ""
   "NMONTH", "INTEGER", ""
   "NDAY", "INTEGER", ""
   "XTIME", "REAL", ""
   "LWAT_SBL", "LOGICAL", ".FALSE."

* :code:`XTS_WATER_UNIF` : uniform prescribed value of water surface temperature supposed at an altitude of 0m (mean sea level altitude). The temperature is then modified for each point depending on its altitude, following a uniform vertical gradient of -6.5 K km-1. This prescribed value, if defined, has priority on the use of CFILE_WATFLX data.

* :code:`CFILE_WATFLX` / :code:`CFILEPGD_WATFLX` : name of the PREP / PGD files used to define the Sea surface Temperature. The use of a file or prescribed value XTS_WATER_UNIF has priority on the data in CFILE_WATFLX file.

* :code:`CTYPE` / :code:`CTYPEPGD` : type of the CFILE_WATFLX / CFILEPGD_WATFLX file, if the latter is provided. CTYPE / CTYPEPGD must then be given. The following values are currently usable:

   * "MESONH": the file type is a MESONH file.
   
   * "GRIB": the file type is a GRIB file, coming from any of these models:

     * "ECMWF ": european center forecast model
     * "ARPEGE": Arpege french forecast model
     * "AROME": AROME french forecast local model
     * "MOCAGE": Mocage french research chemistry model

   * "ASCII ": PREP / PGD Surfex ASCII file

   * "LFI ": PREP/PGD Surfex LFI file
   
* :code:`NYEAR` : year of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read).

* :code:`NMONTH` : month of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read).

* :code:`NDAY` : day of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read).

* :code:`XTIME` : time from midnight of surface UTC time (seconds). It is used only if no atmospheric file or no surface file is given (in those the date can be read). 

* :code:`LWAT_SBL` : activates surface boundary multi layer scheme over inland water.
