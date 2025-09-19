.. _nam_diag_radar_simulator:

NAM_DIAG - RADAR simulator
-----------------------------------------------------------------------------

.. note:: 

   A radar simulator already existed in Meso-NH (Richard et al.,2003) that computes reflectivities in the Rayleigh approximation on each grid points of the model (NVERSION_RAD=1). However, with the view to code an observation operator for radar reflectivities, this simulator was not sufficient. That is why a new simulator was built, while the original version is still available. This new simulator (NVERSION_RAD=2) simulates Plan Position Indicators (PPI), which are cones usually projected on a horizontal plane obtained by scanning the atmosphere at constant elevation. New features are:

   * possibility to choose among several scattering models,
 
   * beam bending taken into account,

   * possibility to take attenuation into account,

   * antenna’s radiation pattern (beam broadening) modeled,
 
   * ouptut on operational (Cartesian) grids of the Aramis French radar network.
   
* add :code:`LRADAR=T` and :code:`NVERSION_RAD=1` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "RARE", "Radar Reflectivity (dBz)", "3D"
   "VDOP", "Radar Doppler fall speed (m/s)", "3D"
   "ZDR", "Radar Differential Reflectivity (dBZ)", "3D"
   "KDP", "Radar Differential Phase shift (degree/km)", "3D"

* add :code:`LRADAR=T` and :code:`NVERSION_RAD=2` in :code:`NAM_DIAG` to store following variables :

.. note::
   
   As output fields are not on the model grid, they have to be written in other files than LFIs. Therefore the following files are written in the following format: AAABBBCC.CDDDX for cartesian coordinates and PAAABBBCC.CX for polar coordinates, where AAA is the descriptor of the field (3 characters, see below for further explanations), BBB is the name of the radar (3 characters), CC.C is the elevation (in degrees), DDD is half the number of pixels on each row or column (3 characters), and X is the name of the input file. Example of file name for cartesian coordinates : ZHHBOL00.4300BOG12.2.SEG04.004RD

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "ZHH", "overall reflectivity (dBZ)", ""
   "ZER", "reflectivity due to rain (dBZ)", ""
   "ZEI", "reflectivity due to pristine ice (dBZ)", ""
   "ZES", "reflectivity due to snow (dBZ)", ""
   "ZEG", "reflectivity due to graupel (dBZ)", ""
   "KDP", "specific differential phase (km-1)", ""
   "ZDR", "differential reflectivity (dB)", ""
   "VRU", "Doppler velocity (m s-1)", ""
   "HAS", "height of middle of beam MSL (m)", ""
   "M_R", "rainwater contents in the middle of the beam (kg kg-1)", ""
   "M_I", "primary ice contents in the middle of the beam (kg kg-1)", ""
   "M_S", "snow contents in the middle of the beam (kg kg-1)", ""
   "M_G", "graupel contents in the middle of the beam (kg kg-1)", ""
   "CIT", "pristine ice concentration in the middle of the beam (kg m-3)", ""
   "AET", "overall two-way specific attenuation (dB km-1) (if LATT=T)", ""
   "AER", "two-way specific attenuation due to rain (dB km-1) (if LATT=T)", ""
   "AEI", "two-way specific attenuation due to pristine ice (dB km-1) (if LATT=T)", ""
   "AES", "two-way specific attenuation due to snow (dB km-1) (if LATT=T)", ""
   "AEG", "two-way specific attenuation due to graupel (dB km-1) (if LATT=T)", ""
   "ATT", "overall two-way path-integrated attenuation (PIA) (dB) (if LATT=T)", ""
   "ATR", "two-way PIA due to rain (dB) (if LATT=T)", ""
   "ATI", "two-way PIA due to pristine ice (dB) (if LATT=T)", ""
   "ATS", "two-way PIA due to snow (dB) (if LATT=T)", ""
   "ATG", "two-way PIA due to graupel (dB) (if LATT=T)", ""
   "RFR", "refractivity in the middle of the beam (if LREFR=T)", ""
   "DNZ", "vertical gradient of refractivity in the middle of the beam (km-1) (if LDNDZ=T)", ""
   "CSR", "index characterizing the pixel", ""
   "PDP", "differential phase beetween horizontal and vertical polarizations (◦)", ""
   "KDR,KDS,KDG", "specific differential phase due to rain, snow or graupel(km-1)", ""
   "ZDA,ZDS,ZDG", "differential reflectivity due to rain, snow or graupel (dB)", ""
   "RHV,RHR,RHS,RHG", "copolar correlation coefficient due to all hydrometeors, rain, snow or graupel (/)", ""
   "TEM", "model temperature (C)", ""
   "DHV", "backscattering differentiel phase ()", ""

