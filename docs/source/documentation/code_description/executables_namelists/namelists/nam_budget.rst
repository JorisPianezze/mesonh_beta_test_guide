.. _nam_budget:

NAM_BUDGET
-----------------------------------------------------------------------------

.. csv-table:: NAM_BUDGET content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CBUTYPE","CHARACTER(LEN=4)","'NONE'"
   "NBUMOD","INTEGER","1"
   "XBULEN","REAL","43200.0"
   "NBUKL","INTEGER","1"
   "NBUKH","INTEGER","0"
   "LBU_KCP","LOGICAL",".TRUE."
   "XBUWRI","REAL","43200.0"
   "NBUIL","INTEGER","1"
   "NBUIH","INTEGER","0"
   "NBUJL","INTEGER","1"
   "NBUJH","INTEGER","0"
   "LBU_ICP","LOGICAL",".TRUE."
   "LBU_JCP","LOGICAL",".TRUE."
   "NBU_MASK","INTEGER","1"

* :code:`CBUTYPE` : type of box used to compute the budget:

  * 'CART' a cartesian box defined by the lowest and highest values of the indices in the 3 directions in the MESONH grid, defined in the following.
  * 'MASK' several areas, described by horizontal masks, are selected according to criteria evaluated at each model timestep.  The budget computations are realized at the selected verticals for each criteria. The criteria must be defined in the routine {\it set\_mask.f90}

* :code:`NBUMOD` : number of the model in which the budget are performed. Only one model must be selected even if the grid-nesting is active.

* :code:`NBUMASK` : Number of masks used to select the budgets' areas, in the case CBUTYPE= 'MASK'. 

* :code:`XBULEN` : Timestep  in seconds, on which the different source terms of all the budget are temporally averaged.

* :code:`XBUWRI` : Duration in seconds, between successive writings in the diachronic file of the budget storage arrays for horizontal masks (CBUTYPE='MASK').

* :code:`NBUKL` : value of the model level K for the bottom of the budget box in physical domain, in the case of a cartesian box (CBUTYPE='CART') (NBUKL=1 corresponds to the first vertical physical level).

* :code:`NBUKH` : Same as NBUKL but for the top of the budget box in physical domain. Inside the budget box: :math:`NBUKL \leq K \leq NBUKH`

* :code:`NBUJL` : value of the model level J for the left side of the budget box, in the case of a cartesian box (CBUTYPE='CART') in physical domain.

* :code:`NBUJH` : Same as NBUJL but for the right side of the budget box in physical domain.  Inside the budget box: :math:`NBUJL \leq J \leq NBUJH`

* :code:`NBUIL` : value of the model level I for the left side of the budget box in physical domain, in the case of a cartesian box (CBUTYPE='CART').

* :code:`NBUIH` : Same as NBUIL but for the right side of the budget box in physical domain. Inside the budget box: :math:`NBUIL \leq J \leq NBUIH`

* :code:`LBU_KCP` : Flag to average or not in the K direction all the budget terms, for any CBUTYPE value.

* :code:`LBU_JCP` : Flag to average or not in the J direction all the budget terms, for CBUTYPE='CART'.

* :code:`LBU_ICP` : Flag to average or not in the I direction all the budget terms, for CBUTYPE='CART'.

The description of the budgets for every prognostic variable is given below. Because all the budgets are performed in the same way, we give here some details on the way to select or cumulate the different source terms.

Firstly, there is a flag to activate or not the budget of a given prognostic variable (in the form LBU_*). It should be noted that the budget terms for the variable :math:`\Psi` have the dimension of :math:`{\partial \left[ \tilde{ \rho} \Psi \right] \over \partial t }`.

Then, all the source terms computed in the model for this prognostic variable can be selected. Each term is associated with a name. Enabled terms are simply selected by putting their names in a list (an array of character strings beginning with CBULIST_*). Each entry in the list will generate an output in the diachronic file. It is possible to write each source term separateley by writing one name by entry in the array. Or source terms can be grouped together by  putting them in the same array entry and separating them with the + (plus) sign without spaces. In the latter case, their respective values are added together.

For example, the following NAM_BU_RU namelist:

.. code-block::

   &NAM_BU_RU
     LBU_RU = .TRUE.
     CBULIST_RU(1)='ADV'
     CBULIST_RU(2)='HTURB+VTURB'
   /

will output 2 different terms. The first one corresponds to the advection source term, the second one to the addition of the horizontal and vertical turbulence source terms.

A special name exists to select all the available source terms: ALL. If set (in the first position of the CBULIST_* array), all the available source terms (depending on the simulation parameters) will be written individually in the diachronic file.

