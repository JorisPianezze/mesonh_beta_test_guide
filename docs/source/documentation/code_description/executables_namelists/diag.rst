.. _diag:

DIAG
***************************************************************************** 

After running the model, useful quantities can be diagnosed from prognostic variables contained in the synchronous backup files. It is done by the program :file:`DIAG` which computes diagnostic variables.

.. csv-table:: DIAG program and its corresponding namelist and function
   :header: "Executable", "Namelist", "Function", "Output"
   :widths: 30, 30, 30, 30

   "DIAG", "DIAG1.nam", "Compute diagnostics after simulation", "DIAGFILE.{des,nc}"
   
The following namelists can be used in the :file:`DIAG1.nam` file :

* :ref:`nam_confio`
* :ref:`nam_diag_default`
* :ref:`nam_diag_general`
* :ref:`nam_diag_deep_convection`
* :ref:`nam_diag_shallow_convection`
* :ref:`nam_diag_microphysics`
* :ref:`nam_diag_turbulence`
* :ref:`nam_diag_radiation`
* :ref:`nam_diag_aerosols`
* :ref:`nam_diag_chemistry`
* :ref:`nam_diag_lightnings`
* :ref:`nam_diag_lagrangian_tracers`
* :ref:`nam_diag_gps_simulator`
* :ref:`nam_diag_satellite_simulator`
* :ref:`nam_diag_radar_simulator`
* :ref:`nam_diag_lidar_simulator`
* :ref:`nam_diag_interpolation`
* :ref:`nam_diag_clustering`
* :ref:`nam_diag_coarse_graining`
* :ref:`nam_diag_blank`
* :ref:`nam_diag_file`
* :ref:`nam_sto_file`
* :ref:`nam_conf_diag`
* :ref:`nam_param_kafrn`
* :ref:`nam_param_radn`
* :ref:`nam_diag_surf_atmn`
* :ref:`nam_write_diag_surfn`
* :ref:`nam_diag_surfn`
* :ref:`nam_diag_isban`
* :ref:`nam_diag_tebn`
* :ref:`nam_diag_flaken`
* :ref:`nam_diag_oceann`

.. note::

   For additional SURFEX namelists, please go to SURFEX documentation https://www.umr-cnrm.fr/surfex/IMG/pdf/surfex_tecdoc.pdf.

.. include:: namelists/nam_confio.rst
.. include:: namelists/nam_diag_default.rst
.. include:: namelists/nam_diag_general.rst
.. include:: namelists/nam_diag_deep_convection.rst
.. include:: namelists/nam_diag_shallow_convection.rst
.. include:: namelists/nam_diag_microphysics.rst
.. include:: namelists/nam_diag_turbulence.rst
.. include:: namelists/nam_diag_radiation.rst
.. include:: namelists/nam_diag_aerosols.rst
.. include:: namelists/nam_diag_chemistry.rst
.. include:: namelists/nam_diag_lightnings.rst
.. include:: namelists/nam_diag_lagrangian_tracers.rst
.. include:: namelists/nam_diag_gps_simulator.rst
.. include:: namelists/nam_diag_satellite_simulator.rst
.. include:: namelists/nam_diag_radar_simulator.rst
.. include:: namelists/nam_diag_lidar_simulator.rst
.. include:: namelists/nam_diag_interpolation.rst
.. include:: namelists/nam_diag_clustering.rst
.. include:: namelists/nam_diag_coarse_graining.rst
.. include:: namelists/nam_diag_blank.rst
.. include:: namelists/nam_diag_file.rst
.. include:: namelists/nam_sto_file.rst
.. include:: namelists/nam_conf_diag.rst
.. include:: namelists/nam_param_kafrn.rst
.. include:: namelists/nam_param_radn.rst
.. include:: namelists/nam_diag_surf_atmn.rst
.. include:: namelists/nam_write_diag_surfn.rst
.. include:: namelists/nam_diag_surfn.rst
.. include:: namelists/nam_diag_isba.rst`
.. include:: namelists/nam_diag_tebn.rst
.. include:: namelists/nam_diag_flaken.rst
.. include:: namelists/nam_diag_oceann.rst
