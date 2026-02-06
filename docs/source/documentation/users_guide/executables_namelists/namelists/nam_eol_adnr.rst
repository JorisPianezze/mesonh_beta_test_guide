.. _nam_eol_adnr:

NAM_EOL_ADNR
-----------------------------------------------------------------------------

If the user wants to simulate two wind farms built with two different types of wind turbines, the user can set two Meso-NH son models using two CSV data files.

.. csv-table:: NAM_EOL_ADNR content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CFARM_CSVDATA","CHARACTER(LEN=128)","'data_farm.csv'"
   "CTURBINE_CSVDATA","CHARACTER(LEN=128)","'data_turbine.csv'"
   "CINTERP","CHARACTER(LEN=3)","'CLS'"

* :code:`CFARM_CSVDATA` : name of the CSV data file containing the description of the wind farm. The file must contain a header and one row of data per wind turbine. The name of the variables in the header can be modified by the user since it is not read by the program. The delimiters of the file are commas. The data and the column order of this file are: 

  * x-axis position [m] of the base of the tower (ideal conditions only),
  * y-axis position [m] of the base of the tower (ideal conditions only),
  * thrust coefficient [-] of the rotor, defined with the infinite upstream velocity (see scientific documentation for details).

.. note::

   Note that the ANDR operates only when the disk is normal to the x-direction, facing the upstream wind. An example for two wind turbines is given below:
   .. code-block::
   
      X [m], Y [m], Ct_inf [-]
      1000, 600, 0.8
      2500, 600, 0.6

* :code:`CTURBINE_CSVDATA` : name of the CSV data file containing the description of the wind turbine. The file must contain a header and one row of data, as only one type of wind turbine can be simulated in a Meso-NH model (or sub-model). The name of the variables in the header can be modified by the user since it is not read by the program. The delimiters of the file are commas. The data and the column order of this file are: 

  * name of the wind turbine [-] (not used by the code, useful for the user),
  * hub height [m],
  * radius of the rotor [m].

.. note::

   One can note that the hub radius, the deport and the tilt are not taken into account with this model. An example for a DTU\_10MW rotor is given below:

   .. code-block::
   
      Turbine name, Hub height [m], Rotor radius [m]
      DTU_10MW, 119,  89.15

* :code:`CINTERP` : method of interpolation of wind conditions at disc position:

  * `CLS' closest cell value (no interpolation).
  * `8NB' eigth neighbourhood interpolation.
