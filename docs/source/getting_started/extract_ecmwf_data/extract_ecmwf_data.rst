Extract ECMWF's data
============================================

Operational data (analysis, forecast or ensemble)
--------------------------------------------------

Access to ECMWF operational data is restricted to registred users. See `ECMWF's website <https://www.ecmwf.int/en/forecasts/accessing-forecasts>`_ for more detailed informations. 

.. _configure_ecmwf_api_key:

Configure ECMWF API
*********************

First you need to create a file called `.ecmwfapirc` in your HOME directory. This file contains your key and email given by ECMWF on https://api.ecmwf.int/v1/key/. Your `.ecmwfapirc` needs to contain lines that look likes:

.. code-block:: bash

   {
    "url"   : "https://api.ecmwf.int/v1",
    "key"   : "your_key",
    "email" : "your_email"
   }

.. warning::

   You need to suppress rules for group and other users with ``chmod 600 .ecmwfapirc``.

.. _get_the_tool:

Get the tool
*******************

To get the tool you can download it with :

.. code-block:: console

   git clone https://github.com/JorisPianezze/EXTRACT_ECMWF.git

.. note::

   This Git's repository is a forked from https://github.com/wurtzj/EXTRACT_ECMWF. It contains additional variables compared to the original.

This tool works as follows :

* `define_parameters.py` is used to read the configuration file called `user_parameters.json` ;

* `main_extract_ecmwf.py` execute `extract_ecmwf.py` file in background with ``nohup``.

.. _install_python_ecmwfapi:

Install python environment
******************************

To install python environment required to extract ECMWF data, if you are using conda, do

.. code-block:: console

   conda env create -f environment.yml

Then load new created python environment :

.. code-block:: console
 
   conda activate env_extract_ecmwf

.. tip:: `environment.yml` file is located in the Git repository.

.. note:: 

   * Last conda environment tested is
  
   .. code-block:: python
   
      name: env_extract_ecmwf
      channels:
        - conda-forge
      dependencies:
        - python=3.11.4
        - numpy=1.25.0
        - pandas=2.1.4
        - ecmwf-api-client=1.6.3
        - eccodes=2.33.0
        
   * `pandas` is used to manage dates and `eccodes` is used to perform some operations on extracted grib files (concatenate and separate by hours)

Define extraction's parameters
**********************************

To define your extraction's area and dates, fill `user_parameters.json` file. This configuration file contains following variables :

.. code-block:: python

   {
  
   "target_directory"   : "",

   "start_date"         : "20170708",
   "end_date"           : "20170708",
   "list_of_dates"      : [],

   "start_time"         :"00",
   "end_time"           :"00",
   "step"               :"06",
   "forecast_start_time":"00",

   "lat_min"            : "",
   "lat_max"            : "",
   "lon_min"            : "",
   "lon_max"            : "",
   "area"               : "",
   "grid"               : ".1",

   "type_data"          : "analysis",

   "get_surface"        : true,
   "get_sea_state"      : false,

   "remove_tmp_files"   : true

   }

.. note::

   * target_directory is where your data will be written.

   * date to be extracted is take between start_date and end_date if list_of_dates is empty ([]).

   * start_time, first time to extract within the day

   * end_time : last time extraction within the day

   * step: time step extraction within the day, if end_time=start_time, only start_time will be extracted

   * forecast_start_time : in case of forecast : time of launch (00 or 12 for instance)

   * domain extension lat_min, lat_max, lon_min, lon_max or area. If empty get Europe domain.

   * grid resolution .1 by default. Could be coarser

   * type_data : type of data to be extracted : analysis, forecast or ensemble.

   * get_surface : get surface parameters or not. Mandatory for Meso-NH users.

   * get_sea_state : get sea state parameters or not. Used only when sea salt aerosols are activated.

   * remove_tmp_files : remove temporary files or not. True by default.


Launch extraction
**********************************

To launch extraction of the desired ECMWF data, if number of dates to extract is lower than 10 do

.. code-block:: bash

   python main_extract_ecmwf.py

