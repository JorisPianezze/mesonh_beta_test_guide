.. _nam_diag_default:

NAM_DIAG - Default
-----------------------------------------------------------------------------

.. csv-table:: NAM_DIAG - default option
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "XDTSTEP", "REAL", "XTSTEP"   
   "CISO", "CHARACTER(LEN=NFILENAMELGTMAX)", "PREVTK"
   "LVAR_RS", "LOGICAL", "TRUE"

* :code:`XDTSTEP` : time step of the DIAG program (one time step is performed). By default time step of the simulation is used (XTSTEP).

* :code:`CISO="PREVTK"` will store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "PABST", "absolute pression [Pa]", "3D"
   "THT", "potential temperature [K]", "3D"
   "POVOT", "potential vorticity [PVU]", "3D"

.. note::

   Other options for CISO are :
   
   * "PR" to store PABST
   * "TK" to store THT
   * "EV" to store POVOT
   * "PRTK" to store PABST + THT
   * "PREV" to store PABST + POVOT
   * "TKEV" to store THT + POVOT   
   
* :code:`LVAR_RS=T` will store following variables :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "UT",  "u-wind speed [m/s]", "3D"
   "VT",  "v-wind speed [m/s]", "3D"
   "WT",  "w-wind speed [m/s]", "3D"
   "RVT", "water vapor mixing ratio [kg/kg]", "3D"

.. tip::

   Add :code:`LWIND_ZM=T` (with :code:`LVAR_RS=T`) in :code:`NAM_DIAG` to store following variables :

   .. csv-table::
      :header: "Name", "Meaning [Unit]", "Dimension"
      :widths: 30, 30, 30
   
      "UT_ZM", "zonal wind speed [m/s]", "3D"
      "VT_ZM", "meridian wind speed [m/s]", "3D"

The numerous following namelists can be added to :code:`NAM_DIAG` namelist :

* :ref:`nam_diag_general`
