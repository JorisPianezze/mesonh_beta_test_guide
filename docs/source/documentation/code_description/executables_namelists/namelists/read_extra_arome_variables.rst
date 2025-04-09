.. _read_extra_arome_variables:

Read extra AROME variables
-----------------------------------------------------------------------------

AROME GRIB files obtained with extractMF contain fields which aren't read by default by PREP_REAL_CASE. You could want to have this extra fields in your FM file. To get this fields, you have to use LDUMMY_REAL=T and fill a free formatted part at the end of PRE_REAL1.nam.

This part must begin by the keyword DUMMY_2D (for 2D fields). Then, the list of the MesoNH dummy fields, and their corresponding GRIB code in the GRIB file (parameter code, and if ambiguity with another variables type and value of level),  is specified as follows (This example  matches with all the extra fields available in AROME GRIB file): 

.. code-block::

   DUMMY_2D
   diagnostiques prevus
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
