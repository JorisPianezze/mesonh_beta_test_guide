Cases catalogue
============================================

This catalogue lists all test cases available in ``MNH-VX-X-X/MY_RUN``

Idealized cases
---------------------
Idealized cases are single column, 2D or 3D simulations initialized with a horizontally uniform vertical profiles.

Boundary-layer cases
*************************

.. toctree::
   :maxdepth: 1

   IDEAL/IHOP/case_description.rst
   IDEAL/FIRE/case_description.rst
   IDEAL/GABLS1/case_description.rst
   IDEAL/ARMCU/case_description.rst
   IDEAL/BOMEX/case_description.rst

.. csv-table:: Boundary-layer idealized cases
   :header: "Name", "Dim.", "Nb pts", "Dx", "Dz","Dt","LBC","Duration"
   :widths: 5, 3, 3, 3, 3,5, 5,5

   "IHOP_1D", "1D", "1x1x100", "100m", "40m", "10s", "CYCL", "7h"
   "IHOP_3D", "3D", "256x256x90", "50m", "10m", "1s",  "CYCL", "14h"
   "FIRE_1D", "1D", "1x1x120", "2500m","10m","120s", "CYCL", "25h"
   "FIRE_3D", "3D", "50x50x120", "50m","10m","1s / 5s", "CYCL","25h"
   "GABLS1_1D", "1D", "1x1x155", "2m","2m","10s", "CYCL","9h"
   "GABLS1_3D", "3D", "100x100x155", "2m","2m","0.2s", "CYCL","9h"
   "ARMCU_1D", "1D", "1x1x100", "40km", "40m", "100s", "CYCL","15h"
   "ARMCU_3D", "3D", "64x64x100", "100m", "40m", "2s", "CYCL","12h"
   "BOMEX", "1D", "1x1x75", "40km","40m", "120s", "CYCL","8h"

.. csv-table:: Boundary-layer idealized cases
   :header: "Name", "Wind Advection", "Surface", "Rad", "Turb", "Shallow conv.", "Micro.", "Deep conv."
   :widths: 5, 3, 3, 3, 5, 5, 5, 5

   "IHOP_1D", "", "ideal Flux", "None", "1D-BL89/RM17","EDKF", "REVE", "None"
   "IHOP_3D", "CEN4TH", "ideal Flux", "None", "3D-DEAR","None", "None","None"
   "FIRE_1D", "", "ideal Flux", "ECMW/ECRAD","1D-BL89","EDKF", "KHKO/LIMA","None"
   "FIRE_3D", "CEN4TH / WENO5", "ideal Flux", "ECMW","3D-DEAR","None", "KHKO","None"
   "GABLS1_1D", "", "ideal TSZ0", "None","1D-BL89/RM17","None", "None", "None"
   "GABLS1_3D", "CEN4TH", "ideal TSZ0", "None","3D-DEAR","None", "None","None"
   "ARMCU_1D", "", "ideal Flux", "None", "1D-BL89", "EDKF", "ICE3","None"
   "ARMCU_3D", "CEN4TH", "ideal Flux", "None", "3D-DEAR", "None", "ICE3", "None"
   "BOMEX", "", "ideal Flux", "None","1D-BL89", "EDKF", "ICE3","None"

Academic cases
*************************
.. toctree::
   :maxdepth: 1

   IDEAL/2Drelief/case_description.rst
   IDEAL/3Drelief/case_description.rst
   IDEAL/HYDRO/case_description.rst
   IDEAL/COLD_BUBBLE/case_description.rst

.. csv-table:: Academic cases
   :header: "Name", "Dim.", "Nb pts", "Dx", "Dz","Dt","LBC","Duration"
   :widths: 5, 3, 3, 3, 3, 5, 5, 5

   "2Drelief", "2D", "256x1x48", "5000m", "40m", "60s", "OPEN","3h"
   "3Drelief", "3D", "128x96x72", "2000m", "250m", "80s",  "OPEN", "10000s"
   "HYDRO", "2D", "90x1x121", "2000m","250m","10s", "CYCL","1500s"
   "COLD_BUBBLE", "2D", "1024x128", "50m","50m","0.5s", "CYCL", "15min"

.. csv-table:: Academic cases
   :header: "Name", "Wind Advection", "Surface", "Rad", "Turb", "Shallow conv.", "Micro.", "Deep conv."
   :widths: 5, 3, 3, 3, 5, 5, 5, 5

   "2Drelief", "CEN4TH", "None", "None", "3D-DELT","None", "None", "None"
   "3Drelief", "CEN4TH", "None", "None", "None","None", "None","None"
   "HYDRO", "CEN4TH", "None", "None","None","None", "None","None"
   "COLD_BUBBLE", "CEN4TH", "None", "None","None","None", "None","None"

