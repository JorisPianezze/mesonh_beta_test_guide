.. _nam_domain_arome:

NAM_DOMAIN_AROME
-----------------------------------------------------------------------------

This namelist is only available for CTYPEFILE='AROME'. It contains the caracteristics of the domain arome in the input file.

.. csv-table:: NAM_DOMAIN_AROME content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "NI", "integer", "750"
   "NJ", "integer", "720"
   "NK", "integer", "60"
   "XDELTAX", "integer", "2500"
   "XDELTAY", "integer", "2500"

* NI : number of points to read in I direction 

* NJ : number of points to read in J direction 

* NK : number of vertical levels to read 

* XDELTAX : gridsize of arome file in I direction (m)

* XDELTAY : gridsize of arome file in J direction (m)    
