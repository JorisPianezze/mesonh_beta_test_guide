.. _nam_diag_general:

NAM_DIAG - General
-----------------------------------------------------------------------------
  
* add :code:`LVAR_LS=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "LSUM",   "large scale u-wind speed [m/s]", "3D"
   "LSVM",  "large scale v-wind speed [m/s]", "3D"
   "LSWM",  "large scale w-wind speed [m/s]", "3D"
   "LSTHM", "large scale potential temperature [K]", "3D"
   "LSRVM", "large scale water vapor mixing ratio [kg/kg]", "3D"   

* add :code:`LVAR_LS=T` and :code:`LWIND_ZM=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "LSUM_ZM", "large scale zonal wind speed [m/s]", "3D"
   "LSVM_ZM", "large scale meridian wind speed [m/s]", "3D"

* add :code:`LVAR_FRC=T` in :code:`NAM_DIAG` (:code:`LFORCING` has to be :code:`T` in :file:`YINIFILE.des`) to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "UFRCn",       "zonal component of horizontal forcing wind [m/s]", "1D"
   "VFRCn",       "meridian component of horizontal forcing wind [m/s]", "1D"
   "WFRCn",       "vertical forcing wind [m/s]", "1D"
   "THFRCn",      ":math:`\theta_{\rm frc}` forcing potential temperature [K]", "1D"
   "RVFRCn",      ":math:`r_{v,\rm frc}` forcing vapor mixing ratio [kg/kg]", "1D"
   "TENDTHFRCn",  ":math:`(\partial \theta/\partial t)_{\rm frc}` (K/s)", "1D"
   "TENDRVFRCn",  ":math:`(\partial r_v/\partial t)_{\rm frc}` ((kg/kg)/s)", "1D"
   "GXTHFRCn",    ":math:`(\partial \theta/\partial x)_{\rm frc}` (K/m)", "1D"
   "GYRVFRCn",    ":math:`(\partial \theta/\partial y)_{\rm frc}` (K/m)", "1D"
   "PGROUNDFRCn", "forcing ground pressure (Pa)", "0D"
   
* add :code:`LTPZH=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "TEMP",  "temperature [C]", "3D" 
   "PRES",  "pressure [hPa]", "3D" 
   "ALT",   "height of model levels (geopotentiel in pressure level) [m]", "3D"
   "REHU",  "relative Humidity [%] (if :code:`LUSERV=T`)", "3D"
   "VPRES", "vapor Pressure [hPa] (if :code:`LUSERV=T`)", "3D"

* add :code:`LCOREF=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "COREF",  "refraction coindex (if :code:`LUSERV=T`)", "3D"
   "MCOREF", "modified refraction coindex (if :code:`LUSERV=T`)", "3D"

* add :code:`LMOIST_V=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "THETAV", "virtual potential Temperature [K]", "3D"
   "POVOV",  "virtual Potential Vorticity [PVU]", "3D"
  
* add :code:`LMOIST_V=T` and :code:`LMEAN_POVO=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "MEAN_POVOV", "mean virtual potential vorticity (PVU)", "2D"

* add :code:`LMOIST_E=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "THETAE", "equivalent potential Temperature [K]", "3D"
   "POVOE",  "equivalent Potential Vorticity [PVU]", "3D"

* add :code:`LMOIST_E=T` and :code:`LMEAN_POVO=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "MEAN_POVOE", "mean equivalent potential vorticity (PVU)", "2D"

* add :code:`LMOIST_ES=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "THETAES", "equivalent saturated potential temperature [K]", "3D"
   "POVOES",  "equivalent saturated potential vorticity [PVU]", "3D"

* add :code:`LMOIST_S1=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "THETAS1", "Moist air Entropy (1st order) potential temperature [K]", "3D"

* add :code:`LMOIST_S2=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "THETAS2", "Moist air Entropy (2nd order) potential temperature [K]", "3D"
   
* add :code:`LMOIST_L=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "THETAL", "Liquid water potential temperature [K]", "3D"   

* add :code:`LMEAN_POVO=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "MEAN_POVO", "Mean Potential Vorticity (PVU)", "2D"

* add :code:`LMEAN_POVO=T` and :code:`LMOIST_V=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "MEAN_POVOV", "Mean virtual Potential Vorticity (PVU)", "2D"

* add :code:`LMEAN_POVO=T` and :code:`LMOIST_E=T` :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "MEAN_POVOE", "Mean equivalent Potential Vorticity (PVU)", "2D"

.. note::

   Add :code:`XMEAN_POVO(1:2)` in :code:`NAM_DIAG` to chose averaged between two isobaric levels in Pa (XMEAN_POVO(1),XMEAN_POVO(2)) (by default (15000,50000))

* add :code:`LVORT=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "ABVOR", "Mean equivalent Potential Vorticity (PVU)", "2D"
   "UM1", "u-relative vorticity components (/s)", "3D"
   "VM1", "v-relative vorticity components (/s)", "3D"
   "WM1", "w-relative vorticity components (/s)", "3D"

* add :code:`LVORT=T` and :code:`LWIND_ZM=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "UM1_ZM", "zonal relative vorticity components (m/s)", "3D"
   "VM1_ZM", "meridian relative vorticity components (m/s)", "3D"

