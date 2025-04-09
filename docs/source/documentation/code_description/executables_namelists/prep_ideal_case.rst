PREP_IDEAL_CASE
***************************************************************************** 

The :program:`PREP_IDEAL_CASE` program prepares a Meso-NH file, that contains all the parameters and fields necessary for the execution of the Meso-NH model. Specifically, the grid parameters, the initial fields and the geophysical fields are included in this file. It is possible using this program to generate idealized fields defined by few parameters. The generated initial conditions are produced analytically, leading to quasi-1D fields or 3D fields or a single profile build with either:

* layers of constant Brunt-Vaisala frequency, shear and humidity

* a Radiosounding and ideal surface fields

* a Radiosounding and real physiographic fields

* a Radiosounding and real and ideal surface fields at the same time

For these latter cases, the initial fields may be hydrostatically or geostrophically balanced or not. For these fields to satisfy the anelastic constraint, a final correction is applied to them. The interaction between the :program:`PREP_IDEAL_CASE` program and the user is made through the :file:`PRE_IDEA1.nam` file. The degrees of freedom are collected in a set of namelists, read by this program.

.. csv-table:: PREP_IDEAL_CASE program and its corresponding namelist and function
   :header: "Executable", "Namelist", "Function"
   :widths: 30, 30, 30

   "PREP_IDEAL_CASE", "PRE_IDEA1.nam", "Prepare atmospheric initial and boundary file"

Contrary to other namelist :file:`PRE_IDEA1.nam` is made of two parts :

*  A namelist-part with directives for the preparation of an idealized case (always present). The order of namelists is free and unset namelists can be ommited.

*  A free-formatted part describing a vertical profile of n layers of constant moist Brunt-Vaisala frequency or a radiosounding and sometimes the explicit list of the heights of the vertical levels. This part can be present or absent in the other cases.

To initialize a simulation with a radiosounding and real terrain conditions, it is necessary to perform the PREP_PGD program to create a Meso-NH physiographic data file. This data file contains the orography and the physiographic data fields (related to the soil scheme). It is also possible to perform a complete ideal case with ideal orography and non trivial surface conditions. The user can combine the two possibilities with flags included in the namelist NAM_REAL_PGD and initialize a simulation with a real orography and idealized homogeneous surface fields. If a PGD file is specified and if the flags in namelist NAM_REAL_PGD are set to FALSE, homogeneous values can be imposed by the user in namelists from the externalized surface facility PGD (namelists NAM_COVER and NAM_ISBA), else the PREP_PGD fields are taken into account.

The following namelists can be used in the :file:`PRE_IDEA1.nam` file :

* :ref:`nam_confio`
* :ref:`nam_aero_pre`
* :ref:`nam_blankn`
* :ref:`nam_ch_mnhcn_pre`
* :ref:`nam_conf_pre`
* :ref:`nam_confn`
* :ref:`nam_confz`
* :ref:`nam_dimn_pre`
* :ref:`nam_dynn_pre`
* :ref:`nam_grid_pre`
* :ref:`nam_gridh_pre`
* :ref:`nam_grn_pre`
* :ref:`nam_ibm_lsf`
* :ref:`ibm_idea`
* :ref:`ibm_gene`
* :ref:`nam_lbcn_pre`
* :ref:`nam_lunitn`
* :ref:`nam_pert_pre`
* :ref:`nam_real_pgd`
* :ref:`nam_sleve`
* :ref:`nam_ver_grid`
* :ref:`nam_vprof_pre`
* :ref:`nam_pgd_schemes`
* :ref:`nam_cover`
* :ref:`nam_isba`
* :ref:`nam_ch_emis_pgd`
* :ref:`nam_dummy_pgd`
* :ref:`nam_prep_surf_atm`
* :ref:`nam_prep_seaflux`
* :ref:`nam_prep_watflux`
* :ref:`nam_prep_teb`
* :ref:`nam_prep_isba`
* :ref:`freeformat_prep_ideal_case`

.. include:: namelists/nam_confio.rst
.. include:: namelists/nam_aero_pre.rst
.. include:: namelists/nam_blankn.rst
.. include:: namelists/nam_ch_mnhcn_pre.rst
.. include:: namelists/nam_conf_pre.rst
.. include:: namelists/nam_confn.rst
.. include:: namelists/nam_confz.rst
.. include:: namelists/nam_dimn_pre.rst
.. include:: namelists/nam_dynn_pre.rst
.. include:: namelists/nam_grid_pre.rst
.. include:: namelists/nam_gridh_pre.rst
.. include:: namelists/nam_grn_pre.rst
.. include:: namelists/nam_ibm_lsf.rst
.. include:: namelists/ibm_idea.rst
.. include:: namelists/ibm_gene.rst
.. include:: namelists/nam_lbcn_pre.rst
.. include:: namelists/nam_lunitn.rst
.. include:: namelists/nam_pert_pre.rst
.. include:: namelists/nam_real_pgd.rst
.. include:: namelists/nam_sleve.rst
.. include:: namelists/nam_ver_grid.rst
.. include:: namelists/nam_vprof_pre.rst
.. include:: namelists/nam_pgd_schemes.rst
.. include:: namelists/nam_cover.rst
.. include:: namelists/nam_isba.rst
.. include:: namelists/nam_ch_emis_pgd.rst
.. include:: namelists/nam_dummy_pgd.rst
.. include:: namelists/nam_prep_surf_atm.rst
.. include:: namelists/nam_prep_seaflux.rst
.. include:: namelists/nam_prep_watflux.rst
.. include:: namelists/nam_prep_teb.rst
.. include:: namelists/nam_prep_isba.rst
.. include:: namelists/freeformat_prep_ideal_case.rst
