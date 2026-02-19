.. _nam_eol_townac:

NAM_EOL_TOWNAC
-----------------------------------------------------------------------------
Parametrization of the turbine's tower and nacelle. In the current implementation, the tower is represented by a cylinder with NNB_TOWELT sections and the nacelle by a disk of radius R\_r (defined in the data\_turbine.csv file). Drag forces are deduced from these geometrical shapes. 
The user can modify the modified drag coefficient. These drag forces are smeared the same way as the body forces of the blades.

.. csv-table:: NAM_EOL_TOWAC content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "NNB_TOWELT", "INTEGER", "84"       
   "XCD_NAC", "REAL", "0.68"
   "XCD_TOW", "REAL", "4.0"       

* :code:`NEMITTING_ROT`: number of rotor that emit tracers. We recommend to limit this number to the number of wind turbines for which the wake meandering will be studied. Having too many additional variables will reduce the code's performance.

* :code:`NNB_TOWELT`: number of elements to add a drag to the tower. We recommend having at least one element per cell size.

* :code:`XCD_NAC`: modified drag coefficient of the nacelle. 

* :code:`XCD_TOW`: modified drag coefficient of the tower.
