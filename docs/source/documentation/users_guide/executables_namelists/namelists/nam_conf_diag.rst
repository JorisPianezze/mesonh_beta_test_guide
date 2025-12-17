.. _nam_conf_diag:

NAM_CONF_DIAG
-----------------------------------------------------------------------------

.. csv-table:: NAM_CONF_DIAG content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "NHALO","INTEGER","1"
   "JPHEXT","INTEGER","1"

* :code:`NHALO` : Size of the halo for parallel distribution. This variable is related to computer performance but has no impact on simulation results.

* :code:`JPHEXT` : Horizontal External points number JPHEXT must be equal to 3 for cyclic cases with WENO5.
