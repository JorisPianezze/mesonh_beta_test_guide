.. _nam_nebn:

NAM_NEBn
-----------------------------------------------------------------------------

This namelist is new and regroup options related to internal clouds life cycle.

.. csv-table:: NAM_NEBn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LHGT_QS","LOGICAL",".FALSE."
   "LSTATNW","LOGICAL",".FALSE."
   "XTMINMIX","REAL","253.16"
   "XTMAXMIX","REAL","273.16"
   "LSUBG_COND","LOGICAL",".FALSE."
   "CCONDENS","CHARACTER(LEN=80)","'CB02'"
   "CLAMBDA3","CHARACTER(LEN=4)","'CB'"
   "LSIGMAS","LOGICAL",".TRUE."
   "VSIGQSAT","REAL","0.02"
   "CFRAC_ICE_ADJUST","CHARACTER(LEN=1)","'S'"
   "CFRAC_ICE_SHALLOW_MF","CHARACTER(LEN=1)","'S'"
   "LCONDBORN","LOGICAL",".FALSE."

* :code:`LHGT_QS` : flag to activate height dependence of qsat variance (VSIGQSAT)

* :code:`LSTATNW` : flag to switch on the full updated statistical cloud scheme

* :code:`XTMINMIX` : minimum temperature of mixed phase (K)

* :code:`XTMAXMIX` : maximum temperature of mixed phase (K)

* :code:`LSUBG_COND` : flag to activate the subgrid condensation scheme (refer to the scientific documentation for more details). It is strongly recommended to activate it at kilometric horizontal resolution (such as in AROME).  With the microphysics scheme LIMA (CCLOUD='LIMA' in :ref:`nam_paramn`), it must be used with time-splitting LPTSPLIT=T in :ref:`nam_param_lima`.

* :code:`CCONDENS` : subgrid distribution used in the saturation adjustment

  * 'CB02' : to use the :cite:t:`chaboureau_simple_2002` formulations
  * 'GAUS' : to use a gaussian PDF

* :code:`CLAMBDA3` : modulation of s'r' computation in the saturation adjustment

  * 'CB' : to use the formulation originally associated to the use of CCONDENS='CB02'
  * 'NONE' : to use a value of 1 (no modulation)

* :code:`VSIGQSAT` : coefficient applied to qsat variance contribution. Only available if LSIGMAS=.TRUE.

* :code:`LSIGMAS` : flag for using Sigma_s from turbulence scheme instead parameterized values in ice subgrid condensation scheme

* :code:`CFRAC_ICE_ADJUST` : Way to compute ice fraction 

  * 'T' : linear formulation according to temperature
  * 'O' : Tao et al. (1989) formulation
  * 'N' : No ice
  * 'S' : Ice fraction given by the slow microphysics

* :code:`CFRAC_ICE_SHALLOW_MF` : Way to compute ice fraction for MF contribution

  * 'T' : linear formulation according to temperature
  * 'O' : Tao et al. (1989) formulation
  * 'N' : No ice
  * 'S' : Ice fraction given by the slow microphysics

* :code:`LCONDBORN` : flag to limit condensation


