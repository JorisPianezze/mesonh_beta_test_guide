.. _nam_nesting:

NAM_NESTING
-----------------------------------------------------------------------------

.. csv-table:: NAM_NESTING content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "NDAD","ARRAY(8*REAL)","m-1"
   "NDTRATIO","ARRAY(8*INTEGER)","1"
   "XWAY","ARRAY(8*REAL)","2"
   "LCOUPLES",LOGICAL",".FALSE."

* :code:`NDAD(m)` : is the model number of the father of each model "m"

* :code:`NDTRATIO(m)` : is the ratio between time step of model m and its father NDAD(m)

* :code:`XWAY(m)` : is the interactive nesting level for model m and its father NDAD(m)

  * 1 one-way interactions
  * 2 two-way interactions : upward information are given to the father (also for 2D fields (Surface precipitation and short wave radiative fluxes) that are used by the surface
  
* :code:`LCOUPLES` : flag to activate the auto-coupling ocean-atmosphere version of Meso-NH. Domains 1 and 2 correspond to the atmosphere model and the ocean model respectively. This work is still in development.
