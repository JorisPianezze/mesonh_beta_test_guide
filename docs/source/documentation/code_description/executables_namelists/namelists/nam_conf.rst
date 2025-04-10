.. _nam_conf:

NAM_CONF
-----------------------------------------------------------------------------

It contains the model configuration parameters common to all the models. They are included in the module MODD_CONF. 

.. csv-table:: NAM_CONF content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CCONF","CHARACTER(LEN=5)","'START'"
   "LFLAT","LOGICAL",".FALSE."
   "CEQNSYS","CHARACTER(LEN=3)","'DUR'"
   "LFORCING","LOGICAL",".FALSE."
   "NMODEL","INTEGER","1"
   "NVERB","INTEGER","5"
   "NHALO","INTEGER","1"
   "JPHEXT","INTEGER","1"
   "CSPLIT","CHARACTER(LEN=10)","'YSPLITTING'"
   "LLG","LOGICAL",".FALSE."
   "LINIT_LG","LOGICAL",".FALSE."
   "CINIT_LG","CHARACTER(LEN=5)","'FMOUT'"
   "LNOMIXLG","LOGICAL",".FALSE."
   "CEXP","CHARACTER(LEN=32)","'EXP01'"
   "CSEG","CHARACTER(LEN=32)","'SEG01'"
   "LCHECK","LOGICAL",".FALSE."

* :code:`CCONF` : configuration of all  models

  * 'START' : for start configuration
  * 'RESTA' : for restart configuration

* :code:`CEQNSYS` : Equation system resolved by the MESONH model

  * 'LHE' : Lipps and HEmler anelastic system
  * 'DUR' : approximated form of the DURran version of the anelastic sytem
  * 'MAE' : classical Modified Anelastic Equations but with not any approximation in the momentum equation

* :code:`LFLAT` : Flag for zero ororography

  * .TRUE. = no orography (zs=0.)
  * .FALSE. = the orography is not zero everywhere

* :code:`LFORCING` : Flag to use forcing sources

  * .TRUE. : add forcing sources
  * .FALSE. : no forcing sources

* :code:`NMODEL` : Number of nested models

* :code:`NVERB` : Level of informations on output-listing

  * 0 : for minimum of prints
  * 5 : for intermediate level of prints
  * 10 : for maximum of prints 

* :code:`NHALO` : Size of the halo for parallel distribution. This variable is related to computer performance but has no impact on simulation results. NHALO must be equal to 3 for WENO5 cases in parallel runs.

* :code:`JPHEXT` :  Horizontal External points number. JPHEXT must be equal to 3 for cyclic cases with WENO5.

* :code:`CSPLIT` : Kind of domain splitting for parallel distribution. This variable is related to computer performance but has no impact on simulation results

  * 'BSPLITTING' : domain is decomposed in Box along X and Y
  * 'XSPLITTING' : the X direction is splitted in stripes along Y
  * 'YSPLITTING' : the Y direction is splitted in stripes along X

* :code:`LLG` : Flag to use Lagrangian variables

* :code:`LINIT_LG` : Flag to reinitialize  Lagrangian variables (with LLG=.T.)

* :code:`CINIT_LG` : with LINIT_LG=T :

  * 'FMOUT' : each time a backup file is written
  * other string : : only when starting a new segment (CCONF='RESTA')

* :code:`LNOMIXLG` : Flag to unset the turbulence for LG variables. You must have LNOMIXLG=.TRUE. with CSCONV='EDKF'

* :code:`CEXP` : Experiment name (name of the set of runs you have performed or want to perform on the same physical subject)

* :code:`CSEG` : Name of segment (name of the future runs you want to perform)

* :code:`LCHECK` : Flag for testing reproducibility

.. note::

   From these last two information, we built the names of the different MESONH backup files: CEXP.n.CSEG.nbr, where n represents the number of the model which generates this output and nbr is the number of the outfile. For instance, if CEXP='HYDRO' and CSEG='INIT1' and we use only one model (no gridnesting) the different output will be called: HYDRO.1.INIT1.001, HYDRO.1.INIT1.002, ...

   By default, nbr is coded on 3 digits. This can be modified with the NFILE_NUM_MAX variable of the :ref:`nam_confio` namelist.

   
