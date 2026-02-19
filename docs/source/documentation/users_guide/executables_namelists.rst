.. _executables_and_namelists:

Executables & Namelists
=============================================================================

In the following subsection, you can find the list of compiled executables and its corresponding namelists :

.. toctree::
   :maxdepth: 1

   executables_namelists/prep_pgd.rst
   executables_namelists/prep_nest_pgd.rst
   executables_namelists/prep_ideal_case.rst
   executables_namelists/prep_real_case.rst
   executables_namelists/spawning.rst
   executables_namelists/mesonh.rst
   executables_namelists/diag.rst
   executables_namelists/spectre.rst
   executables_namelists/latlon_to_xy.rst
   executables_namelists/cdf2cdf.rst
   executables_namelists/prep_surfex.rst

All the information required to launch a given executable are located in a F90 namelist file. The Meso-NH user can change the value of the parameters without any compilation. These files provide the way for the Meso-NH user to interact with the numerical code and finally, they contain the identification cards of the different steps of the numerical experiment.

The information are written in the following form:

.. code-block:: fortran

   &NAM_LUNITn
     CINIFILE = "INIFILE"
   /

   &NAM_CONFn
     LUSERV = T,
     LUSERC = F,
     LUSERR = F,
     LUSERI = F,
     LUSERS = F,
     LUSERG = F,
     LUSERH = F,
     NSV    = 0
   /

:code:`&NAM_LUNITn` is the name of the first namelist of this file, the / character indicates the end of the list of information. These namelist parameters are defined by :code:`VAR = VALUE` and these prescriptions are separated from each others by a comma and a blank character. Note that you can use more than one line to give a namelist, but in this case it is imperative to let a blank character at the end of each line.

.. tip::

   The Meso-NH user does not need to prescribe all the parameters of a namelist, the missing information are taken equal to the default values written in the Fortran code. For example, the second namelist in the previous example can be written as:

   .. code-block:: fortran

      &NAM_CONFn
        LUSERV = T
      /
   
   because the other variables of :code:`&NAM_CONFn` are set to the default values.

In order to clearly separate what can be modified for a given step of a numerical experiment, we affect a different namelist file name for each executables :

.. csv-table:: List of executables and its corresponding namelist and function
   :header: "Executable", "Input namelist file", "Function"
   :widths: 30, 30, 30

   "PREP_PGD", "PRE_PGD1.nam", "Prepare horizontal grid file"
   "PREP_NEST_PGD", "PRE_NEST_PGD1.nam", "Prepare horizontal grid file for grid nesting"
   "PREP_IDEAL_CASE", "PRE_IDEA1.nam", "Prepare initial file for idealized simulation"
   "PREP_REAL_CASE", "PRE_REAL1.nam", "Prepare initial file for real case simulation"
   "SPAWNING", "SPAWN1.nam", "Spawn a Meso-NH file into another one with better horizontal resolution"
   "MESONH", "EXSEGn.nam", "Perform the simulation"
   "DIAG", "DIAG1.nam", "Compute diagnostic after simulation"
   "SPECTRE", "SPEC1.nam", "Compute spectra after simulation"

Because the grid-nesting technique requires the simultaenous presence of multiple models in the computer memory, free-parameters must be fixed for every model. This is performed by associating a namelist file per model, this explains why the namelist are suffixed by a number 1 or n just above. The different parameters present in these files are all given in this book and more details on the description of a given parameter are present in the code itself.
