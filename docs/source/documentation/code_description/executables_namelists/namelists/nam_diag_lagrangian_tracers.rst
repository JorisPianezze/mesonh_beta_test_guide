.. _nam_diag_lagrangian_tracers:

NAM_DIAG - Lagrangian tracers
-----------------------------------------------------------------------------

Only available if LLG=T in YINIFILE.des.

* add :code:`LTRAJ=T` in :code:`NAM_DIAG` to store following variables :


.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "X", "X coordinates (km)", "3D"
   "Y", "Y coordinates (km)", "3D"
   "LGX", "X Lagrangian tracers coordinates (m)", "3D"
   "LGY", "Y Lagrangian tracers coordinates (m)", "3D"
   "LGZ", "Z Lagrangian tracers coordinates (m)", "3D"
   "X_TRAJ", "X Lagrangian tracers coordinates at time origin n", "4D"
   "Y_TRAJ", "Y Lagrangian tracers coordinates at time origin n", "4D"
   "Z_TRAJ", "Z Lagrangian tracers coordinates at time origin n", "4D"
   "THT_TRAJ", "corresponding Theta (K)", "4D"
   "MRV_TRAJ", "corresponding Vapor mixing Ratio (g/kg)", "4D"
  
