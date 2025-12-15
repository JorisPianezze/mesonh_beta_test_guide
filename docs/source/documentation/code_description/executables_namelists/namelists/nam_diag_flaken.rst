.. _nam_diag_flaken:

NAM_DIAG_FLAKEN
-----------------------------------------------------------------------------

.. warning::

   This namelist comes from SURFEX 9.0.0 user guide https://www.umr-cnrm.fr/surfex/IMG/pdf/surfex_tecdoc.pdf.

.. csv-table:: NAM_DIAG_FLAKEN content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LWATER_PROFILE", "LOGICAL", ".FALSE."
   "XZWAT_PROFILE", "REAL", ""

* :code:`LWATER_PROFILE` : flag to save in the output file miscelleaneous fields. The diagnostic is temperature at the depths defined by:

* :code:`XZWAT_PROFILE` : depth of output levels (m) in namelist
