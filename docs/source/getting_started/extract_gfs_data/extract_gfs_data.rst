Extract GFS data
===============================

Data source
-------------------------------

There are several data sources to choose from if you want to force Meso-NH with the GFS model. It is important that the files are of type grib2, as grib1 has not been tested.

Historical mode
*******************************

The NCAR repository allows the download of GDAS/FNL data from 2015 to 2018 at 0.25 degrees resolution. These analyses and forecasts are produced slightly later than GFS forecasts because more observations are integrated in the assimilation cycle:

https://rda.ucar.edu/datasets/d083003/

In Historical mode, the NCAR repository enables download of GFS forecasts from 2006 to 2015 at 0.25 degrees resolution: 

https://rda.ucar.edu/datasets/d084001/

Files can be retrieved from the ncdc repository. Data are available at 0.5 degrees resolution for the latest forecasts going back one year, and for analyses going back to 2004:

.. warning ::

  However, grb files are of the grib1 type and should therefore be avoided.

https://www.ncei.noaa.gov/products/weather-climate-models/global-forecast

Operational mode
***********************************

The files can be downloaded from the NCEP repository. They are available in 0.25, 0.5 or 1 degree resolution, with a two-week hindsight:

https://www.nco.ncep.noaa.gov/pmb/products/gfs/

.. note ::
  Be sure to retrieve the files named: gfs.tCCz.pgrb2.0p25.fFFF

  The files are GFS operational outputs. Only the tree structure shows the date of the files (you can read the grib2 to find out).

GDAS files are also operationally available on this site.

Using the files
------------------------------------

Using GFS files as MesoNH input is very simple. Simply fill in the HATMFILE field with the file name in the PRE_REAL1.nam namelist. Please note that the number of characters in this field is limited, so rename the file if necessary.

Potential problems
-------------------------------------

The files described above have normally been tested. However, differences in the number of available pressure levels may lead to problems. Please check the OUTPUT_LISTING file and report any problems.
