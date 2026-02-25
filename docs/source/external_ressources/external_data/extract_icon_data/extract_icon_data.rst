.. _extracticon:

Extract ICON data
===============================

Data source
-------------------------------

The ICON model is run and support by several institues such as the german national weather services DWD among other (https://www.icon-model.org/about-us/icon-partners/icon-partners)
It is run in a global configuration; a limited-area configuration over europe ICON-EU at 7km resolution updated every 3 hours for the next 120 hours forecast.

The official website is https://www.icon-model.org/

For Meso-NH, only the ICON-EU digestion was tested. 

Historical mode
*******************************

No data are publicly available

Operational mode
***********************************

A new cycle is run every 3 hours
Data are available here http://opendata.dwd.de/weather/nwp/icon-eu/grib/

Using the files
-------------------------------

Only available since MNH-V6-0-0.

Simply fill the HATMFILE field in PRE_REAL1.nam with the file name iconeu.RRz.HH.grib2 extracted with a script found in the GRIB/ICONEU test case. 