or if number of dates is greater than 10, do 

.. code-block:: bash

   nohup python main_extract_ecmwf.py

.. note::

   * Stored grib files are located in target_directory defined in `user_parameters.json` file.

   * At the end of the script extractions are launched in background. If you are using your laptop or personal computer do not switch it off until extraction is complete. If you are using supercomputer you can logout without problems.

   * You can follow extraction processes on https://apps.ecmwf.int/webmars/joblist/.

Add new variables 
***********************************

If you want to add variables to extracted grib files, go to `define_parameters.py` file and add your own grib identifier in the following list :

.. code-block:: python

   if type=="FC":
       pressure="/134"
       param_atm="130/131/132/133"
       param_surf="129/172/139/141/170/183/236/39/40/41/42"+ pressure
       param_sea_stae="229/234/237"
   else:
       pressure="/152"
       param_atm="130/131/132/133" + pressure
       param_surf="129/172/139/141/170/183/236/39/40/41/42"
       param_sea_state="229/234/237"

.. csv-table:: Grib identifier mandatory for Meso-NH
   :header: "Grib Id", "Signification", "Unit", "Type"
   :widths: 10, 35, 10, 20

   "129", "Geopotential", "m**2/s**2", "Model level (ml)"
   "172", "Land-sea lask", "0 - 1", "Surface (sfc)"
    "43", "Soil type", "m**2/s**2", "Surface (sfc)"
   "139", "Soil temperature at level 1", "K", "Surface (sfc)"
   "141", "Snow depth", "m**2/s**2", "Surface (sfc)"
   "170", "Soil temperature at level 2", "K", "Surface (sfc)"
   "183", "Soil temperature at level 3", "K", "Surface (sfc)"
   "236", "Soil temperature at level 4", "K", "Surface (sfc)"
    "39", "Volumetric soil water at layer 1", "m**3/m**3", "Surface (sfc)"
    "40", "Volumetric soil water at layer 2", "m**3/m**3", "Surface (sfc)"
    "41", "Volumetric soil water at layer 3", "m**3/m**3", "Surface (sfc)"
    "42", "Volumetric soil water at layer 4", "m**3/m**3", "Surface (sfc)"      
   "133", "Specific humidity", "kg/kg", "Model level (ml)"  
   "130", "Temperature", "K", "Model level (ml)"  
   "131", "u-wind", "m/s", "Model level (ml)"        
   "132", "v-wind", "m/s", "Model level (ml)"    
   "152 or 134", "lnsp (analysis) or sp (forecast)", "- or Pa", "Model level (ml)" 
   "229", "significant wave height of wind waves and swell", "m", "Wave (wave)" 
   "234", "significant wave height of wind waves", "m", "Wave (wave)" 
   "237", "significant wave height of swell", "m", "Wave (wave)"           

.. note::

   You can find grib identifier  `here <https://codes.ecmwf.int/grib/param-db/>`_.

For CNRM's users
*************************************

* Fill .json file as desired.

* Name it as you want : for instance REQUEST_WURTZJ.json

* Put filed file here /cnrm/ville/USERS/wurtzj/EXTRACT_ECMWF/REQUESTS/

An output is available in this folder with an "out" suffix showing it works: /cnrm/ville/USERS/wurtzj/EXTRACT_ECMWF/JOB_STATUS/REQUEST_WURTZJ.json_out

ERA Interim
---------------------------------------------------------

* Go to http://apps.ecmwf.int/datasets/data/interim-full-daily/

* Login

Get invariant data
*************************************

* select "Invariant" in "ERA Interim Fields"

* select the parameters "Geopotential" and "Land-sea mask"

* click on "retrieve GRIB"


  * download the grib file and rename it "invariant.grib". It should contain the variables "z", "lsm"

Get surface data
*************************************

* select "Daily" in "ERA Interim Fields"
 
* select "Surface" in "Type of level"
 
* select the date YYYY-MM-DD
 
* select the time "HH:00:00"
 
* select the step "0"
 
