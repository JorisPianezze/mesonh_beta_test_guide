Compile
*****************************************************************************

Principle
=============================================================================

.. warning::

   * This subsection is just for your information, please go to the dedicated subsection depending on the computer you want to use to configure and compile your code.

During the first Meso-NH compilation, almost all the numerical schemes and all the physical parameterizations are compiled.
The numerical scheme and physical parameterizations are chosen in namelist files read at the start of the simulations.
In the Meso-NH language, we say that we compile the **MASTER** version. This compilation is quite long,
typically more than 20 minutes on one core.

When you want to modify the code contained in the Meso-NH package, you create a folder containing the modified
code and you compile only the modified code.
In the Meso-NH language, we say that we compile a **VER_USER** version. This compilation is shorter than the
MASTER one, it depends on how many sources are modified.

For the configuration and compilation processes, you will use following commands:

.. code-block:: bash

   cd ~/MNH-VX-Y-Z/src
   ./configure
   export MAKE_FLAGS='-j 8' # optional, to speed up the compilation on up to 8 processes/cores
   . ../conf/profile-mesonh
   make
   make installmaster

.. note::

   * :file:`configure`, script that creates a :ref:`configuration` file :file:`profile_mesonh` in the conf/ directory with an extension reflecting the different choices made automatically to match the computer on which you install Meso-NH.

   * export MAKE_FLAGS='-j 8', optional command to speed up the compilation on up to 8 parallel processes. You can change the number of processes according to the number of cores available for the compilation. If you do not set this variable, the default value is 1 process.

   * :file:`make`, command that compiles the code

   * :file:`make installmaster`, command that links the compiled executables in the exe directory (cf List of compiled executables). Need to be done only one time by "version".

.. note::

   The object files :file:`*.o` and main executables of the Meso-NH package are compiled in one step and created in the directory src/dir_obj-your_configuration/MASTER

   * the :file:`lib.*.a` is only created and removed at the link phase. This allows a parallel compilation of the sources.

   * The name "dir obj..." depends on the different environment variables set by the :file:`profile_mesonh` that you have loaded before the compilation. This allows, by loading different :file:`profile mesonh` files, to compile in the same source/installation directory different versions of Meso-NH with different compilers, versions of MPI, **VER_USER**...

.. note::

   To get information about the compiled executables, go to :ref:`executables_and_namelists`.

.. tip::

   On GENCI (IDRIS, CINES and TGCC/CCRT), ECMWF, Meteo-France and some other supercomputers, the configure script is tuned to automatically identify the machine on which the command is run. For them, the compiler, MPI and NetCDF libraries and optimisation settings are automatically chosen. If necessary, these settings can be modified (see :ref:`compilation_unknown_computer`).

   * To check if the supercomputer you are using is recognized by the :file:`configure` script, look at the :command:`case` condition in the :file:`configure` script to find your configuration:

   .. code-block:: bash

      TARG=$(uname -s -n)
      #
      case "$TARG" in

   * If you do not have sufficient space in your $HOME directory, install the whole package directly on the $WORKDIR. The name of the $WORKDIR differs in the differents computer centers.

     .. warning::

        Consider backing up your installation. The $WORKDIR space is not typically backed up, and on some systems, it may be purged after a while. File system failures with file loss can occur.

   * Due to limitation in time and memory on the interactive shell of some systems, you could have to compile the Meso-NH package in batch mode. Jobs are provided for some computers in the different :file:`src/job_make_mesonh*` files.

Compile on different systems
=============================================================================

.. _compilation_jeanzay_idris:

On Jean-Zay (IDRIS)
-----------------------------------------------------------------------------

The compilation can be done in interactively using the following commands:

..
   .. code-block:: bash
.. parsed-literal::

   cd |MNH_directory_extract_current|/src
   ./configure
   . ../conf/profile_mesonh-LXifort-R8I4-MNH-V\ |MNH_xyz_version_hyphen_current|-MPIINTEL-O2
   make -j16 |& tee error$XYZ
   make installmaster

You can also use the “compil” partition:

.. code-block:: bash

   sbatch job_make_mesonh_HPE_jeanzay

To run the test case examples, do:

.. code-block:: bash

   sbatch -A {your_projet}@cpu job_make_examples_BullX_jeanzay


