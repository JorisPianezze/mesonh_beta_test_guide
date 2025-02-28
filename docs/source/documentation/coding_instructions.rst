Coding instructions
=============================================================================

Meso-NH is build upon many contribution since 30 years. As the code is growing and shared with increasing models and contributors, a number of coding norms must be followed. At each pack release, a new tag is attached to its name (such as MNH-V5-5-0, MNH-V5-7-0 etc). The integration of contributions to a pack depends on its type described in a first part. Coding norms and guidance are described in a second part.

Integration workflow and guidelines
*****************************************************************************

Meso-NH packs VX-X-X can be divided into two categories :

* developement/major release-pack : the first and second X of VX-X (e.g. 5.4, 5.5, 5.6 etc)

* bugfix release-pack : the third X of VX-X-X (e.g. 5.4.1, 5.4.2, 5.4.3...)

A major release contains several scientific and technical changes and numerous bugfixes/commits. The time frequency of major release is about one over 12 to 18 months depending on the amount of contributors. A bugfix release contains a sufficient number of minor commit/bugfixes to justify a new release, or a hot bugfix that may impact a large number of users. The time frequency of bugfix can vary to a few days up to 12 months depending on the stability of the current pack release (usually a few months). At the integrator’s demand2, contributors are invited 1 to 3 months in advance to prepare their git branches on MNH-ladev repo. Depending on the number of potential contribution and their content (only minors or major), the integrator may asks to only fetch bugfixes or main developpement contributions

Bugfix release-pack
-----------------------------------------------------------------------------

In the case of a bugfix release-pack, please follow these guidelines :

* do not forget to base your work on the last version of the master’s branch : use git pull

* only commits with bugfixes are asked. Cherry-picking is possible, please prepare a list of commits hash to share.

.. note::

   Please note that contributions from entire branches with major developments would be declined and postponed to the next call of contributions for a major release.

Major release-pack
-----------------------------------------------------------------------------

In the case of a major release-pack, please follow these guidelines :

* do not forget to merge the master’s branch into your work before sharing your branch : use git pull

* if your development is a new feature, you will be asked to share at least one new test case related to your work with python3 plots showing the interests variables related to your new work. This is important to us to track new bugs in case of non-wanted modifications of a part of your work.

* if your development is a major modification of a current part of the code, you will be asked to share
at least one new test case with python3 plots showing the interests variables related to your new
work; and to have tested your branch on 2 other cases that is impacted by your development. Test
cases used for integration is listed in section 7.

* you will be asked to provide a contribution to the scientific and user’s guides

* your work is published in a peer-reviewd paper (recommended)

Coding guidelines
*****************************************************************************

General
-----------------------------------------------------------------------------
These guidelines apply mostly to every FORTRAN sources in src/ MNH, SURFEX, PHYEX, LIB.

**File structure :**

* Check if the function you code is already coded

* Avoid CONTAINS routines, create a new fortran routine file

* For new file, keep the common structure with an updated statements for the LICENCE and documentation

**Code ergonomy :**

* Maximum 132 characters per line, use &

* Code in CAPITAL characters

* Comments in lower-case characters

* No blank line, use !

* Remove debugging PRINTs and WRITE before committing

* Comment your code !

**Clean code :**

* Remove debugging PRINTs and WRITE before committing

* Remove unused local variables

* Remove unused dummy variables

* Remove unused module variables (USE MODD ...)

* Select the variables used : USE MODD TOTO, ONLY : MYVAR

**Variables :**

* Variables names must follow the DOCTOR norm described in the following table :

.. csv-table:: Norm DOCTOR
   :header: "Type/Status", "INTEGER", "REAL", "LOGICAL", "CHARACTER", "TYPE"
   :widths: 30, 30, 30, 30, 30, 30
   
   "Global", "N", "X", "L (not LP)", "C", "T (not TP, TS, TZ)"
   "Dummy argument", "K", "P", "O (not PP)", "H", "TP"
   "Local", "I", "Z (not IS)", "G (not GS, ZS)", "Y (not YS, YP)", "TZ"   
   "Loop control", "J (not JP)", "-", "-", "-", "-"
   

* Variables names must be consistent through subroutines (a variable must be easily found with grep)

* All variables must be declared, use IMPLICIT NONE

* Allocatables must be deallocated

* Pointer must be initialized by NULL()

**Reproductibility :**

* Use the parallelizaded version of basic functions (functions ended by ll such as MAX ll or SUM3D ll)

* Avoid anticipated exit of a loop with EXIT, CYCLE, RETURN statements

Extra rules for PHYEX
-----------------------------------------------------------------------------

The externalized atmospheric physics PHYEX has extra rules in order to comply with all the models using PHYEX (AROME, HARMONIE-AROME, etc). These rules are more strict in order to transform automatically the code for GPU applications.
The general idea behind these rules is that all the physics can be run with arrays written in one physical
dimension (the vertical axis). The fortran raw code is written in 2D or 3D in a way that automatic
functions (e.g. written in python) can read the fortran code and transform it to another fortran code
that can be run on any type of GPUs. The previous general rules applies to PHYEX.

The following extra rules apply on PHYEX/ :

**Variables :**

* Do not use allocatables

* Dimensions of dummy argument arrays must be explicit : no (:,:), use the structure D%

* No variables from modules can be imported except variables declared with the PARAMETER attribute. Put the variable in a type received by the subroutine interface

* Use loop index JIJ for computation on horizontal dimensions

* Use loop index JL on KSIZE microphysics computation point

* Horizontal dimensions arrays are packed into one dimension : instead of A(D%NIT, D%NJT, D%NKT), use A(D%NIJT, D%NKT) where D%NIT, D%NJT, D%NKT are physical dimensions in x, y, z directions and D%NIJT = D%NIT*D%NJT

**Subroutines :**

* Do not use functions returning arrays, use subroutines

* avoid CONTAINS subroutines, if really needed, the local arrays of the subroutines must have different names than the hosting subroutine or than other contained subroutines Statements

* all calculation on arrays must show explicit dimensions. Instead of A = B + C, write : A(:,:) = B(:,:) + C(:,:) even for initialization

* Do not use nested WHERE, convert it to DO...IF...

* temporary Do not use ANY, COUNT functions on arrays of horizontal dimensions

* temporary no (:) on TYPE%VAR

* compilation keys must be avoided. If really needed, the statements betwen ifdef and else must not split a statement
