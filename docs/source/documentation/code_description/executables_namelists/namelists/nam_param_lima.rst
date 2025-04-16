.. _nam_param_lima:

NAM_PARAM_LIMA
-----------------------------------------------------------------------------

It contains the options for the 2 moment mixed phase cloud parameterizations used  by the model (LIMA). They are included in the declarative module MODD_PARAM_LIMA.

.. csv-table:: NAM_PARAM_LIMA content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "NMOM_C","INTEGER","2"
   "NMOM_R","INTEGER","2"
   "NMOM_I","INTEGER","2"
   "NMOM_S","INTEGER","1"
   "NMOM_G","INTEGER","1"
   "NMOM_H","INTEGER","0"
   "LNUCL","LOGICAL",".TRUE."
   "LSEDI","LOGICAL",".TRUE."
   "LHHONI","LOGICAL",".FALSE."
   "LMEYERS","LOGICAL",".FALSE."
   "NMOD_IFN","INTEGER","1"
   "XIFN_CONC","REAL","100.0"
   "LIFN_HOM","LOGICAL",".TRUE."
   "CIFN_SPECIES","CHARACTER(LEN=8)","'PHILLIPS'"
   "CINT_MIXING","CHARACTER(LEN=8)","'DM2     '"
   "NMOD_IMM","INTEGER","0"
   "NIND_SPECIE","INTEGER","1"
   "CPRISTINE_ICE_LIMA","CHARACTER(LEN=4)","'PLAT'"
   "XFACTNUC_DEP","REAL","1.0"
   "XFACTNUC_CON","REAL","1.0"
   "NPHILLIPS","INTEGER","8"
   "LACTI","LOGICAL",".TRUE."
   "LSEDC","LOGICAL",".TRUE."
   "LACTIT","LOGICAL",".FALSE."
   "NMOD_CCN","INTEGER","1"
   "XCCN_CONC","REAL","300.0"
   "LCCN_HOM","LOGICAL",".TRUE."
   "CCCN_MODES","CHARACTER(LEN=8)","'COPT    '"
   "HINI_CCN","CHARACTER(LEN=3)","'AER'"
   "HTYPE_CCN","CHARACTER(LEN=10)","'M'"
   "XALPHAC","REAL","3.0"
   "XNUC","REAL","1.0"
   "XALPHAR","REAL","1.0"
   "XNUR","REAL","2.0"
   "XFSOLUB_CCN","REAL","1.0"
   "XACTEMP_CCN","REAL","280.0"
   "LSCAV","LOGICAL",".FALSE."
   "LAERO_MASS","LOGICAL",".FALSE."
   "LACTTKE","LOGICAL",".TRUE."
   "LDEPOC","LOGICAL",".TRUE."
   "XVDEPOC","REAL","0.02"
   "LPTSPLIT","LOGICAL",".TRUE."
   "LFEEDBACKT","LOGICAL",".TRUE."
   "NMAXITER","INTEGER","5"
   "XMRSTEP","REAL","0.005"
   "XTSTEP_TS","REAL","20.0"
   "LADJ","LOGICAL",".TRUE."
   "LSPRO","LOGICAL",".FALSE."
   "LKHKO","LOGICAL",".FALSE."
   "LCIBU","LOGICAL",".FALSE."
   "LRDSF","LOGICAL",".FALSE."
   "XNDEBRIS_CIBU","REAL","50.0"
   "LMURAKAMI","LOGICAL",".TRUE."
   "LSNOW_T","LOGICAL",".FALSE."
   "LKESSLERAC","LOGICAL",".FALSE."

* :code:`NMOM_C` : number of prognostic moments for cloud droplets.

* :code:`NMOM_R` : number of prognostic moments for rain drops.

* :code:`NMOM_I` : number of prognostic moments for ice crystals.

* :code:`NMOM_S` : number of prognostic moments for snow/aggregates.

* :code:`NMOM_G` : number of prognostic moments for graupel.

* :code:`NMOM_H` : number of prognostic moments for hail.

