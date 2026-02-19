.. _nam_eol_adr:

NAM_EOL_ADR
-----------------------------------------------------------------------------

.. csv-table:: NAM_EOL_ADR content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CFARM_CSVDATA","CHARACTER(LEN=128)","'data_farm.csv'"
   "CTURBINE_CSVDATA","CHARACTER(LEN=128)","'data_turbine.csv'"
   "CBLADE_CSVDATA","CHARACTER(LEN=128)","'data_blade.csv'"
   "CAIRFOIL_CSVDATA","CHARACTER(LEN=128)","'data_airfoil.csv'"
   "CINTERP","CHARACTER(LEN=3)","'CLS'"
   "NNB_AZIELT","INTEGER","56"
   "NNB_RADELT","INTEGER","18"
   "LTIPLOSSG","LOGICAL",".TRUE."
   "LTECOUTPTS","LOGICAL",".FALSE."
   "LCSVOUTFRM","LOGICAL",".FALSE."

* :code:`CFARM_CSVDATA` : name of the CSV data file containing the description of the wind farm. The file must contain a header and one row of data per wind turbine. The name of the variables in the header can be modified by the user since it is not read by the program. The delimiters of the file are commas. The data and the column order of this file are: 

  * x-axis position [m] of the tower base (if LCARTESIAN = .TRUE.), or latitude [deg] (if LCARTESIAN = .FALSE.),
  * y-axis position [m] of the tower base (if LCARTESIAN = .TRUE.), or longitude [deg] (if LCARTESIAN = .FALSE.), 
  * angular velocity [rad/s] of the rotor (trigonometric convention seen from upstream),
  * yaw angle [rad] of the nacelle (:math:`0 \Leftrightarrow` facing an upstream x-axis wind; trigonometric convention seen from the sky),
  * pitch angle [rad] of the blades (:math:`0 \Leftrightarrow` rotor plane ; :math:`-pi/2 \Leftrightarrow` feathering. Trigonometric convention seen from blade tip).

.. note::

   An example of :file:`data_farm.csv` with one wind turbine is given below:

   .. code-block::
   
      X[m]/Lat[deg], Y[m]/Lon[deg], Omega[rad/s], Nac_yaw[rad], Bla_pitch[rad]
      1000, 600, -1.00531, 0.0, -0.07866

If LFLOAT_EOL is activated (only if LCARTESIAN=T.):

   .. code-block::

      X [m], Y [m], Omega [rad/s], N_yaw [rad], B_pitch [rad], Floating Motions file
      1000, 600, -1.00531, 0.0, -0.07866, data_float.csv 

* :code:`CTURBINE_CSVDATA` : name of the CSV data file containing the description of the wind turbine. The file must contain a header and one row of data, as only one type of wind turbine can be simulated in a Meso-NH modelfootnote{If the user wants to simulate two wind farms built with two different types of wind turbines, the user can set two Meso-NH son models using two CSV data files.} (or sub-model). The name of the variables in the header can be modified by the user since it is not read by the program. The delimiters of the file are commas. The data and the column order of this file are: 

  * name of the wind turbine [-] (not used by the code, useful for the user),
  * number of blades [-],
  * hub height [m],
  * radius of blade root (or hub radius) [m],
  * radius of blade tip (or rotor radius) [m],
  * tilt angle [rad] of the nacelle (:math:`0 \Leftrightarrow` facing an upstream x-axis wind; :math:`pi/2 \Leftrightarrow` facing the sky),
  * hub deport [m],
  * tower radius (for computation of tower body forces) [m],
  * nacelle radius (for computation of nacelle body forces) [m].

.. note::

   An example of :file:`data_turbine.csv` for a DTU_10MW rotor is given below:

   .. code-block::
   
      Turbine, Nb b.[-], H_h [m], R_r [m], R_t [m], N_tilt [rad], H_dep. [m], T_r [m], N_r [m]
      DTU10, 3, 119, 2.8, 89.15, 0.0, 7.1, 2.8, 2.8

