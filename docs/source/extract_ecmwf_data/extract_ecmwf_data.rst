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

   conda env install -f environment.yml

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
   "get_sea_state"      : false

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


Launch extraction
**********************************

To launch extraction of the desired ECMWF data, if number of dates to extract is lower than 10 do

.. code-block:: bash

   python main_extract_ecmwf.py

or if number of dates is greater than 10, do 

.. code-block:: bash

   nohup python main_extract_ecmwf.py

.. note::

   * At the end of the script extractions are launched in background. If you are using your laptop or personal computer do not switch it off until extraction is complete. If you are using supercomputer you can logout without problems.

   * You can follow extraction processes on https://apps.ecmwf.int/webmars/joblist/.

Add new variables 
***********************************

If you want to add variables to extracted grib files, go to define_parameters.py file and add your own grib identifier in the following list :

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

ERA5 data 
--------------------------------------------------

Get invariant data
*************************************

* go to https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=form

* select "Reanalysis" in "Product type"

* In "Other", select the parameters "Geopotential" and "Land-sea mask"

* select the date YYYY-MM-DD

* select the time "HH:00:00"

* select the step "0"

* click on "retrieve GRIB"

* download the grib file and rename it "invariant.grib". It should contain the variables "z", "lsm"

Get surface data
*************************************

* go to https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-single-levels?tab=form
 
* select "Reanalysis" in "Product type"
 
* In "Temperature and pressure", select the parameter "Surface pressure"
 
* In "Snow", select the parameter "Snow depth"
 
* In "Soil", select the parameters "Soil temperature level 1", "Soil temperature level 2", "Soil temperature level 3", "Soil temperature level 4", "Volumetric soil water layer 1", "Volumetric soil water layer 2", "Volumetric soil water layer 3", "Volumetric soil water layer 4"
 
* select the date YYYY-MM-DD
 
* select the time "HH:00:00"
 
* select the step "0"
 
* click on "retrieve GRIB"
 
* download the grib file and rename it "surface.grib". It should contain the variables "sd", "sp", "swvl1", "swvl2", "swvl3", "swvl4", "stl1", "stl2", "stl3", "stl4"

Get model level data
*************************************

* go to https://cds.climate.copernicus.eu/cdsapp#!/dataset/reanalysis-era5-pressure-levels?tab=form
 
* select "Reanalysis" in "Product type"
 
* In "Variable", select the parameters "Geopotential", "Specific humidity", "Temperature", "U component of wind", "V component of wind"
 
* In "Pressure level", select all the levels
 
* select the date YYYY-MM-DD
 
* select the time "HH:00:00"
 
* select the step "0"

* click on "retrieve GRIB"
 
* download the grib file and rename it "model.grib". It should contain the variables "z", "q", "t", "u", "v"

Concatenate the grib files
*************************************

.. code-block:: bash

   $SRC_MESONH/src/dir_obj${XYZ}/MASTER/ECCODES-2.18.0/bin/grib_copy invariant.grib surface.grib model.grib ecmwf.E5.YYYYMMDD.HH

Use extracted GRIB files
--------------------------------------------

To use extracted grib files in Meso-NH, you just have to add the name of the grib file in PRE_REAL1.nam file, by example :

.. code-block:: fortran

   &NAM_FILE_NAMES HATMFILE='name/of/your/grib/file',
                   HATMFILETYPE='GRIBEX',
                   ... /
