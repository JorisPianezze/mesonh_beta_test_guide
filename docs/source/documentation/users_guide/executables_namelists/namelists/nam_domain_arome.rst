.. _nam_domain_arome:

NAM_DOMAIN_AROME
-----------------------------------------------------------------------------

This namelist is only available for CTYPEFILE='AROME'. It contains the caracteristics of the domain arome in the input file.

.. csv-table:: NAM_DOMAIN_AROME content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "NI", "INTEGER", "750"
   "NJ", "INTEGER", "720"
   "NK", "INTEGER", "60"
   "XDELTAX", "INTEGER", "2500"
   "XDELTAY", "INTEGER", "2500"

* :code:`NI` : number of points to read in I direction 

* :code:`NJ` : number of points to read in J direction 

* :code:`NK` : number of vertical levels to read 

* :code:`XDELTAX` : gridsize of arome file in I direction (m)

* :code:`XDELTAY` : gridsize of arome file in J direction (m)    
