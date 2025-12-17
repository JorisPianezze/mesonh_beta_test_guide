.. _nam_recycl_paramn:

NAM_RECYCL_PARAMn
-----------------------------------------------------------------------------

.. csv-table:: NAM_RECYCL_PARAMn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LRECYCL","LOGICAL",".FALSE."
   "LRECYCLW","LOGICAL",".FALSE."
   "LRECYCLE","LOGICAL",".FALSE."
   "LRECYCLS","LOGICAL",".FALSE."
   "LRECYCLN","LOGICAL",".FALSE."
   "XDRECYCLW","REAL","0.0"
   "XDRECYCLE","REAL","0.0"
   "XDRECYCLS","REAL","0.0"
   "XDRECYCLN","REAL","0.0"
   "XARECYCLW","REAL","0.0"
   "XARECYCLE","REAL","0.0"
   "XARECYCLS","REAL","0.0"
   "XARECYCLN","REAL","0.0"
   "NTMOY","INTEGER","0"
   "NNUMBELT","INTEGER","28"
   "NTMOYCOUNT","INTEGER","0"
   "XRCOEFF","REAL","0.2"
   "XTBVTOP","REAL","500.0"
   "XTBVBOT","REAL","300.0"

* :code:`LRECYCL` : Flag to activate turbulence recycling method or not.

  * .TRUE. : turbulence recycling method is activated.
  * .FALSE. : turbulence recycling method is not activated.

.. warning:: 

   In its current version, the turbulence recycling method has only been validated with flat terrain (LFLAT=.TRUE.), cartesian coordinates (LCARTESIAN=.TRUE.), and a near-neutral boundary layer.

* :code:`LRECYCLW,E,S,N` : Flag to activate turbulence recycling method on the West, East, South, North boundaries of the domain or not.

  * .TRUE.: turbulence recycling method is activated on the West, East, South, North boundaries of the domain.
  * .FALSE.: turbulence recycling method is not activated on the West, East, South, North boundaries of the domain.

* :code:`XDRECYCLW,E,S,N` : Distance (in meters) of the recycling plan to the West, East, South, North boundary (1/4 of the domain is recommended).

* :code:`XARECYCLW,E,S,N` : Angle between the recycling plan and the West, East, South, North boundary (0. for X-direction and :math:`\frac{\pi}{2}` for Y-direction).

* :code:`NTMOY` : Total number of time-steps within time window for the calculation of the moving temporal average.

* :code:`NNUMBELT` : Number of elements used for the variable averaging.

* :code:`NTMOYCOUNT` : Number of time-steps between an update of the averaged variable (NTMOYCOUNT=NTMOY/NNUMBELT)

* :code:`XRCOEFF` : Weighting coefficient for the turbulent fluctuations, preventing calculation divergence. XRCOEFF in [0.1-0.3] for near-neutral simulations.

* :code:`XTBVTOP` : Threshold to filter the gravity waves. Shoud be equal to approximatively 4 times the Brunt-Vaisala period.

* :code:`XTBVBOT` : Threshold to filter the gravity waves. Shoud be equal to approximatively 2 times the Brunt-Vaisala period.
 

