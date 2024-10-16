Installing Meso-NH with GIT
******************************

Following A-INSTALL:



c) Cloning the Meso-NH Source repository on the developpement branch MNH-57-branch
--------------------------------------------------------------------------------------

Finally you can clone the Meso-NH Git repository with the following command:
  
.. code:: bash
  git clone anongit@anongit_mesonh:/gitrepos/MNH-git_open_source-lfs.git -b MNH-57-branch MNH-V5-7-1

that will create the MNH-V5-7-1 directory containing a clone (copy) of the Meso-NH package on the remote developpement branch MNH-57-branch.

d) Checking out a given version of MESONH
-----------------------------------------

Once the repository is cloned, it's better for you to checkout your own branch (by default, you are on HEAD of the MNH-57-branch development branch  ).

To create your local branch corresponding to the V5-7-1 version, type:

.. code:: bash
  cd MNH-V5-7-1
  git checkout -b MYB-MNH-V5-7-1 PACK-MNH-V5-7-1

**MYB-MNH-V5-7-1** is the name of the local branch you created
and
**PACK-MNH-V5-7-1** is the remote/origin tag on which it is based.

The advantage of this way of downloading the package is that in the future you could check/update quickly differences with the new version of the package without having to download entirely the full package.


#  Suppose that a new version, for example "PACK-MNH-V5-7-1", is announced.
#
#  To see the differences with your working copy, do:
#

git fetch
git diff HEAD PACK-MNH-V5-7-1

#
#  To go to the new version, you can, for example, create a new local branch:
#

git checkout -b MYB-MNH-V5-7-1 PACK-MNH-V5-7-1

#
# At any time, you can also check for "uptodate" changes in the Git branch
# dedicated to the MNH57 version before the official release of the "bugN+1"
# bugfix version.
#

git fetch
git diff HEAD MNH-57-branch

#
# And, test this development (not yet official) version by going to this branch:
#

git checkout --track origin/MNH-57-branch
