How to force Meso-NH with ECMWF's data ?
============================================

Non-exhaustive list of available data
----------------------------------------

* ERA5 data downloadable via CDSAPI

* Operational analyses or forecast downloadable via ECMWFAPI

.. _extraction:

Extraction
---------------

Extract ERA5 data
******************

To extract ERA5 data, you can use the script located in bin/ directory. 

Before launching the script you have to adapt user's section :

.. code-block:: python

   # #########################################################
   # ###           To be defined by user                   ###
   # #########################################################

   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   # - -     First and last date to be extracted           - -
   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   first_date_to_be_extracted = datetime.datetime(2005, 1, 1, 0, 0, 0)
   last_date_to_be_extracted  = datetime.datetime(2005, 1, 1, 6, 0, 0)

   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   # - -          Type of data to be extracted             - -
   # - -         analyses (an) or forecast (fc)            - -
   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   type_data_to_be_extracted = 'an'

   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   # - -     period_in_hr between two forcing files        - -
   # - -          must be a multiple of 6                  - -
   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   period_between_last_and_first_dates_in_hr = 6

   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   # - -     Area to be extracted : 'North/West/South/East'- -
   # - -     Benguela    : '-20.0/5.0/-40.0/25.0'          - -
   # - -     Gulf Stream : '50.0/-90.0/20.0/-30.0'         - -
   # - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
   area_to_be_extracted = '50.0/-90.0/20.0/-30.0'

   # #########################################################
   
And then you can launch the scritp :

.. code-block:: console

   python extract_era5_instantaneous_fields_for_mesonh_and_abl1d.py

Extract oper data
******************

Use in Meso-NH / PREP_REAL_CASE
--------------------------------

You have to add the name of your extracted grib's file in PRE_REAL1.nam file, by example :

.. code-block:: fortran

   &NAM_FILE_NAMES HATMFILE='name/of/your/grib/file',
                   HATMFILETYPE='GRIBEX',
                   ... /
