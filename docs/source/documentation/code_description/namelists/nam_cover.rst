.. _nam_cover:

NAM_COVER
-----------------------------------------------------------------------------

This namelist gives the information to compute the surface cover fractions when ECOCLIMAP is used. It is possible to use an existing ECOCLIMAP map or the define the ECOCLIMAP covers for the user's domain.

.. csv-table:: NAM_COVER content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XUNIF_COVER", "real", "none"
   "YCOVER", "character(LEN=28)", ""
   "YCOVERFILETYPE", "character(LEN=6)", "none"
   "XRM_COVER", "real", "10−6"
   "XRM_COAST", "real", "1."
   "XRM_LAKE", "real", "0."
   "XRM_SEA", "real", "0."
   "LORCA_GRID", "logical", "F"
   "XLAT_ANT", "real", "-77."
   "LIMP_COVER", "logical", "F"
   "LRM_RIVER", "logical", "F"

* XUNIF_COVER: specified values for uniform cover fractions. For each index i between 1 and 573, XUNIF_COVER(i) is the fraction of the ith ecosystem of ecoclimap. The same fraction of each ecosystem is set to all points of the grid. The sum of all ecosystem fractions must be equal to one. If XUNIF_COVER is set, it has priority on the use of an ecosystem file (see next item: YCOVER). In the case of grid without any reference to geographical coordinates ("CARTESIAN " or "NONE "), XUNIF_COVER must be set.

* YCOVER: ecoclimap data file name. It is used only if XUNIF_COVER is not set.

* YCOVERFILETYPE: type of YCOVER file ('DIRECT', 'BINLLV', 'BINLLF', 'ASCLLV').

* XRM_COVER: for each point, all fractions of ecosystems that are below XRM_COVER are removed (i.e. set to zero), and the corresponding area fractions are distributed among the remaining ecosystem fractions. Whatever the value of XRM_COVER, at least one ecosystem remains for each grid point.

* XRM_COAST: limit of coast coverage under which the coast is replaced by sea or inland water.

* XRM_LAKE: limit of inland lake coverage under which the water is removed.

* XRM_SEA: limit of sea coverage under which the sea is removed.

* LORCA_GRID: flag to ensure the compatibility between surfex and Orca grid which minimal latitude over Antarctica is 77S

* XLAT_ANT: minimum Orca grid latitude over Antarctica

* LIMP_COVER: reads the cover fractions in an existing PGD file to avoid their computation

* LRM_RIVER: if T, rivers (cover 3) are removed
