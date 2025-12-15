.. _nam_prep_surf_atm:

NAM_PREP_SURF_ATM
-----------------------------------------------------------------------------

.. warning::

   This namelist comes from SURFEX 9.0.0 user guide https://www.umr-cnrm.fr/surfex/IMG/pdf/surfex_tecdoc.pdf.

This namelist information is used to (possibly):

* initialize the date of all surface schemes. The namelist information is used only if no input data file is used, either from namelist or by fortran code (as in :program:`MESONH` program). If a file is used, the date is read in it.

* define the default file in which each scheme can read the needed data (e.g. temperature). Note that, all the information given in this namelist can be erased for each scheme by the namelist corresponding to this scheme, as the information in the shceme namelists have priority on namelist NAM_PREP_SURF_ATM.

.. csv-table:: NAM_PREP_SURF_ATM content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CFILE", "CHARACTER(LEN=28)", ""
   "CFILETYPE", "CHARACTER(LEN=6)", ""
   "CFILEPGD", "CHARACTER(LEN=28)", ""
   "CFILEPGDTYPE", "CHARACTER(LEN=6)", ""
   "NYEAR", "INTEGER", ""
   "NMONTH", "INTEGER", ""
   "NDAY", "INTEGER", ""
   "XTIME", "REAL", ""
   "NHALO_PREP", "INTEGER", "2"
   "LWRITE_EXTERN", "LOGICAL", ".FALSE."

* :code:`CFILE` / :code:`CFILEPGD` : name of the prep / pgd file used to define the date and the file in which to read the needed data (e.g. temperature).

.. note::

   * The use of a file or prescribed value in each scheme namelist has priority on the data in CFILE / CFILEPGD file of namelist NAM_PREP_SURF_ATM.
   
   * CFILE and CFILEPGD can identify the same file.
   
* :code:`CFILETYPE` / :code:`CFILEPGDTYPE` : type of the CFILE / CFILEPGD file, if the latter is provided. The following values are currently usable:

  * "MESONH": the file type is a MESONH file.
  
  * "GRIB": the file type is a GRIB file, coming from any of these models:
  
     * "ECMWF ": european center forecast model
     * "ARPEGE": Arpege french forecast model
     * "AROME": AROME french forecast local model
     * "MOCAGE": Mocage french research chemistry model
     
  * "ASCII ": ASCII Surfex PREP/PGD file
  
  * "LFI ": LFI Surfex PREP/PGD file

* :code:`NYEAR` : year of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read).

* :code:`NMONTH` : month of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read).

* :code:`NDAY` : day of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read).

* :code:`XTIME` : time from midnight of surface UTC time. It is used only if no atmospheric file or no surface file is given (in those the date can be read). (seconds).

* :code:`NHALO_PREP` : halo size for the extrapolation of pronostic fields from input file

* :code:`LWRITE_EXTERN` : The new key LWRITE_EXTERN is added. If LWRITE_EXTERN=T, soil depths for ISBA and TEB are written in the current output PREP file.
