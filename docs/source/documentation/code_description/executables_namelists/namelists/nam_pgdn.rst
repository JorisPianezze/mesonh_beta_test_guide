.. _nam_pgdn:

NAM_PGDN
-----------------------------------------------------------------------------

.. warning::

   This namelist comes from SURFEX 9.0.0 user guide https://www.umr-cnrm.fr/surfex/IMG/pdf/surfex_tecdoc.pdf.

.. csv-table:: NAM_PGDN content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "YPGDN", "CHARACTER(LEN=128)", ""
   "IDAD", "INTEGER", "0"

* :code:`YPGDN` : name of the PGD file N.

* :code:`IDAD` : number of the DAD file of file N. The DAD file number IDAD must be smaller than N.

.. note::

   N goes from 1 to 8, by example :
   
   .. code-block:: fortran
   
      &NAM_PGD1 YPGD1='PGDFILE1' /
      &NAM_PGD2 YPGD2='PGDFILE2', IDAD=1 /