* :code:`CBLADE_CSVDATA` : name of the CSV data file containing the description of the blade. The file must contain a header and one row of data per blade element centre. The name of the variables in the header can be modified by the user since it is not read by the program. The delimiters of the file are commas. The data and the column order of this file are: 

  * center position [%] along blade length (from root radius to tip) of the element,
  * chord [m] of the element,
  * twist angle [rad] of the element (:math:`0 \Leftrightarrow` rotor plane ; :math:`-pi/2 \Leftrightarrow` feathering. Trigonometric convention seen from blade tip),
  * name of the airfoil [-].

.. note::

   An example of :file:`data_blade.csv` for a blade description rotor is given below:

   .. code-block::

      Center [%], Chord [m], Twist [rad], Airfoil [-] 
      0.03111, 5.37574, -0.25188, Cylinder   
      0.07854, 5.40375, -0.25311, Cylinder   
      0.11164, 5.53313, -0.24859, FFA-W3-600 
      ...                                 
      0.98605, 1.33250, 0.057858, FFA-W3-241 
      0.99527, 0.94924, 0.059291, FFA-W3-241 

* :code:`CAIRFOIL_CSVDATA` : name of the CSV data file containing the descprition of the airfoils. The file must contain a header and tabulated polars for all the airfoils of the blade. For each airfoil, one row of data per angle of attack must be specified. The name of the variables in the header can be modified by the user since it is not read by the program. The delimiters of the file are commas. The data and the column order of this file are: 

   * name of the airfoil [-],
   * angle of attack [deg],
   * Reynolds number [-] (not used by the code, useful for the user),
   * lift coefficient [-],
   * drag coefficient [-]
   * moment coefficient [-] (not used by the code yet).

.. note::

   An example  of :file:`data_airfoil.csv` for an airfoil data file is given below:

   .. code-block::
   
      Airfoil name, AoA [deg], Re [-], C_l [-], C_d [-], C_m [-] 
      Cylinder,     -180,      0.0,    0.0,      0.6,      0.0    
      Cylinder,      0.0,      0.0,    0.0,      0.6,      0.0    
      Cylinder,      180,      0.0,    0.0,      0.6,      0.0    
      FFA-W3-241,   -180,      0.0,    0.0,      0.0,      0.0    
      FFA-W3-241,   -175,      0.0,    0.1736,   0.01142,  0.0218 
      FFA-W3-241,   -170,      0.0,    0.3420,   0.04523,  0.0434 
      ...                                                      
      FFA-W3-600,   170,       0.0,   -0.342,    0.0392,  -0.0434 
      FFA-W3-600,   175,       0.0,   -0.1736,   0.0099,  -0.0218 
      FFA-W3-600,   180,       0.0,    0.0,      0.0,      0.0    

* :code:`CINTERP` : method of interpolation of wind conditions at blade element position:

  * `CLS' closest cell value (no interpolation).
  * `8NB' eight neighbourhood interpolation.

* :code:`NNB_AZIELT` : number of elements for the azimutal discretisation of the disc. To determine the value to be specified, refer to the scientific documentation.

* :code:`NNB_RADELT` : number of elements for the radial discretisation of the disc. This value is independent of the number of elements in CBLADE_CSVDATA, as the algorithm will proceed to its own discretization through an interpolation of the data given by the blade description (CBLADE_CSVDATA). To determine the value to be specified, refer to the scientific documentation.

* :code:`LTIPLOSSG` : flag to activate the tip loss correction of Glauert. Usually applied to alleviate the over-predicted loads at the blade tip region when the low resolution or the smearing method cannot capture tip vortices. One can note that this correction should only be used with models such as the Actuator Disc with Rotation to correct for finite number of blades.

  * .TRUE.  activates the tip loss correction of Glauert.
  * .FALSE. no activation.

* :code:`LTECOUTPTS` : flag to enable the output of geometrical points (XYZ) for wind turbines in a Tecplot file. This provides spatial positions at each element point of the wind turbine, facilitating setup checks such as geometry and wind farm layout.

  * .TRUE.  activates Tecplot output.
  * .FALSE. deactivates it.

* :code:`LCSVOUTFRM` : flag to enable the output of frames :math:`\left(\overrightarrow{e_x},\overrightarrow{e_y},\overrightarrow{e_z}\right)` for wind turbines in a CSV file. This describes the spatial positions and orientations of frames for each kinematic part of the wind turbine. Useful for verifying setup details, including positions and orientations of its components.

  * .TRUE.  activates the CSV output.
  * .FALSE. deactivates it.

