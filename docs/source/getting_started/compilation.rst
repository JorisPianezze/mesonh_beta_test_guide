Compilation
=============================================================================

Principles
*****************************************************************************

.. warning::

   * This subsection is just for your information, please go to the dedicated following subection to configure and compile your code.

During the first Meso-NH's compilation, almost all the numerical schemes and all the physical parameterizations are compiled and it is then in namelist (during simulations) that we choose the type of numerical scheme and physical parameterization. In the Meso-NH language, we say that we compile the **MASTER**. This compilation is quite long, more than 20 minutes in 1 core in O2.

When you want to modify the code contained in the Meso-NH's package, you create a folder containing the modified code and you compile only the modified code: in the Meso-NH language we say that we compile the **VER_USER**. This compilation is shorter than the MASTER one, it depends on how many sources are modified.

For the configuration and the compilation processes, you will use following commands :

.. code-block:: bash

   cd ~/MNH-VX-Y-Z/src
   ./configure
   . ../conf/profile-mesonh
   make
   make installmaster

.. note::

   * :file:`configure` script will create a :ref:`configuration` file :file:`profile_mesonh` in conf/ directory with an extension reflecting the different choices made automatically to match the computer on which you want to install Meso-NH.
   
   * :file:`make` will compile the code
   
   * :file:`make installmaster` will link the compiled executables in the exe directory (cf List of compiled executable). Need to be done only one time by "version".

   * the object files "*.o" and main executables of the Meso-NH's package are compiled in one step and created in the directory src/dir_obj-your_configuration/MASTER
   
      * the lib.*.a is only created and removed at the link phase this allows a parallel compilation of the sources ...
      
      * The name "dir obj..." depends on the different environment variables set by the "profile_mesonh" which you have loaded before the compilation. This allows by loading different "profile mesonh ..." files to compile in the same source/installation directory different versions of Meso-NH, with different compilers, different versions of MPI, different USER sources ...
      
.. note::

   To have information about compiled executables, go to :ref:`executables_and_namelists`.

.. tip::

   On GENCI, ECMWF, Meteo-France and some supercomputers, the configure script is tuned to identify the machine on which the command is run. For them, the compiler, MPI and NetCDF libraries are automatically chosen.

   * To verify if the supercomputer you are using is recognized by :file:`configure` script, look at the :command:`case` condition in the :file:`configure` script to find your configuration :
   
   .. code-block:: bash
   
      TARG=$(uname -s -n)
      #
      case "$TARG" in

   * If you do not have sufficient space in your $HOME directory, install the whole package directly on the $WORKDIR. The name of the $WORKDIR differs in the differents computer center, most of them manage disk space throw 'multi-projet' with only one unique login.

     .. warning::

        Think to do a backup of your installation. $WORKDIR space is not everytime purged but a crash disk could/will probably occur !!!      
 
   * Due to limitation in time and memory on interactive connection, in some computer you have to compile the Meso-NH's package in batch mode with the different 'src/job_make_mesonh*' files.

.. _compilation_jeanzay_idris:

On Jean-Zay (IDRIS)
*****************************************************************************      

The compilation can be do in interactive :

.. code-block:: bash

   cd MNH-V5-7-1/src
   ./configure
   . ../conf/profile_mesonh-LXifort-R8I4-MNH-V5-7-0-MPIINTEL-O2
   make -j16 |& tee error$XYZ
   make installmaster

You can also use the “compil” partition :

.. code-block:: bash

   sbatch job_make_mesonh_HPE_jeanzay
   
To run the test case examples, do :

.. code-block:: bash

   sbatch -A {your_projet}@cpu job_make_examples_BullX_jeanzay

.. _compilation_adastra_cines:

On ADASTRA (CINES)
*****************************************************************************  

Install the PACKAGE in your $HOME (default 50Go of quota) and compile in interactive mode :