Applicatives cases
*************************
.. toctree::
   :maxdepth: 1

   IDEAL/COPT81/case_description.rst
   IDEAL/EOLIENNE/case_description.rst
   IDEAL/SUPERCELL/case_description.rst
   IDEAL/IBM/case_description.rst
   IDEAL/BLAZE/case_description.rst
   IDEAL/STERAO/case_description.rst
   IDEAL/OCEAN_LES/case_description.rst
   IDEAL/BLOWSNOW_c1b1D/case_description.rst

.. csv-table:: Applicatives cases
   :header: "Name", "Dim.", "Nb pts", "Dx", "Dz","Dt","LBC","Duration"
   :widths: 5, 3, 3, 3, 3, 5, 5, 5

   "SUPERCELL", "3D", "600x600x89", "500m", "10.9m", "2s", "OPEN", "3h"
   "BLAZE", "3D", "100x50x30", "25m", "10m", "1s", "OPEN", "600s"
   "COPT81", "2D", "320x1x46", "1250m", "7.2m", "10s", "OPEN", "8h"
   "STERAO", "3D", "160x160x50", "1000m", "77m", "2.5s", "OPEN", "3h"
   "OCEAN_LES", "3D", "128x128x100", "125m", "20m", "10s", "CYCL", "6h"
   "", "3D", "320x240x100", "12.5m", "20m", "5s", "OPEN", "6h"
   "BLOWSNOW_c1b1D", "1D", "1x1x70", "10000m", "6m", "0.5s", "CYCL", "1200s"
   "IBM/CUBE", "3D", "640x160x41", "3.12cm", "3.12cm", "0.0175s", "OPEN", "1250s"
   "IBM/CYCLINDER", "3D", "60x400x10", "10m", "10m", "2.5s", "OPEN+WALL", "100000s"
   "IBM/ICIF_OBJ", "3D", "1200x1200x150", "1m", "1m", "0.04s", "OPEN", "100s"
   "IBM/MUST", "3D", "1200x1200x40", "0.6m", "0.3m", "0.02s", "OPEN", "150s"
   "", "3D", "1200x1200x40", "0.3m", "0.3m", "0.02s", "OPEN", "150s"
   "EOL/ADNR/01-1WT", "3D", "450x120x80", "10m", "10m", "1s", "CYCL", "3600s"
   "EOL/ADNR/02-1WT", "3D", "90x40x80", "50m", "10m", "5s", "CYCL", "2400s"
   "", "3D", "250x100x80", "50m", "10m", "1s", "CYCL", "2400s"
   "EOL/ALM/01-1WT", "3D", "900x240x160", "5m", "5m", "0.05s", "CYCL", "306.25s"
   "EOL/ALM/02-1WT", "3D", "2250x600x168", "2m", "2m", "0.01s", "CYCL", "6.25s"
   "EOL/ALM/03-2WT", "3D", "90x40x80", "50m", "10m", "1s", "CYCL", "2400s"
   "", "3D", "250x100x80", "50m", "10m", "0.1s", "CYCL", "2400s"
   "EOL/ADR", "3D", "450x120x80", "10m", "10m", "1s", "CYCL", "306.25s"
   
.. csv-table:: Applicatives cases
   :header: "Name", "Wind Advection", "Surface", "Rad", "Turb", "Shallow Conv.", "Micro.", "Deep conv."
   :widths: 5, 3, 3, 3, 5, 5, 5, 5
   
   "SUPERCELL", "CEN4TH", "None", "None", "3D-DEAR","None", "ICE4/LIMA", "None"
   "BLAZE", "WENO3", "ISBA", "None", "None", "None", "None", "None"   
   "COPT81", "CEN4TH", "ideal Flux", "None", "3D-DELT","None", "ICE3", "None"
   "STERAO", "CEN4TH", "None", "None", "3D-DELT","None", "ICE3", "None"
   "OCEAN_LES", "CEN4TH", "None", "None", "1D-DELT","None", "None", "None"
   "", "CEN4TH", "None", "None", "3D-DELT","None", "None", "None"
   "BLOWSNOW_c1b1D", "", "ISBA", "None", "1D-BL89","None", "None", "None"
   "IBM/CUBE", "WENO5", "ideal Flux", "None", "3D-DELT","None", "None", "None"
   "IBM/CYLINDER", "WENO5", "ideal Flux", "None", "None","None", "None", "None"
   "IBM/ICIF_OBJ", "WENO5", "ideal Flux", "None", "3D-DEAR","None", "None", "None"
   "IBM/MUST", "WENO5", "ideal Flux", "None", "3D-DEAR","None", "None", "None"
   "", "WENO5", "ideal Flux", "None", "3D-DEAR","None", "None", "None"
   "EOL/ADNR/ADR/ALM", "CEN4TH", "SEAFLUX", "None", "3D-HM21","None", "None", "None"


