.. _nam_diag_interpolation:

NAM_DIAG - Interpolation levels
-----------------------------------------------------------------------------

Interpolation on altitude, isobaric and isentropic levels

.. csv-table::
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LISOAL", "logical", ".FALSE."
   "XISOAL", "array(real)", "99*-1"
   "LISOPR", "logical", ".FALSE."
   "XISOPR", "array(real)", "10*0"
   "LISOTH", "logical", ".FALSE."
   "XISOTH", "array(real)", "10*0"

* LISOAL: flag to interpolate on altitude levels the following variables: potential vorticity, wind, cloud (liquid water and ice) and precipitation (rain, snow and graupel) mixing ratio, dust extinction (if available). The outputs are 3D fields named: ALT_CLOUD, ALT_PRECIP, ALT_PRESSURE, ALT_PV, ALT_U, ALT_V and ALT_DSTEXT (if available).

* XISOAL: altitude of the isobaric levels

* LISOPR: flag to interpolate on pressure levels the following variables: potential temperature, wind, water vapour mixing ratio, geopotential (in meters). The outputs are 2D fields named with suffix ’xxxxHPA’ where ’xxxx’ stands for the pressure value

* XISOPR: altitude of the isobaric levels

* LISOTH: flag to interpolate on isentropic levels the following variables: pressure, potential vorticity, wind, water. The outputs are 2D fields named with suffix ’xxxK’ where ’xxx’ stands for the temperature value

* XISOTH: altitude of the isentropic levels 
