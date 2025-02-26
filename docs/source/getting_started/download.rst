Download (TD, PW)
================================================

.. note::

    The following instructions assume that you are working on a Linux machine.



Meso-NH package is developed and maintained using |git_link| .
It is now strongly recommended, but not mandatory, for all users to download Meso-NH package using Git (next Section), because:

* It's easier for us (Meso-NH support's team) to give you some assistance in case of trouble... as Git allows us to know exactly what you have changed in the original package ;

* It's much easier for you to update to the last version...  or at least see the changes made for bug fix directly on our installation. ("our installation" or "your installation" ??)

* Git is strongly recommended if you intend to modify the code.


However, if you are allergic to Git, you can still download a tarball of Meso-NH package (Section XXX).

.. |git_link| raw:: html

   <a href="https://git-scm.com/" target="_blank">Git</a>


Download via git (for users only ; highly recommended)
------------------------------------------------



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




Cloning
*****************************************************************************


Clone the Meso-NH Source repository from the developpement branch MNH-57-branch with the following command:

.. code-block:: bash

   git clone https://src.koda.cnrs.fr/mesonh/mesonh-code.git -b MNH-57-branch MNH-V5-7-1

that will create the MNH-V5-7-1 directory containing a clone (copy) of the Meso-NH package on the remote developpement branch MNH-57-branch.

The next step is to configure the Meso-NH package, for that go to Section XXX.


Download a tarball of Meso-NH (for basic users ; not recommended)
------------------------------------------------

If you are a basic user of Meso-NH, you can download a tarball containing Meso-NH package. With your preferred web browser go to the |mesonh_link| and click on **Download** link on the left part.
Alternatively, you can directlyly download the last validated version of Meso-NH `here <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_MESONH/MNH-V5-7-1.tar.gz>`_.

Then untar the file MNH-V5-7-1.tar.gz where you want to.
For example, in your home directory:

.. code-block:: bash

   cd
   tar xvfz MNH-V5-7-1.tar.gz

The next step is to configure the Meso-NH package, for that go to Section XXX.

.. |mesonh_link| raw:: html

   <a href="http://mesonh.aero.obs-mip.fr/mesonh" target="_blank">Meso-NH's website</a>

.. note::

  A conserver ?

   * If you will modify the code, go to Section XXX.

   * Some basic Git commands are presented in Appendice XXX.

