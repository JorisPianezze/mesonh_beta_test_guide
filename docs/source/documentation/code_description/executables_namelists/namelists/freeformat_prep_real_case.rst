.. _freeformat_prep_real_case:

Free-format part
-----------------------------------------------------------------------------

Vertical grid
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

If you want to define your own vertical grid (CZGRID_TYPE = 'MANUAL' in :ref:`nam_ver_grid`), you must give the heights of the vertical velocity levels. You must NKMAX + 1 values from the surface to the top of the domain.

.. note::

   Example of free part of :file:`PRE_REAL1.nam` :

   .. code-block::
                 
      &NAM_VER_GRID NKMAX       = 10,
                    YZGRID_TYPE = 'MANUAL' /

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

Chemical species
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

This part is only used if you have previously run extractarpege with MOCAGE outputs. This part must begin by the keyword MOC2MESONH.
Then, the list of the Meso-NH chemical species, and their corresponding GRIB code in the GRIB file, is specified as follows: 

.. note::

   Example of free part of :file:`PRE_REAL1.nam` :

   .. code-block::

      MOC2MESONH
      transfer mocage/RACM variables (default values)
      2 # NUMBER OF OPTIONAL GRIB VARIABLES
      (A4,1X,I5)
      O3   180
      NO2  183

.. _read_extra_arome_variables:

Read extra AROME variables
-----------------------------------------------------------------------------

AROME GRIB files obtained with :ref:`extract_meteofrance_data` contain fields which aren't read by default by :ref:`prep_real_case` program. To use these fields, you have to use LDUMMY_REAL=T in :ref:`nam_real_conf` and fill a free formatted part at the end of :file:`PRE_REAL1.nam`. This part must begin by the keyword **DUMMY_2D** (for 2D fields). Then, the list of the Meso-NH dummy fields, and their corresponding GRIB code in the GRIB file (parameter code, and if ambiguity with another variables type and value of level),  is specified as follows :

.. code-block::

   DUMMY_2D
   diagnostics
   10
   ACCPLUIE 62
   ACCNEIGE 79
   ACCGRAUPEL 78
   INSPLUIE 169
   INSNEIGE 64
   INSGRAUPEL 63
   UM05 33 105 10
   VM05 34 105 10
   CLSHUMI.RELA 52 105 2
   CLSTEMPE 11 105 2      
