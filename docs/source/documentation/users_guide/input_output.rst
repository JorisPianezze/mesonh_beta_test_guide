.. _input_output:

Output files
=============================================================================

Meso-NH writes files by group of 2:

* a descriptive part (.des) containing namelist's information (in ASCII characters)

* a netcdf part where the fields are stored. NetCDF is a self-describing, machine-independent fileformat. In Meso-NH, these files are mostly compliant with the CF conventions (version 1.7) and the COMODO extensions (version 1.4).

Three different filetypes are taken into account in the Meso-NH project:

* the synchronous backup file : contains all the values of all the fields allowing a restart of the model and of some diagnostic fields desired by the Meso-NH user. All these informations are obtained at the same instant during the simulation, hence their synchronous name.

* the diachronic file : contains time series of information requested by the Meso-NH user. They are obtained during more than one time step of the model.

* the output files. They contain only user-selected fields. They are useful, for example, if you need to output frequently some data without spending too much diskspace and too much time writing them.

Backup file
*****************************************************************************

This type of file contains only information corresponding to the same instant of the simulation, it remains open during a whole time step of the simulation, and the writing orders can be given from any routine of the model.

**The descriptive part:**
This part is the list of all the namelists of the EXSEGn.nam file. Thus, a complete description of this part is given with the :file:`EXSEGn.nam` description in chapter 9. If the file has been generated during a segment of the model integration, the .des part contains the different namelists fixing the free-parameters for the dynamics and the physics of the Meso-NH model. This allows the user to know a large part of the history of this file. For the namelists or variables ommited in the :file:`EXSEGn.nam` file, the values are set to the default ones. If the file is the result of the initialization programs (:ref:`prep_ideal_case`, :ref:`prep_real_case` or :ref:`spawning`), the values of the namelists variables are the ones of the descriptive part of the input file of the program if it does exist. Otherwise, the values are set to the default ones, except for these that can be initialized during the initialization program (e.g. :code:`CINIFILE` or :code:`LUSERV`). Note that a physiographic file does not have a descriptive part.

**The binary part:**
This type of file is in netCDF fileformat (historically LFI fileformat). It should be noted that additional fields can be added to these basic information, which have been obtained at the same instant. In order to be easily drawn by the Meso-NH graphic package, the comment field must be filled, according to the following rules:

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

.. _diachronic_file:

Time series
*****************************************************************************

A diachronic file (time-series) is a file obtained during a segment of simulation. The file directly obtained during the simulation has a name ended by .000, and contains records such as averaged variables, tendencies, fluxes stored at different times of the simulation on the whole or some parts of the domain. Such records are obtained by requesting temporal series, budgets, aircraft or balloon, profiler or station, or LES diagnostics.

On-demand outputs
*****************************************************************************

An on-demand output file is obtained at the user request. They are written at once for a given timestep. They contain only user-selected fields. They are useful, for example, if you need to output frequently some data without spending too much diskspace and too much time writing them. In contrast to the synchronous backup files, output files does not contain enough information to restart a calculation. 
Furthermore, they are not associated with a descriptive file.
