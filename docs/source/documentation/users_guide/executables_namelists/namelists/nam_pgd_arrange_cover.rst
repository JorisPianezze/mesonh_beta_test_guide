.. _nam_pgd_arrange_cover:

NAM_PGD_ARRANGE_COVER
-----------------------------------------------------------------------------

.. warning::

   This namelist comes from SURFEX 9.0.0 user guide https://www.umr-cnrm.fr/surfex/IMG/pdf/surfex_tecdoc.pdf.

This namelist initializes change water (not lake) to nature and/or town to rock keys.

.. csv-table:: NAM_PGD_ARRANGE_COVER content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LWATER_TO_NATURE", "LOGICAL", ".FALSE."
   "LTOWN_TO_ROCK", "LOGICAL", ".FALSE."
   "LTOWN_TO_COVER", "LOGICAL", ".FALSE."
   "NREPLACE_COVER", "INTEGER", ""

* :code:`LWATER_TO_NATURE` : Change Wetland treated as inland water into nature, i.e. covers with 0. :math:`\leq` FRAC_WATER :math:`\leq` 1.

* :code:`LTOWN_TO_ROCK` : Change Town into Rock

* :code:`LTOWN_TO_COVER` : Option to replace (if T) urban landuse by the ecoclimap cover ICOVER

* :code:`NREPLACE_COVER` : cover number to replace urban by this cover. If LTOWN_TO_COVER=T and NREPLACE=ICOVER, the urban landuse is replaced by the ECOCLIMAP cover number ICOVER (ICOVER must be present in the domain)
