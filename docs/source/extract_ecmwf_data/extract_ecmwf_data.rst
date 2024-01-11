Extract ECMWF's data
============================================

Operational data (analysis, forecast or ensemble)
--------------------------------------------------

.. _get_the_tool:

Get the tool
*******************

To get the tool you can download it via 

.. code-block:: console

   git clone https://github.com/JorisPianezze/EXTRACT_ECMWF.git

.. note::

   This Git's repository is a forked from https://github.com/wurtzj/EXTRACT_ECMWF. It contains additional variables : sea state, oceanic wave spectra and 10m wind speed.

* define_parameters_extractecmwf.py - Read PARAMS_EXTRACT.json file

* main_extract_ecmwf_python.py execute extractecmwf_run.py file in backend with nohup

.. _configure_ecmwf_api_key:

Configuration 
*******************

First you need to create a file called .ecmwfapirc in your HOME directory. To get the key go to https://api.ecmwf.int/v1/key/. Your .ecmwfapirc needs to contain lines that look likes:

.. code-block:: bash

   {
    "url"   : "https://api.ecmwf.int/v1",
    "key"   : "your_key",
    "email" : "your_email"
   }

.. note::

   You need to do a chmod 600 .ecmwfapirc to suppress rules for group and other users.

.. _install_python_ecmwfapi:

Install python environment
******************************

To install python environment required to extarct ECMWF data, if you are using conda, do

.. code-block:: console

   conda env install -f environment.yml

or if you are using mamba

.. code-block:: console

   mamba env install -f environment.yml

Then load new created python environment :

.. code-block:: console
 
   conda activate env_extract_ecmwf

Define extraction's parameters
**********************************

.. code-block:: python

   {
  
   "target_directory"   : "/home/piaj/02_models/EXTRACT_ECMWF/test/",

   "start_date"         : "20170708",
   "end_date"           : "20170710",
   "list_of_dates"      : ["20220617"],

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

   "get_surface"        : True,
   "get_sea_state"      : True

   }

.. note::

   * target_directory is where your data will be written.

   * date to be extracted is take between start_date and end_date if list_of_dates is empty ([]).

   * start_time, 1st time extraction

   * end_time : last time extraction

   * step: time step extraction within the day

   * forecast_start_time : in case of forecast : time of launch (00 or 12 for instance)

   * domain extension lat_min, lat_max, lon_min, lon_max. If empty get Europe domain.

   * grid resolution .1 by default. Could be coarser

   * type_data : type of data to be extracted : analysis, forecast or ensemble.

   * get_surface : get surface parameters or not. Mandatory for Meso-NH users.

   * get_sea_state : get sea state parameters or not. Used only when sea salt aerosols are activated.


Launch extraction
**********************************

.. code-block:: bash

   python main_extract_ecmwf_python.py

.. note::

   You can follow extraction processes on https://apps.ecmwf.int/webmars/joblist/.

Extraction for CNRM users
*************************************

Fill .json file as desired.
Name it as you want : for instance   REQUEST_WURTZJ.json

Put filed file here :

/cnrm/ville/USERS/wurtzj/EXTRACT_ECMWF/REQUESTS/

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

You just have to add the name of your extracted grib's file in PRE_REAL1.nam file, by example :

.. code-block:: fortran

   &NAM_FILE_NAMES HATMFILE='name/of/your/grib/file',
                   HATMFILETYPE='GRIBEX',
                   ... /
