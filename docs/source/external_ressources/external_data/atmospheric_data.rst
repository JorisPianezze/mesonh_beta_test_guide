.. _atmospheric_data:

Initialization of atmospheric and surface data
================================================

* decrire les donnees atmospheriques et de surface :
  * 3d atmospheric data (u, v, t, q, lnsp, z, ...) --> initialisation atmosphere + surface, forçage aux CLL + nudging si souhaité
  * source : GFS, ERA5, ECMWF oper, AROME, ARPEGE avec les liens

* champs atmosphériques pour la chimie :
  * CAMS

.. toctree::
   :maxdepth: 2

   extract_ecmwf_data/extract_ecmwf_data.rst
   extract_meteofrance_data/extract_meteofrance_data.rst
   extract_gfs_data/extract_gfs_data.rst
   extract_hrrr_data/extract_hrrr_data.rst
   extract_icon_data/extract_icon_data.rst
   extract_cams_data/extract_cams_data.rst