.. code-block:: bash

   cd MNH-V5-7-1/src
   . ../conf/profile_mesonh-LXifort-R8I4-MNH-V5-7-1-MPIINTEL-O2
   make -j16 |& tee error$XYZ
   make installmaster

To run the test case examples, do :

.. code-block:: bash

   sbatch job_make_examples_BullX_occigen

.. _compilation_irene_tgcc:

On IRENE (TGCC)
***************************************************************************** 

At TGCC, you have two architectures accessible throw 2 differents frontals but with a commun disk space, for both install Meso-NH in your $CCCHOME (default 20Go of quota) and compile in interactive mode :

* On intel Skylake, do:

.. code-block:: bash

   cd MNH-V5-7-1/src
   ./configure
   . ../conf/profile_mesonh-LXifort-R8I4-MNH-V5-7-0-MPIAUTO-O2
   make -j16 |& tee error$XYZ
   make installmaster

* On intel AMD, do :

.. code-block:: bash

   cd MNH-V5-7-1/src
   ./configure   
   . ../conf/profile_mesonh-LXifort-R8I4-MNH-V5-7-0-AMD-MPIAUTO-O2
   make -j16 |& tee error$XYZ
   make installmaster

To run the test case examples, do :

* On intel Skylake :

.. code-block:: bash

   ccc msub job_make_examples_BullX_irene

* On intel Knl :

.. code-block:: bash

   ccc msub -q knl job_make_examples_BullX_irene

* On intel AMD :

.. code-block:: bash

   ccc msub job_make_examples_BullX_irene_AMD
   
.. _compilation_hpc_ecmwf:

On hpc-login (ECMWF)
***************************************************************************** 

To compile Meso-NH's package go to $HPCPERM directory and connect to an interactive compute node and compile the code (16 core 16GO of memory) :

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
***************************************************************************** 

Due to limitation in time memory on interactive connection, compile Meso-NH in batch mode with :

.. code-block:: bash

   cd MNH-V5-7-1/src
   ./configure
   sbatch job_make_mesonh_BullX_belenos

This job does "gmake -j 4", then "make installmaster".

To run test case examples, do :

.. code-block:: bash

   sbatch job_make_examples_BullX_belenos
     
.. _compilation_olympe_calmip:
     
On Olympe (CALMIP)
***************************************************************************** 

Compile in interactive mode using :

.. code-block:: bash

   cd MNH-V5-7-1/src
   ./configure
   . ../conf/profile-mesonh
   make
   make installmaster

To run test case examples, do :

.. code-block:: bash

   sbatch job_make_examples_BullX_olympe

.. _compilation_unknown_computer:

On unknown computer
***************************************************************************** 

If you are installing Meso-NH on an unknown computer, to configure the Meso-NH package, there are 3 main environment variables that can be set:

- `ARCH`: the architecture to use (OS + compiler, default is `LXgfortran` for Linux with gfortran compiler)
- `VER_MPI`: the version of MPI to use (default is `MPIVIDE` for no parallel run)
- `OPTLEVEL`: the level of optimization for the compiler (default is `DEBUG` for development purpose, debugging and fast compilation)

If needed, you can change the default values of these environment variables. For example, if you want to use the Intel compiler `ifx`` with the Intel MPI library and an optimisation level of `-O2`, you can run the following commands:

.. code-block:: bash

   export ARCH=LXifort
   export VER_MPI=MPIAUTO
   export OPTLEVEL=O2
   ./configure

.. note::

   - The options specific to the architecture and compiler such as `OPTLEVEL` are defined inside the `Rules.${ARCH}.mk` files.
   - The options specific to the MPI library (`VER_MPI`) are defined inside `Makefile.MESONH.mk` **is it correct? est-ce qu'il y a aussi des options pour les bibli dans les Rules?**
   - There are also options for the netCDF library (see the `VER_CDF` variable)
   - If needed, for adaptation to your requirements, look inside the files and changes options for your needs.
   - On a Linux PC, if you need to compile the MPI library, look at the "MesonhTEAM Wiki" to know `how to compile the OpenMPI library with MESONH <http://mesonh.aero.obs-mip.fr/mesonh57/MesonhTEAMFAQ/PC_Linux>`_ **A remplacer par un nouveau lien, texte pas à jour**

