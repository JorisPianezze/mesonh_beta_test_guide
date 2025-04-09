.. _nam_diag_gps_simulator:

NAM_DIAG - GPS simulator
-----------------------------------------------------------------------------


* put :code:`NGPS=0` in :code:`NAM_DIAG` to store following variable :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "ZTD", "Zenithal Total Delay (m)", "2D"

* put :code:`NGPS=1` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   ZTD", "Zenithal Total Delay (m)", "2D"
   ZHD", "Zenithal Hydrostatic Delays (m)", "2D"
   ZWD", "Zenithal Wet Delays (m)", "2D"

.. warning::

   Following options has to be set in NAM_DIAG when NGPS > -1 :
     
   .. csv-table::
      :header: "Fortran name", "Fortran type", "Default value"
      :widths: 30, 30, 30
   
      "CNAM_GPS", "ARRAY(CHARACTER)", "50*"
      "XLAT_GPS", "ARRAY(REAL)", "50* XUNDEF"
      "XLON_GPS", "ARRAY(REAL)", "50* XUNDEF"
      "XZS_GPS", "ARRAY(REAL)", "50* -999.0"
      "XDIFFORO", "REAL", "150.0"

   * :code:`CNAM_GPS` : name of the GPS stations

   * :code:`XLAT_GPS` : latitude of the GPS stations
   
   * :code:`XLON_GPS` : longitude of the GPS stations
   
   * :code:`XZS_GPS` : height of the GPS stations (m)

   * :code:`XDIFFORO` : maximum difference between model orography and station height accepted when computing interpolated delays value (m)
   
   For stations where latitude, longitude and height are different from default values, the interpolated values of GPS delays are written in ASCII files YINIFILEYSUFFIXGPS[.P00n] (where n is the number of processor).
