.. _nam_diag_interpolation:

NAM_DIAG - Interpolation levels
-----------------------------------------------------------------------------

Interpolation on altitude, isobaric and isentropic levels

.. csv-table::
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LISOAL", "LOGICAL", ".FALSE."
   "XISOAL", "ARRAY(REAL)", "99*-1"
   "LISOPR", "LOGICAL", ".FALSE."
   "XISOPR", "ARRAY(REAL)", "10*0"
   "LISOTH", "LOGICAL", ".FALSE."
   "XISOTH", "ARRAY(REAL)", "10*0"

* :code:`LISOAL` : flag to interpolate on altitude levels the following variables: potential vorticity, wind, cloud (liquid water and ice) and precipitation (rain, snow and graupel) mixing ratio, dust extinction (if available). The outputs are 3D fields named: ALT_CLOUD, ALT_PRECIP, ALT_PRESSURE, ALT_PV, ALT_U, ALT_V and ALT_DSTEXT (if available).

* :code:`XISOAL` : altitude of the isobaric levels

* :code:`LISOPR` : flag to interpolate on pressure levels the following variables: potential temperature, wind, water vapour mixing ratio, geopotential (in meters). The outputs are 2D fields named with suffix 'xxxxHPA' where 'xxxx' stands for the pressure value

* :code:`XISOPR` : altitude of the isobaric levels

* :code:`LISOTH` : flag to interpolate on isentropic levels the following variables: pressure, potential vorticity, wind, water. The outputs are 2D fields named with suffix 'xxxK' where 'xxx' stands for the temperature value

* :code:`XISOTH` : altitude of the isentropic levels 
