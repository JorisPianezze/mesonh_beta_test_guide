.. _download:

Download
=============================================================================

.. note::

    The following instructions assume that you are working on a Linux machine.

Meso-NH package is developed and maintained using |git_link|.
It is strongly recommended, but not mandatory, to download Meso-NH package using :ref:`Git repository <git>`, because:

* It is easier for the Meso-NH's support team to give you some assistance in case of trouble as Git allows us to know exactly what you have changed in the original package ;

* It is easier for you to update to the last version or at least see the changes made for bug fix directly on your installation ;

* Git is strongly recommended if you intend to modify the code.

A :ref:`Tarball (from Zenodo) <tarball>` of Meso-NH package with an associated DOI is also available and can be use to cite Meso-NH in your publications.

.. |git_link| raw:: html

   <a href="https://git-scm.com/" target="_blank">Git</a>

.. _git:

Git repository
-----------------------------------------------------------------------------

Prerequisites
*****************************************************************************

To clone the Meso-NH Git repository the |gitlfs_link| extension, not included by default in the Git package, is required to handle binary (or large) files (LFS meaning Large File Storage). To install this extension:

* either, install the |gitlfs_link| package on your system (you need root access)

* or, if not possible, install it in your own environment:

  * download the git-lfs archive from the link on the |gitlfs_link| web page ;

  * extract the archive and copy the git-lfs binary in a `$HOME/bin` directory by example (create this directory if it doesn't exist) ;

  * from any directory, you can now execute:

    .. code-block:: bash

       export PATH=$PATH:$HOME/bin
       git lfs install

    that will set up some filters under the name 'lfs' in the global Git config file `$HOME/.gitconfig`.

.. |gitlfs_link| raw:: html

   <a href="https://git-lfs.github.com/" target="_blank">Git LFS</a>

Cloning
*****************************************************************************

Clone the Meso-NH Git repository from the development branch with the following command:

.. code-block:: bash
   :substitutions:

   git clone https://src.koda.cnrs.fr/mesonh/mesonh-code.git -b |MNH_branch_current| |MNH_directory_extract_current|

that will create the |MNH_directory_extract_current| directory containing a clone (copy) of the Meso-NH package on the remote developpement branch |MNH_branch_current|.

.. warning::

   This version of Meso-NH doesn't correspond to a stable version. Please continue this documentation to :ref:`check out a given version <check_out_given_version>`. However if you want to stay in this development branch you can go directly to :ref:`compilation` section.

.. _check_out_given_version:

Checking out a given version
*****************************************************************************

Once the repository is cloned, it's better for you to work on a stable version of Meso-NH (by default, you are on HEAD of the |MNH_branch_current| development branch). To go to the stable |MNH_xyz_version_current| version, you can do:

.. code-block:: bash
   :substitutions:

   cd |MNH_directory_extract_current|
   git checkout -b MYB-MNH-V|MNH_xyz_version_hyphen_current| |MNH_pack_current|

MYB-MNH-V |MNH_xyz_version_hyphen_current| is the name of the local branch you created and |MNH_pack_current| is the tag on which it is based.

.. note::

   The |MNH_pack_current| tag corresponds to the same :ref:`Tarball (from Zenodo) <tarball>` version of Meso-NH.

.. tip::

   In the future you could check and update quickly differences with the new version of the package without having to download entirely the full package. Suppose that a new version, for example "PACK-MNH-V9-8-7", is announced. To see the differences with your working copy, do:

   .. code-block:: bash

      git fetch
      git diff HEAD PACK-MNH-V9-8-7

To go to the new version, you can, for example, create a new local branch:

.. code-block:: bash

   git checkout -b MYB-MNH-V9-8-7 PACK-MNH-V9-8-7

At any time, you can also check the latest changes in the Git branch dedicated to the |MNH_xy_version_current|
version before the official release of the "bugN+1" bugfix version.

.. code-block:: bash
   :substitutions:

   git fetch
   git diff HEAD |MNH_branch_current|

And, test this development (not yet official) version by going to this branch:

.. code-block:: bash
   :substitutions:

   git checkout --track origin/|MNH_branch_current|

.. tip::

   The next step is to :ref:`compile <compilation>` Meso-NH package.

.. _tarball:

Tarball (from Zenodo)
-----------------------------------------------------------------------------

You can also download a compressed tarball containing the Meso-NH package from |zenodo_mesonh_link| .
Then untar the file MNH-V |MNH_xyz_version_hyphen_current|.tar.gz where you want :

.. code-block:: bash
   :substitutions:

   tar xvfz MNH-V|MNH_xyz_version_hyphen_current|.tar.gz

.. note::

   The archive of Meso-NH you've downloaded from Zenodo corresponds to the same tag version in the :ref:`Git repository <git>`.

.. tip::

   The next step is to :ref:`compile <compilation>` Meso-NH package.

.. |zenodo_mesonh_link| raw:: html

   <a href="https://doi.org/10.5281/zenodo.15095130" target="_blank">Meso-NH on Zenodo website</a>

What do you download ?
-----------------------------------------------------------------------------

Meso-NH's package contains sources, makefiles, pre-compiled executables, graphic tools and basic examples.

Hereafter is a very quick description of Meso-NH's tree :

.. role:: gray
   :class: text-gray
   
.. treeview::

   - :dir:`folder` |MNH_directory_extract_current|/

     - :dir:`folder` bin/ :gray:`: Miscellaneous scripts for compilation and execution`
     - :dir:`folder` conf/ :gray:`: Location of profile_mesonh files (`:ref:`compilation`:gray:`)`
     - :dir:`folder` exe/ :gray:`: Links to binary` :ref:`compiled <compilation>` :gray:`programs`
     - [-] :dir:`folder` MY_RUN/ :gray:`: Tests cases and benchmarks (`:ref:`compilation`:gray:`)`

       - :dir:`folder` BENCH/
       - :dir:`folder` INTEGRATION_CASES/
       - :dir:`folder` KTEST/
     
     - :dir:`folder` pub/ :gray:`: Public tools`
     - :dir:`folder` src/
     
       - :dir:`folder` ARCH_SRC/
       - [-] :dir:`folder` LIB/ :gray:`: External libraries (ECCODES, ECRAD, NETCDF, OASIS, ...)`
       
         - :dir:`folder` FOREFIRE/
         - :dir:`folder` MEGAN/
         - :dir:`folder` MPIvide/
         - :dir:`folder` NEWLFI/
         - :dir:`folder` Python/
         - :dir:`folder` RAD/
         - :dir:`folder` s4py/
         - :dir:`folder` SURCOUCHE/         
         - :dir:`file` eccodes-2.41.0-Source.tar.gz                        
         - :dir:`file` grib_api-1.26.0-Source.tar.gz
         - :dir:`file` hdf5-1.14.6.tar.gz
         - :dir:`file` libaec-1.1.3.tar.gz
         - :dir:`file` netcdf-c-4.9.3.tar.gz
         - :dir:`file` netcdf-cxx4-4.3.1.tar.gz
         - :dir:`file` netcdf-fortran-4.6.1.tar.gz
         - :dir:`file` oasis3-mct_5.0.tar.gz
         - :dir:`file` toy_2.0.tar.gz
         
       - :dir:`folder` MNH/ :gray:`: Meso-NH's source code`
       - :dir:`folder` ACLIB/ :gray:`: ACLIB's source code`       
       - :dir:`folder` PHYEX/ :gray:`: PHYEX's source code`
       - :dir:`folder` SURFEX/ :gray:`: SURFEX's source code`       
       - :dir:`file` configure :gray:`: Script to configure Meso-NH (`:ref:`compilation`)
       - :dir:`file` job_make_mesonh_* :gray:`: Script to` :ref:`compile <compilation>` :gray:`Meso-NH`
       - :dir:`file` job_make_examples_* :gray:`: Script to launch examples on different computers`           
       - :dir:`file` Makefile :gray:`: Script for` :ref:`compilation`
       - :dir:`file` Makefile.MESONH.mk :gray:`: Script for` :ref:`compilation`
       - :dir:`file` Rules.* :gray:`: Compiled options for various compilers`

     - :dir:`file` README_MNH_CONDA :gray:`: Instructions to install` `MNHPy <https://github.com/QuentinRodier/MNHPy>`_
     - :dir:`file` A-INSTALL :gray:`: Instructions to install Meso-NH`     
     - :dir:`file` Licence_CeCILL-C_V1-en.txt
     - :dir:`file` Licence_CeCILL-C_V1-fr.txt
     - :dir:`file` LICENSE       
     
