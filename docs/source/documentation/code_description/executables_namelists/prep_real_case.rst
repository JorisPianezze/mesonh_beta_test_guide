PREP_REAL_CASE
***************************************************************************** 

PREP_REAL_CASE program performs the change of orography and vertical grid by inter-
polating horizontally and vertically for a GRIB file or only vertically for a MESO-NH file. The
MESO-NH output file will be used either for the beginning of the simulation or for coupling.
The main hypothesis is that hydrostatism is verified. Therefore, if the input file is a MESO-NH
file, there is a small loss of information.

.. csv-table:: PREP_REAL_CASE program and its corresponding namelist and function
   :header: "Executable", "Namelist", "Function"
   :widths: 30, 30, 30

   "PREP_REAL_CASE", "PRE_REAL1.nam", "Prepare atmospheric initial and boundary file"
   
What’s going in and out?
• Input:
– a file containing the atmospheric 3D and surface 2D variable fields (hereafter called
atmospheric file); it can be either
∗ a GRIB file (from AROME, ARPEGE, IFS, GFS or ERA5) obtained from ex-
tractecmwf or extractarpege
∗ or a MESO-NH file (obtained with SPAWNING for example)
In the first case, both horizontal and vertical interpolations are carried utn by the
PREP_REAL_CASE. In the second case, only vertical interpolation is carried on by
PREP_REAL_CASE as the horizontal interpolation is already done by the spwaning
(see chapter 7)
– a physiographic data file (it can also be a complete MESO-NH file).
– an optional file containing the chemical species (here after called chemical file); it is
used only if the atmospheric file is a GRIB file. It can be either
∗ a GRIB file (e.g. a file from the MOCAGE french model)
∗ or a MESO-NH file (obtained in a previous simulation for example)
