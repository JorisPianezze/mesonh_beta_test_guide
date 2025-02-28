.. _nam_pgd_arrange_cover:

NAM_PGD_ARRANGE_COVER
-----------------------------------------------------------------------------

This namelist initializes change water (not lake) to nature and/or town to rock keys.

.. csv-table:: NAM_PGD_ARRANGE_COVER content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LWATER_TO_NATURE", "logical", "F"
   "LTOWN_TO_ROCK", "logical", "F"
   "LTOWN_TO_COVER", "logical", "F"
   "NREPLACE_COVER", "integer", ""

* LWATER_TO_NATURE: Change Wetland treated as inland water into nature, i.e. covers with 0. ≤ FRAC_WATER ≤ 1.

* LTOWN_TO_ROCK: Change Town into Rock

* LTOWN_TO_COVER: Option to replace (if T) urban landuse by the ecoclimap cover ICOVER

* NREPLACE_COVER: cover number to replace urban by this cover. If LTOWN_TO_COVER=T and NREPLACE=ICOVER, the urban landuse is replaced by the ECOCLIMAP cover number ICOVER (ICOVER must be present in the domain)
