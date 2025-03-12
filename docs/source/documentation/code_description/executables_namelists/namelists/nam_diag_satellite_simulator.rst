.. _nam_diag_satellite_simulator:

NAM_DIAG - Satellite simulator
-----------------------------------------------------------------------------

Since RTTOV requires a license agreement, no RTTOV package is included in the open source version of Meso-NH. However, a subroutine calling RTTOV 13 is included in Meso-NH version 57. To compile and use Meso-NH with RTTOV, you must follow the instructions in :ref:`compile_mesonh_with_rttov`.
  
.. csv-table::
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
  
   "NRTTOVinfo", "INTEGER(1:4,10)", "999"

For each instrument nb you want (1 ≤ nb ≤ 10) :

* NRTTOVinfo(1,nb) : Plt = Plateforme

* NRTTOVinfo(2,nb) : Sat = Satellite

* NRTTOVinfo(3,nb) : Sen = Sensor

* NRTTOVinfo(4,nb) : 0

Following variable will be store :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "BT", "Brightness temperature (K)", "2D"

To simulate an instrument, use the code given in the following tables reproduced from the RTTOV users guide (see https://www.nwpsaf.eu/site/software/rttov).
For example, to simulate both all the SEVIRI channels of MSG-2 and all the AMSU-B channels of NOAA-16, write in DIAG1.nam

.. code-block:: fortran

   &NAM_DIAG NRTTOVinfo(:,1)= 12 2 21 0,
             NRTTOVinfo(:,2)= 1 16 4 0 /
   
For this specific choice, you need to have four files: :file:`rtcoef_msg_2_seviri.dat`, :file:`sccldcoef_msg_2_seviri.dat`, :file:`rtcoef_noaa_16_amsub.dat` and :file:`hydrotable_noaa_amsub.dat`.
The AMSU-B coefficient files can be found in directories rttov13pred54L and hydrotable (or to be downloaded from the RTTOV web site). The MSG-2 coefficient files are aliased following:

* for IR only calculation, do:

.. code-block:: bash

   ln -sf []/rttov13pred54L/rtcoef_msg_2_seviri_7gas_ironly.dat rtcoef_msg_2_seviri.dat
   ln -sf []/cldaer_ir/sccldcoef_msg_2_seviri_ironly.dat sccldcoef_msg_2_seviri.dat

* for visible and IR calculation, do:

.. code-block:: bash

   ln -sf []/rttov13pred54L/rtcoef_msg_2_seviri_o3co2.dat rtcoef_msg_2_seviri.dat
   ln -sf []/cldaer_visir/sccldcoef_msg_2_seviri.dat .
   
In addition, download the brdf_data file and set NRTTOVinfo(4,1) to 1.
   
.. csv-table:: List of Plt and Sat variables
   :header: "Platform", "Plt", "Sat range"
   :widths: 30, 30, 30
      
   "NOAA","1","1 to 18"
   "DMSP","2","8 to 16"
   "Meteosat","3","5 to 7"
   "GOES","4","8 to 12"
   "GMS","5","5"
   "FY-2","6","2 to 3"
   "TRMM","7","1"
   "ERS","8","1 to 2"
   "EOS","9","1 to 2"
   "METOP","10","1 to 3"
   "ENVISAT","11","1"
   "MSG","12","1 to 2"
   "FY-1","13","3"
   "ADEOS","14","1 to 2"
   "MTSAT","15","1"
   "CORIOLIS","16","1"
   
.. csv-table:: List of Sen variables
   :header: "Sensor","RTTOVid (Sen)","Sensor Channel","RTTOV-8 Channel"
   :widths: 30, 30, 30, 30
   
   "HIRS","0","1 to 19","1 to 19"
   "MSU","1","1 to 4","1 to 4"
   "SSU","2","1 to 3","1 to 3"
   "AMSU-A","3","1 to 15","1 to 15"
   "AMSU-B","4","1 to 5","1 to 5"
   "AVHRR","5","3b to 5","1 to 3"
   "SSMI","6","1 to 7","1 to 4"
   "VTPR1","7","1 to 8","1 to 8"
   "VTPR2","8","1 to 8","1 to 8"
   "TMI","9","1 to 9","1 to 9"
   "SSMIS","10","1 to 24","1 to 21"
   "AIRS","11","1 to 2378","1 to 2378"
   "HSB","12","1 to 4","1 to 4"
   "MODIS","13","1 to 17","1 to 17"
   "ATSR","14","1 to 3","1 to 3"
   "MHS","15","1 to 5","1 to 5"
   "IASI","16","1 to 8461","1 to 8461"
   "AMSR","17","1 to 14","1 to 7"
   "MVIRI","20","1 to 2","1 to 2"
   "SEVIRI","21","4 to 11","1 to 8"
   "GOES-Imager","22","1 to 4","1 to 4"
   "GOES-Sounder","23","1 to 18","1 to 18"
   "GMS/MTSAT imager","24","1 to 4","1 to 4"
   "FY2-VISSR","25","1 to 2","1 to 2"
   "FY1-MVISR","26","1 to 3","1 to 3"
   "CriS","27","TBD","TBD"
   "CMISS","28","TBD","TBD"
   "VIIRS","29","TBD","TBD"
   "WINDSAT","30","1 to 10","1 to 5"

