.. _nam_elec:

NAM_ELEC
-----------------------------------------------------------------------------

It contains the different parameters used by the electrical scheme.  They are included in the declarative module MODD_ELEC_DESCRn.

.. csv-table:: NAM_ELEC content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LOCG","LOGICAL",".FALSE."
   "LELEC_FIELD","LOGICAL",".TRUE."
   "LFLASH_GEOM","LOGICAL",".TRUE."
   "LFW_HELFA","LOGICAL",".FALSE."
   "LCOSMIC_APPROX","LOGICAL",".FALSE."
   "LION_ATTACH","LOGICAL",".TRUE."
   "CDRIFT","CHARACTER(LEN=3)","'PPM'"
   "LRELAX2FW_ION","LOGICAL",".FALSE."
   "LINDUCTIVE","LOGICAL",".FALSE."
   "LSAVE_COORD","LOGICAL",".FALSE."
   "LLNOX_EXPLICIT","LOGICAL",".FALSE."
   "LSERIES_ELEC","LOGICAL",".FALSE."
   "NTSAVE_SERIES","INTEGER","60"
   "NFLASH_WRITE","INTEGER","100"
   "CNI_CHARGING","CHARACTER(LEN=5)","'TAKAH'"
   "XQTC","REAL","263.0"
   "XLIM_NI_IS","REAL","10.E-15"
   "XLIM_NI_IG","REAL","30.E-15"
   "XLIM_NI_SG","REAL","100.E-15"
   "CLSOL","CHARACTER(LEN=5)","'RICHA'"
   "NLAPITR_ELEC","INTEGER","4"
   "XRELAX_ELEC","REAL","1"
   "XETRIG","REAL","200.E3"
   "XEBALANCE","REAL","0.1"
   "XEPROP","REAL","15.E3"
   "XQEXCES","REAL","2.E-10"
   "XQNEUT","REAL","1.E-10"
   "XDFRAC_ECLAIR","REAL","2.3"
   "XDFRAC_L","REAL","1500.0"
   "XWANG_A","REAL","0.34E21"
   "XWANG_B","REAL","1.3E16"

* :code:`LOCG` : 

  * .TRUE. : only the cloud electrification is computed.
  * .FALSE. : lightning flashes can be produced.

* :code:`LELEC_FIELD` :

  * .TRUE. : the electric field is computed.
  * .FALSE. : the electric field is not computed.

* :code:`LFLASH_GEOM` : when .TRUE., the lightning flash branches are produced randomly. (only one lightning scheme implemented, then must be set to .TRUE.)

* :code:`LFW_HELFA` : when .TRUE., Helsdon-Farley Fair Weather field

* :code:`LCOSMIC_APPROX` : when .TRUE., neglecting height variations of fair ion weather ion current in calculating ion source from cosmic rays

* :code:`LION_ATTACH` : when .TRUE., ion attachment to hydrometeors is considered

* :code:`CDRIFT` : ion drift

  * 'PPM' : PPM advection scheme
  * 'DIV' : divergence form

* :code:`LRELAX2FW_ION` : when .TRUE., relaxation to fair weather concentration in rim zone and top absorbing layer

* :code:`LINDUCTIVE` : when .TRUE., the inductive charging mechanism is taken into account.

* :code:`LSAVE_COORD` : when .TRUE., the flash coordinates are written in an ascii file.

* :code:`LSERIES_ELEC` : when .TRUE., some dynamical and microphysical parameters are computed and saved in an ascii file

* :code:`NTSAVE_SERIES` : time interval (s) at which data from series_cloud_elec are written in an ascii file

* :code:`NFLASH_WRITE` : number of flashes to be saved before writing the diag and/or coordinates in ascii files

* :code:`LLNOX_EXPLICIT` : when .TRUE., nitrogen oxides are produced along the lightning path (not yet implemented)

* :code:`CNI_CHARGING` : non-inductive charging parameterization

  * 'HELFA' : based on Helsdon and Farley (1987)
  * 'TAKAH' : based on Takahashi (1978)
  * 'SAUN1' : based on Saunders et al. (1991), but does not take into account the marginal positive and negative regions at low liquid water content
  * 'SAUN2' : based on Saunders et al. (1991)
  * 'SAP98' : based on Saunders and Peck (1998)
  * 'GARDI' : based on Gardiner et al. (1985)

* :code:`XQTC` : temperature charge reversal (K), only if CNI_CHARGING = 'HELFA'

* :code:`XLIM_NI_IS` : max magnitude of dq for I-S non-inductive charging (C)

* :code:`XLIM_NI_IG` : max magnitude of dq for I-G non-inductive charging (C)

* :code:`XLIM_NI_SG` : max magnitude of dq for S-G non-inductive charging (C)

* :code:`CLSOL` : Laplace equation solver for the electric field

* :code:`NLAPITR_ELEC` : number of iterations for the electric field solver

* :code:`XRELAX_ELEC` : relaxation factor for the electric field solver

* :code:`XETRIG` : electric field threshold (V :math:`m^{-1}`) for lightning flash triggering

* :code:`XEBALANCE` : (1-XEBALANCE) is the proportion of XETRIG over which a lightning can be triggerred to take into account the subgrid scale variability

* :code:`XEPROP` : electric field threshold (V :math:`m^{-1}`) for the bidirectional leader propagation

* :code:`XQEXCES` : charge density threshold (C :math:`m^{-3}`) for neutralization

* :code:`XDFRAC_ECLAIR` : fractal dimension of lightning flashes

* :code:`XDFRAC_L` : linear coefficient for the branch number

* XWANG_A` : a parameter of the Wang et al. (1998) formula for LNOx production (not yet implemented)

* XWANG_B` : b parameter of the Wang et al. (1998) formula for LNOx production (not yet implemented)

