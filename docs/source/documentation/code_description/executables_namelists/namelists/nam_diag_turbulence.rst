.. _nam_diag_turbulence:

NAM_DIAG - Turbulence
-----------------------------------------------------------------------------

* define :code:`LVAR_TURB=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "TKET", "Turbulent Kinetic Energy (m2/s2)", "3D"
   "SIGS", "Sigma_s from turbulence scheme (kg/kg2)", "3D"
   "SRCM", "Normalized 2nd_order moment (kg/kg2)", "3D"
   "BL_DEPTH", "Boundary Layer Depth if CTOM=’TM06’ (m)", "3D"

* define :code:`LTURBDIAG=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "AMOIST", "(m) See Scientific documentation part III, chap 7 equation 7.29", "3D"
   "ATHETA", "(m) See Scientific documentation part III, chap 7 equation 7.30", "3D"
   "RED_TH1, RED_R1, RED2_TH3, RED2_R3, RED2_THR3", "Redelsperger numbers", "3D"
   "TKE_DP", "dynamical production of TKE (m2/s3)", "3D"
   "TKE_TP", "thermal production of TKE (m2/s3)", "3D"
   "TKE_TR", "transport of TKE (m2/s3)", "3D"
   "TKE_DISS", "dissipation of TKE (m2/s3)", "3D"
   "LM_CLEAR_SKY", "mixing length in clear sky (m)", "3D"
   "COEF_AMPL", "amplification of the mixing length (-)", "3D"
   "LM_CLOUD", "mixing length in the clouds (m)", "3D"
   "LM", "mixing length (m)", "3D"
   "THLM", "conservative potential temperature (K)", "3D"
   "RNPM", "conservative mixing ratio (kg/kg)", "3D"
   "RVCI", "rv + rc + ri (kg/kg)", "3D"
   "GX_RVCI,GY_RVCI", "x and y gradient of RVCI (kg/kg/m)", "3D"
   "GNORM_RVCI", "Horizontal norm of the gradient of RVCI (kg/kg/m)", "3D"
   "QX_RVCI", "x gradient of the advection of RVCI (kg/kg/m)", "3D"
   "QY_RVCI", "y gradient of the advection of RVCI (kg/kg/m)", "3D"
   "QNORM_RVCI", "Horizontal norm of the gradient of the advection of RVCI (kg/kg/m)", "3D"
   "CEI", "Cloud entrainment instability index (kg/kg/m/s)", "3D"

* define :code:`LTURBFLX=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "PHI3", "Turbulent Prandtl number (-)", "3D"
   "PSI3", "Turbulent Schmidt number (-)", "3D"
   "PSI_SV_n", "Turbulent Schmidt number for the scalar variables (-)", "3D"

* define :code:`LTURBFLX=T` in :code:`NAM_DIAG` and if CTURBDIM='1D' in YINIFILE.des following variables will stored :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "THW_FLX", "theta vertical flux (K*m/s)", "3D"
   "RCONSW_FLX", "rv vertical flux (kg*m/s/kg)", "3D"
   "RCW_FLX", "liquid water mixing ratio vertical flux (kg*m/s/kg)", "3D"
   "THL_VVAR", "< T Hl, T Hl > (K2)", "3D"
   "THLRCONS_VCOR", "< T Hl, Rnp >( K*kg/kg)", "3D"
   "RTOT_VVAR", "< Rnp, Rnp > ((kg/kg)2)", "3D"
   "UW_VFLX, VW_VFLX", "wind component vertical flux (m2/s2)", "3D"
   "WSV_FLX_n", "< W, SV th >(SVunit m/s)", "3D"

* define :code:`LTURBFLX=T` in :code:`NAM_DIAG` and if CTURBDIM='3D' in YINIFILE.des following variables will stored :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "THW_FLX", "theta vertical flux (K*m/s)", "3D"
   "RCONSW_FLX", "rv vertical flux (kg*m/s/kg)", "3D"
   "RCW_FLX", "liquid water mixing ratio vertical flux (kg*m/s/kg)", "3D"
   "THL_VVAR", "< T Hl, T Hl > (K2)", "3D"
   "THLRCONS_VCOR", "< T Hl, Rnp >( K*kg/kg)", "3D"
   "RTOT_VVAR", "< Rnp, Rnp > ((kg/kg)2)", "3D"
   "UW_VFLX, VW_VFLX", "wind component vertical flux (m2/s2)", "3D"
   "WSV_FLX_n", "< W, SV th >(SVunit m/s)", "3D"   
   "U_VAR", "U variance ((m/s)2)", "3D"
   "V_VAR", "V variance ((m/s)2)", "3D"
   "W_VAR", "W variance ((m/s)2)", "3D"
   "UV_FLX", "< U, V >((m/s)2,)", "3D"
   "UW_HFLX", "< U, W > ((m/s)2)", "3D"
   "VW_HFLX", "< V, W > ((m/s)2)", "3D"
   "USV_FLX_n", "< U, SV th > ( SVunit m/s)", "3D"
   "VSV_FLX_n", "< V, SV th > ( SVunit m/s)", "3D"
   "THL_HVAR", "< T Hl, T Hl > (K2)", "3D"
   "THLR_HCOR", "< T Hl, Rnp > (K*kg/kg)", "3D"
   "R_HVAR", "< Rnp, Rnp > ( (kg/kg)2)", "3D"
   "UTHL_FLX", "horizontal < U, T Hl > (K*m/s)", "3D"
   "VTHL_FLX", "horizontal < V, T Hl > (K*m/s)", "3D"
   "UR_FLX", "horizontal < U, Rnp > (kg/kg*m/s)", "3D"
   "VR_FLX", "horizontal < V, Rnp > (kg/kg*m/s)", "3D"

  
