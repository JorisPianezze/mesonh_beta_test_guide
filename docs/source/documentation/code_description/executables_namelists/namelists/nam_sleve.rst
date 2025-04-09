.. _nam_sleve:

NAM_SLEVE
-----------------------------------------------------------------------------

This namelist defines the orography file and orographic treatment to be done.

.. csv-table:: NAM_SLEVE content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "NSLEVE","INTEGER","12"
   "XSMOOTH_ZS","REAL","XUNDEF"

* :code:`NSLEVE` : number of iteration for computation of smooth orography.

* :code:`XSMOOTH_ZS` : optional uniform smooth orography.
