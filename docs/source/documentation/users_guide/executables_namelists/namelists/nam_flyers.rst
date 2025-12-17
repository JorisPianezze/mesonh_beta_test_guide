.. _nam_flyers:

NAM_FLYERS
-----------------------------------------------------------------------------

This namelist is used to set the number of flyers (aircrafts and balloons) that will be simulated in the run. It is a preliminary phase to use the namelists :ref:`nam_aircrafts` and :ref:`nam_balloons`.

.. csv-table:: NAM_FLYERS content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "NAIRCRAFTS","INTEGER","0"
   "NBALLOONS","INTEGER","0"

* :code:`NAIRCRAFTS` : number of aircrafts to declare in :ref:`nam_aircrafts`.

* :code:`NBALLOONS` : number of balloons to declare in :ref:`nam_balloons`.
