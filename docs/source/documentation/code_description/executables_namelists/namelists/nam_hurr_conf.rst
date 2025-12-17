.. _nam_hurr_conf:

NAM_HURR_CONF
-----------------------------------------------------------------------------

The purpose of this namelist is to replace an existing cyclone (**hurricane filtering**) with another one whose characteristics are defined (**vortex bogussing**). Each step (**hurricane filtering** and **vortex bogussing**) has to be done separately with the :ref:`prep_real_case` program.

In a mono-model configuration, the first :ref:`prep_real_case` job allows to remove analysed hurricane from the input GRIB fields: filtered and interpolated fields are written in a Meso-NH file (**hurricane filtering**).
It is used as input file for the second :ref:`prep_real_case` job during which the analytical vortex is added (**vortex bogussing**).

For a grid-nesting simulation, the **hurricane filtering** is first applied for the outer domain (dad model), with the program :ref:`prep_real_case`. The filtered fields are then horizontally interpolated for inner domains with the program :ref:`spawning`. Then, for each inner domain, a **vortex bogussing** is added with the program :ref:`prep_real_case`.

.. note::

   * The **hurricane filtering** can be applied on five atmospheric GRIB fields (HATMFILETYPE='GRIBEX' in :ref:`nam_file_names` in :file:`PRE_REAL1.nam`) : the two horizontal components of wind, the absolute temperature, the humidity and the surface pressure reduced to ground level. Each output field is decomposed into three parts: first, the BASic part is computed by the low-pass Barnes filter; then the hurricane (symmetric) disturbance is computed from the remainder disturbance part. The initial fields are then remplaced by their ENVironmental part: total field minus hurricane disturbance part.

   * The **vortex bogussing** consists on a symmetric vortex added to the input atmospheric Meso-NH fields (HATMFILETYPE='MESONH' in :ref:`nam_file_names` in :file:`PRE_REAL1.nam`). The tangential wind is computed from an analytical formulation :cite:`holland_analytic_1980`: Mercator projection must be used to respect hypotheses of Holland. Then, the balanced mass field is deduced from the thermal wind relation. The bogus of the two horizontal components of wind and the potential temperature is added to the initial (filtered) fields.



.. warning::

   For hurricane filtering and vortex bogussing :ref:`prep_real_case` must be launch on 1 core. It's not yet parallelized.

.. csv-table:: NAM_HURR_CONF content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LFILTERING","LOGICAL",".FALSE."
   "CFILTERING","CHARACTER(LEN=5)","'UVT'"
   "NK","INTEGER","50"
   "XLAMBDA","REAL","0.2"
   "XLATGUESS","REAL","XUNDEF"
   "XLONGUESS","REAL","XUNDEF"
   "XBOXWIND","REAL","XUNDEF"
   "XRADGUESS","REAL","XUNDEF"
   "NPHIL","INTEGER","24"
   "NDIAG_FILT","INTEGER","-1"
   "NLEVELR0","INTEGER","15"
   "LBOGUSSING","LOGICAL",".FALSE."
   "XLATBOG","REAL","XUNDEF"
   "XLONBOG","REAL","XUNDEF"
   "XVTMAXSURF","REAL","XUNDEF"
   "XRADWINDSURF","REAL","XUNDEF"
   "XMAX","REAL","16000.0"
   "XC","REAL","0.7"
   "XRHO_Z","REAL","-0.3"
   "XRHO_ZZ","REAL","0.9"
   "XB_0","REAL","1.65"
   "XBETA_Z","REAL","-0.5"
   "XBETA_ZZ","REAL","0.35"
   "XANGCONV0","REAL","0.0"
   "XANGCONV1000","REAL","0.0"
   "XANGCONV2000","REAL","0.0"
   "CDADATMFILE","CHARACTER(LEN=128)",""
   "CDADBOGFILE","CHARACTER(LEN=128)",""

* :code:`LFILTERING` : Flag to filter the fields (U,V,T,Q,reduced Ps) of the atmospheric file

* :code:`CFILTERING` : to choose the fields to be filtered (U,V,T,reduced Ps).

  * 'UVT' : U,V,T are filtered (default),
  * 'UVTQ' : U,V,T,Q are filtered (default),
  * 'UVTP' : U,V,T and reduced PS are filtered,
  * 'UVTPQ' : U,V,T,Q and reduced PS are filtered,

* :code:`NK` : number of points of the half-width of the window in which the Barnes filter is applied to compute low-pass component of a given field

* :code:`XLAMBDA` : a coefficient in the exponential weighting function of the Barnes filter

* :code:`XLATGUESS` : latitude of the guessed position of the cyclone center

* :code:`XLONGUESS` : longitude of the guessed position of the cyclone center

* :code:`XBOXWIND` : half-width of the box inside which the dynamical center is searched from the guessed position (km)

* :code:`XRADGUESS` : guess  of the radius of the domain in which the cyclone will be filtered (km)

* :code:`NPHIL` : number of azimuthal directions used for the cylindrical coordinates

* :code:`NDIAG_FILT` : allows storage of several components calculated from total fields. Be careful, the components are on the GRIB vertical grid. Then to visualize all the GRIB vertical levels, the number of MesoNH vertical levels must be equal or greater than the number of levels in the input GRIB file.

  * 0 : total (unfiltered) fields: UT15, VT15 for wind components; TEMPTOT, PRESTOT for absolute temperature and surface pressure, environmental (filtered) fields (total field minus hurricane disturbance component): UT16, VT16, TEMPENV, PRESENV,
  * 0,1 : basic fields (low-pass component isolated by the Barnes filter): UT17, VT17, TEMPBAS, PRESBAS, 
  * 0,1,2 : total disturbance tangential wind component (XVTDIS).

* :code:`NLEVELR0` : level used to compute R0

* :code:`LBOGUSSING` : Flag to switch on the addition of the bogus vortex (logical)

* :code:`XLATBOG` : latitude of the bogussed position of the analytical cyclone center

* :code:`XLONBOG` : longitude of the bogussed position of the analytical cyclone center

* :code:`XVTMAXSURF` : maximum tangential wind near the surface or about 500 m altitude (m/s)

* :code:`XRADWINDSURF` : radius of maximum wind near the surface or about 500 m altitude (km)

* :code:`XMAX` : altitude where the tangential wind vanishes (m)

* The following variables are parameters describing tangential wind in Holland's law (see formulation in routine :file:`holland_vt.f90`).

  * :code:`XC` : standard coefficient for maximum tangential wind,
  * :code:`XRHO_Z`, :code:`XRHO_Z` : standard coefficients for radius of maximum wind,
  * :code:`XB_0`, :code:`XBETA_Z`, :code:`XBETA_ZZ` : standard coefficients for B parameter.

* :code:`XANGCONV0`, :code:`XANGCONV1000`, :code:`XANGCONV2000` : convergence angle of wind near the surface, at 1000m and 2000m altitude.  

* :code:`CDADATMFILE` : if LBOGUSSING=.TRUE. : name of the dad of HATMFILE

* :code:`CDADBOGFILE` : if LBOGUSSING=.TRUE. : name of the dad of CINIFILE. The program will check that CDADATMFILE and CDADBOGFILE have the same  characteristics, before replacing the dad name of CINIFILE by CDADBOGFILE instead of CDADATMFILE. CDADBOGFILE must exist before running the PREP_REAL_CASE job. 


