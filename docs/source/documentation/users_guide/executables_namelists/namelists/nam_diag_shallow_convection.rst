.. _nam_diag_shallow_convection:

NAM_DIAG - Shallow convection
-----------------------------------------------------------------------------

* add :code:`LMFFLX=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "MF_THW_FLX", "Conservative potential temperature vertical flux (K*m/s)", "3D"
   "MF_RCONSW_FLX", "Conservative mixing ratio vertical flux (kg/kg*m/s)", "3D"
   "MF_THVW_FLX", "Theta_v vertical flux (K*m/s)", "3D"
   "MF_UW_VFLX", "U momentum vertical flux (m2/s2)", "3D"
   "MF_VW_VFLX", "V momentum vertical flux (m2/s2)", "3D"
  
