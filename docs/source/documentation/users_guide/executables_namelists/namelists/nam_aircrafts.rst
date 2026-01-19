.. _nam_aircrafts:

NAM_AIRCRAFTS
-----------------------------------------------------------------------------

This namelist allows to add virtual aircrafts to the simulation. Before using this namelist, the total number of aircrafts must be set in the :ref:`nam_flyers` namelist.

All the prognostic fields (zonal and meridian wind (from U and V components), vertical velocity, potential temperature, pression, mixing ratios, tke, radiative surface temperature...) are recorded along the trajectories of the aircrafts, as well as their trajectories themselves (positions in X, Y and Z directions and orography). All records are stored in the :ref:`diachronic file<diachronic_file>` (.000).

.. csv-table:: NAM_AIRCRAFTS content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CFILE","CHARACTER(LEN=128)(:)",""
   "CMODEL","CHARACTER(LEN=3)(:)","'FIX'"
   "CTITLE","CHARACTER(LEN=10)(:)","'AIRCRAnnn'"
   "LALTDEF","LOGICAL(:)",".FALSE."
   "NMODEL","INTEGER(:)","0"
   "NPOS","INTEGER(:)","0"
   "TLAUNCH","TYPE(DATE_TIME)(:)","default value of type(date_time)"
   "XTSTEP","REAL(:)","60.0"

* :code:`CFILE` : name of the .csv file with the aircraft positions (one file per aircraft)

* :code:`CMODEL` : 'FIX' if the aircraft stays on the same grid model, 'MOB' if the aircraft may change of grid model (always the finest depending on the horizontal position). 'FIX' by default

* :code:`CTITLE` : name of the aircraft. If not provided, it is set to 'AIRCRAnnn' with nnn the number of the aircraft

* :code:`LALTDEF` : if .FALSE. (by default), atlitude is given in meters; if .TRUE. altitude is given in pressure (hPa)

* :code:`NMODEL` : number of the grid model where the aircraft flies. If CMODEL='FIX', it may be any grid model number (forced to 1 if NMODEL not set and only one domain). If CMODEL='MOB', NMODEL is forced to 1 at simulation start but will change during flight to always fly on the finest model at a given horizontal position.

* :code:`NPOS` : number of aircraft positions that will be read in the .csv file

* :code:`TLAUNCH` : instant of launch. This type has 4 fields (nyear, nmonth, nday and xtime).

  .. note::

     For example:

     .. code-block::
     
        TLAUNCH(1)%nyear  =  2023
        TLAUNCH(1)%nmonth =     1
        TLAUNCH(1)%nday   =    16
        TLAUNCH(1)%xtime  = 21600.

* :code:`XTSTEP` : data storage frequency. If not set, it is forced to 60s. The frequency must be a multiple of the timestep of the chosen model NMODEL if CMODEL='FIX' or of the main model 1 if CMODEL='MOB'. It will be enforced at run.

The .csv files should follow the format example hereafter (the first line is ignored, here the altitude is given in pressure):

.. code-block::

   Time Lat Lon Alt(p)
   0.   45.  -4. 1003.6
   150. 47.5 -.5 990.8
   300. 50.  2.  988.1


.. warning::

   If the altitude is given in pressure, the units are hPa and not Pa.

.. warning::

   The first time should be 0. as the times correspond to the time since the launch of the aircraft.