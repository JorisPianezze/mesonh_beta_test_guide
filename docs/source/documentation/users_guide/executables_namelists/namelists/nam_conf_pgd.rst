.. _nam_conf_pgd:

NAM_CONF_PGD
-----------------------------------------------------------------------------

.. warning::

   This namelist comes from SURFEX 9.0.0 user guide https://www.umr-cnrm.fr/surfex/IMG/pdf/surfex_tecdoc.pdf.

.. csv-table:: NAM_CONF_PGD content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "NHALO_MNH", "INTEGER", "1"
   "JPHEXT", "INTEGER", "1"   

* :code:`NHALO_MNH` : Size of the halo for parallel distribution. This variable is related to computer performance but has no impact on simulation results.

* :code:`JPHEXT` : Horizontal External points number. JPHEXT must be equal to 3 for cyclic cases with WENO5.
