.. _nam_eol_tracers:

NAM_EOL_TRACERS
-----------------------------------------------------------------------------

.. csv-table:: NAM_EOL_TRACERS content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "NEMITTING_ROT", "INTEGER", "1"       
   "NNB_EMITTING_ROT", "INTEGER(:)", "(1,0,0,..)"
   "XTRAC_DIST", "REAL", "120"       
   "XTRAC_RAD", "REAL", "-60"      

* :code:`NEMITTING_ROT`: number of rotor that emit tracers. We recommend to limit this number to the number of wind turbines for which the wake meandering will be studied. Having too many additional variables will reduce the code's performance.

* :code:`NNB_EMITTING_ROT`: list of size NEMITTING_ROT which indicates the indices of tracked turbines. 

* :code:`XTRAC_DIST`: Distance (in meters) in the hub frame between the rotor hub and the centre of the emitting disk (positive is upstream, negative is downstream).

* :code:`XTRAC_RAD`: Radius (in meters) of the emitting disk.