.. _compilation_adastra_cines:

On Adastra (CINES)
-----------------------------------------------------------------------------

Install the Meso-NH package in your $HOME (default 50GB of quota) and compile in interactive mode:

..
   .. code-block:: bash
.. parsed-literal::

   cd |MNH_directory_extract_current|/src
   ./configure
   . ../conf/profile_mesonh-LXifort-R8I4-MNH-V\ |MNH_xyz_version_hyphen_current|-MPIINTEL-O2
   make -j16 |& tee error$XYZ
   make installmaster

To run the test case examples, do:

.. code-block:: bash

   sbatch job_make_examples_BullX_occigen


.. _compilation_irene_tgcc:

On Irene (TGCC)
-----------------------------------------------------------------------------

At TGCC, you have two architectures accessible through 2 differents frontals but with a common filesystem. To install Meso-NH in your $CCCHOME (default 20GB of quota) and compile in interactive mode:

* On Intel Skylake nodes, do:

..
   .. code-block:: bash
.. parsed-literal::

   cd |MNH_directory_extract_current|/src
   ./configure
   . ../conf/profile_mesonh-LXifort-R8I4-MNH-V\ |MNH_xyz_version_hyphen_current|-MPIAUTO-O2
   make -j16 |& tee error$XYZ
   make installmaster

* On AMD nodes, do:

..
   .. code-block:: bash
.. parsed-literal::

   cd |MNH_directory_extract_current|/src
   ./configure
   . ../conf/profile_mesonh-LXifort-R8I4-MNH-V\ |MNH_xyz_version_hyphen_current|-AMD-MPIAUTO-O2
   make -j16 |& tee error$XYZ
   make installmaster

To run the test case examples, do:

* On Intel Skylake nodes:

.. code-block:: bash

   ccc msub job_make_examples_BullX_irene

* On intel AMD nodes:

.. code-block:: bash

   ccc msub job_make_examples_BullX_irene_AMD


.. _compilation_hpc_ecmwf:

On hpc-login (ECMWF)
-----------------------------------------------------------------------------

To the compile Meso-NH package, go to the $HPCPERM directory, connect to an interactive compute node
and compile the code (16 cores, 16GB of memory):

.. code-block:: bash

   ecinteractive -c16 -m 16G -t 12:00:00
   ./configure
   . ../profile_mesonh-your_configuration
   make
   make installmaster

To run test case examples, do :

.. code-block:: bash

   sbatch job_make_examples_Atos_HPCF


.. _compilation_belenos_meteofrance:

On belenos (Meteo-France)
-----------------------------------------------------------------------------

Due to limitation in time and memory in interactive shell, Meso-NH has to be compiled in batch mode:

..
   .. code-block:: bash
.. parsed-literal::

   cd |MNH_directory_extract_current|/src
   ./configure
   sbatch job_make_mesonh_BullX_belenos

This job does "gmake -j 4", then "make installmaster".

To run test case examples, do:

.. code-block:: bash

   sbatch job_make_examples_BullX_belenos


.. _compilation_olympe_calmip:

On Olympe (CALMIP)
-----------------------------------------------------------------------------

Compile in interactive mode using:

..
   .. code-block:: bash
.. parsed-literal::

   cd |MNH_directory_extract_current|/src
   ./configure
   . ../conf/profile-mesonh
   make
   make installmaster

To run test case examples, do:

.. code-block:: bash

   sbatch job_make_examples_BullX_olympe


.. _compilation_unknown_computer:

On other systems
-----------------------------------------------------------------------------

If you are installing Meso-NH on an unknown computer (not predefined in the :file:`configure` script),
there are 3 main environment variables that can be set to configure the Meso-NH package:

- `ARCH`: the architecture to use (OS + compiler, default is `LXgfortran` for Linux with gfortran compiler)
- `VER_MPI`: the version of MPI to use (default is `MPIVIDE` for no parallel run)
- `OPTLEVEL`: the level of optimization for the compiler (default is `DEBUG` for development purpose, debugging and fast compilation)

If needed, you can change the default values of these environment variables. For example, if you want to use the Intel compiler `ifx` with the Intel MPI library and an optimisation level of `-O2`, you can run the following commands:

.. code-block:: bash

   export ARCH=LXifx
   export VER_MPI=MPIAUTO
   export OPTLEVEL=O2
   ./configure