.. note::

   Note that the full flexibility is only available with the time-splitted version of LIMA (with LPTSPLIT=T). With the original version, two configurations only are available : the original parameterization with NMOM_C=NMOM_R=NMOM_I=2 and NMOM_S=NMOM_G=1; and 2 moments for all species with NMOM_x=2.

* :code:`LNUCL` : Switch to activate pristine ice crystals nucleation (both from IFN and homogeneous freezing)

* :code:`LSEDI` : Switch to activate the sedimentation of pristine ice crystals

* :code:`LSNOW_T` : Switch to activate the representation of snow proposed by Wurtz et al. 2023 which improves the extension and cloud composition of anvils in convective systems.

* :code:`LMURAKAMI` : Switch to activate the snow riming and conversion to graupel process can be computed following Murakami (1990). Only avaiable with LPTSPLIT=T.

* :code:`LCIBU` : swith to activate the representation of collisional ice break-up (CIBU, Hoarau et al., 2018), a secondary ice production mechanism (ice is produced by the fragmentation of snow upon impact with graupel). The number of fragments formed per collision can be fixed by XNDEBRIS_CIBU.

* :code:`XNDEBRIS_CIBU` : number of fragments formed per collision in the ice collisional break-up mechanism. Negative values result in a random number of fragments formed for each collision.

* :code:`LRDSF` : switch to activate raindrop shattering freezing, a secondary ice production mechanism.

* :code:`LKHKO` : switch to activate a replicate behaviour of the KHKO scheme (useful for stratocumulus clouds and drizzle formation) with LIMA code.

* :code:`LHHONI` : Switch to activate CCN homogeneous freezing

* :code:`LMEYERS` : Switch to activate the ice nucleation parameterization by Meyers (1992) instead of using the IFN

* :code:`NMOD_IFN` : Number of IFN modes

