.. _extracthrrr:

Extract HRRR data
===============================

Data source
-------------------------------

The HRRR (High-Resolution Rapid Refresh) is a NOAA real-time 3-km resolution, hourly updated, cloud-resolving, convection-allowing atmospheric model, 
initialized by 3km grids with 3km radar assimilation based on the WRF model
Radar data is assimilated in the HRRR every 15 min over a 1-h period adding further detail to that provided by the hourly data assimilation from the 13km radar-enhanced Rapid Refresh.
The forecst lead time is 48 hours.

Data, tutorial, licence and informations can be found here https://registry.opendata.aws/noaa-hrrr-pds/

The official website is https://rapidrefresh.noaa.gov/hrrr/

Historical mode
*******************************

Browse the bucket here https://noaa-hrrr-bdp-pds.s3.amazonaws.com/index.html

Data are stored since 2014-07-30.

Download surface grib2 and pressure-level grib2 files with these commands:

.. note ::
    wget -c -nd https://noaa-hrrr-bdp-pds.s3.amazonaws.com/hrrr.${YYYYMMDD}/conus/hrrr.t${RR}z.wrfsfcf${HH}.grib2

    wget -c -nd https://noaa-hrrr-bdp-pds.s3.amazonaws.com/hrrr.${YYYYMMDD}/conus/hrrr.t${RR}z.wrfprsf${HH}.grib2

    cat hrrr.t${RR}z.wrfprsf${HH}.grib2 hrrr.t${RR}z.wrfsfcf${HH}.grib2 >> hrrr.${YYYYMMDD}${RR}z.${HH}.grib2

With YYYYMMDD and RR are the date and assimilation start date of the run. HH is the forecast lead time.

Example YYYYMMDD=20260924 RR=12, HH=06 <==> forecast of 20260924 18 UTC based on the 13UTC run.

Operational mode
***********************************

Files are updated hourly. HRRR runs a cycle every hour.

Using the files
------------------------------------
Only available since MNH-V6-0-0.

Simply fill the HATMFILE field in PRE_REAL1.nam with the file name hrrr.tRRz.wrffHH.grib2.