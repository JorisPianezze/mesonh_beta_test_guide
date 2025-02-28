Executables & Namelists
=============================================================================

In the following subsection, you can find the list of compiled executables and its corresponding namelists.

PREP_PGD
*****************************************************************************

PREP_PGD program is used to create the horizontal grid file for some realistic Meso-NH applications. This file is called the PGD (for PhysioGraphic Data) file in Meso-NH terminology and it contains :

* the definition of the projection, the horizontal grid extension and resolution ;

* the interpolated physiographic fields (soil cover, orography, ...).

.. tip::

   The number of horizontal points must satisfy certain rules because of the pressure solver. To find out the number of horizontal grid points allowed go to :ref:`get_horizontal_grid_point`.

.. csv-table:: PREP_PGD program and its corresponding namelist and function
   :header: "Executable", "Input namelist file", "Function", "Output"
   :widths: 30, 30, 30, 30

   "PREP_PGD", "PRE_PGD1.nam", "Prepare horizontal grid file", "PGDFILE.{des,nc}"

The following namelists can be used in the :file:`PRE_PGD1.nam` file :

* :ref:`nam_confio`
* :ref:`nam_conf_pgd`
* :ref:`nam_pgdfile`
* :ref:`nam_pgd_grid`
* :ref:`nam_conf_proj`
* :ref:`nam_conf_proj_grid`
* :ref:`nam_inifile_conf_proj`
* :ref:`nam_pgd_schemes`
* :ref:`nam_zs`
* :ref:`nam_zsfilter`
* :ref:`nam_cover`
* :ref:`nam_pgd_arrange_cover`
* :ref:`nam_isba`
* :ref:`nam_seabathy`
* :ref:`nam_dummy_pgd`
* :ref:`nam_ch_emis_pgd`

.. note::

   For additional SURFEX namelists (NAM_CARTESIAN, ...) , please go to SURFEX documentation https://www.umr-cnrm.fr/surfex/IMG/pdf/surfex_tecdoc.pdf.

.. include:: namelists/nam_confio.rst
.. include:: namelists/nam_conf_pgd.rst
.. include:: namelists/nam_pgdfile.rst
.. include:: namelists/nam_pgd_grid.rst
.. include:: namelists/nam_conf_proj.rst
.. include:: namelists/nam_conf_proj_grid.rst
.. include:: namelists/nam_inifile_conf_proj.rst
.. include:: namelists/nam_pgd_schemes.rst
.. include:: namelists/nam_zs.rst
.. include:: namelists/nam_zsfilter.rst
.. include:: namelists/nam_cover.rst
.. include:: namelists/nam_pgd_arrange_cover.rst
.. include:: namelists/nam_isba.rst
.. include:: namelists/nam_seabathy.rst
.. include:: namelists/nam_dummy_pgd.rst
.. include:: namelists/nam_ch_emis_pgd.rst

PREP_NEST_PGD
*****************************************************************************

In order to run models with the gridnesting technique, a condition on the orography must be satisfied. In the following, if file #2 is completely included in (and therefore in interaction during the run with) file #1, file #2 will be called the SON file, and file #1 the DAD file. In the following, the DAD file number must be smaller than any of its SON number. The condition on the orography is: "the mean of orography for a SON file in the domain corresponding to the grid mesh of its DAD file, must be equal to the orography of the DAD file in this mesh". Such a condition is not automatically satisfied when using enhanced orographies. The program PREP_NEST_PGD performs post-treatments on the orographies of up to 8 PGD files that will be used to create initialization files for a gridnested run. It modifies the orography of a DAD from the mean of the orography of its (several) SON(s).

.. csv-table:: PREP_NEST_PGD program and its corresponding namelist and function
   :header: "Executable", "Namelist", "Function"
   :widths: 30, 30, 30

   "PREP_NEST_PGD", "PRE_NEST_PGD1.nam", "Prepare surface file when grid nesting is used"
   
ZOOM_PGD
*****************************************************************************

The previous condition on the orography needed when using the gridnesting technique implies that all the PGD files have to be created (with PREP_PGD and PREP_NEST_PGD programs) before beginning the run. However, the user is not always sure where (and when) to initialize the inner models. To avoid to set exactly the domain of inner models at the PREP_PGD step, one solution is to make PGD file on larger domain and then, zoom it2 on the part of the domain of interest when known with the following program ZOOM_PGD. Then the output PGD file is used as PGD file for the interpolations of atmospheric fields with SPAWNING and PREP_REAL_CASE programs.

