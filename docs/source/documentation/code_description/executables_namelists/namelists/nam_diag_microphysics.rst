.. _nam_diag_microphysics:

NAM_DIAG - Microphysics
-----------------------------------------------------------------------------

* add :code:`LTHW=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "THVW", "Thickness of Vapor Water (mm) (if LUSERV=T)", "2D"
   "THCW", "Thickness of Cloud Water (mm) (if LUSERC=T)", "2D"
   "THRW", "Thickness of Rain Water (mm) (if LUSERR=T)", "2D"
   "THIC", "Thickness of Ice (mm) (if LUSERI=T)", "2D"
   "THSN", "Thickness of Snow (mm) (if LUSERS=T)", "2D"
   "THGR", "Thickness of Graupel (mm) (if LUSERG=T)", "2D"
   "THHA", "Thickness of Hail (mm) (if LUSERH=T)", "2D"

* add :code:`LVAR_MRW=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "MRV", "Mixing Ratio for Vapor (g/kg)(if LUSERV=T)", "3D"
   "MRC", "Mixing Ratio for Cloud (g/kg) (if LUSERC=T)", "3D"
   "MRR", "Mixing Ratio for Rain (g/kg) (if LUSERR=T)", "3D"
   "MRI", "Mixing Ratio for Ice (g/kg) (if LUSERI=T)", "3D"
   "CIT", "Ice concentration (m−3 (if LUSECI=T)", "3D"
   "MRS", "Mixing Ratio for Snow (g/kg) (if LUSERS=T)", "3D"
   "MRG", "Mixing Ratio for Graupel (g/kg) (if LUSERG=T)", "3D"
   "MRH", "Mixing Ratio for Hail (g/kg) (if LUSERH=T)", "3D"
   "CCCN", "if CCLOUD=’C2R2’", "3D"
   "CCLOUD", "if CCLOUD=’C2R2’", "3D"
   "CRAIN", "if CCLOUD=’C2R2’", "3D"
   "SUPSAT", "if CCLOUD=’C2R2’ and LSUPSAT=T", "3D"
   "CICE", "if CCLOUD=’C1R3’", "3D"
   "CIN", "if CCLOUD=’C1R3’", "3D"

* add :code:`LVAR_PR=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "ACPRR", "Accumulated explicit Precipitation Rate for Rain (mm) (accumulated from the beginning of the simulation) (if LUSERR=T)", "2D"
   "INPRR", "Instantaneous explicit Precipitation Rate (mm/h) (if LUSERR=T)", "2D"
   "INPRR3D", "Instantaneous explicit 3D Rain Precipitation flux (m/s) (if LUSERR=T)", "3D"
   "EVAP3D", "Instantaneous 3D Rain Evaporation flux (kg/kg/s) (if LUSERR=T)", "3D"
   "ACPRC",  "Accumulated Cloud Precipitation Rate (mm) (if LUSERC=T)", "2D"
   "INPRC", "Instantaneous Cloud Precipitation Rate (mm/h) (if LUSERC=T)", "2D"
   "ACPRS", "Accumulated explicit Precipitation Rate for Snow (mm) (if LUSERS=T)", "2D"
   "INPRS", "Instantaneous explicit Precipitation Rate for Snow (mm/h) (if LUSERS=T)", "2D"
   "ACPRG", "Accumulated explicit Precipitation Rate for Graupel (mm) (if LUSERG=T)", "2D"
   "INPRG", "Instantaneous explicit Precipitation Rate for Graupel (mm/h) (if LUSERG=T)", "2D"
   "ACPRH", "Accumulated explicit Precipitation Rate for Hail (mm) (if LUSERH=T)", "2D"
   "INPRH", "Instantaneous explicit Precipitation Rate for Hail (mm/h) (if LUSERH=T)", "2D"
   "ACPRT", "[2D] Total Accumulated explicit Precipitation Rate (mm) (if LUSERR=T)", "2D"
   "INPRT", "Total Instantaneous explicit Precipitation Rate (mm/h) (if CCLOUD not NONE) ", "2D"
   "PACCONV", "Convective Accumulated Precipitation Rate (mm) (if CDCONV not NONE) ", "2D"
   "PRCONV", "Convective Instantaneous Precipitation Rate (mm/h) (if CDCONV not NONE)", "2D"
   "PRSCONV", "Convective instantaneous Precipitation Rate for Snow (mm/h) (if CDCONV not  NONE)", "2D"
   "PRECIP_WAT", "Precipitable water (kg/m2)", "2D"

* add :code:`LCHAQDIAG=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "WC_O3", "Chemical scalar variables in aqueous phase (cloud and rain) as defined in BASIC.f90 (M)", "3D"

