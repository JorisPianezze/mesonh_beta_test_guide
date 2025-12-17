.. _nam_blankn:

NAM_BLANKn
-----------------------------------------------------------------------------

.. csv-table:: NAM_BLANKn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XDUMMY1 ... XDUMMY8","REAL","0.0"
   "NDUMMY1 ... NDUMMY8","INTEGER","0"
   "LDUMMY1 ... LDUMMY8","LOGICAL","TRUE"
   "CDUMMY1 ... CDUMMY8","CHARACTER(LEN=80)",""
   "XDUMMY","ARRAY(REAL)","20*0.0"
   "NDUMMY","ARRAY(INTEGER)","20*0"
   "LDUMMY","ARRAY(LOGICAL)","20*.TRUE."
   "CDUMMY","ARRAY(CHARACTER(LEN=80))","20*''"

Eight dummy variables and arrays (real, integer, logical, and character of length 80) are defined for testing and debugging. They are read through the namelist but are not used by any Meso-NH routine. If a developer wants to temporarily add a parameter to a subroutine, they can include a :code:`USE MODD_BLANK_n` statement in that subroutine. This allows them to access and modify these variables via the namelist input.
