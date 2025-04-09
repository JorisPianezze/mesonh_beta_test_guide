.. _prep_real_case:

PREP_REAL_CASE
***************************************************************************** 

:program:`PREP_REAL_CASE` program performs the change of orography and vertical grid by interpolating horizontally and vertically for a GRIB file or only vertically for a Meso-NH file. The Meso-NH output file will be used either for the beginning of the simulation or for coupling. The main hypothesis is that hydrostatism is verified. Therefore, if the input file is a Meso-NH file, there is a small loss of information.

.. csv-table:: PREP_REAL_CASE program and its corresponding namelist and function
   :header: "Executable", "Namelist", "Function"
   :widths: 30, 30, 30

   "PREP_REAL_CASE", "PRE_REAL1.nam", "Prepare atmospheric initial and boundary file"
   
The following namelists can be used in the :file:`PRE_REAL1.nam` file :

* :ref:`nam_aero_conf`
* :ref:`nam_blankn`
* :ref:`nam_ch_conf`
* :ref:`nam_confio`
* :ref:`nam_confz`
* :ref:`nam_file_names`
* :ref:`nam_hurr_conf`
* :ref:`nam_ibm_lsf`
* :ref:`ibm_idea`
* :ref:`nam_real_conf`
* :ref:`nam_ver_grid`
* :ref:`nam_prep_surf_atm`
* :ref:`nam_prep_seaflux`
* :ref:`nam_prep_watflux`
* :ref:`nam_prep_flake`
* :ref:`nam_prep_isba`
* :ref:`nam_prep_teb`
* :ref:`freeformat_prep_real_case`
* :ref:`read_extra_arome_variables`
 
.. include:: namelists/nam_aero_conf.rst
.. include:: namelists/nam_blankn.rst
.. include:: namelists/nam_ch_conf.rst
.. include:: namelists/nam_confio.rst
.. include:: namelists/nam_confz.rst
.. include:: namelists/nam_file_names.rst
.. include:: namelists/nam_hurr_conf.rst
.. include:: namelists/nam_ibm_lsf.rst
.. include:: namelists/ibm_idea.rst
.. include:: namelists/nam_real_conf.rst
.. include:: namelists/nam_ver_grid.rst
.. include:: namelists/nam_prep_surf_atm.rst
.. include:: namelists/nam_prep_seaflux.rst
.. include:: namelists/nam_prep_watflux.rst
.. include:: namelists/nam_prep_flake.rst
.. include:: namelists/nam_prep_isba.rst
.. include:: namelists/nam_prep_teb.rst
.. include:: namelists/freeformat_prep_real_case.rst
.. include:: namelists/read_extra_arome_variables.rst