* select the parameters "Snow depth", "Soil temperature level 1", "Soil temperature level 2", "Soil temperature level 3", "Soil temperature level 4", "Volumetric soil water layer 1", "Volumetric soil water layer 2", "Volumetric soil water layer 3", "Volumetric soil water layer 4"
 
* click on "retrieve GRIB"
 
* download the grib file and rename it "surface.grib". It should contain the variables "sd", "swvl1", "swvl2", "swvl3", "swvl4", "stl1", "stl2", "stl3", "stl4"

Get model level data
*************************************

* select "Daily" in "ERA Interim Fields"

* select "Model levels" in "Type of level"

* select the date YYYY-MM-DD

* select the time "HH:00:00"

* select the step "0"

* select the parameters "Logarithm of surface pressure", "Specific humidity", "Temperature", "U component of wind", "V component of wind"

* click on "retrieve GRIB"

* download the grib file and rename it "model.grib". It should contain the variables "lnsp", "q", "t", "u", "v"

Concatenate the grib files
*************************************

.. code-block:: bash

   $SRC_MESONH/src/dir_obj${XYZ}/MASTER/ECCODES-2.18.0/bin/grib_copy invariant.grib surface.grib model.grib ecmwf.EI.YYYYMMDD.HH


ERA5
--------------------------------------------

Registration
********************************************

Access to CDS data is restricted to registred users. See `CDS's website <https://cds.climate.copernicus.eu/cdsapp#!/home>`_ for more detailed informations. 

.. _configure_cds_api_key:

Configure
********************************************

Once your account create, you need to configure CDS API following https://cds.climate.copernicus.eu/api-how-to instructions. 
First you need to create a file called `.cdsapirc` in your HOME directory. Your `.cdsapirc` file needs to contain lines that look likes:

.. code-block:: bash

   url: https://cds.climate.copernicus.eu/api/v2
   key: your_key

.. note::

   To fill this file go to https://cds.climate.copernicus.eu/api-how-to.

.. warning::

   You need to suppress rules for group and other users with ``chmod 600 .cdsapirc``.

.. _install_python_cdsapi:

Installation
********************************************

You can install CDS API required to extract CAMS data using following conda command in your conda environment, do

.. code-block:: console

   conda install cdsapi
   
If you want to used a dedicated conda environment you can create an environment.yml file containing :

.. code-block:: python
   
   name: env_extract_cdsapi
   channels:
       - conda-forge
   dependencies:
       - cdsapi==0.7.0
       - eccodes==2.35.0
       - pip==24.0
       - pip:
           - yaml-config==0.1.5

.. note:: 
  
   * This is the last version of cdsapi and yaml-config tested.
   * yaml-config is used to read `.adsapirc` file if your are intent to extract CAMS files. For ERA5, only cdsapi is necessary.
   * eccodes is used to concatenate grib files.

Then you can create your conda environment with :

.. code-block:: console
 
   conda env create -f environment.yml

Then load new created python environment :

.. code-block:: console
 
   conda activate env_extract_cdsapi


Example
********************************************

To extract ERA5 data, you can adapt the area and the date in the following script :