* add :code:`LDIV=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "HDIV", "Horizontal divergence (/s)", "3D"
   "HMDIV", "Horizontal Moisture divergence (kg/m3/s)", "3D"

* add :code:`LGEO=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "UM88", "Geostrophic u-wind components (m/s)", "3D"
   "VM88", "Geostrophic v-wind components (m/s)", "3D"
   "WM88", "Geostrophic w-wind components (m/s)", "3D"

* add :code:`LGEO=T` and :code:`LWIND_ZM=T` in :code:`NAM_DIAG` to store following variables :
  
.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "UM88_ZM", "Geostrophic zonal wind components (m/s)", "3D"
   "VM88_ZM", "Geostrophic meridian wind components (m/s)", "3D"
     
* add :code:`LAGEO=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "UM89", "Ageostrophic u-wind components (m/s)", "3D"
   "VM89", "Ageostrophic v-wind components (m/s)", "3D"
   "WM89", "Ageostrophic w-wind components (m/s)", "3D"
   
* add :code:`LAGEO=T` and :code:`LWIND_ZM=T` in :code:`NAM_DIAG` to store following variables :
  
.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "UM89_ZM", "Ageostrophic zonal wind components (m/s)", "3D"
   "VM89_ZM", "Ageostrophic meridian wind components (m/s)", "3D"

* add :code:`LMSLP=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "MSLP", "Mean Sea Level Pressure (hPa)", "2D"

* add :code:`LBV_FR=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "BV", "Brunt-Vaissala frequency (/s)", "3D"
   "BVE", "Equivalent Brunt-Vaissala frequency (/s)", "3D"

* add :code:`LVAR_MRSV=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "MRSVnnn", "Mixing Ratio for User Scalar Variable n (g/kg)", "3D"

* define :code:`CBLTOP="RICHA"` in :code:`NAM_DIAG` to store following variable :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "HBLTOP", "Height of boundary layer top (m) computed with bulk Richardson number method", "2D"

* define :code:`CBLTOP="THETA"` in :code:`NAM_DIAG` to store following variable :
  
.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "HBLTOP", "Height of boundary layer top (m) computed with parcel method", "2D"

* add :code:`LHU_FLX=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "UM90", "u-wind components of moisture ground flux (kg/s/m2)", "2D"
   "VM90", "v-wind components of moisture ground flux (kg/s/m2)", "2D"   
   "UM91", "u-wind components of moisture ground flux integrated on 3000 meters (kg/s/m)", "2D"
   "VM91", "v-wind components of moisture ground flux integrated on 3000 meters (kg/s/m)", "2D"   
   "HMCONV", "Horizontal CONVergence of moisture flux (kg/s/m2)", "2D"
   "HMCONV3000", "Horizontal CONVergence of moisture flux integrated on 3000 meters (kg/s/m2)", "2D"
   "UM92", "u-wind components of hydrometeores ground flux (if CCLOUD=ICE3 or ICE4) (kg/s/m2)", "2D"
   "VM92", "v-wind components of hydrometeores ground flux (if CCLOUD=ICE3 or ICE4) (kg/s/m2)", "2D"   
   "UM93", "u-wind components of hydrometeor ground flux (if CCLOUD=ICE3 or ICE4) (kg/s/m)", "2D"
   "VM93", "v-wind components of hydrometeor ground flux (if CCLOUD=ICE3 or ICE4) (kg/s/m)", "2D"   
   "HMCONV_TT", "Horizontal CONVergence of hydrometeor flux (kg/s/m2)", "2D"
   "HMCONV3000_TT", "Horizontal CONVergence of hydrometeor flux integrated on 3000 meters (kg/s/m2)", "2D"

*  define NCAPE=0 in :code:`NAM_DIAG` to store following variables :
  
.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "CAPEMAX", "maximum of CAPE3D (J/kg)", "2D"
   "CINMAX", "value of CIN3D corresponding to CAPEMAX (J/kg)", "2D"

*  define NCAPE=1 in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "CAPEMAX", "maximum of CAPE3D (J/kg)", "2D"
   "CINMAX", "value of CIN3D corresponding to CAPEMAX (J/kg)", "2D"
   "CAPE3D", "Convective Available Potential Energy (J/kg)", "3D"
   "CIN3D", "Convective INhibition energy (J/kg)", "3D"
   "DCAPE3D", "Downdraft cape (J/kg)", "3D"


*  define NCAPE=2 in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "CAPEMAX", "maximum of CAPE3D (J/kg)", "2D"
   "CINMAX", "value of CIN3D corresponding to CAPEMAX (J/kg)", "2D"
   "CAPE3D", "Convective Available Potential Energy (J/kg)", "3D"
   "CIN3D", "Convective INhibition energy (J/kg)", "3D"
   "DCAPE3D", "Downdraft cape (J/kg)", "3D"   
   "VKE", "Vertical Kinetic Energy (from explicit vertical motion) (J/kg)", "3D"