.. note::

   - The options specific to the architecture and compiler such as `OPTLEVEL` are defined inside the :file:`Rules.${ARCH}.mk` files.
   - The options specific to the MPI library (`VER_MPI`) are defined inside `Makefile.MESONH.mk`
   - There are also options for the netCDF library (see the `VER_CDF` variable). `CDFAUTO`, the recommended and default option, compiles and uses the netCDF library included in the Meso-NH package.
   - If needed, for adaptation to your requirements, look inside the files and changes options.
   - On a Linux PC, if you need to compile the MPI library, look at the "MesonhTEAM Wiki" to know `how to compile the OpenMPI library with MESONH <http://mesonh.aero.obs-mip.fr/mesonh57/MesonhTEAMFAQ/PC_Linux>`_ **A remplacer par un nouveau lien, texte pas à jour**

Compile the code :

.. code-block:: bash

   . ../conf/profile-mesonh-your_configuration
   export MAKE_FLAGS='-j 8' # optional, to speed up the compilation on up to 8 processes/cores
   make
   make installmaster


.. tip::

   The compilation takes about 20 minutes on one core. To speedup the compilation, set the environment variable `MAKE_FLAGS` to the number of cores you want to use.


Clean previous compiled version
=============================================================================

If you have already compiled the same version of Meso-NH on this computer (same $XYZ value), you first have to clean it with:

.. code-block:: bash

   make cleanmaster

.. note::

   This will delete the dir-obj$XYZ directory content with all the preprocessed sources contained in it.


Compile with additional libraries (FOREFIRE, RTTOV, ECRAD, MEGAN, OASIS...)
=============================================================================

MNH_FOREFIRE for forefire runs (external package needed)
-----------------------------------------------------------------------------

If you want to use coupled (inline) run with FOREFIRE and MESONH you could compile the interfaced/coupling routine by activating this variable before any compilation:

.. code-block:: bash

   export MNH_FOREFIRE=1

and then configure and compile the code:

.. code-block:: bash

   ./configure
   export MAKE_FLAGS='-j 8' # optional, to speed up the compilation on up to 8 processes/cores
   make
   make installmaster

The |forefire_link| package must be compiled independently from Meso-NH. It can cloned with:

.. code-block:: bash

   git clone https://github.com/forefireAPI/firefront.git

It depend on netCDF and scons for its compilation. The :file:`libForeFIre.so` that has been generated must be referenced either by adding its path to the LD_LIBRARY_PATH environment variable or by moving or linking it to the :file:`exe/` directory of Meso-NH.

.. |forefire_link| raw:: html

   <a href="https://github.com/forefireAPI/firefront.git" target="_blank">FOREFIRE API</a>


.. _compile_mesonh_with_rttov:

MNH_RTTOV for optional radiative computation
-----------------------------------------------------------------------------

The RTTOV 13.2 package was not included into the open source version of Meso-NH because it needs a licence agrement.
Run the "configure" script preceded with the setting of the MNH_RTTOV variable:

.. code-block:: bash

   cd MNH/src/
   export MNH_RTTOV=1
   export VER_RTTOV=13.2

Download the RTTOV package :file:`rttov132.tar.xz` by following the instructions given on the RTTOV website. Install the RTTOV package :file:`rttov132.tar.xz`:

.. code-block:: bash

   cd MNH/src/LIB
   mkdir RTTOV-13.2
   cd RTTOV-13.2
   tar xJf rttov132.tar.xz
   cd build

edit :file:`Makefile.local` and set HDF5_PREFIX, FFLAGS_HDF5 and LDFLAGS_HDF5 as shown below:

.. code-block:: bash

   HDF5_PREFIX = $(SRC_MESONH)/src/dir_obj${XYZ}/MASTER/NETCDF-${VERSION_CDFF}
   FFLAGS_HDF5 = -D_RTTOV_HDF $(FFLAG_MOD)$(HDF5_PREFIX)/include
   LDFLAGS_HDF5 = -L$(HDF5_PREFIX)/lib64 -lhdf5hl_fortran -lhdf5_hl -lhdf5_fortran -lhdf5 -lsz -laec -lz -ldl

and build RTTOV:

.. code-block:: bash

   cd src
   ../build/Makefile.PL RTTOV_HDF=1
   make ARCH=ifort

