.. _nam_balloons:

NAM_BALLOONS
-----------------------------------------------------------------------------

This namelist allows to add virtual balloons to the simulation. Before using this namelist, the total number of balloons must be set in the :ref:`nam_flyers` namelist.

Balloons are advected by the wind of the model. They can crash. All the prognostic fields (zonal and meridian wind (from U and V components), vertical velocity, potential temperature, pression, mixing ratios, tke, radiative surface temperature...) are recorded along the trajectories of the balloons, as well as their trajectories themselves (positions in X, Y and Z directions and orography). All records are stored in the :ref:`diachronic file<diachronic_file>` (.000).

.. csv-table:: NAM_BALLOONS content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CMODEL","CHARACTER(LEN=3)(:)","'FIX'"
   "CTITLE","CHARACTER(LEN=10)(:)","CTYPE//nnn"
   "CTYPE","CHARACTER(LEN=6)(:)","''"
   "NMODEL","INTEGER(:)","0"
   "TLAUNCH","TYPE(DATE_TIME)(:)","default value of type(date_time)"
   "XTSTEP","REAL(:)","60.0"
   "XLATLAUNCH","REAL(:)","XUNDEF"
   "XLONLAUNCH","REAL(:)","XUNDEF"
   "XALTLAUNCH","REAL(:)","XNEGUNDEF"
   "XPRES","REAL(:)","XNEGUNDEF"
   "XWASCENT","REAL(:)","XNEGUNDEF"
   "XDIAMETER","REAL(:)","XNEGUNDEF"
   "XVOLUME","REAL(:)","XNEGUNDEF"
   "XMASS","REAL(:)","XNEGUNDEF"
   "XAERODRAG","REAL(:)","XNEGUNDEF"
   "XINDDRAG","REAL(:)","XNEGUNDEF"

* :code:`CMODEL` : 'FIX' if the balloon stays on the same grid model, 'MOB' if the balloon may change of grid model (always the finest depending on the horizontal position). 'FIX' by default

* :code:`CTITLE` : name of the balloon. If not provided, it is set to CTYPE//nnn with $nnn$ the number of the balloon

* :code:`CTYPE` : 'CVBALL' for constant volume balloon, 'ISODEN' for iso-density balloon, 'RADIOS' for radiosounding balloon. Mandatory

* :code:`NMODEL` : number of the grid model where the balloon flies. If CMODEL='FIX', it may be any grid model number (forced to 1 if NMODEL not set). If CMODEL='MOB', NMODEL is forced to 1 at simulation start but will change during flight to always fly on the finest model at a given horizontal position.

* :code:`TLAUNCH` : instant of launch. Mandatory. This type has 4 fields (nyear, nmonth, nday and xtime).

  .. note::

     For example:
   
     .. code-block::

        TLAUNCH(1)%nyear  =  2023
        TLAUNCH(1)%nmonth =     1
        TLAUNCH(1)%nday   =    16
        TLAUNCH(1)%xtime  = 21600.

* :code:`XTSTEP` : data storage frequency. If not set, it is forced to 60s. The frequency must be a multiple of the timestep of the chosen model NMODEL if CMODEL='FIX' or of the main model 1 if CMODEL='MOB'. It will be enforced at run. Balloon positions are not computed with this timestep but with the model one.

* :code:`XLATLAUNCH` : latitude of the launching site. Mandatory

* :code:`XLONLAUNCH` : longitude of the launching site. Mandatory

* :code:`XALTLAUNCH` : altitude of the launching site (mandatory if CTYPE='RADIOS'; if not set for 'CVBALL' or 'ISODEN', XPRES must be provided)

* :code:`XPRES` : pressure at the launching site (in Pascal). Must be provided for 'CVBALL' or 'ISODEN' if XALTLAUNCH is not set. Ignored for 'RADIOS'

* :code:`XWASCENT` : ascentional vertical speed of the ballon. Speed in calm air for 'RADIOS' (added to air vertical speed, default 5 m/s), initial value for 'CVBALL' (default 0 m/s), not used for 'ISODEN'

* :code:`XDIAMETER` : diamater of the balloon (for 'CVBALL'). If not provided, XVOLUME must be set.

* :code:`XVOLUME` : volume of the balloon (for 'CVBALL'). If not provided, XDIAMETER must be set.

* :code:`XMASS` : mass of the balloon (for 'CVBALL'). Mandatory

* :code:`XAERODRAG` : aerodynamic drag coefficient of the balloon (for 'CVBALL'). Default: 0.44

* :code:`XINDDRAG` : induced drag coefficient (i.e. air shifted by the balloon, only for 'CVBALL'). Default: 0.014