Realistic cases
---------------------
Realistic cases are high-fidelity simulations based on realistic description of the surface from research or operational surface databases with
the initialization and coupling of the atmosphere from operational data (forecast, analysis or reanalysis).

.. toctree::
   :maxdepth: 1

   REAL/AZF_2M/case_description.rst
   REAL/BIOMAIDO/case_description.rst
   REAL/CHARMEX/case_description.rst
   REAL/CYCLONE/case_description.rst
   REAL/DUST/case_description.rst
   REAL/FANNY/case_description.rst
   REAL/FOG_3D/case_description.rst
   REAL/HAIC/case_description.rst
   REAL/ICART2M/case_description.rst
   REAL/ICCARE_CORSE/case_description.rst
   REAL/KMAP/case_description.rst
   REAL/PANAME/case_description.rst
   REAL/SALT/case_description.rst
   REAL/SNOW_BLOW/case_description.rst
   REAL/TROCCINOX/case_description.rst
   REAL/XYNTHIA_2.5km/case_description.rst

.. csv-table:: Realistic cases
   :header: "Name", "Nb pts", "Dx", "Dz","Dt","Duration", "Date", "Init/Cpl", "Location"
   :widths: 5, 3, 3, 3, 3, 2, 4, 5, 5

   "AZF_2M", "50x50x40", "2500m", "72m", "10s", "1h", "2001-09-21", "IFS", "South-West France"
   "", "120x90x40", "500m", "72m", "2s", "", "", "", "Toulouse"
   "BIOMAIDO", "60x60x45", "8000m", "60m", "30s", "6h", "2019-03-28", "IFS", "La Reunion"
   "", "60x60x45", "2000m", "60m", "6s", "", "", "", ""
   "CHARMEX", "20x20x61", "50000m", "10m", "30s", "12h", "2014-06-30", "IFS", "Europe"
   "CYCLONE", "240x240x70", "4000m", "25m", "5s", "48h", "", "ideal", "Ocean"
   "DUST", "30x30x30", "30000m", "100m", "120s", "72h", "2000-09-24", "IFS", "South-West Africa"
   "FANNY", "250x225x40", "2500m", "72m", "10s", "24h", "2008-09-03", "AROME", "South-East France"
   "FOG_3D", "300x300x34", "500m", "0.25m", "4s", "12h", "2009-02-27", "AROME", "Paris"
   "HAIC", "360x250x70", "2500m", "30m", "10s", "24h", "2015-05-29", "AROME", "Guyana"
   "ICART2M", "30x30x60", "15000m", "60m", "120s", "3h", "2004-08-10", "IFS", "?"
   "", "60x60x60 ", "2500m", "60m", "30s", "3h", "", "", ""

.. csv-table:: Realistic cases
   :header: "Name", "Wind Advection", "Surface", "Rad", "Turb", "Shallow Conv.", "Micro.", "Deep conv."
   :widths: 5, 3, 3, 3, 5, 5, 5, 5
   
   "AZF_2M", "CEN4TH", "SURFEX", "ECMW", "1D-BL89","EDKF", "ICE3", "None"
   "", "CEN4TH", "SURFEX", "ECMW", "1D-BL89","None", "ICE3", "None"
   "BIOMAIDO", "WENO5", "SURFEX", "ECMW", "1D-BL89","EDKF", "LIMA", "None"
   "CHARMEX", "WENO5", "SURFEX", "ECMW", "1D-BL89","EDKF", "LIMA", "KAFR"
   "CYCLONE", "CEN4TH", "SURFEX", "ECMW", "1D-BL89","KAFR", "ICE3", "None"
   "DUST", "WENO5", "SURFEX", "ECMW", "1D-BL89","KAFR", "ICE3", "KAFR"
   "FANNY", "WENO5", "SURFEX", "ECMW", "1D-BL89","KAFR", "ICE3/LIMA", "None"
   "FOG_3D", "CEN4TH", "SURFEX", "ECMW/ECRAD", "1D-BL89","None", "ICE3/LIMA", "None"
   "HAIC", "CEN4TH", "SURFEX", "ECMW/ECRAD", "1D-BL89","EDKF", "ICE3/LIMA", "None"
   "ICART2M", "CEN4TH", "SURFEX", "ECMW", "1D-BL89","EDKF", "ICE3", "KAFR"
   "", "CEN4TH", "SURFEX", "ECMW", "1D-BL89","EDKF", "ICE3", "None"

Technical cases
---------------------
Technical cases are demonstration use-cases of a specific technical pipeline.

.. toctree::
   :maxdepth: 1

   TECHNICAL/16JAN/case_description.rst
   TECHNICAL/DOUBLE_GRIDNESTING/case_description.rst
   TECHNICAL/GRIB/case_description.rst
   TECHNICAL/STATIONS_PROF_BALLON_AIRCR_4doms/case_description.rst
