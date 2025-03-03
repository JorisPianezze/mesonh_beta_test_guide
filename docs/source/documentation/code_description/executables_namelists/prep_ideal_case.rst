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

