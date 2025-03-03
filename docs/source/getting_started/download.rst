Download
=============================================================================

.. note::

    The following instructions assume that you are working on a Linux machine.

Meso-NH package is developed and maintained using |git_link|.
It is now strongly recommended, but not mandatory, for all users to download Meso-NH package using :ref:`git <git>`, because:

* It's easier for us (Meso-NH support's team) to give you some assistance in case of trouble... as Git allows us to know exactly what you have changed in the original package ;

* It's much easier for you to update to the last version...  or at least see the changes made for bug fix directly on our installation ;

* Git is strongly recommended if you intend to modify the code.

However, if you are allergic to Git, you can still download a :ref:`tarball <tarball>` of Meso-NH package.

.. |git_link| raw:: html

   <a href="https://git-scm.com/" target="_blank">Git</a>

.. _git:

Git (highly recommended)
-----------------------------------------------------------------------------

Prerequisites
*****************************************************************************

In order to clone the Meso-NH git repository the Git LFS extension is required to handle binary (or large) files (LFS meaning Large File Storage). So before starting, be sure:

To install the Git LFS extension (not included by default in the Git package):

* either, install the Git LFS package on your system (you need root access)

* or, if not possible, install it in your own environment

  * get the git-lfs archive from the 'Download vX.Y.Z' link on the web page |gitlfs_link|

  * extract the archive and copy the git-lfs binary in your `$HOME/bin` (the provided install.sh script doesn't need to be executed)

  * add the following command if it's not already in your `$HOME/.bash_profile`: `export PATH=$PATH:$HOME/bin`

  * from any directory, you can now execute:

.. code-block:: bash

   git lfs install

that will set up some filters under the name 'lfs' in the global Git config file `$HOME/.gitconfig`.

.. |gitlfs_link| raw:: html

   <a href="https://git-lfs.github.com/" target="_blank">Git LFS</a>

.. error::

   * C'est toujours utile ?


Cloning
*****************************************************************************


Clone the Meso-NH Source repository from the developpement branch MNH-57-branch with the following command:

.. code-block:: bash

   git clone https://src.koda.cnrs.fr/mesonh/mesonh-code.git -b MNH-57-branch MNH-V5-7-1

that will create the MNH-V5-7-1 directory containing a clone (copy) of the Meso-NH package on the remote developpement branch MNH-57-branch.

.. tip::

   The next step is to :ref:`configure <configuration>` of the Meso-NH package.

.. error::

   * Faire le lien entre cette section et celle du depot zenodo
   
   * plutot que de recuperer la branche MNH-57-branch il faudrait plutot recuperer le tag MNH-V5-7-1 non ?

Checking out a given version
*****************************************************************************

Once the repository is cloned, it's better for you to checkout your own branch (by default, you are on HEAD of the MNH-57-branch development branch). To create your local branch corresponding to the V5-7-1 version, type:

.. code-block:: bash

   cd MNH-V5-7-1
   git checkout -b MYB-MNH-V5-7-1 PACK-MNH-V5-7-1

MYB-MNH-V5-7-1 is the name of the local branch you created and PACK-MNH-V5-7-1 is the remote/origin tag on which it is based. The advantage of this way of downloading the package is that in the future you could check and update quickly differences with the new version of the package without having to download entirely the full package.

Suppose that a new version, for example "PACK-MNH-V5-7-1", is announced. To see the differences
with your working copy, do:

.. code-block:: bash

   git fetch
   git diff HEAD PACK-MNH-V5-7-1

To go to the new version, you can, for example, create a new local branch:

.. code-block:: bash

   git checkout -b MYB-MNH-V5-7-1 PACK-MNH-V5-7-1

At any time, you can also check for "uptodate" changes in the Git branch dedicated to the MNH57
version before the official release of the "bugN+1" bugfix version.

.. code-block:: bash

   git fetch
   git diff HEAD MNH-57-branch

And, test this development (not yet official) version by going to this branch:

.. code-block:: bash

   git checkout --track origin/MNH-57-branch

.. tip::

   The next step is to :ref:`configure <configuration>` of the Meso-NH package.

.. _tarball:

Tarball (not recommended)
-----------------------------------------------------------------------------

You can also download a tarball containing Meso-NH's package. With your preferred web browser go to the |mesonh_link| and click on **Download** link on the left part. Alternatively, you can directly download the last validated version of Meso-NH `here <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_MESONH/MNH-V5-7-1.tar.gz>`_.

Then untar the file MNH-V5-7-1.tar.gz where you want to.
For example, in your home directory:

.. code-block:: bash

   cd
   tar xvfz MNH-V5-7-1.tar.gz

.. tip::

   The next step is to :ref:`configure <configuration>` of the Meso-NH package.

.. |mesonh_link| raw:: html

   <a href="http://mesonh.aero.obs-mip.fr/mesonh" target="_blank">Meso-NH's website</a>

.. note::

  A conserver ?

   * If you will modify the code, go to Section XXX.

   * Some basic Git commands are presented in Appendice XXX.

.. error::

   * Remplacer tous les liens vers l'ancien site mesonh par un depot zenodo.

What do you download ?
-----------------------------------------------------------------------------

Meso-NH's package contains sources, makefiles, pre-compiled executables, graphic tools and basic examples.

Hereafter is a very quick description of Meso-NH's tree :

.. csv-table:: Description of the Meso-NH's package
   :header: "Tree", "Description"
   :widths: 30, 30

   "A-INSTALL", "Instructions to install Meso-NH"
   "bin/", "Miscellaneous scripts for compilation and execution"
   "bin_tools/", ""
   "conf/", "Location of profile_mesonh files (:ref:`configuration`)"
   "exe/", "Links to binary :ref:`compiled <compilation>` programs"
   "LIBTOOLS/", ""
   "Licence_CeCILL-C_V1-en.txt", "Licence in French"
   "Licence_CeCILL-C_V1-fr.txt", "Licence in English"
   "LICENSE", ""
   "MY_RUN/", "Ktests and benchmarks (:ref:`compilation`)"
   "pub/", "Public tools"
   "README_MNH_CONDA", "Instructions to install https://github.com/QuentinRodier/MNHPy via conda, a python library to plot Meso-NH outputs"
   "src/ARCH_SRC/", ""
   "src/configure", "Script to configure Meso-NH (:ref:`configuration`)"
   "src/include/", ""
   "src/job_make_examples_*", "Script to launch examples on different computers"
   "src/job_make_mesonh_*", "Script to :ref:`compile <compilation>` Meso-NH on different computers"
   "src/LIB/", "Mocation of external libraries (ECCODES, ECRAD, NETCDF, OASIS, ...)"
   "src/Makefile", "Script for :ref:`compilation`"
   "src/Makefile.MESONH.mk", "Script for :ref:`compilation`"
   "src/MNH/", "Meso-NH's source code"
   "src/PHYEX/", "PHYEX's source code, externalized atmospheric physics common to AROME and HARMONIE-AROME"
   "src/Rules.*", "Compiled options for various compilers"
   "src/SURFEX/", "SURFEX's source code"