.. note::

   Other available options are gfortran, NAG, pgf90 and IBM.

Then, you can follow the steps described in the section dedicated to your computer (interactive or batch mode).


MNH_ECRAD for optional compilation of new ECRAD radiative library from ECMWF
-----------------------------------------------------------------------------

The default version of ECRAD is 1.4.0 (open-source) and is provided in the Meso-NH package. To use ECRAD, do:

.. code-block:: bash

   export MNH_ECRAD=1
   ./configure

The version of ECRAD is set by (by default):

.. code-block:: bash

   export VER_ECRAD=140

If you want to use a different version of ECRAD, you can set the environment variable `VER_ECRAD` to the desired version number. But you must have the corresponding ECRAD package installed in the Meso-NH source directory.

.. note::

   ECRAD has been tailored to Meso-NH. The modified files are included in the directory :file:`${SRC_MESONH}/src/LIB/RAD/ecrad-1.4.0_mnh`.

To compile Meso-NH with ECRAD, you can follow the steps described in the section dedicated to
your computer (interactive or batch mode). To use ECRAD during a simulation, replace RAD=’ECMW’ by RAD=’ECRA’ in EXSEG1.nam and
add link to all “ecrad-1.X.X/data” files in your Meso-NH run directory:

.. code-block:: bash

   ln -sf ${SRC_MESONH}/src/LIB/RAD/ecrad-1.X.X/data/* .

.. tip::

   You can replace CDATADIR = “.” by CDATADIR = “data” of ini radiations ecrad.f90 to link only the data folder instead of all the files one by one. See :file:`MY_RUN/KTEST/007_16janvier/008_run2` test case for example.


MNH_MEGAN for optional compilation of MEGAN code
-----------------------------------------------------------------------------

To use MEGAN, do:

.. code-block:: bash

   export MNH_MEGAN=1
   ./configure

To compile Meso-NH with MEGAN, you can follow the steps described in the section dedicated to your computer (interactive or batch mode).


Compile with modified and/or new sources
=============================================================================
Now you can generate and recompile your own sources.

Prepare your source directory
-----------------------------------------------------------------------------

Suppose you want to create a MY_MODIF version of Meso-NH. First, put your own sources in a subdirectory :file:`src/MY_MODIF`. All subdirectories in MY_MODIF will be scanned during the compilation process. So if you want, you could make a subdirectory for each component of the Meso-NH package, for example:

.. code-block:: bash

   cd MY_MODIF
   mkdir MNH
   mkdir SURFEX
   cp ../MNH/mesonh.f90 MNH/
   cp ../SURFEX/isba.f90 SURFEX/

.. caution::

   In this subdirectory, put only fortran source you want to compile. Don't use it as a trash with old sources file like :file:`mysource.f90.old` or :file:`tar` files. All unexpected file types could confuse the :file:`make` command.


Configure with modified sources
-----------------------------------------------------------------------------

Logout of the current session to be sure to unset all the environment variables loaded with the your MASTER :file:`profile_mesonh`. Login again and:

* set the environment variable VER USER to the name of your user directory (MY_MODIF, for example),
* set also the optional environment variable ARCH, VER MPI... you want to use (they need to be the same as the MASTER)

and run again the :file:`configure` command:

.. code-block:: bash

   export VER_USER=MY_MODIF
   ./configure

This generates a :file:`profile_mesonh` file with the $VER USER information.


Compile with modified sources
-----------------------------------------------------------------------------

Now you can compile with the :file:`make user` command in interactive with:

.. code-block:: bash

   . ../conf/profile_mesonh...${VER_USER}...
   make user
   make installuser

or in batch mode using the script you used to compile the MASTER. For belenos, for example, use the script job_make_mesonh_user_BullX_belenos to compile your own sources.

.. note::

   * This will compile only your sources and the files depending on your sources and generate the new executables in your own directory :file:`dir_obj-your_configuration/${VER_USER}`
   * The "make installuser" needs to be done only one time by version. When you run the examples, your version should appear in the name of the used executables.
   * Before compiling your own sources be sure that these ones are younger than the ”*.o” files of the MASTER directory. If any doubt, at any time use the command on your sources ,and only on yours:

   .. code-block:: bash

      touch *.f*
