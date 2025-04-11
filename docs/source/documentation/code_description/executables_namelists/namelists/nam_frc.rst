.. _nam_frc:

NAM_FRC
-----------------------------------------------------------------------------

Application of a specific forcing is enabled by a dedicated flag. When a Newtonian relaxation is requested, the damping time XRELAX_TIME_FRC and the height (fixed or physically based) above which the forcing is applied, XRELAX_HEIGHT_FRC and CRELAX_HEIGHT_TYPE, must be set.

.. csv-table:: NAM_FRC content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LGEOST_UV_FRC","LOGICAL",".FALSE."
   "LGEOST_TH_FRC","LOGICAL",".FALSE."
   "LTEND_THRV_FRC","LOGICAL",".FALSE."
   "LTEND_UV_FRC","LOGICAL",".FALSE."
   "LVERT_MOTION_FRC","LOGICAL",".FALSE."
   "LRELAX_THRV_FRC","LOGICAL",".FALSE."
   "LRELAX_UV_FRC","LOGICAL",".FALSE."
   "LRELAX_UVMEAN_FRC","LOGICAL",".FALSE."
   "XRELAX_TIME_FRC","REAL","10800.0"
   "XRELAX_HEIGHT_FRC","REAL","0.0"
   "CRELAX_HEIGHT_TYPE","CHARACTER(LEN=4)","'FIXE'"
   "LTRANS","LOGICAL",".FALSE."
   "XUTRANS","REAL","0.0"
   "XVTRANS","REAL","0.0"
   "LDEEPOC","LOGICAL",".FALSE."
   "XCENTX_OC","REAL","16000.0"
   "XCENTY_OC","REAL","16000.0"
   "XRADX_OC","REAL","8000.0"
   "XRADY_OC","REAL","8000.0"


* :code:`LGEOST_UV_FRC` : flag to use a prescribed geostrophic wind.

  * .TRUE. to integrate a geostrophic wind with a constant Coriolis parameter :math:`f=2 \times \Omega \times SIN(XLAT0)`. The LCORIO flag of :ref:`nam_dyn` must be .TRUE.
  * .FALSE. not active

* :code:`LGEOST_TH_FRC` : flag to apply a large scale horizontal advection on the potential temperature field. The gradients result from the thermal wind balance.

  * .TRUE. to integrate an horizontal advection of :math:`\theta`.
  * .FALSE. not active

* :code:`LTEND_THRV_FRC` : flag to simulate a large scale :math:`\theta` and humidity tendency.

  * .TRUE. to integrate a tendency for :math:`\theta` and :math:`r_v`.
  * .FALSE. not active

* :code:`LTEND_UV_FRC` : flag to simulate a large scale wind tendency.

  * .TRUE. to integrate a tendency for u and v.
  * .FALSE. not active

* :code:`LVERT_MOTION_FRC` : flag to simulate a large scale vertical transport of all the prognostic fields.

  * .TRUE. to integrate a vertical transport with an upstream scheme.
  * .FALSE. not active

* :code:`LRELAX_THRV_FRC` : flag to apply a Newtonian relaxation on the potential temperature and humidity fields.

  * .TRUE. to relax :math:`\theta` and :math:`r_v` towards large scale values.
  * .FALSE. not active

* :code:`LRELAX_UV_FRC` : flag to apply a Newtonian relaxation on each horizontal wind component.

  * .TRUE. to relax the horizontal wind towards large scale values.
  * .FALSE. not active

* :code:`LRELAX_UVMEAN_FRC` : flag to apply a Newtonian relaxation on the horizontal mean value of each horizontal wind component.

  * .TRUE. to relax the horizontal mean wind towards large scale values.
  * .FALSE. not active

* :code:`XRELAX_TIME_FRC` : constant damping time for the forced relaxation.

* :code:`XRELAX_HEIGHT_FRC` : height above which a forced relaxation is enabled when CRELAX_HEIGHT_TYPE='FIXE' or minimal height if 'THGR' is used.

* :code:`CRELAX_HEIGHT_TYPE` : definition of the height above which a forced relaxation is enabled.

  * 'FIXE' means that a forced relaxation is never applied below XRELAX_HEIGHT_FRC.
  * 'THGR' means that a forced relaxation is never applied below the maximal height between XRELAX_HEIGHT_FRC and the height above which :math:`\partial \theta / \partial z` is the highest for each column.

* :code:`LTRANS` : flag to apply a Galilean translation of the domain of simulation

  * .TRUE. The translation speed of the domain of simulation will be XUTRANS,XVTRANS
  * .FALSE. : not active

* :code:`LDEEPOC` : flag to activate an idealized forcing at the surface for oceanic deep convection (if LOCEAN=T)

* :code:`XCENTX_OC` : x-position (in meters) of the center of the surface forcing for ideal ocean deep convection (if LOCEAN=T and LDEEPOC=T)

* :code:`XCENTY_OC` : y-position (in meters) of the center of the surface forcing for ideal ocean deep convection (if LOCEAN=T and LDEEPOC=T)

* :code:`XRADX_OC` : x-radius (in meters) of the surface forcing for ideal ocean deep convection (if LOCEAN=T and LDEEPOC=T)

* :code:`XRADY_OC` : y-radius (in meters) of the surface forcing for ideal ocean deep convection (if LOCEAN=T and LDEEPOC=T)

