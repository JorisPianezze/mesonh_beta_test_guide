Input / Output
=============================================================================

.. error:: 

   Merger ce qu'il y avait dans le user guide (que j'ai mis en dessous) avec ce qu'il y a dans le notebook https://github.com/PhilippeWautelet/2022-mesonh-io-lecture/blob/main/io_mnh.ipynb ?

The F90 namelists
*****************************************************************************

All the information required to perform a given step of a numerical experiment are provided by different files including a NAMELIST set. Thus, the Meso-NH user can change the value of the parameters without any compilation. These files provide the way for the Meso-NH user to interact with the numerical code and finally, they contain the identification cards of the different steps of the numerical experiment.

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

&NAM_LUNITn is the name of the first namelist of this file, the / character indicates the end of the list of information. These namelist parameters are defined by VAR = VALUE and these prescriptions are separated from each others by a comma and a blank character. Note that you can use more than one line to give a namelist, but in this case it is imperative to let a blank character at the end of each line.

.. tip::

   The Meso-NH user does not need to prescribe all the parameters of a namelist, the missing information are taken equal to the default values written in the Fortran code. For example, the second namelist in the previous example can be written as:

   .. code-block:: fortran

      &NAM_CONFn
        LUSERV = T
      /
   
   because the other variables of &NAM_CONFn are set to the default values.

In order to clearly separate what can be modified for a given step of a numerical experiment, we affect a different namelist file name for each executables :

.. csv-table:: List of executables and its corresponding namelist and function
   :header: "Executable", "Input namelist file", "Function"
   :widths: 30, 30, 30

   "PREP_PGD", "PRE_PGD1.nam", "Prepare horizontal grid file"
   "PREP_NEST_PGD", "PRE_NEST_PGD1.nam", "Prepare horizontal grid file for grid nesting"
   "PREP_ZOOM_PGD", "PRE_ZOOM1.nam", "Prepare a zoomed horizontal grid file"
   "PREP_IDEAL_CASE", "PRE_IDEA1.nam", "Prepare initial file for idealized simulation"
   "PREP_REAL_CASE", "PRE_REAL1.nam", "Prepare initial file for real case simulation"
   "SPAWNING", "SPAWN1.nam", "Spawn a Meso-NH file into another one with better horizontal resolution"
   "MESONH", "EXSEGn.nam", "Perform the simulation"
   "DIAG", "DIAG1.nam", "Compute diagnostic after simulation"
   "SPECTRE", "SPEC1.nam", "Compute spectra after simulation"

Because the grid-nesting technique requires the simultanous presence of multiple models in the computer memory, free-parameters must be fixed for every model. This is performed by associating a namelist file per model, this explains why the namelist are suffixed by a number 1 or n just above. The different parameters present in these files are all given in this book and more details on the description of a given parameter are present in the code itself.

Output files
*****************************************************************************

.. error::

   Il manque des informations sur les OUTPUT_LISTING0 et 1, ... ce serait pas mal d'avoir une petite explication de ce qu'il y a dans ces fichiers, CFL, temps de calcul à la fin du job, ...

Meso-NH writes files by group of 2:

* a descriptive part (.des) containing namelist's information (in ASCII characters)

* a binary part where the fields are stored. Two different fileformat are available:

  * NetCDF (files with a .nc suffix). This is the recommanded fileformat and is the default since Meso-NH 5.4.0. NetCDF is a self-describing, machine-independent fileformat. In Meso-NH, these files are mostly compliant with the CF conventions (version 1.7) and the COMODO extensions (version 1.4).
  * LFI (files with a .lfi suffix). This is the historic fileformat for Meso-NH. Its structure is a direct access type file, written and read by routines developped by Météo-France (Fischer, 1994) based on LFI routines (Clochard, 1989), which can be used on a lot of different computers. These binary files are used to store all the data necessary to run any step of a numerical experiment.

Three different filetypes are taken into account in the Meso-NH project:

* the synchronous backup file : contains all the values of all the fields allowing a restart of the model and of some diagnostic fields desired by the Meso-NH user. All these informations are obtained at the same instant during the simulation, hence their synchronous name.

* the diachronic file : contains time series of information requested by the Meso-NH user. They are obtained during more than one time step of the model. If in LFI fileformat, it is the type in which your file must be if you want to plot it with the graphics software diaprog (you can convert a synchronous file into a diachronic one with conv2dia).

* the output files. They contain only user-selected fields. They are useful, for example, if you need to output frequently some data without spending too much diskspace and too much time writing them.

The synchronous backup file
-----------------------------------------------------------------------------

This type of file contains only information corresponding to the same instant of the simulation, it remains open during a whole time step of the simulation, and the writing orders can be given from any routine of the model.

**The descriptive part**

This part is the list of all the namelists of the EXSEG$n.nam file. Thus, a complete description of this part is given with the EXSEG$n.nam description in chapter 9. If the file has been generated during a segment of the model integration, the .des part contains the different namelists fixing the free-parameters for the dynamics and the physics of the Meso-NH model. This allows the user to know a large part of the history of this file. For the namelists or variables ommited in the EXSEG$n.nam file, the values are set to the default ones (see the tables in ch.9). If the file is the result of the initialization programs (PREP_IDEAL_CASE, PREP_REAL_CASE or SPAWNING), the values of the namelists variables are the ones of the descriptive part of the input file of the program if it does exist. Otherwise, the values are set to the default ones, except for these that can be initialized during the initialization program (e.g. CINIFILE or LUSERV). Note that a physiographic file does not have a descriptive part.

**The binary part**
This type of file can be in netCDF or LFI fileformat. It should be noted that additional fields can be added to these basic information, which have been obtained at the same instant. In order to be easily drawn by the Meso-NH graphic package, the comment field must be filled, according to the following rules:

* the length of the character string is equal to 100
* the type of the supplementary field must be specified:

.. csv-table::  Variables in output
   :header: "Type", "Comment", "Field"
   :widths: 30, 30, 30
   
   "3D", "scalar", "X_Y_Z_varname (UNIT)"
   "2D", "scalar", "X_Y_varname (UNIT)"
   "3D", "vector", "VX_xvarname_VY_yvarname_VZ_zvarname (UNIT)"
   "2D", "scalar", "VX_xvarname_VY_yvarname_VZ_zvarname (UNIT) or VX_xvarname_VY_yvarname (UNIT)"
   "1D", "scalar", "Z_zvarname (UNIT)"


The diachronic file
-----------------------------------------------------------------------------

A diachronic file is a file obtained during a segment of simulation or resulting of the conversion of a synchronous file with conv2dia for graphical purposes (available only for LFI fileformat). The file directly obtained during the simulation has a name ended by .000, and contains records such as averaged variables, tendencies, fluxes stored at different times of the simulation on the whole or some parts of the domain. Such records are obtained by requesting temporal series, budgets, aircraft or balloon, profiler or station, or LES diagnostics.

The output file
-----------------------------------------------------------------------------

An output file is obtained at the user request. They are written at once for a given timestep. They contain only user-selected fields. They are useful, for example, if you need to output frequently some data without spending too much diskspace and too much time writing them. In contrast to the synchronous backup files, output files does not contain enough information to restart a calculation. Furthermore, they are not associated with a descriptive file.