.. note::

   * `MNHPy <https://github.com/QuentinRodier/MNHPy>`_ is a python library used to plot Meso-NH outputs.
   * ACLIB is the externalized chemistry and aerosols of Meso-NH and other models.   
   * PHYEX is the externalized atmospheric physics common to AROME and HARMONIE-AROME.
   * SURFEX is the externalized surface physics (also used in AROME and ARPEGE).

Releases
------------------------------------------------------------------------

.. csv-table:: Releases of Meso-NH
   :header: "Date", "Tarball", "Git tag", "Release note"
   :widths: 30, 40, 40, 40
   
   "16/05/2025", "`5-7-2 <https://zenodo.org/records/15698760/files/MNH-V5-7-2.tar.gz?download=1>`_", "`PACK-MNH-V5-7-2 <https://src.koda.cnrs.fr/mesonh/mesonh-code/-/tags/PACK-MNH-V5-7-2>`_", ":ref:`5-7-2 <release_note_572>`"
   "04/09/2024", "`5-7-1 <https://zenodo.org/records/15095131/files/MNH-V5-7-1.tar.gz?download=1>`_", "`PACK-MNH-V5-7-1 <https://src.koda.cnrs.fr/mesonh/mesonh-code/-/tags/PACK-MNH-V5-7-1>`_", "`5-7-1 <http://mesonh.aero.obs-mip.fr/mesonh57/Download?action=AttachFile&do=view&target=WHY_BUGFIX_571.pdf>`_"
   "11/01/2024", "`5-7-0 <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_MESONH/MNH-V5-7-0.tar.gz>`_", "`PACK-MNH-V5-7-0 <https://src.koda.cnrs.fr/mesonh/mesonh-code/-/tags/PACK-MNH-V5-7-0>`_", "`5-7-0 <http://mesonh.aero.obs-mip.fr/mesonh57/Download?action=AttachFile&do=view&target=update_from_masdev56_to_570.pdf>`_"

