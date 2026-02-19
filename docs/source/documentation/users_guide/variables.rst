Output Variables
=============================================================================

.. note::

   Please contact `us <https://mesonh.cnrs.fr/contact/>`_ if you need more variables in the following tables.

.. toctree::
   :maxdepth: 1
 
   variables/diagnostics.rst
   variables/eolienne.rst       



Only the Meso-NH variables are referenced, not SURFEX one.

.. csv-table:: List of general output variables dedicated to MESONH program
   :header: "Name","Meaning"
   :widths: 30,30

   "ACPRC","Accumulated Cloud Precipitation Rain Rate (mm)"
   "ACPRG","Accumulated Precipitation Graupel Rate (mm)"
   "ACPRH","Accumulated Precipitation Hail Rate (mm)"
   "ACPRR","Accumulated Precipitation Rain Rate (mm)"
   "ACPRS","Accumulated Precipitation Snow Rate (mm)"
   "ACPRT","Total Accumulated Precipitation Rate (mm)"
   "EMIS","Emissivity"
   "EVAP3D","Instantaneous 3D Rain Evaporation flux (kg/kg/s)"
   "INPRC","Instantaneous Cloud Precipitation Rain Rate (mm/h)"
   "INPRG","Instantaneous Precipitation Graupel Rate (mm/h)"
   "INPRH","Instantaneous Precipitation Hail Rate (mm/h)"
   "INPRR","Instantaneous Precipitation Rain Rate (mm/h)"
   "INPRR3D","Instantaneous 3D Rain Precipitation flux (m/s)"
   "INPRS","Instantaneous Precipitation Snow Rate (mm/h)"
   "INPRT","Total Instantaneous Precipitation  Rate (mm/h)"
   "LSPABSM","Large scale absolute pression at time t-dt (Pa)"
   "LSRVM","Large scale Vapor mixing Ratio at time t-dt (kg/kg)"
   "LSTHM","Large scale  potential temperature at time t-dt (K)"
   "LSUM","Large scale horizontal component U of wind at time t-dt (m/s)"
   "LSVM","Large scale horizontal component V of wind at time t-dt (m/s)"
   "LSWM","Large scale vertical wind at time t-dt (m/s)"
   "PABST","Absolute pression at time t (Pa)"
   "RCT","Cloud mixing Ratio at time t (kg/kg)"
   "RGT","Graupel mixing Ratio at time t (kg/kg)"
   "RHODREF","Dry density for reference state with orography (kg/m3)"
   "RHOREFZ","rhodz for reference state without orography (kg/m3)"
   "RHT","Hail mixing Ratio at time t (kg/kg)"
   "RIT","Ice mixing Ratio at time t (kg/kg)"
   "RRT","Rain mixing Ratio at time t (kg/kg)"
   "RST","Snow mixing Ratio at time t (kg/kg)"
   "RVT","Vapor mixing Ratio at time t (kg/kg)"
   "THT","potential temperature at time t (K)"
   "THVREF","Thetav for reference state with orography (K)"
   "THVREFZ","Thetavz for reference state without orography (K)"
   "TKET","Turbulent Kinetic Energy at time t (m2/s2)"
   "TSRAD","Radiative Surface Temperature (K)"
   "UT","Horizontal component U of wind at time t (m/s)"
   "VT","Horizontal component V of wind at time t (m/s)"
   "WT","Vertical wind at time t (m/s)"
   "ZS","Orography (m)"
   "ZSMT","Smoothed orography for SLEVE vertical coordinate (m)"
   "...","..."

.. csv-table:: List of general output variables dedicated to DIAG program
   :header: "Name","Meaning"
   :widths: 30,30
   
   "ZS","Orography [m,2D]"
   "ZSMT","Smoothed orography for SLEVE vertical coordinate [m,2D]"
   "RHODREF","Dry density for reference state with orography [kg/m3,3D]"
   "THVREF","Thetav for reference state with orography [K,3D]"
   "RHOREFZ","Rhodz for reference state without orography [kg/m3,1D]"
   "THVREFZ","Thetavz for reference state without orography [K,1D]"
   "EXNTOP","Exner function at model top"
   "UT","U-wind speed [m/s,3D]"
   "VT","V-wind speed [m/s,3D]"
   "WT","W-wind speed [m/s,3D]"
   "RVT","Water vapor mixing ratio [kg/kg,3D]"
   "UT_ZM","Zonal component of horizontal wind [m/s,3D]" 
   "...","..."                             
  
.. csv-table:: List of variables dedicated to hurricane initialization in PREP_REAL_CASE program
   :header: "Name","Meaning"
   :widths: 30,30
      
   "UT15","Component U of Total wind (m/s)"
   "VT15","Component V of Total wind (m/s)"
   "TEMPTOT","Total Temperature (K)"
   "PRESTOT","Total pressure (Pa)"
   "UT16","component U of Environmental wind (m/s)"
   "VT16","component V of Environmental wind (m/s)"
   "TEMPENV","Environmental Temperature (K)"
   "PRESENV","Environmental pressure (Pa)"
   "UT17","component U of Basic (filtered) wind (m/s)"
   "VT17","component V of Basic (filtered) wind (m/s)"
   "TEMPBAS","Basic (filtered) Temperature (K)"
   "PRESBAS","Basic (filtered) pressure (Pa)"
   "VTDIS","Total disturbance tangential wind (m/s)"
   "...","..."     
