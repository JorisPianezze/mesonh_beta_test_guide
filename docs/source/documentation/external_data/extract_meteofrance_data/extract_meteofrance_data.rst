Extract Meteo-France's data
=============================================================================

Historically, in the early days of AROME, only surface data from the AROME coupler model (ALADIN then ARPEGE) were available. model (ALADIN then ARPEGE), which are still available in the AROME analysis file. However, with the introduction of SURFEX in AROME, and in particular of surface analysis performed by AROME, it became essential to be able to use the AROME's surface analysis data rather than that of its coupler model.

To initialize Meso-NH as close as possible to AROME, we need to run a PREP REAL CASE with two files input files:

* the grib2 atmospheric file

* the AROME surface analysis file: lfi file + its associated PGD file.

.. note::

   The namelist NAM_PREP_SURF_ATM must be added to PRE REAL1.nam. This namelist will contain the files to be used by SURFEX: the AROME surface analysis and the associated AROME PGD file.

Non-belenos user
*****************************************************************************

For IT security reasons, it is not possible to extract Météo-France operational data from outside Météo-France (belenos). To obtain them, please send an e-mail to mesonhsupport .at. obs-mip.fr containing :

* the desired model and type of data :

  * AROME (operational since December 2008) : analysis, forecast, first guess 
  * ARPEGE : analysis, forecast, first guess, initialized analysis, short-cycle forecast 
  * ALADIN (before 26/03/2012) : analysis, analysis with digital filters, forecast, first guess, initialized analysis 
  * ALADIN-REUNION : analysis, analysis with digital filters, forecast, first guess, initialized analysis 
  * MOCAGE : please indicate the directories where SM and HM data are stored 

* dates (start and end dates, step, ...)
        
belenos user
*****************************************************************************

To extract ARPEGE or AROME data, we now use belenos or taranis with the extractMF procedure. Its use is limited to ARPEGE and AROME-France. For Aladin-Reunion and Forecast-Olive, continue with extarome at CNRM. For AROME-OM, the procedure is under development. Extractions are available on request.
For Mocage and Arpege-Climat, there is currently no way of extracting these data automatically. Using extractMF A reference extractMFrc file is available on belenos in $MESONH/procedures/ . Copy this file into the directory from which you will launch extractMF, in order to insert the desired extraction parameters.

.. code-block:: bash

   OUTDIR="EXTRACT/"
   DATE=20120924 TIME=12 STEP=00
   LOOPTIME=03
   LOOPSTEP=00
   NBLOOP=7
   
The MODEL variable can take the values arome or arpifs,

.. code-block:: bash

   MODEL=arome
  
or

.. code-block:: bash

   MODEL=arpifs

In the case of AROME extraction, surface files are automatically renamed with the date (see extractMF return for exact names). The TYPE variable can take the values AN for analyses (every 1h for arome) or FC for forecasts.

.. code-block:: bash

   TYPE = AN
   

or

.. code-block:: bash

   TYPE = FC

AROME can zoom in to extract a sub-domain of the AROME-FRANCE domain with the LZOOM=T flag. You then need to enter the edges of the domain, for example :

.. code-block:: bash

   LZOOM=T
   LATMIN=45.5
   LATMAX=48.5
   LONMIN=3.0
   LONMAX=7.9

The use of zoom is highly recommended in order to reduce memory requirements at the stage of interpolating AROME fields onto the MesoNH grid at the PREP REAL CASE stage. The various variables are documented in the reference extractMFrc file.

.. tip::

   In the extractMF return file, you can find at the end a message indicating the namelist NAM_PREP_SURF_ATM to be transferred to your PRE REAL1.nam file.

.. note::

   * Arome operational, ExtractMF get following files :

     * analysis : ˜mxpt001/arome/oper/production/YYYY/MM/DD/RR/analyse
     * guess : ˜mxpt001/arome/oper/production/YYYY/MM/DD/RR/guess
     * forecast : ˜mxpt001/arome/oper/production/YYYY/MM/DD/RR/ICMSHAROM+000x
     
     * surface analysis :
  
       * jusqu'au cycle 37 : ˜mxpt001/arome/oper/production/YYYY/MM/DD/RR/INIT_SURF.lfi, ce fichier est renomm´e automatiquement en INIT SURF.YYYYMMDD.RR.lfi
       * a partir du cycle 38 : ˜mxpt001/arome/oper/production/YYYY/MM/DD/RR/analyse.sfx, ce fichier est transform´e automatiquement en fichier lfi et nomm´e INIT SURF.YYYYMMDD.RR.lfi

   * Fichiers AROME issus d'une exp´erience OLIVE:**

     * analyse : xp/XXXX/YYYYMMDDHHHP/pseudotraj/analyse
     * forecast : xp/XXXX/YYYYMMDDHHHP/forecast/ICMSHAROM+000x
     * analyse de surface : `a r´ecup´erer dans xp/XXXX/YYYYMMDDHHHP/surfan/ (le nom varie suivant l'exp´erience et le cycle AROME)
     * PGD AROME : si cycle au moins 38 il faut r´ecup´erer le fichier PGD au format LFI aupr`es du cr´eateur de l'ex´eprience OLIVE

   * Exp´eriences arome WESTMED `a utiliser
   
     * oper de 2012 : /gmap_obs/mrpa/bressone/xp/S024 (en cycle 36 avant le 25/09
     * oper de 2012 : /gmap_obs/mrpa/bressone/xp/S02X (en cycle 37 apr`es le 25/09)
     * r´eanalyse 1 : /cnrm2/mrmp/mrmp235/xp/B2SZ (a ´et´e refaite en cycle 37 sur toute la SOP1)