.. csv-table:: ZOOM_PGD program and its corresponding namelist and function
   :header: "Executable", "Namelist", "Function"
   :widths: 30, 30, 30

   "ZOOM_PGD", "PRE_ZOOM1.nam", "Zoom on PGD file to make an inner domain at the same resolution"

PREP_IDEAL_CASE
***************************************************************************** 

The "PREP_IDEAL_CASE" program prepares a MESONH file, that contains all the parameters and fields necessary for the execution of the MESONH model. Specifically, the grid parameters, the initial fields and the geophysical fields are included in this file. It is possible using this program to generate idealized fields defined by few parameters. The generated initial conditions are produced analytically, leading to quasi-1D fields or 3D fields or a single profile build with either:

* layers of constant Brunt-Vaisala frequency, shear and humidity

* a Radiosounding and ideal surface fields

* a Radiosounding and real physiographic fields

* a Radiosounding and real and ideal surface fields at the same time

For these latter cases, the initial fields may be hydrostatically or geostrophically balanced or not. For these fields to satisfy the anelastic constraint, a final correction is applied to them. The interaction between the PREP_IDEAL_CASE program and the user is made through the PRE_IDEA1.nam file. The degrees of freedom are collected in a set of namelists, read by this program.

.. csv-table:: PREP_IDEAL_CASE program and its corresponding namelist and function
   :header: "Executable", "Namelist", "Function"
   :widths: 30, 30, 30

   "PREP_IDEAL_CASE", "PRE_IDEA1.nam", "Prepare atmospheric initial and boundary file"
   
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
69   
   
SPAWNING
***************************************************************************** 

This program performs the horizontal interpolation from one MESO-NH file into another (re-
spectively file 1 and file 2). The grid of the file 2 must be exactly included in the grid of file 1.
The file 2 can be directly used for a model run, but it contains smooth surface fields (especially
the orography). It is possible to run the model with the two files with gridnesting interaction,
since a iterative procedure insures the gridnesting condition on the orographies.
The domain of the file 2 can be defined either:
1. by namelist NAM_GRID2_SPA specification.
2. with the domain of another FM file, which grid is coherent with the input file. For example
this file can be a PGD file created by PREP_PGD with a domain defined from the domain
of file 1 and the same type of specifications as those in NAM_GRID2_SPA (see above)

.. csv-table:: SPAWNING program and its corresponding namelist and function
   :header: "Executable", "Namelist", "Function"
   :widths: 30, 30, 30

   "SPAWNING", "SPAWN1.nam", "Horizontal interpolations from a Meso-NH file
into another Meso-NH file, with a finer resolution and smaller domain."

MESONH
***************************************************************************** 

The MESONH user will specify some free parameters of the run by fixing their new values in
the NAMELISTs of the file EXSEG$n.nam.
When more than one model is present, each model needs its own MESONH file to be
initialized and its own EXSEG$n.nam file to fix the free-parameters (note that a lot of physical
free-parameters depends on the mesh and therefore vary with the model number).
The input files are read by the program in order to realize the initialization and the eventual
coupling of the MESONH model with a large-scale model ( CEP, Arpège. . . ).
The output files are of two types:
• synchronous files for a given instant of the run. They contain the prognostic fields and
eventually, additional records for supplementary diagnostic fields at the same instant. The
file name ends by 00n with n>0
• a diachronic file for the temporal series of prognostic or diagnostic fields. The file name
ends by 000

.. csv-table:: MESONH program and its corresponding namelist and function
   :header: "Executable", "Namelist", "Function"
   :widths: 30, 30, 30

   "MESONH", "EXSEG1.nam", "Launch simulation"

DIAG
***************************************************************************** 

After running the model, useful quantities can be diagnosed from prognostic variables contained in the synchronous backup files. It is done by the program :file:`DIAG` which computes diagnostic variables.

.. csv-table:: DIAG program and its corresponding namelist and function
   :header: "Executable", "Namelist", "Function"
   :widths: 30, 30, 30

   "DIAG", "DIAG1.nam", "Compute diagnostics after simulation"

SPECTRE
***************************************************************************** 

After running the model, you can compute spectra with the program SPECTRE, that gives the
kinetic energy density according to the wavelength or the wave number (see Ricard et al., 2011).
The calculation uses a discrete cosinus transform to convert grid-point fields into spectral space
ones.

.. csv-table:: SPECTRE program and its corresponding namelist and function
   :header: "Executable", "Namelist", "Function"
   :widths: 30, 30, 30

   "SPECTRE", "SPEC1.nam", "Compute spectra after simulation"

LATLON
***************************************************************************** 

LFI2CDF
***************************************************************************** 

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

MNH2LPDM
***************************************************************************** 



