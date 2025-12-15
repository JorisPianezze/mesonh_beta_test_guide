.. _nam_real_conf:

NAM_REAL_CONF
-----------------------------------------------------------------------------

.. csv-table:: NAM_REAL_CONF content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CEQNSYS","CHARACTER(LEN=3)","'DUR'"
   "CPRESOPT","CHARACTER(LEN=5)","'CRESI'"
   "NVERB","INTEGER","1"
   "LSHIFT","LOGICAL",".TRUE./.FALSE."
   "LDUMMY_REAL","LOGICAL",".FALSE."
   "LRES","LOGICAL",".FALSE."
   "XRES","REAL","1.E-07"
   "NITR","INTEGER","4"
   "LCOUPLING","LOGICAL",".FALSE."
   "NHALO","INTEGER","1"
   "JPHEXT","INTEGER","1"

* :code:`CEQNSYS` : EQuatioN SYStem

  * 'LHE': Lipps-HEmler 1982
  * 'MAE': Modified Anelastic Equations
  * 'DUR': following DURran 1990 derivations

.. note::

   By default, if if HATMFILETYPE = 'GRIBEX', CEQNSYS='DUR' and if HATMFILETYPE = 'MESONH', CEQNSYS is fixed to the one in input Meso-NH file.

* :code:`CPRESOPT` : option for pressure solver ('RICHA', 'CGRAD', 'CRESI', 'ZRESI').

* :code:`NVERB` : verbosity level (error diagnostics are computed if NVERB>4)

* :code:`LSHIFT` : flag to shift altitudes in boundary layer

.. note::

   By default, if if HATMFILETYPE = 'GRIBEX', LSHIFT=.TRUE. and if HATMFILETYPE = 'MESONH', LSHIFT is fixed to the one in input Meso-NH file.

* :code:`LDUMMY_REAL` : flag to read dummy fields stored in the GRIB file asking for additional fields by modifying FULLPOS namelist or {\bf extractecmwf} by modifying MARS requests).You have to fill also a free formatted part as described in the exemple of AROME field.

* :code:`LRES` : flag to change the residual divergence limit.

* :code:`XRES` : Value of the residual divergence limit

* :code:`NITR` : number of  iterations used for the resolution of the elliptic equation (solver = "CPRESOPT").

* :code:`LCOUPLING` : Flag to handle the output file as coupling file instead of initial file : no surface field will be computed. (time saving and smaller file) }

* :code:`NHALO` : Size of the halo for parallel distribution. This variable is related to computer performance but has no impact on simulation results.

* :code:`JPHEXT` :  Horizontal External points number. JPHEXT must be equal to 3 for cyclic cases with WENO5.
