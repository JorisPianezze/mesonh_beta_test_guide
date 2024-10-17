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

Get Meso-NH's package
------------------------------------------------

Meso-NH package is developed and maintained using Git [#git]_.
It is now strongly recommended, but not mandatory, for all users to download Meso-NH package using Git (Section XXX), because:

* It's more easy for us (Meso-NH support's team) to give you some assistance in case of trouble... as Git permits us to know exactly what you have changed in the original package ;

* It's much more easy for you to update to the last version...  or at least see the change made for bug fix directly on our installation.

However, if you are allergic to Git, you can still download a tarball of Meso-NH package (Section XXX).

.. [#git] https://git-scm.com/

Download a tarball of Meso-NH (for basic users ; not recommended)
*****************************************************************************

If you are a basic user of Meso-NH, you can download a tarball containing Meso-NH package. With your preferred web browser go to the `Meso-NH's website <http://mesonh.aero.obs-mip.fr/mesonh>`_ and click on **Download** link on the left part or you can directly download the last validated version of Meso-NH via http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_MESONH/MNH-V5-7-1.tar.gz.
Then untar the file MNH-V5-7-1.tar.gz where you want to.
For example, in your home directory:

.. code-block:: bash

   cd
   tar xvfz MNH-V5-7-1.tar.gz

Next step is to configure Meso-NH package, for that go to Section XXX.


Download via git (for users only ; highly recommended)
*****************************************************************************

.. note::

   * If you will modify the code, go to Section XXX.
   
   * Some basic Git commands are presented in Appendice XXX.
   
   
Prerequisites
++++++++++++++++++++++++++++++++++++++++

In order to clone the Meso-NH git repository the git LFS extension is required to handle binary (or large) files (LFS meaning Large File Storage). So before starting, be sure:

* to have git v1.8.2 or higher installed on your workstation. You can run and check with:

.. code-block:: bash

   git --version

* to install the git LFS extension (not included by default in the Git package :

  * get the linux git-lfs archive from the 'Download v1.X.Y (Linux)' link on the web page https://git-lfs.github.com/
  
  * extract the archive and copy the git-lfs binary in your `$HOME/bin` (the provided install.sh script doesn't need to be executed)
  
  * execute the following command if it's not already in your `$HOME/.bash_profile`: `export PATH=$PATH:$HOME/bin`
  
  * from any directory, you can now execute:

.. code-block:: bash

   git lfs install

that will set up some filters under the name 'lfs' in the global Git config file `$HOME/.gitconfig`.


Before cloning
++++++++++++++++++++++++++++++++++++++++

...

