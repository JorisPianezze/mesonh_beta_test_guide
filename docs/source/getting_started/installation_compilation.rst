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

