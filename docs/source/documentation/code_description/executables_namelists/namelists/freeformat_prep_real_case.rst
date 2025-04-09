.. _freeformat_prep_real_case:

Free format for PREP_REAL_CASE
-----------------------------------------------------------------------------

Vertical grid
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This part is optional in the file, read only if YZGRID_TYPE='MANUAL'. It must begin by the keyword ZHAT. In this case (NKMAX+1) levels are written in meters in free format after the keyword, from ground level (generally 0) to rigid top level.

Chemical species
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This part is only used if you have previously run extractarpege with MOCAGE outputs. This part must begin by the keyword MOC2MESONH.
Then, the list of the MesoNH chemical species, and their corresponding GRIB code in the GRIB file, is specified as follows: 

.. code-block::

   MOC2MESONH
   transfer mocage/RACM variables (default values)
   2 # NUMBER OF OPTIONAL GRIB VARIABLES
   (A4,1X,I5)
   O3   180
   NO2  183


Examples of PRE_REAL1.nam
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

* GRIBEX file, levels being calculated, and chemical species

.. code-block::

   &NAM_FILE_NAMES HATMFILE   ='ALT90101500'     , HATMFILETYPE='GRIBEX' ,
                   HPGDFILE   ='PGDFILE_10km'    ,
                   CINIFILE   ='CPL_example1'    /
   &NAM_REAL_CONF CEQNSYS="LHE", NVERB=7 /
   &NAM_VER_GRID NKMAX=60, YZGRID_TYPE='FUNCTN', ZDZGRD=50., ZDZTOP=500., 
                 ZZMAX_STRGRD=3000., ZSTRGRD=2., ZSTRTOP=6. /
              
   MOC2MESONH
   transfer mocage/RACM variables 
   2 # NUMBER OF OPTIONAL GRIB VARIABLES
   (A4,1X,I5)
   O3   180
   NO2  183

* MESONH file and levels given manually

.. code-block::

   &NAM_FILE_NAMES HATMFILE   ='POI03.1.DAY01.001'  , HATMFILETYPE='MESONH' ,
                   HPGDFILE   ='PGDFILE_10km'       ,
                   CINIFILE   ='CPL_example2'       /
   &NAM_REAL_CONF NVERB=5 /
   &NAM_VER_GRID NKMAX=10, YZGRID_TYPE='MANUAL' /
   ZHAT
   0.
   1050.
   2100.
   3250.
   4300.
   5200.
   6100.
   7000.
   8000.
   9000.
   10000.

