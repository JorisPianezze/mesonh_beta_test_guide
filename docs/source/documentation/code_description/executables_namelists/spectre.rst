SPECTRE
***************************************************************************** 

After running the model, you can compute spectra with the program SPECTRE, that gives the kinetic energy density according to the wavelength or the wave number :cite:p:`ricard_kinetic_2013`. The calculation uses a discrete cosinus transform to convert grid-point fields into spectral space ones.

.. csv-table:: SPECTRE program and its corresponding namelist and function
   :header: "Executable", "Namelist", "Function"
   :widths: 30, 30, 30

   "SPECTRE", "SPEC1.nam", "Compute spectra after simulation"

The following namelists can be used in the :file:`SPEC1.nam` file :

* :ref:`nam_spectre_file`
* :ref:`nam_spectre`
* :ref:`nam_zoom_spectre`
* :ref:`nam_domain_arome`

.. include:: namelists/nam_spectre_file.rst
.. include:: namelists/nam_spectre.rst
.. include:: namelists/nam_zoom_spectre.rst
.. include:: namelists/nam_domain_arome.rst