.. code-block:: bash

   #!/bin/python
   # --------------------------------------------------------
   #
   #                 Author  (    date    ) :
   #             J. Pianezze ( 17.05.2024 )
   #
   #                    ~~~~~~~~~~~~~~~
   #       Script used to extract ERA5 instantaneous fields
   #        for Meso-NH (PREP_REAL_CASE) (1 time / file)
   #                    ~~~~~~~~~~~~~~~
   #
   # --------------------------------------------------------
   # https://cds.climate.copernicus.eu/api-how-to
   # conda install cdsapi

   import os, sys
   import glob
   import cdsapi
   import datetime

   cds = cdsapi.Client()

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

   # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   #   Define function to iterate over first and last dates
   # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   def range_for_date(start_date, end_date, period_in_hr):
     for n in range(int((end_date - start_date).total_seconds()/(3600.0*period_in_hr))+1):
       yield start_date + datetime.timedelta(seconds=n*3600.0*period_in_hr)

   # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   #   Loop over dates
   # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
   for date in range_for_date(first_date_to_be_extracted, last_date_to_be_extracted, period_between_last_and_first_dates_in_hr):

     # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     #   Compute date and time variables
     #     date_an format is yyyy-mm-dd
     #     time_an format is hh
     # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     date_to_be_extracted   = str(date.year)+'-'+str(date.month).zfill(2)+'-'+str(date.day).zfill(2)
     time_to_be_extracted   = str(date.hour).zfill(2)
     name_of_extracted_file = str(date.year)+str(date.month).zfill(2)+str(date.day).zfill(2)+'.'+str(date.hour).zfill(2)

     # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     #   Retrieve Model Level fields : u, v, t, q
     # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     cds.retrieve('reanalysis-era5-complete', {
           'date'     : date_to_be_extracted,
           'levelist' : '1/to/137',
           'levtype'  : 'ml',
           'param'    : 'u/v/t/q',
           'stream'   : 'oper',
           'time'     : time_to_be_extracted,
           'type'     : type_data_to_be_extracted,
           'area'     : area_to_be_extracted,
           'grid'     : '0.28125/0.28125',
       }, 'model_levels_uvtq_'+name_of_extracted_file+'.grib')

     # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     #   Retrieve Model Level fields : lnsp
     # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     cds.retrieve('reanalysis-era5-complete', {
           'date'     : date_to_be_extracted,
           'levelist' : '1',
           'levtype'  : 'ml',
           'param'    : 'lnsp',
           'stream'   : 'oper',
           'time'     : time_to_be_extracted,
           'type'     : type_data_to_be_extracted,
           'area'     : area_to_be_extracted,
           'grid'     : '0.28125/0.28125',
       }, 'model_levels_lnsp_'+name_of_extracted_file+'.grib')

     # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     #   Retrieve SurFaCe fields : z, lsm
     # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     cds.retrieve('reanalysis-era5-complete', {
           'date'     : date_to_be_extracted,
           'levtype'  : 'sfc',
           'param'    : 'z/lsm',
           'stream'   : 'oper',
           'time'     : time_to_be_extracted,
           'type'     : type_data_to_be_extracted,
           'area'     : area_to_be_extracted,
           'grid'     : '0.28125/0.28125',
       },  'surface_levels_'+name_of_extracted_file+'.grib')

     # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     #   Retrieve SurFaCe fields : swlv1, ...
     # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     cds.retrieve('reanalysis-era5-complete', {
         'date'     : date_to_be_extracted,
         'levtype'  : 'sfc',
         'param'    : '139/141/170/183/236/39/40/41/42',
         'stream'   : 'oper',
         'time'     : time_to_be_extracted,
         'type'     : type_data_to_be_extracted,
         'area'     : area_to_be_extracted,
         'grid'     : '0.28125/0.28125',
     }, 'surface_'+name_of_extracted_file+'.grib')

     # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     #   Concatenate & remove grib files
     # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     os.system('grib_copy surface_levels_'+name_of_extracted_file+'.grib    '+\
                         'surface_'+name_of_extracted_file+'.grib           '+\
                         'model_levels_uvtq_'+name_of_extracted_file+'.grib '+\
                         'model_levels_lnsp_'+name_of_extracted_file+'.grib '+\
                         'era5.'+name_of_extracted_file)

     for file in glob.glob('*.grib'):
       os.remove(file)

.. note::

   You need to have eccodes installed.

Then, you can launch the extraction with :

.. code-block:: bash

   ./your_script.sh

.. note::

   At the end of the extraction you need to have files called era5.${YEAR}${MONTH}${DAY}.${HOUR} !

Use extracted GRIB files
--------------------------------------------

To use extracted grib files in Meso-NH, you just have to add the name of the grib file in PRE_REAL1.nam file, by example :

.. code-block:: fortran

   &NAM_FILE_NAMES HATMFILE='name/of/your/grib/file',
                   HATMFILETYPE='GRIBEX',
                   ... /
