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