.. note::

   Following options can be used in :code:`NAM_DIAG` when :code:`LRADAR=T` and :code:`NVERSION_RAD=2` is activated :

   .. csv-table::
      :header: "Fortran name", "Fortran type", "Default value"
      :widths: 30, 30, 30
      
      "XLAT_RAD","array of reals","XUNDEF"
      "XLON_RAD","array of reals","XUNDEF"
      "XALT_RAD","array of reals","XUNDEF"
      "CNAME_RAD","array of strings","XUNDEF"
      "XLAM_RAD","array of reals","XUNDEF"
      "XDT_RAD","array of reals","XUNDEF"
      "XELEV","2-dim array of reals","XUNDEF"
      "NBSTEPMAX","integer","-1"
      "XSTEP_RAD","real","XUNDEF"
      "LATT","logical",".FALSE."
      "LQUAD","logical",".FALSE."
      "NPTS_H","integer","1"
      "NPTS_V","integer","1"
      "CARF","character(5)", "PB70"
      "LREFR","logical",".FALSE."
      "LDNDZ","logical",".FALSE."
      "NCURV_INTERPOL","integer","0"
      "LCART_RAD","integer",".TRUE."
      "NBAZIM","logical",".720"
      "NDIFF","integer","0"
      "NPTS_GAULAG","integer","7"
      "XGRID","real","2000.0"
      "LFALL","logical",".FALSE."
      "LWREFL","logical",".FALSE."
      "LWBSCS","logical",".FALSE."
      "XREFLMIN","real","-30."
      "XREFLVDOPMIN","real","-990."
      "LSNRT","logical",".TRUE."
      "XSNRMIN","real","0"

   * :code:`XLAT_RAD` : latitude of each radar

   * :code:`XLON_RAD` : longitude of each radar
   
   * :code:`XALT_RAD` : altitudes of radars (m)
   
   * :code:`CNAME_RAD` : names of radars
   
   * :code:`XLAM_RAD` : radar wavelengths
   
   * :code:`XDT_RAD` : beam width to the -3 dB level for one-way transmission (:math:`\Delta\theta`)
   
   * :code:`XELEV` : radar elevations (:math:`\theta`). First dimension: radar; second: site number
   
   * :code:`NBSTEPMAX` : number of gates
   
   * :code:`XSTEP_RAD` : gate length (m)
   
   * :code:`LATT` : attenuation is taken into account if true
   
   * :code:`LQUAD` : if true Gauss-Legendre quadrature if false Gauss-Hermite quadrature
   
   * :code:`NPTS_H` : number of angles for the quadrature in horizontal
   
   * :code:`NPTS_V` : number of angles for the quadrature in vertical
   
   * :code:`CARF` : 
   
     * "PB70" : Pruppacher and Beard (1970).
     * "AND99" : axis ratio of raindrops : Andsager et al. (1999).
     * "BR02" : axis ratio of raindrops : Brandes et al. (2002).
     * "SPHE" : axis ratio for spheres (r=1)
     
   * :code:`LREFR` : if true writes out refractivity (:math:`N\equiv(n-1)\times10^6`)
   
   * :code:`LDNDZ` : if true writes out vertical gradient of refractivity (:math:`\partial N/\partial z`)
   
   * :code:`NCURV_INTERPOL` : 
   
     * 0 : use an average beam bending equivalent to 4/3 of the Earth's radius
     * 1 : compute the beam bending at each gate by using model variables

   * :code:`LCART_RAD` : if true interpolation of reflectivity on a cartesian grid ; false if polar
   
   * :code:`NBAZIM` : Number of azimuths in polar coordinates (used only if LCART_RAD=.FALSE)
   
   * :code:`NDIFF` : 
   
     * 0 : Rayleigh scattering
     * 1 : Mie scattering
     * 3 : Rayleigh for spheroids scattering
     * 4 : Rayleigh with 6th order for attenuation calculations
     * 7 : T-matrix scattering (from lookup tables reading)

   * :code:`NPTS_GAULAG` : number of points of the quadrature
   
   * :code:`XGRID` : size of the Cartesian grid (m)
   
   * :code:`LFALL` : if true takes into account hydrometeor fall speeds
   
   * :code:`LWREFL` : if true takes into account the weighting by reflectivities
   
   * :code:`LWBSCS` : if true takes into account the weighting by hydrometeor concentrations
   
   * :code:`XREFLMIN` : minimum detectable reflectivity (in dBZ)
   
   * :code:`XREFLVDOPMIN` : minimum detectable reflectivity to compute Doppler velocities (in dBZ; useless when LWREFL=.FALSE.)
   
   * :code:`LSNRT` : if true ZHH ZER ZEI ZES ZEG and doppler velocity are thresholded when NR < XSNRMIN
   
   * :code:`XSNRMIN` : minimum SNR (used only if LSNRT=T)