* add :code:`LTOTAL_PR=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "ACTOPR", "Accumulated Total Precipitation (mm)", "2D"
   "INTOPR", "Instantaneous Total Precipitation (mm/h)", "2D"
  
* add :code:`LTOTAL_PR=T` and :code:`LMEAN_PR=T` in :code:`NAM_DIAG` to store following variables :
   
.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "LS_ACTOPR", "Large scale accumulated Total Precipitation (mm)", "2D"
   "LS_INTOPR", "Large scale instantaneous Total Precipitation (mm/h)", "2D"
      
* XMEAN_PR (1,1) nb of grid points of the small-scale model inside the LS grid mesh along x, y for LMEAN_PR

* add :code:`LCLD_COV=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "HECL", "Height of Explicit CLoud top (km)", "2D"
   "HCL", "Height of maximum CLoud top (km)", "2D"
   "TCL", "Temperature of maximum Cloud top)", "2D"
   "CLDFR", "Cloud Fraction (_)", "3D"
   "VISI_HOR", "Visibility (m)", "3D"

* add :code:`LLIMA_DIAG=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "MRV", "Mixing Ratio for Vapor (g/kg)(if LUSERV=T)", "3D"
   "MRC", "Mixing Ratio for Cloud (g/kg)", "3D"
   "MRR", "Mixing Ratio for Rain (g/kg)", "3D"
   "MRI", "Mixing Ratio for Ice (g/kg)", "3D"
   "MRS", "Mixing Ratio for Snow (g/kg)", "3D"
   "MRG", "Mixing Ratio for Graupel (g/kg)", "3D"
   "MRH", "Mixing Ratio for Hail (g/kg) (if LUSERH=T)", "3D"
   "NCT", "Cloud concentration (:math:`\rm cm^{-3}`)", "3D"
   "NRT", "Rain concentration (:math:`\rm cm^{-3}`)", "3D"
   "NFREE", "Free CCN concentration (:math:`\rm cm^{-3}`)", "3D"
   "NCCN", "CCN concentration (:math:`\rm cm^{-3}`)", "3D"
   "MASSAP", "Scavenging (:math:`\rm kg.cm^{-3}`)", "3D"
   "CICE", "Ice concentration (:math:`\rm cm^{-3}`)", "3D"
   "CIFNFREE", "Free IFN concentration (:math:`\rm cm^{-3}`)", "3D"
   "CIFNNUCL", "Nucleated IFN concentration (:math:`\rm cm^{-3}`)", "3D"
   "CCNINIMM", "Nucleated IMM concentration (:math:`\rm cm^{-3}`)", "3D"
   "CCCNNUCL", "Homogeneous Freezing of CCN (:math:`\rm cm^{-3}`)", "3D"
   "LWC", "Liquid Water content (:math:`\rm g.m^{-3}`) (if LUSERC=T)", "3D"
   "IWC", "Ice Water content (:math:`\rm  g.m^{-3}`) (if LUSERC=T)", "3D"  
   
* add :code:`LVISI=T` in :code:`NAM_DIAG` to store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "VISIKUN", "Visibility from Kunkel (m) (if CCLOUD/=REVE or NONE)", "3D"
   "VISIGUL", "Visibility from Gultepe (m) (if CCLOUD=C2R2 or KHKO)", "3D"
   "VISIZHA", "Visibility from Zhang (m) (if CCLOUD=C2R2 or KHKO)", "3D"
