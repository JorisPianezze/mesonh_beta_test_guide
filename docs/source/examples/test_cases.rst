Cases catalogue
============================================

This catalogue lists all test cases available in the folder ``MNH-VX-X-X/MY_RUN``

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
   :header: "Name", "Wind Advection", "Surface", "Rad", "Turb", "Shallow Conv.", "Deep Conv.", "Micro"
   :widths: 5, 3, 3, 3, 5, 5, 5, 5

   "IHOP_1D", "-", "ideal Flux", "None", "1D-BL89/RM17","EDKF", "None", "REVE"
   "IHOP_3D", "CEN4TH", "ideal Flux", "None", "3D-DEAR","None", "None","None"
   "FIRE_1D", "-", "ideal Flux", "ECMW/ECRAD","1D-BL89","EDKF", "None","KHKO/LIMA"
   "FIRE_3D", "CEN4TH / WENO5", "ideal Flux", "ECMW","TKE-3D-DEAR","None", "None","KHKO"
   "GABLS1_1D", "-", "ideal TSZ0", "None","1D-BL89/RM17","None", "None", "None"
   "GABLS1_3D", "CEN4TH", "ideal TSZ0", "None","3D-DEAR","None", "None","None"
   "ARMCU_1D", "-", "ideal Flux", "None", "1D-BL89", "EDKF", "None","ICE3"
   "ARMCU_3D", "CEN4TH", "ideal Flux", "None", "3D-DEAR", "None", "None", "ICE3"
   "BOMEX", "-", "ideal Flux", "None","1D-BL89", "EDKF", "None","ICE3"

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
   :header: "Name", "Wind Advection", "Surface", "Rad", "Turb", "Shallow Conv.", "Deep Conv.", "Micro"
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

   "COPT81", "2D", "320x1x46", "1250m", "7.2m", "10s", "OPEN", "8h"
   "STERAO", "3D", "160x160x50", "1000m", "77m", "2.5s", "OPEN", "3h"
  

.. csv-table:: Applicatives cases
   :header: "Name", "Wind Advection", "Surface", "Rad", "Turb", "Shallow Conv.", "Deep Conv.", "Micro"
   :widths: 5, 3, 3, 3, 5, 5, 5, 5

   "COPT81", "CEN4TH", "ideal Flux", "None", "3D-DELT","None", "None", "ICE3"
   "STERAO", "CEN4TH", "None", "None", "3D-DELT","None", "None", "ICE3"


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

Technical cases
---------------------
Technical cases are demonstration use-cases of a specific technical pipeline.

.. toctree::
   :maxdepth: 1

   TECHNICAL/16JAN/case_description.rst
   TECHNICAL/DOUBLE_GRIDNESTING/case_description.rst
   TECHNICAL/GRIB/case_description.rst
   TECHNICAL/STATIONS_PROF_BALLON_AIRCR_4doms/case_description.rst
