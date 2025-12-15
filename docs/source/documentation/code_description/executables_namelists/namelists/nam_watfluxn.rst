.. _nam_watfluxn:

NAM_WATFLUXn
----------------------------------------------------------------------------- 

.. warning::

   This namelist comes from SURFEX 9.0.0 user guide https://www.umr-cnrm.fr/surfex/IMG/pdf/surfex_tecdoc.pdf.

.. csv-table:: NAM_WATFLUXn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
 
   "CINTERPOL_TS", "CHARACTER(LEN=6)", "'NONE'"
   "CWAT_ALB", "CHARACTER(LEN=4)", "'UNIF'" 

* :code:`CWAT_ALB` : type of formulation used to set albedo over water

* :code:`CINTERPOL_TS` : interpolate monthly TS to daily TS

  * 'LINEAR' : Linear interpolation between 3 months.Current value is reached evry 16 of each month, except in February every 15.
  * 'UNIF' : uniform TS
  * 'QUADRA' : quadractic interpolation between 3 months, especially relevant to conserv the TS monthly mean value.
