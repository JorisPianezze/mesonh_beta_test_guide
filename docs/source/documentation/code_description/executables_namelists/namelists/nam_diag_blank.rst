.. _nam_diag_blank:

NAM_DIAG_BLANK
-----------------------------------------------------------------------------

.. csv-table:: NAM_DIAG_BLANK content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XDUMMY_DIAG","array(real)","20* 0."
   "NDUMMY_DIAG","array(integer)","20* 0"
   "LDUMMY_DIAG","array(logical)","20* TRUE"
   "CDUMMY_DIAG","array(80 characters)","20* ''"

.. note::

   Similar use than :ref:`nam_blankn`. Add :file:`USE MODD_DIAG_BLANK` in a :ref:`diag` subroutine to use any of these variables.
