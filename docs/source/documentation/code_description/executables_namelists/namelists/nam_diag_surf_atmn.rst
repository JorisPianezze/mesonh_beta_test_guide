.. _nam_diag_surf_atmn:

NAM_DIAG_SURF_ATMN
-----------------------------------------------------------------------------

Diagnostics relative to each grid cell.

.. csv-table:: NAM_DIAG_SURF_ATMN content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LFRAC", "LOGICAL", ".FALSE."
   "LDIAG_GRID", "LOGICAL", ".FALSE."
   "LT2MMW", "LOGICAL", ".FALSE."
   "LDIAG_MIP", "LOGICAL", ".FALSE."
   
* :code:`LFRAC` : flag to save in the output file the sea, inland water, natural covers and town fractions.

* :code:`LDIAG_GRID` : flag for mean grid diagnostics

* :code:`LT2MMW` : gAlternative weighting of grid average T2M giving more weight to the land tile.

* :code:`LDIAG_MIP` : flag to perform intercomparison of land surface model diagnostics as required by several MIP (such as CMIP, SnowMIP, GCP, GSWP, etc.). These diag are only implemented for general surf_atm diags, seaflux, Flake and ISBA. Note that when this key is activated, the following namelist are not used: NAM_DIAG_SURF_ATMn, NAM_DIAG_SURFn, NAM_DIAG_ISBAn.