Compile the code :

.. code-block:: bash

   . ../conf/profile-mesonh-your_configuration
   make
   make installmaster


.. note::

   The compilation will take about 20 minutes on modern PC-Linux ... If you have a multi-processor machine you can speedup the compilation, for example on four cores, with:

   .. code-block:: bash
 
      make -j 4

Clean previous compiled version
***************************************************************************** 

If you have already compiled exactly the same version of Meso-NH on this computer (same $XYZ value) you have first to clean this version with

.. code-block:: bash

   make cleanmaster

.. note::

   This will delete the dir-obj $XYZ directory and all the preprocessed sources contained on it.

Compile with additional libraries (FOREFIRE, RTTOV, ECRAD, MEGAN, OASIS, ...)
***************************************************************************** 

MNH_FOREFIRE for forefire runs ( external package needed)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

If you want to use coupled (inline) run with FOREFIRE and MESONH you could compile the interfaced/coupling routine by activating this variable before any compilation :

.. code-block:: bash

   export MNH_FOREFIRE=1.0

and then the configure and compile the code :

.. code-block:: bash

   ./configure
   make
   make installmaster
   
The FOREFIRE API package himself must be compiled independently from Meso-NH. The git repository is here https://github.com/forefireAPI/firefront/tree/2014.01 it could be cloned with :

.. code-block:: bash

   git clone -b 2014.01 https://github.com/forefireAPI/firefront.git

It depend on netcdf and scons for is compilation the 'libForeFIre.so' generate must by referenced in the LD_LIBRARY_PATH or move/linked to the exe directory of Meso-NH.

.. _compile_mesonh_with_rttov:

MNH_RTTOV for optional radiative computation
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The RTTOV 13.2 package was not included into the open source version of Meso-NH because it needs a licence agrement.
Run the "configure" script preceded with the setting of the MNH_RTTOV variable:

.. code-block:: bash

   cd MNH.../src/
   export MNH_RTTOV=1
   export VER_RTTOV=13.2

Download the RTTOV package rttov132.tar.xz by following the instructions given on RTTOW website. Install the RTTOV package rttov132.tar.xz :

.. code-block:: bash

   cd MNH.../src/LIB
   mkdir RTTOV-13.2
   cd RTTOV-13.2
   tar xJf rttov132.tar.xz
   cd build

edit Makefile.local and set HDF5 PREFIX, FFLAGS HDF5 and LDFLAGS HDF5 as shown below :

.. code-block:: bash

   HDF5_PREFIX = $(SRC_MESONH)/src/dir_obj${XYZ}/MASTER/NETCDF-${VERSION_CDFF}
   FFLAGS_HDF5 = -D_RTTOV_HDF $(FFLAG_MOD)$(HDF5_PREFIX)/include
   LDFLAGS_HDF5 = -L$(HDF5_PREFIX)/lib64 -lhdf5hl_fortran -lhdf5_hl -lhdf5_fortran -lhdf5 -lsz -laec -lz -ldl

and build RTTOV :

.. code-block:: bash

   cd src
   ../build/Makefile.PL RTTOV_HDF=1
   make ARCH=ifort

.. note::

   Other available options are gfortran, NAG, pgf90 and IBM.

Then, you can follow the steps described in the section dedicated to your computer (interactive or batch mode).

MNH_ECRAD for optional compilation of new ECRAD radiative library from ECMWF
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

The default version of ECRAD is 1.4.0 (open-source). To use ECRAD, do :

.. code-block:: bash

   export MNH_ECRAD=1
   ./configure

The version of ECRAD is set by (by default):

.. code-block:: bash

   export VER_ECRAD=140

