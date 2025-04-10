.. _nam_coupling_levelsn:

NAM_COUPLING_LEVELSn
-----------------------------------------------------------------------------

This namelist allows to specify the number of atmospheric levels (NLEV_COUPLE) for which the meteorological forcing data is sent to SURFEX. A value of 1 for NLEV_COUPLE corresponds to the standard use of SURFEX; only the lowest atmospheric level is coupled. A value higher than 1 implies multi-layer coupling and is currently only used by the Town Energy Balance TEB, as described in Schoetter et al. (2020, GMD).

In the case a value of NLEV_COUPLE greater than 1 is used, the model user must ensure that the height above ground level of the highest model level is larger than the height of the highest building in the domain. Furthermore, the drag force, heat, and moisture fluxes from buildings should be activated in :ref:`nam_dragbldgn`.

.. csv-table:: NAM_COUPLING_LEVELSn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "NLEV_COUPLE", "INTEGER", "1"

* :code:`NLEV_COUPLE` : The number of atmospheric levels sent to SURFEX.
