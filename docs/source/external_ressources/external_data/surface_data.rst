Surface data
================================================

Surface data are necessary if you want to prepare idealised and/or real case study above realistic surface using PREP_PGD program.
For that purpose, you need 4 files : topography, soil texture and land user, all of them with hdr and dir suffixes. The disk space required to store the files is about 3 Go.

Download 
***********

You can download the files using direct download in following subsections or with following bash script :

.. code-block:: bash

   #!/bin/bash
   
   export dir_pgd_files='http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_PGDFILES'

   for file in LICENSE_ECOCLIMAP.txt LICENSE_soil_data.txt \
               gtopo30.hdr           gtopo30.dir           \
               SAND_HWSD_MOY.hdr     SAND_HWSD_MOY.dir     \
               CLAY_HWSD_MOY.hdr     CLAY_HWSD_MOY.dir     \
               ECOCLIMAP_v2.0.hdr    ECOCLIMAP_v2.0.dir    \
               etopo2.nc
   do
      if [ ! -f ${file} ]
      then
         echo 'Download' ${file}
         wget -c -nd ${dir_pgd_files}/${file}.gz ; gunzip ${file}.gz
      fi
   done

.. note::

   * This script download gtopo30 for the topography, SANS_HWSD_MOY and CLAY_HWSD_MOY for soil texture and ECOCLIMAPO_v2.0 for land use. In following section, all the databases available on Meso-NH server are described. If you need other database available in http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_PGDFILES, you have to adapt this bash script or download them directly via the link.
   * Files are compressed with gunzip, don't forget to uncompressed them before using it with Meso-NH.

Topography
***********

* GTOPO30, a global digital elevation model (DEM) with a horizontal grid spacing of 30 arc seconds (approximately 1 kilometer).

  * **Source :** https://lta.cr.usgs.gov/GTOPO30
  * **Download :** 

    * :download:`gtopo30.hdr.gz <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_PGDFILES/gtopo30.hdr.gz>`
    * :download:`gtopo30.dir.gz <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_PGDFILES/gtopo30.dir.gz>`

* SRTM NE at 250 m between 30°W-180°E and 0-60°N

  * A digital elevation model (DEM) with a horizontal grid spacing of approximately 250 meters (derived from srtm90 tiles, see https://bigdata.cgiar.org/srtm-90m-digital-elevation-database, only over the North East part of the world (latitude from 60N to 0N and longitude from 30W to 180E 
  * **Download :** 

    * :download:`srtm_ne_250m.hdr.gz <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_PGDFILES/srtm_ne_250m.hdr.gz>`
    * :download:`srtm_ne_250m.dir.gz <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_PGDFILES/srtm_ne_250m.dir.gz>`

* SRTM SE at 250 m between 30°W-180°E and 0-60°S

  * **Download :**

    * :download:`srtm_se_250m.hdr.gz <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_PGDFILES/srtm_se_250m.hdr.gz>`
    * :download:`srtm_se_250m.dir.gz <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_PGDFILES/srtm_se_250m.dir.gz>`

* SRTM at 30 m over France between 5°W-10°E and 40-55°N see domain

  * **Download :**
    
    * :download:`srtm_france_30m.hdr.gz <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_PGDFILES/srtm_france_30m.hdr.gz>`
    * :download:`srtm_france_30m.dir.gz <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_PGDFILES/srtm_france_30m.dir.gz>`

Soil texture
*************

* HWSD at 1 km, v2 (global). In v2, maps with missing data (relative to the land/sea mask from ECOCLIMAP_v1) are corrected, setting the default value 0.33 for sand and clay in missing data points.

  * **Source :** http://www.iiasa.ac.at/Research/LUC/External-World-soil-database/HTML/
  * **Download :**
    
    * :download:`CLAY_HWSD_MOY_v2.hdr.gz <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_PGDFILES/CLAY_HWSD_MOY_v2.hdr.gz>`
    * :download:`CLAY_HWSD_MOY_v2.dir.gz <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_PGDFILES/CLAY_HWSD_MOY_v2.dir.gz>`
    * :download:`SAND_HWSD_MOY_v2.hdr.gz <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_PGDFILES/SAND_HWSD_MOY_v2.hdr.gz>`
    * :download:`SAND_HWSD_MOY_v2.dir.gz <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_PGDFILES/SAND_HWSD_MOY_v2.dir.gz>`
    * :download:`LICENSE_soil_data.txt.gz <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_PGDFILES/LICENSE_soil_data.txt.gz>`.

Land use
***********

* ECOCLIMAP v1.8, a 1 km global database for land use

  * **Download :**
    
    * :download:`ECOCLIMAP_I_GLOBAL_V1.8.hdr.gz <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_PGDFILES/ECOCLIMAP_I_GLOBAL_V1.8.hdr.gz>`
    * :download:`ECOCLIMAP_I_GLOBAL_V1.8.dir.gz <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_PGDFILES/ECOCLIMAP_I_GLOBAL_V1.8.dir.gz>`
    * :download:`LAKE_DEPTH_ECO_I_V1.7.hdr.gz <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_PGDFILES/LAKE_DEPTH_ECO_I_V1.7.hdr.gz>`
    * :download:`LAKE_DEPTH_ECO_I_V1.7.dir.gz <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_PGDFILES/LAKE_DEPTH_ECO_I_V1.7.dir.gz>`

* ECOCLIMAP v2.6, a 1 km global database with improved land use data over Europe (11°W-62°E, 25°N-75°N)

  * **Download :**
    
    * :download:`ECOCLIMAP_II_EUROP_V2.6.hdr.gz <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_PGDFILES/ECOCLIMAP_II_EUROP_V2.6.hdr.gz>`
    * :download:`ECOCLIMAP_II_EUROP_V2.6.dir.gz <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_PGDFILES/ECOCLIMAP_II_EUROP_V2.6.dir.gz>`
    * :download:`LAKE_DEPTH_ECO_II_V2.6.tgz <http://mesonh.aero.obs-mip.fr/mesonh/dir_open/dir_PGDFILES/LAKE_DEPTH_ECO_II_V2.6.tgz>`

Additional databases
**********************

For more choices of topography, soil texture, land use, bathymetry and lakes cover databases, follow the SURFEX dedicated web page : http://www.umr-cnrm.fr/surfex/spip.php?rubrique14.
