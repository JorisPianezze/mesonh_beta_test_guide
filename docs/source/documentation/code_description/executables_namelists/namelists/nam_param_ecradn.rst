.. _nam_param_ecradn:

NAM_PARAM_ECRADn
-----------------------------------------------------------------------------

It contains the options for the ECRAD radiative scheme. ECRAD version is defined in the compilation procedure by setting VERSION_ECRAD.

.. note::

   Since the version 1.4.0, ECRAD is open-source. To use ECRAD, you must link specific files found at $SRC_MESONH/src/LIB/RAD/ecrad-VERSION_ECRAD/data/ in the folder of the simulation.

.. csv-table:: NAM_PARAM_ECRADn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "NSWSOLVER","INTEGER","0 if VER_ECRAD=101"
   "","","1 if VER_ECRAD=140"
   "NLWSOLVER","INTEGER","0 if VER_ECRAD=101"
   "","","1 if VER_ECRAD=140"
   "NLIQOPT","INTEGER","3"
   "NICEOPT","INTEGER","3"
   "NOVLP","INTEGER","1"
   "NRADLP","INTEGER","1"
   "NRADIP","INTEGER","1"
   "NREG","INTEGER","3"
   "XCLOUD_FRAC_STD","REAL","1.0"
   "NLWSCATTERING","INTEGER","2"
   "NAERMACC","INTEGER","0"
   "LSPEC_EMISS","LOGICAL",".FALSE"
   "LSPEC_ALB","LOGICAL",".FALSE."
   "SURF_TYPE","CHARACTER(LEN=4)","'SNOW'"

* :code:`NSWSOLVER` : SW solver. The possible values are 0 for 'McICA' , 1 for 'SPARTACUS' and 2 for 'SPARTACUS' with 3D effects

* :code:`NLWSOLVER` : LW solver. The possible values are 0 for 'McICA' , 1 for 'SPARTACUS' and 2 for 'SPARTACUS' with 3D effects

* :code:`NLIQOPT` : optical properties of liquid particles ; 2 = Slingo ; 3 = SOCRATES

* :code:`NICEOPT` : optical properties of ice particles ; 3 = Fu ; 4 = Baran ; 7 = coherent with LIMA with CPRISTINE_ICE_LIMA = {YPLA, YCOL, YBUR, YHCO, YHBU}

* :code:`NOVLP` :  overlap assumption ; 0= 'Max-Ran' ; 1= 'Exp-Ran'; 2 = 'Exp-Exp'

* :code:`NRADLP` : liquid effective radius calculation

  * 0: ERA-15, 
  * 1: Zhang and Rossow,
  * 2: Martin (1994), 
  * 3: Martin (1994) and Woods (2000)
  * 4: use droplets mixing ratio and concentration from LIMA

* :code:`NRADIP` : ice water effective radius calculation

  * 0: 40 mum
  * 1: Liou and Ou (1994)
  * 2: Liou and Ou (1994) improved
  * 3: Sun and Rikus (1999)
  * 4: use ice crystals mixing ratio and concentration from LIMA

* :code:`NREG` : Number of regions for Triple Clouds

* :code:`XCLOUD_FRAC_STD` : Cloud water content horizontal fractional standard deviation in a gridbox

* :code:`NLWSCATTERING` : longwave scattering

  * 0: No longwave scattering
  * 1: Longwave scattering by clouds only
  * 2: Longwave scattering by clouds and aerosol

* :code:`NAERMACC` :  Use of Tegen (0) or MACC (1) aerosol classification(that is over 6 or 12 aerosols species)

* :code:`LSPEC_EMISS` : flag to use an idealized (horizontally homogeneous) spectral emissivity defined by SURF_TYPE

* :code:`LSPEC_ALB` : flag to use an idealized (horizontally homogeneous) spectral albedo defined by SURF_TYPE

* :code:`SURF_TYPE` : type of surface for idealized spectral emissivity and albedo among  "VEGE", "SNOW", "OCEA", "DESE", "ZERO", "UNIT". Values are read in ECRAD data files (spectral_albedo.nc spectral_emissivity.nc (these files are in src/LIB/RAD/data_mnh). 

