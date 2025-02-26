Cases catalogue
============================================

This catalogue lists all test cases available in the folder ``MNH-VX-X-X/MY_RUN``

.. csv-table:: Idealized cases
   :header: "Name", "Dim.", "Nb pts", "Res.","Surface", "Rad", "Turb", "Shallow", "Micro", "Boundary conditions"
   :widths: 7, 3, 3, 5, 3, 5, 5, 5, 5, 5

   "2Drelief", "2D", "", "","","","","","",""
   "3Drelief", "3D", "0", "1", "","","","","",""
   "HYDRO", "2D", "", "", "","","","","",""
   "IHOP", "3D", "", "", "","","","","",""
   "COLD_BUBBLE", "2D ", "1024x128", "50m", "None", "None","None","None","None","CYCL"
   "FIRE_1D", "1D", "", "","","","","","",""
   "FIRE_3D", "3D", "", "","","","","","",""
   "GABLS1_1D", "1D", "", "","","","","","",""
   "GABLS1_3D", "3D", "", "","","","","","",""
   "ARMCU_1D", "1D", "", "","","","","","",""
   "ARMCU_3D", "3D", "", "","","","","","",""
   "BOMEX", "3D", "", "","","","","","",""
   "COPT81", "2D", "", "","","","","","",""
   "EOLIENNE", "3D", "", "","","","","","",""
   "SUPERCELL", "3D", "", "","","","","","",""
   "IBM", "3D", "", "","","","","","",""
   "BLAZE", "3D", "", "","","","","","",""
   "STERAO", "3D", "", "","","","","","",""  
   "OCEAN_LES", "3D", "", "","","","","","",""        
   "BLOWSNOW", "1D", "", "","","","","","",""         


Idealized cases
---------------------
Idealized cases are single column, 2D or 3D simulations initialized with a horizontally uniform vertical profiles.

Boundary-layer cases
*************************

.. toctree::
   :maxdepth: 1

   IDEAL/FIRE/case_description.rst
   IDEAL/GABLS1/case_description.rst
   IDEAL/ARMCU/case_description.rst
   IDEAL/BOMEX/case_description.rst

Academic cases
*************************
.. toctree::
   :maxdepth: 1

   IDEAL/2Drelief/case_description.rst
   IDEAL/3Drelief/case_description.rst
   IDEAL/HYDRO/case_description.rst
   IDEAL/COLD_BUBBLE/case_description.rst

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
