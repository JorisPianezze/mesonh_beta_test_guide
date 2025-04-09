.. _ibm_idea:

ibm_idea.nam
-----------------------------------------------------------------------------

.. csv-table:: ibm_idea.nam content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "NOBJ", "INTEGER", ""
   "NOBJ_TYPE", "INTEGER", ""
   "NTYPE", "INTEGER", ""
   "NOBJ_ETYPE", "INTEGER", ""
   "XX1", "REAL", ""
   "XX2", "REAL", ""
   "XY1", "REAL", ""
   "XY2", "REAL", ""
   "XZ1", "REAL", ""
   "XZ2", "REAL", ""
   
* :code:`NOBJ` : Total number of obstacles (parallelepiped and ellipsoide).

* :code:`NOBJ_TYPE` : Number of obstacles type (parallelepiped and/or ellipsoide).

* :code:`NTYPE` : Obstacle type:

  * 1: Parallelepiped.
  * 2: Ellipsoide.

* :code:`NOBJ_ETYPE` : Number of obstacles for each type.

* :code:`XX1`, :code:`XX2`, :code:`XY1`, :code:`XY2`, :code:`XZ1`, :code:`XZ2` : Locations of the obstacles.

  * if type 1 (parallelepiped): I1/I2 = min/max in direction (X,Y,Z)
  * if type 2 (ellipsoide): X1/Y1/Z1 locations of object center, X2/Y2/Z2 axe lenght in each direction

Example (case of 4 parallelepipeds and 1 ellipsoide) :

.. code-block::

   5 2 # NOBJ / NOBJ_TYPE
   1 4 # NTYPE / NOBJ_ETYPE
   +51.00 +53.42 +51.45 +63.65 -1.00 +2.54 # XX1/XX2/XY1/XY2/XZ1/XZ2
   +51.00 +53.42 +71.55 +83.75 -1.00 +2.54 #
   +51.00 +53.42 +91.65 +103.85 -1.00 +2.54 #
   +51.00 +53.42 +111.75 +123.95 -1.00 +2.54 #
   2 1 # NTYPE / NOBJ_ETYPE
  +100. +10. +100. +10. -1. 10. # XX1/XX2/XY1/XY2/XZ1/XZ2
  
In the case of obstacles in contact with the ground it is necessary to have negative value of XZ1.