The full ECRAD package 1.0.1 was not included into the open source version of Meso-NH because it needs a licence agrement. See here to get the licence and full sources https://software.ecmwf.int/wiki/display/ECRAD/ECMWF+Radiation+Scheme+Home

.. note::

   Some of the files modified for MNH are included in the directory $SRC MESONH/src/LIB/RAD/ecrad-1.0.1_mnh.
   
Install the ECRAD package ecrad-1.0.1.tar.gz in the MNH tree directory :

.. code-block:: bash

   cd ${SRC_MESONH}/src/LIB/RAD
   tar xvfz ecrad-1.0.1.tar.gz
   
To use this version of ECRAD, do :

.. code-block:: bash

   export MNH_ECRAD=1
   export VER_ECRAD=101
   ./configure
   
To compile Meso-NH with ECRAD, you can follow the steps described in the section dedicated to
your computer (interactive or batch mode). To use ECRAD during a simulation, replace RAD=’ECMW’ by RAD=’ECRA’ in EXSEG1.nam and
add link to all “ecrad-1.X.X/data” files in your Meso-NH run directory :

.. code-block:: bash

   ln -sf ${SRC_MESONH}/src/LIB/RAD/ecrad-1.X.X/data/* .
   
.. note::

   You can replace CDATADIR = “.” by CDATADIR = “data” of ini radiations ecrad.f90 to link only the data folder instead of all the files one by one. See MY RUN/KTEST/007 16janvier/008 run2 test case for example.
   
MNH_MEGAN for optional compilation of MEGAN code
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

To use MEGAN, do :

.. code-block:: bash

   export MNH_MEGAN=1
   ./configure

To compile Meso-NH with MEGAN, you can follow th steps described in the section dedicated to your computer (interactive or batch mode).

Compile with modified and/or new sources
*****************************************************************************

Now you can generate and recompile your own sources.

Prepare your source directory
-----------------------------------------------------------------------------

Suppose you want to create a MY_MODIF version of Meso-NH. Put your own sources in a subdirectory src/MY_MODIF. All subdirectories in MY_MODIF will be scanned during compilation process. So if you want, you could make a subdirectory for each component of the Meso-NH's package, by example :

.. code-block:: bash

   cd MY_MODIF
   mkdir MNH
   mkdir SURFEX
   cp ../MNH/mesonh.f90 MNH/
   cp ../SURFEX/isba.f90 SURFEX/
   
.. tip::

   In this subdirectory, put only fortran source you want to compile !!! Don't use it as a trash with old sources file like :file:`mysource.f90.old` or :file:`tar` files. All spirituous file will confuse the :file:`make` command.

Configure with modified sources
-----------------------------------------------------------------------------

Logout of the current session to be sure to unset all the environment variables loaded with the your MASTER :file:`profile_mesonh`. Login again and:

* set the environment variable VER USER to the name of your user directory (MY_MODIF, by example),
* set also the optional environment variable ARCH, VER MPI... you want to use, has to be the same as the MASTER

and run again the :file:`configure` command

.. code-block:: bash

   export VER_USER=MY_MODIF
   ./configure

This will regenerate the :file:`profile_mesonh` file and a copy of this with the $VER USER information.

Compile with modified sources
-----------------------------------------------------------------------------

Now you can compile with the :file:`make user` command in interactive with

.. code-block:: bash

   . ../conf/profile_mesonh...${VER_USER}...
   make user
   make installuser
   
or in batch mode using script you used to cpompiler the MASTER. For belenos, by example, use the script job_make_mesonh_user_BullX_belenos to compile your own sources.
   
.. note::

   * This will compile only your sources and the files depending on your sources and generate the new executables in your own directory dir_obj-your_configuration/${VER_USER}
   * The "make installuser" needs to be done only one time by version. And run the examples. Your version should appear in the name of the used executables.
   * Before compiling your own sources be sure that these ones are younger than the ”*.o” files of the MASTER directory. If any doubt, at any time use the command (on your sources, and only on yours do that!!!) :

   .. code-block:: bash 
   
      touch *.f*
