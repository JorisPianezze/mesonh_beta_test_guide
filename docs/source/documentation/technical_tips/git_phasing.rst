Installing Meso-NH with GIT
===============================

*Retranscription of a part of A-INSTALL*

.. note::

  On a *development branch* there is a version of the code that includes the latest changes of the code made by the developpers and the support team, including parts that are not yet tested. The following steps show you how to c) get the code and d) go to a version that was tested and officially released: a version with a *tag*.


c) Cloning the Meso-NH Source repository located on the developpement branch MNH-57-branch
--------------------------------------------------------------------------------------

Finally you can clone the Meso-NH Git repository with the following command:
  
``git clone anongit@anongit_mesonh:/gitrepos/MNH-git_open_source-lfs.git -b MNH-57-branch MNH-V5-7-1``

that will create the MNH-V5-7-1 directory [#note1]_ containing a clone (copy) of the Meso-NH package located on the remote developpement branch MNH-57-branch.

.. [#note1] you can choose another name for this directory, then adapt following insctructions

d) Checking out a given version of MESONH
--------------------------------------------

Once the repository is cloned, it's better for you to checkout your own branch (by default, you are on HEAD of the MNH-57-branch development branch).

To create your local branch corresponding to the V5-7-1 version, type:

``cd MNH-V5-7-1``

``git checkout -b MYB-MNH-V5-7-1 PACK-MNH-V5-7-1``

**MYB-MNH-V5-7-1** is the name of the local branch you created

and

**PACK-MNH-V5-7-1** is the remote/origin tag on which it is based.

This last insctruction makes two things:

1) it changes the code you downloaded so that it corresponds now to the official and tested version with the tag **PACK-MNH-V5-7-1**

2) it creates a local branch starting from this tagged version with the name **MYB-MNH-V5-7-1**. You can later make evolve this branch by adding your code when you create/modify some sources. To do so use ``git add file.f90`` where ``file.f90`` is the source code that you added/changed in your user repository. You can do it for as many files as you whish. And then do ``git commit: "description of the changes since last commit"`` to include thsese changes on your local branch.

The advantages of this way of downloading the package are:

1) you can easily restore a previous version of your code, in case you are not happy with your last changes,

2) in the future you could check/update quickly the differences with the new released version of the package without having to download entirely the full package:


Suppose that a new version, for example "PACK-MNH-V5-7-2", is announced.

To see the differences with your working copy, do:

``git fetch``

``git diff HEAD PACK-MNH-V5-7-2``


To go to the new version, you can, for example, create a new local branch:

``git checkout -b MYB-MNH-V5-7-2 PACK-MNH-V5-7-2``

.. warning::

  So this create a new local branch, does it stil include the user's previous changes? Should we say to the user that they have to recompile then?


At any time, you can also check for "uptodate" changes in the Git branch dedicated to the MNH57 version, *even before* the official release of the "bugN+1" bugfix version:

``git fetch``

``git diff HEAD MNH-57-branch``

And, test this development (not yet official) version by going to this branch:

``git checkout --track origin/MNH-57-branch``

.. warning::

  What really happens then? Do you add the last developments to your branch - like a merge?
