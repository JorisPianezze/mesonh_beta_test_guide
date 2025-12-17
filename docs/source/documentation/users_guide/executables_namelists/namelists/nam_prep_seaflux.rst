.. _nam_prep_seaflux:

NAM_PREP_SEAFLUX
-----------------------------------------------------------------------------

.. warning::

   This namelist comes from SURFEX 9.0.0 user guide https://www.umr-cnrm.fr/surfex/IMG/pdf/surfex_tecdoc.pdf.

This namelist information is used to initialize the "SEAFLX" sea scheme temperature.

.. csv-table:: NAM_PREP_SEAFLUX content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XSST_UNIF", "REAL", ""
   "CFILE_SEAFLX", "CHARACTER(LEN=28)", ""
   "CTYPE_SEAFLX", "CHARACTER(LEN=6)", ""
   "CFILEPGD_SEAFLX", "CHARACTER(LEN=28)", ""
   "CTYPEPGD", "CHARACTER(LEN=6)", ""
   "CFILEWAVE_SEAFLX", "CHARACTER(LEN=28)", ""
   "CTYPEWAVE", "CHARACTER(LEN=6)", ""
   "NYEAR", "INTEGER", ""
   "NMONTH", "INTEGER", ""
   "NDAY", "INTEGER", ""
   "XTIME", "REAL", ""
   "LSEA_SBL", "LOGICAL", ".FALSE."
   "LOCEAN_MERCATOR", "LOGICAL", ".FALSE."
   "LOCEAN_CURRENT", "LOGICAL", ".FALSE."
   "XTIME_REL", "REAL", "25920000.0"
   "LCUR_REL", "LOGICAL", ".FALSE."
   "LTS_REL", "LOGICAL", ".FALSE."
   "LZERO_FLUX", "LOGICAL", ".FALSE."
   "LCORR_FLUX", "LOGICAL", ".FALSE."
   "XCORFLX", "REAL", "0.0"
   "LDIAPYC", "LOGICAL", ".FALSE."
   "CSEAICE_SCHEME", "CHARACTER(LEN=6)", ""
   "XSSS_UNIF", "REAL", "1.E+20"
   "XSIC_UNIF", "REAL", "1.E+20"

* :code:`XSST_UNIF` : uniform prescribed value of Sea Surface Temperature. This prescribed value, if defined, has priority on the use of CFILE_SEAFLX data.

* :code:`CFILE_SEAFLX` / :code:`CFILEPGD_SEAFLX` : name of the PREP/PGD files used to define the Sea surface Temperature. The use of a file or prescribed value XSST_UNIF has priority on the data in CFILE_SEAFLX file.

* :code:`CTYPE_SEAFLX` / :code:`CTYPEPGD` : type of the CFILE_SEAFLX / CFILEPGD_SEAFLX files, if the latter is provided. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.
  
  * "GRIB": the file type is a GRIB file, coming from any of these models:
  
    * "ECMWF ": european center forecast model
    * "ARPEGE": Arpege french forecast model
    * "AROME": AROME french forecast local model
    * "MOCAGE": Mocage french research chemistry model

  * "NETCDF": the file type is a NETCDF file, coming from MERCATOR (possible only for CTYPE_SEAFLX)

  * "ASCII ": PREP/PGD Surfex ASCII file
  
  * "LFI ": PREP/PGD Surfex LFI file

* :code:`CFILEWAVE_SEAFLX` : name of the file used to define the significant wave height (Hs) and the peak period (Tp)

* :code:`CTYPEWAVE` : type of the CFILEWAVE_SEAFLX file if the latter is provided. CTYPEWAVE must be given. The ‘NETCDF’ value (if the file type is a netcdf file) is the only one usable. Other ‘PREP_SEAFLUX’ types are under development and lead now to uniform values of wave parameters.

* :code:`NYEAR` : year of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read).

* :code:`NMONTH` : month of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read).

* :code:`NDAY` : day of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read).

* :code:`XTIME` : time from midnight of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read). (seconds).

* :code:`LSEA_SBL` : activates surface boundary multi layer scheme over sea.

* :code:`LOCEAN_MERCATOR` : oceanic variables initialized from MERCATOR if T

* :code:`LOCEAN_CURRENT` : initial ocean state with current (if F ucur=0, vcur=0)

* :code:`XTIME_REL` : time of relaxation (s)

* :code:`LCUR_REL` : flag for relaxation on current

* :code:`LTS_REL` : flag for relaxation on ocean temperature

* :code:`LZERO_FLUX` : flag for testing zero incoming flux at the ocean surface

* :code:`LCORR_FLUX` : flag for flux correction

* :code:`XCORFLX` : correction coefficient for surface fluxes

* :code:`LDIAPYC` : flag for diapycnal mixing activation

* :code:`XSSS_UNIF` : from V8, uniform prescribed value of Sea Surface Salinity. This prescribed value, if defined, has priority on the use of CFILE_SEAFLX data.

* :code:`CSEAICE_SCHEME` : from V8, name of the sea-ice scheme to activate.

* :code:`XSIC_UNIF` : uniform sea ice covert fraction
