.. _nam_diag_lidar_simulator:

NAM_DIAG - LIDAR simulator
-----------------------------------------------------------------------------

* add :code:`LLIDAR=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "LIDAR", "Total backscatter coefficient (1/m/sr)", "3D"
   "LIPAR", "Particle backscatter coefficient (1/m/sr)", "3D"
   
.. note::

   Following options can be used in :code:`NAM_DIAG` when :code:`LLIDAR` is activated :
   
   .. csv-table::
      :header: "Fortran name", "Fortran type", "Default value"
      :widths: 30, 30, 30
   
      "CVIEW_LIDAR", "CHARACTER(LEN=5)", "'NADIR'"
      "XALT_LIDAR", "REAL", "0"
      "XWVL_LIDAR", "REAL", "0.532E-6"

   * :code:`CVIEW_LIDAR` : gives the lidar point of view : either 'NADIR' or 'ZENIT'
 
   * :code:`XALT_LIDAR` : gives the altitude of the lidar source (in meters) (by default, the altitude of the ground will be used for zenithal view, and the altitude of the model top will be used for nadir view)
   
   * :code:`XWVL_LIDAR` : gives the wavelength of the lidar source (in meters)
