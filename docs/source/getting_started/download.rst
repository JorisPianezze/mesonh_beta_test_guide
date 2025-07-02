.. _download:

Download
=============================================================================

.. note::

    The following instructions assume that you are working on a Linux machine.

Meso-NH package is developed and maintained using |git_link|.
It is strongly recommended, but not mandatory, to download Meso-NH package using :ref:`git <git>`, because:

* It is easier for the Meso-NH support team to give you some assistance in case of trouble... as Git allows us to know exactly what you have changed in the original package ;

* It is easier for you to update to the last version...  or at least see the changes made for bug fix directly on our installation ;

* Git is strongly recommended if you intend to modify the code.

A :ref:`tarball <tarball>` of Meso-NH package is available.

.. |git_link| raw:: html

   <a href="https://git-scm.com/" target="_blank">Git</a>

.. _git:

Git repository
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


Clone the Meso-NH Source repository from the developpement branch |MNH_branch_current| with the following command:

..
  PW: J'ai remplacé les code-block par des parsed-literal pour rendre possible la
      substitution qui n'est pas possible dans 1 code-block
      mais le syntax highligting est perdu...
  .. code-block:: bash
.. parsed-literal::

   git clone https://src.koda.cnrs.fr/mesonh/mesonh-code.git -b |MNH_branch_current| |MNH_directory_extract_current|

that will create the |MNH_directory_extract_current| directory containing a clone (copy) of the Meso-NH package on the remote developpement branch |MNH_branch_current|.

.. tip::

   The next step is to :ref:`configure <configuration>` of the Meso-NH package.


Checking out a given version
*****************************************************************************

Once the repository is cloned, it's better for you to checkout your own branch (by default, you are on HEAD of the |MNH_branch_current| development branch). To create your local branch corresponding to the |MNH_xyz_version_current| version, type:

..
   .. code-block:: bash
.. parsed-literal::

   cd |MNH_directory_extract_current|
   git checkout -b MYB-MNH-V\ |MNH_xyz_version_hyphen_current| |MNH_pack_current|

MYB-MNH-V\ |MNH_xyz_version_hyphen_current| is the name of the local branch you created and |MNH_pack_current| is the remote/origin tag on which it is based. The advantage of this way of downloading the package is that in the future you could check and update quickly differences with the new version of the package without having to download entirely the full package.

Suppose that a new version, for example "PACK-MNH-V9-8-7", is announced. To see the differences
with your working copy, do:

.. code-block:: bash

   git fetch
   git diff HEAD PACK-MNH-V9-8-7

To go to the new version, you can, for example, create a new local branch:

.. code-block:: bash

   git checkout -b MYB-MNH-V9-8-7 PACK-MNH-V9-8-7

At any time, you can also check the latest changes in the Git branch dedicated to the |MNH_xy_version_current|
version before the official release of the "bugN+1" bugfix version.

..
   .. code-block:: bash
.. parsed-literal::

   git fetch
   git diff HEAD |MNH_branch_current|

And, test this development (not yet official) version by going to this branch:

..
   .. code-block:: bash
.. parsed-literal::

   git checkout --track origin/|MNH_branch_current|

.. tip::

   The next step is to :ref:`configure <configuration>` of the Meso-NH package.

.. _tarball:

Tarball (from Zenodo)
-----------------------------------------------------------------------------

You can download a compressed tarball containing the Meso-NH package from |zenodo_mesonh_link| .

Then untar the file MNH-V\ |MNH_xyz_version_hyphen_current|.tar.gz where you want to.
For example, in your home directory:

..
   .. code-block:: bash
.. parsed-literal::

   cd
   tar xvfz  MNH-V\ |MNH_xyz_version_hyphen_current|.tar.gz

.. tip::

   The next step is to :ref:`configure <configuration>` of the Meso-NH package.

.. |zenodo_mesonh_link| raw:: html

   <a href="https://doi.org/10.5281/zenodo.15095130" target="_blank">Meso-NH on Zenodo website</a>

.. note::

  A conserver ?

   * If you will modify the code, go to Section XXX.

   * Some basic Git commands are presented in Appendice XXX.


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
   "src/SURFEX/", "SURFEX's source code, externalized surface physics (also used in AROME and ARPEGE)"

Releases
------------------------------------------------------------------------

Tarball of releases are available following the links below. A release note describes the change from the previous version.

.. toctree::
   :maxdepth: 1

   releases/release_note_572.rst

.. csv-table:: Releases of Méso-NH
   :header: "Date", "Tarball", "Release note"
   :widths: 30, 40, 40
   
   "16/05/2025", "`5-7-2 <https://zenodo.org/records/15698760/files/MNH-V5-7-2.tar.gz?download=1>`_", ":ref:`release_note_572 <release_note_572>`"
   "04/09/2024", "`5-7-1 <https://zenodo.org/records/15095131/files/MNH-V5-7-1.tar.gz?download=1>`_", "`Note <http://mesonh.aero.obs-mip.fr/mesonh57/Download?action=AttachFile&do=view&target=WHY_BUGFIX_571.pdf>`_"
   "11/01/2024", "`5-7-0 <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_MESONH/MNH-V5-7-0.tar.gz>`_", "`Note <http://mesonh.aero.obs-mip.fr/mesonh57/Download?action=AttachFile&do=view&target=update_from_masdev56_to_570.pdf>`_"


.. error::
    * mettre tous les liens vers les releases et notes vers zenodo (quand sera dispo)
