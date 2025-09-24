.. _nam_param_radn:

NAM_PARAM_RADN
-----------------------------------------------------------------------------

.. csv-table:: NAM_PARAM_RADN content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XDTRAD","REAL","60.0"
   "XDTRAD_CLONLY","REAL","60.0"
   "CLW","CHARACTER(LEN=4)","'RRTM'"
   "CAER","CHARACTER(LEN=4)","'SURF'"
   "CEFRADL","CHARACTER(LEN=4)","'MART'"
   "CEFRADI","CHARACTER(LEN=4)","'LIOU'"
   "COPWLW","CHARACTER(LEN=4)","'SMSH'"
   "COPILW","CHARACTER(LEN=4)","'EBCU'"
   "COPWSW","CHARACTER(LEN=4)","'FOUQ'"
   "COPISW","CHARACTER(LEN=4)","'EBCU'"
   "CAOP","CHARACTER(LEN=4)","'CLIM'"
   "LCLEAR_SKY","LOGICAL","FALSE"
   "NRAD_COLNBR","INTEGER","1000"
   "NRAD_DIAG","INTEGER","0"
   "XFUDG","REAL","1.0"
   "LAERO_FT","LOGICAL","FALSE"
   "LFIX_DAT","LOGICAL","FALSE"
   "NRAD_AGG","INTEGER","1"

* :code:`XDTRAD` : Interval of time (in seconds) between two full radiation computations. ( the radiative tendency is computed for all verticals levels). This is done to save CPU time because the radiation scheme is very expensive and the radiative  tendency is not evolving too much, in some cases, during periods greater than the model timestep XTSTEP. In this case, the "radiation timestep" is increased to XDTRAD

* :code:`XDTRAD_CLONLY` : Interval of time (in seconds) between two radiation computations for the cloudy columns only. This is based on the same principle as the intermittent full radiation call: the cloudy column radiative tendency may, in some cases, evolve faster than the dry ones but still slower than the timestep XTSTEP. In this case, the "cloudy radiation timestep" is increased from XDTRAD to XDTRAD_CLONLY. Of course, when all and part of the radiative tendencies must be refreshed at the same MESONH timestep, only the full radiation call is performed. 

* :code:`CLW` : choice of long wave radiative code

  * 'RRTM': RAPID RADIATIVE TRANSFER MODEL
  * 'MORC': MORCRETTE model

* :code:`CAER` : type of aerosol distribution

  * 'SURF': deduced from cover data
  * 'TEGE': computed from Tegen et al. (1997) mensual climatology (horizontal resolution is 4 degrees of latitude by 5 degrees fo longitude
  * 'TANR': computed from ECMWF T5 climatology
  * 'NONE': no aerosol

* :code:`CEFRADL` : liquid effective radius calculation

  * 'MART' : based on Martin et al. (1994, JAS)
  * '2MOM' : based on the prediction of the number concentrations. Recommended with the 2-moment microphysical schemes.
  * 'PRES' : very old parametrization as f(pressure)
  * 'OCLN' : simple distinction between land (10) and ocean (13)

* :code:`CEFRADI` : ice water effective radius calculation

  * 'LIOU' : ice particle effective radius =f(T) from Liou and Ou (1994)
  * 'SURI' : ice particle effective radius =f(T,IWC) from Sun and Rikus (1999)
  * '2MOM' : based on the prediction of the number concentrations. Recommended with the 2-moment microphysical schemes (not yet available for mixed clouds).
  * 'FX40' : fixed 40 micron effective radius

* :code:`COPWLW` : cloud water LW optical properties

  * 'SMSH': Smith-Shi formulation
  * 'SAVI': Savijarvi formulation (recommended only with 1-moment microphysical schemes with small precipitation)
  * 'MALA': Malavelle formulation (recommended only with 2-moment microphysical schemes with small precipitation)

* :code:`COPILW` : ice water  LW optical properties

  * 'EBCU': Ebert-Curry formulation
  * 'SMSH': Smith-Shi formulation, only with CLW='RRTM'
  * 'FULI': Fu-Liou  formulation, only with CLW='MORC'

* :code:`COPWSW` : cloud water short wave optical properties

  * 'FOUQ': Fouquart, 1991 formulation
  * 'SLIN': Slingo, 1989 formulation
  * 'MALA': Only for 2-moment microphysical schemes. According to Malavelle.

* :code:`COPISW` : ice water short wave optical properties

  * 'EBCU': Ebert-Curry formulation
  * 'FULI': Fu-Liou formulation

* :code:`CAOP` : type of aerosol optical properties calculation

  * 'CLIM': climatological aerosols
  * 'EXPL': explicit aerosols (if LORILAM=.T. in NAM_CH_ORILAM or LDUST=.T. in NAM_DUST)

* :code:`LCLEAR_SKY` : When this flag is set  to .TRUE., the radiative computations are made for a mean clear-sky and for the whole cloudy columns. This is still the way to spare some CPU time, by postulating that the clear sky columns do not lead to very different radiative tendencies. This hypothesis is only valid in academical cases.

* :code:`NRAD_COLNBR` : Maximal number of air columns called by a single call of the radiative subroutine. This is performed in order to save memory, because the radiation subroutine allocate for every column of size NKMAX , NKMAX working arrays . This leads to a quadratic dependency of the memory with the number of vertical levels of the model. A way to limit the necessary memory is to split the number of columns passed to the radiation subroutine in several sets of NRAD_COLNBR column. Finally, all the desired columns (depending on the preceding parameters ) will be treated  by sequentially calling the radiation subroutine for every set of column.

* :code:`NRAD_DIAG` : number of diagnostic fields related to the radiative scheme stored in every output synchronous file (same fields as NRAD_3D in DIAG program). WARNING, a lot of variables are written only if NAM_DIAG_SURFn N2M=2.

* :code:`XFUDG` : subgrid cloud inhomogeneity factor.

* :code:`LAERO_FT` : for a temporal interpolation of aerosol and ozone distribution. By default, they consist of monhtly averages kept constant for each month If true, the climatology of O3 and aerosols (only in TEGE case) are interpolated at each call of phys_paramnn. It is not usefull if your simulation lasts less than a month or does not contain any restard. It is necessary for long-term simulation with several segments to avoid too strong  a perturbation at the beginning of each month.

* :code:`LFIX_DAT` : flag to fix the date to a constant perpetual day. It is set by the initial SOUNDING date (RSOU). Note that the diurnal cycle is still considered.

.. note::

   The cloud overlap assumption is defined in the routine :file:`ini_radconf.f90`. The different assumptions are :

   * NOVLP=5 : Random overlap for Clear Sky fraction and Effective Zenithal Angle. It is the best choice without subgrid condensation.
   * NOVLP=6 : Maximum Random Overlap for Clear Sky fraction, and Random Overlap for Effective Zenithal Angle (DEFAULT VALUE). This option is well adapted to multi-layer clouds.
   * NOVLP=7 : Maximum overlap for Clear Sky fraction and Random Overlap for Effective Zenithal Angle. This option is well adapted in the absence of multi-layer clouds.
   * NOVLP=8 : Maximum Random overlap for Clear Sky fraction and Effective Zenithal Angle.

* :code:`NRAD_AGG` : side of a square of aggregated columns on which the radiation code will be called. This allows cheaper numerical cost of the radiation code and reduce its cost by NRAD AGG2. If NRAD AGG = 1, the radiation code is called on every columns (historical version). May be useful for very high resolution LES on which calling radiation on every columns is not necessary

