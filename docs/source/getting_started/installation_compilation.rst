Installation & compilation (TD, JE & PW)
================================================


Description of Meso-NH's package
------------------------------------------------

Meso-NH's package contains sources, makefiles, pre-compiled executables, graphic tools and basic examples.

Hereafter is a very quick description of Meso-NH's tree :

* A-INSTALL : instructions to install Meso-NH,  all informations are available in this document.

* bin/ miscellaneous scripts for compilation and execution

* bin_tools/

* conf/ : location of profile_mesonh files (See Section XXX)

* exe/ : links to binary compiled programs (See Section XXX)

* LIBTOOLS/

* Licence_CeCILL-C_V1-en.txt : licence in French

* Licence_CeCILL-C_V1-fr.txt : licence in English

* LICENSE

* MY_RUN/ : ktests and benchs  (See Section XXX)

* pub/ : public tools

* README_MNH_CONDA : instructions to install https://github.com/QuentinRodier/MNHPy via conda, a python library to plot Meso-NH outputs

* src/

  * ARCH_SRC/
  
  * configure : script to configure Meso-NH (See Section XXX)
  
  * include/
  
  * job_make_examples_* : script to launch examples on different computers
  
  * job_make_mesonh_* : script to launch examples on different computers
  
  * LIB/ : location of external libraries (ECCODES, ECRAD, NETCDF, OASIS, ...)
  
  * Makefile : script for compilation
  
  * Makefile.MESONH.mk : script for compilation
  
  * MNH/ : Meso-NH source code
  
  * PHYEX/ : PHYEX source code, externalized atmospheric physics common to AROME and HARMONIE-AROME
  
  * Rules.* : compiled options for different compilers
  
  * SURFEX/ : SURFEX source code

.. csv-table:: Description of the Meso-NH's package
   :header: "Tree", "Description"
   :widths: 30, 30

   "A-INSTALL", "Instructions to install Meso-NH"
   "bin/", "Miscellaneous scripts for compilation and execution"
   "bin_tools/", ""
   "conf/", "location of profile_mesonh files (See Section XXX)"
   "exe/", "links to binary compiled programs (See Section XXX)"
   "LIBTOOLS/", ""
   "Licence_CeCILL-C_V1-en.txt", "licence in French"
   "Licence_CeCILL-C_V1-fr.txt", "licence in English"
   "LICENSE", ""
   "MY_RUN/", "ktests and benchs  (See Section XXX)"
   "pub/", "public tools"
   "README_MNH_CONDA", "instructions to install https://github.com/QuentinRodier/MNHPy via conda, a python library to plot Meso-NH outputs"
   "src/ARCH_SRC/", ""
   "src/configure", "script to configure Meso-NH (See Section XXX)"
   "src/include/", ""
   "src/job_make_examples_*", "script to launch examples on different computers"
   "src/job_make_mesonh_*", "script to launch examples on different computers"
   "src/LIB/", "location of external libraries (ECCODES, ECRAD, NETCDF, OASIS, ...)"
   "src/Makefile", "script for compilation"
   "src/Makefile.MESONH.mk", "script for compilation"
   "src/MNH/", "Meso-NH source code"
   "src/PHYEX/", "PHYEX source code, externalized atmospheric physics common to AROME and HARMONIE-AROME"
   "src/Rules.*", "compiled options for different compilers"
   "src/SURFEX/", "SURFEX source code"


Configuring the Meso-NH package
*****************************************************************************

For the installation process, you could now use the `./configure` script like this:

.. code-block:: bash

   cd ~/MNH-V5-7-1/src
   ./configure
   . ../conf/profile_mesonh

This will create a configuration file `profile_mesonh` with an extension reflecting the different choices made automatically to match the computer on which you want to install Meso-NH.

.. warning::

  On GENCI, ECMWF, Meteo-France and some supercomputers, the './configure' script is tuned to identify the machine on which the command is run. For them, the compiler, MPI and netCDF libraries are automatically chosen.

  To install this version on one of these machines, go to go to Section XXX (COMPILING/INSTALLING ON GENCI & ECMWF & METEO COMPUTERS).

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

Then, you have to source the generated file before compiling the code:

.. code-block:: bash
   . ../conf/profile_mesonh-LXifx-R8I4-MNH-V5-7-1-MPIINTEL-O2

.. note::

   - The options specific to the architecture and compiler such as `OPTLEVEL` are defined inside the `Rules.${ARCH}.mk` files.
   - The options specific to the MPI library (`VER_MPI`) are defined inside `Makefile.MESONH.mk` **is it correct? est-ce qu'il y a aussi des options pour les bibli dans les Rules?**
   - There are also options for the netCDF library (see the `VER_CDF` variable)
   - If needed, for adaptation to your requirements, look inside the files and changes options for your needs.
   - On a Linux PC, if you need to compile the MPI library, look at the "MesonhTEAM Wiki" to know `how to compile the OpenMPI library with MESONH <http://mesonh.aero.obs-mip.fr/mesonh57/MesonhTEAMFAQ/PC_Linux>`_ **A remplacer par un nouveau lien, texte pas à jour**

Compiling and installing the Meso-NH package
*****************************************************************************