Use of extracted GRIB files
*****************************************************************************

Depending on the simulated date, the NAM_PREP_SURF_ATM changes. The changes are described in the following table :

.. csv-table:: NAM_PREP_SURF_ATM options
   :header: "Start date", "Arome cycle", "SURFEX version", "Namelist NAM_PREP_SURF_ATM"
   :widths: 20, 20, 20, 20
   
   "avant juillet 2013", "cy37 et avant", "6", "CFILE='INIT SURF.20120924.12'"
   "", "", "", "CFILETYPE = 'MESONH'"
   "", "", "", "CFILEPGD = 'INIT SURF.20120924.12'"
   "", "", "", "CFILEPGDTYPE = 'MESONH'"
   "02/07/2013 00h", "cy38 / cy39", "7.2", "CFILE='INIT SURF.20130702.12'"
   "", "", "", "CFILETYPE='MESONH'"
   "", "", "", "CFILEPGD='pgd frangp.02km50.02'"
   "", "", "", "CFILEPGDTYPE='MESONH'"
   "13/04/2015 06h", "cy40", "7.2", "CFILE='INIT SURF.20150624.12'"
   "", "", "", "CFILETYPE='MESONH'"
   "", "", "", "CFILEPGD='pgd franmg.01km30.01'"
   "", "", "", "CFILEPGDTYPE='MESONH'"
   "08/12/2015 03h", "cy41", "7.3", "CFILE='INIT SURF.20160124.12'"
   "", "", "", "CFILETYPE='MESONH'"
   "", "", "", "CFILEPGD='PGD oper 41t1.01km30'"
   "", "", "", "CFILEPGDTYPE='MESONH'"
   "02/07/2019 03h", "cy43", "8.0", "CFILE='INIT SURF.20190702.12'"
   "", "", "", "CFILETYPE='MESONH'"
   "", "", "", "CFILEPGD='PGD oper 43t2.01km30.05'"
   "", "", "", "CFILEPGDTYPE='MESONH'"
   "22/06/2022 06h", "cy46", "8.1", "CFILE='INIT SURF.20220622.06'"
   "", "", "", "CFILETYPE='MESONH'"
   "", "", "", "CFILEPGD='PGD oper 46t1.01km30.05'"
   "", "", "", "CFILEPGDTYPE='MESONH'"

.. note::

   * Since version 7.2 of surfex, surface fields are separated into two files: the PGD part and the PREP part. Up to AROME cycle 37, everything is stored in a single file (CFILE=CFILEPGD).
   
   * For the convenience of METEO-FRANCE staff, PGD files are available under $MESONH/PGD (don't forget to create the empty .des file). By default, the operational PGD associated with the date of your extraction is not available. is not recovered by the extarome procedure. If you wish to retrieve it, you must add the line LGET_PGD_AROME=T in your extaromerc.

   * From arome cycle 40 onwards (April 2015), MESONH version 5-1-4 or higher must be used.

   * Starting with aroma cycle 41 (December 2015), arome analyses are available every hour. However, surface analyses are only available on the main cycles ( 03 06 09 12 15 18 21). Therefore, if a loop is requested with an hourly frequency for analyses, no surface analysis will be extracted by extarome. In this case, you need to request the first file (from a main cycle) separately to obtain the aroma surface analysis.

   * From MESO-NH version 5-4-0 onwards, add &NAM_CONFIO NIO_ABORT_LEVEL=1 NGEN_ABORT_LEVEL=1. Since this mˆeme version we can have MESONH PGD files in netcdf and arome surface files (+pgd arome) in lfi.

Example of PRE REAL1.nam namelist with AROME surface analysis :

.. code-block::

   &NAM_CONFIO
     LCDF4            = T,
     NIO_ABORT_LEVEL  = 1,
     NGEN_ABORT_LEVEL = 1
   /
   &NAM_FILE_NAMES
     HATMFILE     = 'arome.PT.20160602.12',
     HATMFILETYPE = 'GRIBEX',
     HPGDFILE     = 'PGD_AZF',
     CINIFILE     = 'couplage_arome'
   /
   &NAM_REAL_CONF
     NVERB   = 5,
     CEQNSYS = 'DUR'
   /
   &NAM_VER_GRID
     NKMAX        = 50,
     YZGRID_TYPE  = 'FUNCTN',
     ZDZGRD       = 60.,
     ZDZTOP       = 700.,
     ZZMAX_STRGRD = 2500.,
     ZSTRGRD      = 9.,
     ZSTRTOP      = 7.
   /
   &NAM_PREP_SURF_ATM
     CFILE        = 'INIT_SURF.20160602.12',
     CFILETYPE    = 'MESONH',
     CFILEPGD     = 'PGD_oper_41t1.01km30',
     CFILEPGDTYPE = 'MESONH'
   /


