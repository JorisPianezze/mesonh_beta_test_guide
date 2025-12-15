.. _nam_diag_lightnings:

NAM_DIAG - Lightnings
-----------------------------------------------------------------------------

If :code:`LCH_CONV_LINOX=T` and :code:`LUSECHEM=F` in :file:`YINIFILE.des` with :code:`LCHEMDIAG=F` in :file:`DIAG1.nam`, following variables will be stored :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "LINOX", "Linox scalar variables (ppb)", "3D"
   "IC_RATE", "IntraCloud lightning Rate (/s)", "2D"
   "CG_RATE", "CloudGround lightning Rate (/s)", "2D"
   "IC_TOTAL_NB", "IntraCloud lightning Number (-)", "2D"
   "CG_TOTAL_NB", "CloudGround lightning Number (-)", "2D"
  
