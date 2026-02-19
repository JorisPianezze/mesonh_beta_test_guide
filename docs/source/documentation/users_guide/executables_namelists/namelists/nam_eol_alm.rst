.. _nam_eol_alm:

NAM_EOL_ALM
-----------------------------------------------------------------------------

.. csv-table:: NAM_EOL_ALM content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CFARM_CSVDATA","CHARACTER(LEN=128)","'data_farm.csv'"
   "CTURBINE_CSVDATA","CHARACTER(LEN=128)","'data_turbine.csv'"
   "CBLADE_CSVDATA","CHARACTER(LEN=128)","'data_blade.csv'"
   "CAIRFOIL_CSVDATA","CHARACTER(LEN=128)","'data_airfoil.csv'"
   "CINTERP","CHARACTER(LEN=3)","'CLS'"
   "NNB_RADELT","INTEGER","42"
   "LTIMESPLIT","LOGICAL",".FALSE."
   "LTIPLOSSG","LOGICAL",".TRUE."
   "LTECOUTPTS","LOGICAL",".FALSE."
   "LCSVOUTFRM","LOGICAL",".FALSE."

* :code:`CFARM_CSVDATA` : see :ref:`nam_eol_adr`

* :code:`CTURBINE_CSVDATA` : see :ref:`nam_eol_adr`

* :code:`CBLADE_CSVDATA` : see :ref:`nam_eol_adr`

* :code:`CAIRFOIL_CSVDATA` : see :ref:`nam_eol_adr`

* :code:`CINTERP` : see :ref:`nam_eol_adr`

* :code:`NNB_RADELT` : number of blade elements for the discretisation of the blade radius. This value is independent of the number of elements in CBLADE_CSVDATA, as the algorithm will proceed to its own discretization through an interpolation of the data given by the blade description (CBLADE_CSVDATA). To determine the value to be specified, refer to the scientific documentation. 

* :code:`LTIMESPLIT` : flag to activate time-splitting method (also known as Actuator Sector). The CFL criterion of Meso-NH imposes a time step. Nevertheless, the ALM often requires a smaller time step in order to ensure that a blade element will not skip a mesh cell during this time step. As it could be too restrictive, the ALM algorithm can be called a few times during the main CFL-based time step duration, in order to respect the ALM time step criterion. It allows computational cost saving, but results can be less accurate. Note that in this case, the ADR model can also be considered.

  * .TRUE.  activates time-splitting method only if XTSTEP (:ref:`nam_dynn`) is too high.
  * .FALSE. desactivates it.

* :code:`LTIPLOSSG` : see :ref:`nam_eol_adr`

* :code:`LTECOUTPTS` : see :ref:`nam_eol_adr`

* :code:`LCSVOUTFRM` : see :ref:`nam_eol_adr`