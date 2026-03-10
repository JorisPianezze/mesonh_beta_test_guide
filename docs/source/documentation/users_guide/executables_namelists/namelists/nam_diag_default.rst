.. _nam_diag_default:

NAM_DIAG - Default
-----------------------------------------------------------------------------

By default, the following variables are written in the output file created by the DIAG program:

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "ZS", "orography [m]", "2D"
   "ZSMT", "smoothed orography for SLEVE vertical coordinate [m]", "2D"
   "RHODREF", "dry density for reference state with orography [:math:`kg/m^3`]", "3D"
   "THVREF", ":math:`\theta_v` for reference state with orography [K]", "3D"
   "RHOREFZ", ":math:`\rho_d(z)` for reference state without orography [:math:`kg/m^3`]", "1D"
   "THVREFZ", ":math:`\theta_v(z)` for reference state with orography [K]", "1D"
   "EXNTOP", "exner function at model top [-]", ""
   "SVPPn", "passive pollutant n concentration only if :code:`LPASPOL=T` in YINIFILE.des [:math:`g/m^3`]", "3D"

Surface variables by default only if :code:`CSURF='EXTE'` in YINIFILE.des:

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "UM10, VM10", "zonal and meridional wind at 10 m height AGL [m/s]", "2D"
   "FF10MAX", "wind gusts at 10 m height AGL, with TKE component taken at first mass level :math:`4\sqrt{TKE_{IKB}}` (only if CTURB='TKEL') [m/s]", "2D"
   "FF10MAX2", "wind gusts at 10 m height AGL, with TKE component taken at 10m :math:`4\sqrt{TKE_{10m}}` (only if CTURB='TKEL') [m/s]", "2D"
   "FF10MAX_AROME", "wind gusts at 10 m height AGL, with TKE component taken at 20m :math:`3.8\sqrt{TKE_{20m}}` as in AROME-France (only if CTURB='TKEL')", "2D"
   "SFCO2", ":math:`CO_2` flux if present in YINIFILE [mg/m²/s]", "2D"