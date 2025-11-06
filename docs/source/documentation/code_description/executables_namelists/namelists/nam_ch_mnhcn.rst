.. _nam_ch_mnhcn:

NAM_CH_MNHCn
-----------------------------------------------------------------------------

.. csv-table:: NAM_CH_MNHCn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LUSECHEM","LOGICAL",".FALSE."
   "LUSECHAQ","LOGICAL",".FALSE."
   "LUSECHIC","LOGICAL",".FALSE."
   "LCH_INIT_FIELD","LOGICAL",".FALSE."
   "LCH_CONV_SCAV","LOGICAL",".FALSE."
   "LCH_CONV_LINOX","LOGICAL",".FALSE."
   "LCH_PH","LOGICAL",".FALSE."
   "LCH_RET_ICE","LOGICAL",".FALSE."
   "XCH_PHINIT","REAL","5.2"
   "XRTMIN_AQ","REAL","5.e-8"
   "CCHEM_INPUT_FILE","CHARACTER(LEN=128)","'EXSEG1.nam'"
   "CCH_TDISCRETIZATION","CHARACTER(LEN=10)","'SPLIT'"
   "NCH_SUBSTEPS","INTEGER","1"
   "LCH_TUV_ONLINE","LOGICAL",".TRUE."
   "CCH_TUV_LOOKUP","CHARACTER(LEN=128)","'PHOTO.TUV39'"
   "CCH_TUV_CLOUDS","CHARACTER(LEN=4)","'NONE'"
   "XCH_TUV_ALBNEW","REAL","-1.0"
   "XCH_TUV_DOBNEW","REAL","-1.0"
   "XCH_TUV_TUPDATE","REAL","600.0"
   "CCH_VEC_METHOD","CHARACTER(LEN=3)","'MAX'"
   "NCH_VEC_LENGTH","INTEGER","50"
   "XCH_TS1D_TSTEP","REAL","600.0"
   "CCH_TS1D_COMMENT","CHARACTER(LEN=80)","'no comment'"
   "CCH_TS1D_FILENAME","CHARACTER(LEN=128)","'IO1D'"

* :code:`LUSECHEM` : switch to activate chemistry.

* :code:`LUSECHAQ` : switch to activate aqueous phase chemistry.

* :code:`LUSECHIC` : switch to activate ice phase chemistry. This means that several pronostics variables are added equal to the number of solubles gases. These variables represent the mixing ratio of the soluble gases inside the precipitating iced hydrometeors.

* :code:`LCH_INIT_FIELD` : switch to activate initialization subroutine CH_INIT_FIELD_n. If .TRUE. initialized with ASCII file, if .FALSE. initialized with MOCAGE.

* :code:`LCH_CONV_SCAV` : switch to activate scavenging of chemical species (gazeous or aerosol) and dusts by convective precipitations.

* :code:`LCH_CONV_LINOX` : switch to activate the production of NOx by LIghtning flashes inside deep convective clouds and its transport (LCHTRANS must be set to TRUE).

   * LUSECHEM=.FALSE. : a scalar variable named LINOX are written in the Meso-NH file
   * LUSECHEM=.TRUE. : the convective source is added to the NO chemical variable.

* :code:`LCH_PH` : switch to activate the computing of pH in cloud water and rainwater as diagnostic variables. XPHC and XPHR are added in synchronous backup files.

* :code:`LCH_RET_ICE` : switch to activate the retention of solubles gase in iced hydrometeors without considering additional pronostics variables. LUSECHIC is set to FALSE. Be carefull this option leads to a loss of mass.

* :code:`XCH_PHINIT` : pH value when aqueous phase chemistry is activated (LUSECHAQ is set to TRUE). 

  * LCH_PH=.TRUE. : XCH_PHINIT is the initial pH value,
  * LCH_PH=.FALSE. : XCH_PHINIT is the constant pH value during the whole simulation.

* :code:`XRTMIN_AQ` : when aqueous phase chemistry is activated (LUSECHAQ is set to TRUE), XRTMIN_AQ is the threshold value for cloud water (or rainwater) content from which aqueous phase chemistry and exchange between gas and liquid phases are computed.

* :code:`CCHEM_INPUT_FILE` : name of the general purpose input file.

* :code:`CCH_TDISCRETIZATION` : temporal discretization

  * 'SPLIT' : use time-splitting, input fields for solver are scalar variables at t+dt (derived from XRSVS)
  * 'CENTER' : use centered tendencies, input fields for solver are scalar variables at t (XSVT)
  * 'LAGGED' : use lagged tendencies, input fields for solver are scalar variables at t-dt (XSVM)

* :code:`NCH_SUBSTEPS` : number of steps to be taken by the solver during two time steps of MesoNH; the time step of the solver is thus equal to 2*XTSTEP/NCH_SUBSTEPS

* :code:`LCH_TUV_ONLINE` : switch to activate online photolysis rates calculations (only for 1D simulation). If false, photolysis rates are pre-calculated as a function of solar zenith angle and surface albedo and interpolated on the model grid.

* :code:`CCH_TUV_LOOKUP` : name of the lookup table file.

* :code:`CCH_TUV_CLOUDS` : method for calculating the impact of clouds on UV radiations (only for 3-D version)

  * 'NONE' : No cloud correction on UV radiations
  * 'CHAN' : Cloud correction on UV radiations following Chang et al., [1987]

* :code:`XCH_TUV_ALBNEW` : surface albedo for photolysis rates calculations (only for 1-D version. For 3-D version, albedos are prescribed as a function of the surface characteristics).

* :code:`XCH_TUV_DOBNEW` : scaling factor for ozone column dobson.

* :code:`XCH_TUV_TUPDATE` : update frequency to refresh photolysis rates.

* :code:`CCH_VEC_METHOD` : type of vectorization mask

  * 'MAX' : take NCH_VEC_LENGTH points
  * 'TOT' : take all grid points
  * 'HOR' : take horizontal layers
  * 'VER' : take vertical columns

* :code:`NCH_VEC_LENGTH` : number of points for 'MAX' option.

* :code:`XCH_TS1D_TSTEP` : time between two call to write_ts1d.

* :code:`CCH_TS1D_COMMENT` : comment for write_ts1d.

* :code:`CCH_TS1D_FILENAME` : filename for write_ts1d files.
