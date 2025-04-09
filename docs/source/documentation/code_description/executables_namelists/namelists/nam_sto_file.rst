.. _nam_sto_file:

NAM_STO_FILE
-----------------------------------------------------------------------------

Controls trajectories computation, only read if LTRAJ=.TRUE. in NAM_DIAG.

.. csv-table:: NAM_STO_FILE content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CFILES","ARRAY(CHARACTER(LEN=128)",""
   "NSTART_SUPP","ARRAY(INTEGER)","100*NUNDEF"


* :code:`CFILES` : name of all the input synchronous backup files used to compute trajectories. They must be in inverse chronological order, and correspond to a reinitialisation of Lagrangian tracers (see :ref:`mesonh`).

* :code:`NSTART_SUPP` : extra origins for trajectory computations. In the second example below, the output files will contain the set of variables (X_TRAJ, Y_TRAJ, Z_TRAJ, THT_TRAJ, MRV_TRAJ).

.. note::

   * Example 1 :
   
   .. code-block:: fortran

      &NAM_DIAG
         LVAR_LS=T, NCONV_KF=2, NRAD_3D=1,
         LVAR_MRW=T, LVAR_MRSV=T, LMOIST_V=T, LMOIST_E=F,
         LTPZH=T, LVORT=F, LMSLP=F, LGEO=T, LAGEO=T, LWIND_ZM=F,
         LTHW=T, LCLD_COV=T,
         LVAR_PR=F, LTOTAL_PR=F, LMEAN_PR=F, XMEAN_PR(1,2)=4. ,
         NCAPE=1, LRADAR=T, LTRAJ=F /
     &NAM_DIAG_BLANK /
     &NAM_DIAG_FILE YINIFILE(1) = "F9801.1.06A12.002" ,
                    YINIFILEPGD(1) = "PGD_F9801" ,
                    YSUFFIX = "diag" /
     &NAM_DIAG_ISBAn N2M=2, LSURF_BUDGET=T /
     
   * Example 2 : Namelist file for 6 files using trajectories computation

   .. code-block:: fortran
   
      &NAM_DIAG
      LVAR_PR=T, LTOTAL_PR=T, LTPZH=T, LVAR_MRSV=T, LTRAJ=T /
      &NAM_DIAG_FILE YSUFFIX='d18-6',
      YINIFILE(1) = "NAPE2.1.APE05.001" ,
      YINIFILEPGD(1) = "PGD_NAPE2" /
      &NAM_STO_FILE CFILES(1) = "NAPE2.1.APE05.001" ,
      CFILES(2) = "NAPE2.1.APE04.001" ,
      CFILES(3) = "NAPE2.1.APE03.001" ,
      CFILES(4) = "NAPE2.1.APE02.001" ,
      CFILES(5) = "NAPE2.1.APE01.001" ,
      CFILES(6) = "APE10_ARP19990919.18" ,
      NSTART_SUPP(1)= 4 ,
      NSTART_SUPP(2)= 2 /

   * Example 3 : Namelist file for simulator of radar To simulate the radar of Nancy, with T-matrix scattering, for 1 elevation (1.3)

   .. code-block:: fortran
   
      &NAM_DIAG
      LRADAR=T,NVERSION_RAD=2,NCURV_INTERPOL=0,LCART_RAD=T,
      LQUAD=F,LWBSCS=T,LDNDZ=F, LFALL=F,LWREFL=F,LREFR=F,
      NPTS_GAULAG=7,NPTS_H=1,NPTS_V=1,CARF="AND99",
      NDIFF=0,NBSTEPMAX=400,XSTEP_RAD=700.,XGRID=2000.,LATT=F,
      XELEV(1,1)=01.3, XLAT_RAD(1)=48.7167,XLON_RAD(1)=6.5825,XALT_RAD(1)=297.55,
      CNAME_RAD(1)="NANCY",XLAM_RAD(1)=0.0535,XDT_RAD(1)=1.3
      /
      &NAM_DIAG_FILE YSUFFIX = "RD",
      YINIFILE(1) = "ALD00.2.SOG12.004",
      YINIFILEPGD(1) = "PGD_ALD00.2" /
