.. _nam_series:

NAM_SERIES
----------------------------------------------------------------------------- 

.. csv-table:: NAM_SERIES content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LSERIES","LOGICAL",".FALSE."
   "LMASKLANDSEA","LOGICAL",".FALSE."
   "LWMINMAX","LOGICAL",".FALSE."
   "LSURF","LOGICAL",".FALSE."

* :code:`LSERIES` : flag to write temporal series in the diachronic file (.000) of each model:

  * evolution of horizontally and vertically averaged fields (t), 
  * evolution of horizontally averaged vertical profiles (z,t), 
  * evolution of y-horizontally averaged fields at one level or vertically averaged between 2 levels (x,t). 

* :code:`LMASKLANDSEA` :  flag to separate sea and land points in temporal series (t) and (z,t),

* :code:`LWMINMAX` : flag to compute minimum and maximum of vertical velocity W in temporal serie (t).

* :code:`LSURF` : flag to compute temporal series on surface fields. You have to introduce in the code the surface fields you want  : 

  * In :file:`get_seriesn.f90` of SURFEX : put the requested fields in ZINF. In the example of the current version XTS, XT_MNW,XT_BOT, XCT, XH_ML from :file:`modd_flaken.f90` are requested.
  * In :file:`get_surf_varn.f90` of SURFEX : adjust the tile necessary to be present (in the example PWATER is required)
  * In :file:`ini_seriesn.f90` of Meso-NH : put the number of requested fields  : ex: for 5 fields, NSTEMP_SERIE1 = NSTEMP_SERIE1 +5 and give the tittle of each field
  * In :file:`seriesn.f90` of Meso-NH : give the tittle of each field

.. note::

   See also the namelist :ref:`nam_seriesn`.

   Some examples of temporal series are available which treat pronostic fields averaged or not vertically. For other fields (for example diagnostic fields such as relative humidity), the following Fortran routines must be modified:

   * :file:`ini_series.f90` for initialization of size and name of diachronic records,
   * :file:`seriesn.f90` to store and possibly vertically average values during the run,
   * :file:`write\_seriesn.f90` to horizontally average and write series in diachronic file.

