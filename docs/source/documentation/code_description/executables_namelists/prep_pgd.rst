.. _prep_pgd:

PREP_PGD
*****************************************************************************

:program:`PREP_PGD` program is used to create the horizontal grid file for some realistic Meso-NH applications. This file is called the PGD (for PhysioGraphic Data) file in Meso-NH terminology and it contains :

* the definition of the projection, the horizontal grid extension and resolution ;

* the interpolated physiographic fields (soil cover, orography, ...).

.. tip::

   The number of horizontal points must satisfy certain rules because of the pressure solver. To find out the number of horizontal grid points allowed go to :ref:`get_horizontal_grid_point`.

.. csv-table:: PREP_PGD program and its corresponding namelist and function
   :header: "Executable", "Input namelist file", "Function", "Output"
   :widths: 30, 30, 30, 30

   "PREP_PGD", "PRE_PGD1.nam", "Create horizontal grid file", "PGDFILE.{des,nc}"

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

   For additional SURFEX namelists (:code:`NAM_CARTESIAN`, ...) , please go to SURFEX documentation https://www.umr-cnrm.fr/surfex/IMG/pdf/surfex_tecdoc.pdf.

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
