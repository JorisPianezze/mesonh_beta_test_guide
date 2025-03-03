PREP_SURFEX
*****************************************************************************

PREP_SURFEX performs the interpolations of surface fields from one grid to another.
What’s going in and out?
• Input:
– a file containing the surface 2D variable fields (hereafter called input file); it can be
either
∗ a GRIB file obtained from extractecmwf or extractarpege
∗ a MESO-NH file (obtained with SPAWNING for example)
– a physiographic data file (it can also be a complete MESO-NH file).
– the file PRE_REAL1.nam which contains the directives for PREP_SURFEX
• Output:
– the FM-file containing the physiographic and pronostic surface fields.

