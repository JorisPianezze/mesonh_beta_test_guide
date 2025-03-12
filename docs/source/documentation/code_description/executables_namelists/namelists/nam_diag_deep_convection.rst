.. _nam_diag_deep_convection:

NAM_DIAG - Deep convection
-----------------------------------------------------------------------------

* define :code:`NCONV_KF=0` in :code:`NAM_DIAG` to store following variables :
  
.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "CAPE", "Convective Available Potentiel Energy (J/kg)", "2D"
   "CLTOPCONV", "top of convective clouds(km)", "2D"
   "CLBASCONV", "base of convective clouds(km)", "2D"

* define :code:`NCONV_KF=1` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "CAPE", "Convective Available Potentiel Energy (J/kg)", "2D"
   "CLTOPCONV", "top of convective clouds(km)", "2D"
   "CLBASCONV", "base of convective clouds(km)", "2D"
   "DTHCONV", "Convective tendency for potential temperature (K/s)", "3D"
   "DRVCONV", "Convective tendency for vapor (/s)", "3D"
   "DRCCONV", "Convective tendency for cloud (/s)", "3D"
   "DRICONV", "Convective tendency for ice (/s)", "3D"
   "DSVCONVnn", "Convective tendency for scalar variables (/s)", "3D"

* define :code:`NCONV_KF=2` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "CAPE", "Convective Available Potentiel Energy (J/kg)", "2D"
   "CLTOPCONV", "top of convective clouds(km)", "2D"
   "CLBASCONV", "base of convective clouds(km)", "2D"
   "DTHCONV", "Convective tendency for potential temperature (K/s)", "3D"
   "DRVCONV", "Convective tendency for vapor (/s)", "3D"
   "DRCCONV", "Convective tendency for cloud (/s)", "3D"
   "DRICONV", "Convective tendency for ice (/s)", "3D"
   "DSVCONVnnn*", "Convective tendency for scalar variables (/s)", "3D"
   "UMFCONV", "Updraft Convective Mass Flux (m2 kg/s)", "3D"
   "DMFCONV", "Downdraft Convective Mass Flux (m2 kg/s)", "3D"
   "PRLFLXCONV", "Liquid PRecipitation Convective FLuX (m/s)", "3D"
   "PRSFLXCONV", "Solid PRecipitation Convective FLuX (m/s)", "3D"
  