* :code:`XIFN_CONC` : Initial reference number concentration for each IFN mode (\verb?#/L?)

* :code:`LIFN_HOM` : If set to true, the initial concentration of IFN is homogeneous on the vertical. If set to false, the IFN concentration is equal to the reference value XIFN_CONC below 1000m and exponentially decreasing above.

* :code:`CINT_MIXING` : String to select the proportion of each IFN type in each IFN mode. Possible values :

  * 'DM1' pure small dust particles
  * 'DM2' pure large dust particles
  * 'BC'  pure black carbon
  * 'O'   pure organics
  * 'CAMS', 'CAMS_JPP', 'CAMS_AIT', 'CAMS_ACC', 'MOCAGE',  mix for use of CAMS or MOCAGE aerosols
  * 'DEFAULT' mix as in Phillips et al 2008 or 2013

* :code:`CIFN_SPECIES` : String to select the IFN modes size distribution parameters. Available options are :

  * 'MOCAGE', 'CAMS_JPP', 'CAMS_AIT', 'CAMS_ACC' for use with MOCAGE/CAMS aerosols
  * 'DEFAULT' to use the same parameters as in Phillips et al. 2008 or 2023

* :code:`NMOD_IMM` :Number of “coated IFN” modes

* :code:`NIND_SPECIE` : Type of the “coated IFN” mode. 1 for dust, 2 for black carbon or 3 for organics

* :code:`CPRISTINE_ICE_LIMA` : Select the shape of pristine ice among:

  * 'PLAT' : plates 
  * 'COLU' : columns
  * 'BURO' : bullet rosettes
  * 'YPLA' : plates from Yang et al. 2013
  * 'YCOL' : column from Yang et al. 2013
  * 'YBUR' : solid bullet rosette from Yang et al. 2013
  * 'YDRO' : droxtal from Yang et al. 2013
  * 'YHCO' : hollow column from Yang et al. 2013
  * 'YHBU' : hollow bullet rosette from Yang et al. 2013

* :code:`XFACTNUC_DEP` : Amplification factor for IN nucleation by deposition (only used if LMEYERS=T)

* :code:`XFACTNUC_CON` : Amplification factor for IN  nucleation by contact (only used if LMEYERS=T)

* :code:`NPHILLIPS` : Version of the Phillips parameterization : 8 for the 2008 paper ; 13 for the 2013 paper

* :code:`LACTI` : Switch to activate the CCN activation 

* :code:`LSEDC` : Switch to activate the cloud droplets sedimentation

* :code:`LACTIT` : Switch to activate the representation of radiative cooling in the diagnostic maximum supersaturation computation

* :code:`NMOD_CCN` : Number of CCN modes

* :code:`XCCN_CONC` : Reference concentration for each CCN mode (\verb?#/cm3?)

* :code:`LCCN_HOM` : If set to true, the initial concentration of CCN is homogeneous on the vertical. If set to false, the CCN concentration is equal to the reference value XCCN_CONC below 1000m and exponentially decreasing above.

* :code:`CCCN_MODES` : Select the size distribution of CCN modes ('JUNGFRAU','COPT','CAMS', 'CAMS_JPP','CAMS_ACC','CAMS_AIT','SIRTA','CPS00','FREETROP')

* :code:`HINI_CCN` : Switch to use aerosols as CCN or to describe directly the CCN activation spectrum : 'AER' (use aerosols) or 'CCN' (use the CCN activation spectrum directly)

* :code:`HTYPE_CCN` : Switch to affect maritime or continental activation properties to each CCN mode : 'C' continental or 'M' maritime. NH42SO4 (=C), NH4NO3, NaCl (=M), H2SO4, NaNO3, NaHSO4, Na2SO4, NH43HSO42, SOA

* :code:`XALPHAC,XNUC` : Droplets size distribution parameter

* :code:`XALPHAR,XNUR` : Rain size distribution parameter

* :code:`XFSOLUB_CCN` : Fractional solubility of the CCN

* :code:`XACTEMP_CCN` : Expected temperature of CCN activation

* :code:`LSCAV` : Switch to activate below cloud scavenging of aerosols by rain

* :code:`LAERO_MASS` : Switch to track the mass of scavenged aerosols

* :code:`LACTTKE` :  flag to use TKE in the CCN activation formulation

* :code:`LDEPOC` :  flag to activate droplet deposition

* :code:`XVDEPOC` : Droplet deposition velocity

* :code:`LPTSPLIT` : flag to activate the time-splitting scheme

* :code:`LFEEDBACKT` : Flag to recompute tendencies if temperature reaches 0 (for the time-splitting scheme)

* :code:`NMAXITER` : Maximum number of iterations (for the time-splitting scheme)

* :code:`XMRSTEP` : Recompute tendencies if any mixing ratio changes by more than XMRSTEP (0=no limit) (for the time-splitting scheme)

* :code:`XTSTEP_TS` : Maximum length of sub-time-steps (for the time-splitting scheme)

* :code:`LSPRO` : flag to activate the saturation adjustement from Thouron et al. 2012 (diagnostic supersaturation)

* :code:`LADJ` : flag to use a saturation adjustment for cloud droplets (if set to T) or the "diagnostic supersaturation" from Thouron et al. 2012 (if set to F and LSPRO=F).

* :code:`LKESSLERAC` : Set to T to use the Kessler autoconversion of cloud droplets into rain drops, based on the droplets mixing ratio. Useful if NMOM_C=1 to have results closer to ICE3 simulations.

.. note::

   Use of CAMS with LIMA. You must have set HCAMSFILE and HCAMSFILETYPE at the :ref:`prep_real_case` step).

   .. code-block::
   
      &NAM_PARAM_LIMA  HTYPE_CCN(1)='NaCl',
                	HTYPE_CCN(2)='NH42SO4',
                	HTYPE_CCN(3)='SOA',
                	NMOD_CCN=3,
                	CCCN_MODES='CAMS_AIT',
                	NMOD_IFN=2,
                	CIFN_SPECIES='CAMS_AIT',
                	CINT_MIXING='CAMS',
                	NMOD_IMM=1 /
