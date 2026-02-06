Wind turbine
================================================



Here is a list of the variables available in Meso-NH when wind turbines are simulated. 

* 'R' stands for the number of rotors (wind turbines).
* 'B' stands for the number of blades for one rotor.
* 'AE' stands for the number of azimutal elements of the rotor.
* 'RE' stands for the number of radial elements of a blade.
* '3' stands for the three component of the vecteur (x,y,z).


*  The 'global frame' denotes the coordinate system of Meso-NH.
*  The 'hub frame' the coordinate system linked to the hub.
*  The 'blade element frame' the coordinate system linked to a blade element.
*  The 'relative frame' the aerodynamic coordinate system linked to the relative wind speed.
   
See the Scientific documentation for more details. The mean values of variables are computed between two backup outputs.

Main variables
------------------------------------------------------------------------------

:code:`LMAIN_EOL=T`

.. csv-table::
   :header: "Name", "Dimension", "Meaning", "Units"
   :widths: 20, 15, 60, 5

   "FX_RG", "[x,y,z]", "X-component field of aerodynamic force (wind$\rightarrow$rotor) in global frame", "N"
   "FY_RG", "[x,y,z]", "Y-component field of aerodynamic force (wind$\rightarrow$rotor) in global frame", "N"
   "FZ_RG", "[x,y,z]", "Z-component field of aerodynamic force (wind$\rightarrow$rotor) in global frame", "N"
   "FX_SMR_RG", "[x,y,z]", "X-component field of smeared aerodynamic force (wind$\rightarrow$rotor) in global frame", "N"
   "FY_SMR_RG", "[x,y,z]", "Y-component field of smeared aerodynamic force (wind$\rightarrow$rotor) in global frame", "N"
   "FZ_SMR_RG", "[x,y,z]", "Z-component field of smeared aerodynamic force (wind$\rightarrow$rotor) in global frame", "N"

Non-Rotating Actuator Disc (ADNR)
------------------------------------------------------------------------------
Instantaneous variables
**********************************************************************

:code:`LMAIN_EOL=T` and :code:`CMETH_EOL='ADNR'`

.. csv-table::
   :header: "Name", "Dimension", "Meaning", "Units"
   :widths: 20, 15, 60, 5

   "A_INDU", "[R]", "induction factor", "-"
   "CT_D", "[R]", "thrust coefficient at disc ($C_{t_d} \neq C_{t_\infty}$)", "-"
   "THRUT", "[R]", "instantaneous thrust (wind$\rightarrow$rotor) in hub frame", "N"


Averaged variables
**********************************************************************

:code:`LMAIN_EOL=T`, :code:`CMETH_EOL='ADNR'` and :code:`LMEAN_FIELD=T`

.. csv-table::
   :header: "Name", "Dimension", "Meaning", "Units"
   :widths: 20, 15, 60, 5
   
   "THRUMME","[R]", "averaged thrust (wind$\rightarrow$rotor) in hub frame", "N"    


Rotation Actuator Disc (ADR)
------------------------------------------------------------------------------
Instantaneous variables
**********************************************************************

:code:`LMAIN_EOL=T` and :code:`CMETH_EOL='ADR'`


.. csv-table::
   :header: "Name", "Dimension", "Meaning", "Units"
   :widths: 20, 15, 60, 5

   "ELT_RAD", "[R,AE,RE]", "radial position of an element (0m at hub)", "m"
   "ELT_AZI", "[R,AE,RE]", "azimutal angle of an element", "rad"
   "AOA", "[R,AE,RE]", "instantaneous angle of attack", "rad"
   "AOA_BLEQ", "[R,RE]", "blade equivalent instantaneous angle of attack", "rad"
   "FLIFT", "[R,AE,RE]", "instantaneous lift force in relative frame", "N"
   "FDRAG", "[R,AE,RE]", "instantaneous drag force in relative frame", "N"
   "FAERO_RA", "[R,AE,RE,3]", "instantaneous aerodynamic force in annular element frame", "N"
   "FAERO_RG", "[R,AE,RE,3]", "instantaneous aerodynamic force in global frame", "N"
   "FAERO_BLEQ_RA", "[R,RE,3]", "blade equivalent instantaneous aerodynamic force in annular element frame", "N"
   "THRUT", "[R]", "instantaneous thrust (wind$\rightarrow$rotor) in hub frame", "N"
   "TORQT", "[R]", "instantaneous torque (wind$\rightarrow$rotor) in hub frame", "Nm"
   "POWT", "[R]", "instantaneous power (wind$\rightarrow$rotor)", "W"
   "OMEGAT", "[R]", "instantaneous angular velocity", "rad/s"
   "PITCHT", "[R]", "instantaneous blade pitch", "rad"
   "AZIMUTHT", "[R]", "instantaneous angular position of the hub frame", "rad"     

Averaged variables
**********************************************************************

:code:`LMAIN_EOL=T`, :code:`'CMETH_EOL='ALM'` and :code:`LMEAN_FIELD=T`

.. csv-table::
   :header: "Name", "Dimension", "Meaning", "Units"
   :widths: 20, 15, 60, 5
 
   "AOAMME", "[R,AE,RE]", "averaged angle of attack", "rad"
   "AOAMME_BLEQ", "[R,RE]", "blade equivalent averaged angle of attack", "rad"
   "FAEROMME_RA", "[R,AE,RE,3]", "averaged aerodynamic force in annular element frame", "N"
   "FAEROMME_BLEQ_RA", "[R,RE,3]", "blade equivalent averaged aerodynamic force in annular element frame", "N"
   "THRUMME", "[R]", "averaged thrust (wind$\rightarrow$rotor) in hub frame", "N"
   "TORQMME", "[R]", "averaged torque (wind$\rightarrow$rotor) in hub frame", "Nm"
   "POWMME", "[R]", "averaged power (wind$\rightarrow$rotor)", "W"
   "OMEGAMME", "[R]", "averaged angular velocity", "rad/s"
   "PITCHMME", "[R]", "averaged blade pitch", "rad"


Actuator Line Method (ALM)
------------------------------------------------------------------------------
Instantaneous variables
**********************************************************************

:code:`LMAIN_EOL=T` and :code:`'CMETH_EOL='ALM'`
 
.. csv-table::
   :header: "Name", "Dimension", "Meaning", "Units"
   :widths: 20, 15, 60, 5
 
   "ELT_RAD", "[R,B,RE]", "radius (0m at hub)", "m"
   "AOA", "[R,B,RE]", "instantaneous angle of attack", "rad"
   "FLIFT", "[R,B,RE]", "instantaneous lift force in relative frame", "N"
   "FDRAG", "[R,B,RE]", "instantaneous drag force in relative frame", "N"
   "FAERO_RE", "[R,B,RE,3]", "instantaneous aerodynamic force in blade element frame", "N"
   "FAERO_RG", "[R,B,RE,3]", "instantaneous aerodynamic force in global frame", "N"
   "THRUT", "[R]", "instantaneous thrust (wind$\rightarrow$rotor) in hub frame", "N"
   "TORQT", "[R]", "instantaneous torque (wind$\rightarrow$rotor) in hub frame", "Nm"
   "POWT", "[R]", "instantaneous power (wind$\rightarrow$rotor)", "W"
   "OMEGAT", "[R]", "instantaneous angular velocity", "rad/s"
   "PITCHT", "[R]", "instantaneous blade pitch", "rad"
   "AZIMUTHT", "[R]", "instantaneous angular position of the hub frame", "rad"  

Averaged variables
**********************************************************************

:code:`LMAIN_EOL=T`, :code:`'CMETH_EOL='ALM'` and :code:`LMEAN_FIELD=T`

.. csv-table::
   :header: "Name", "Dimension", "Meaning", "Units"
   :widths: 20, 15, 60, 5

   "AOAMME", "[R,B,RE]", "averaged angle of attack", "rad"
   "FAEROMME_RE", "[R,B,RE,3]", "averaged aerodynamic force in blade element frame", "N"
   "THRUMME", "[R]", "averaged thrust (wind$\rightarrow$rotor) in hub frame", "N"
   "TORQMME", "[R]", "averaged torque (wind$\rightarrow$rotor) in hub frame", "Nm"
   "POWMME", "[R]", "averaged power (wind$\rightarrow$rotor)", "W"
   "OMEGAMME", "[R]", "averaged angular velocity", "rad/s"
   "PITCHMME", "[R]", "averaged blade pitch", "rad"


Controller variables
------------------------------------------------------------------------------
:code:`LMAIN_EOL=T`, :code:`LCONTROL_EOL=T`, :code:`CMETH_OPS='JONKM'`, :code:`'CMETH_EOL='ALM'` or :code:`'ADR'`

.. csv-table::
   :header: "Name", "Dimension", "Meaning", "Units"
   :widths: 20, 15, 60, 5

   "REGION_JONKM", "[R]", "Which of the 5-region is currently used for rotational velocity control", "-"
   "OMEGA_FILTERED", "[R]", "Current filtered rotational velocity", "rad/s"
   "TORQUE_GEN", "[R]", "Current generator torque", "Nm"
   "OMEGA_GEN", "[R]", "Current generator rotational velocity", "rad/s"
   "OMEGA_ERROR_INTEG", "[R]", "Current integrated error on rotational velocity", "rad"


:code:`LMAIN_EOL=T`, :code:`LCONTROL_EOL=T`, :code:`CMETH_OPS='ROSCO'`, :code:`'CMETH_EOL='ALM'` or :code:`'ADR'`
 
.. csv-table::
   :header: "Name", "Dimension", "Meaning", "Units"
   :widths: 20, 15, 60, 5

   "REGION_ROSCO", "[R]", "Which of the 5-region is currently used for rotational velocity control", "-"
   "TORQUE_GEN", "[R]", "Current generator torque", "Nm"
   "OMEGA_GEN", "[R]", "Current generator rotational velocity", "rad/s"
   "GENF_INLAST1", "[R]", "Last input omega generator 1 [2nd order filter]", "rad/s"
   "GENF_INLAST2", "[R]", "Last input omega generator 2 [2nd order filter]", "rad/s"
   "GENF_OUTLAST1", "[R]", "Last output omega generator 1 [2nd order filter]", "rad/s"
   "GENF_OUTLAST2", "[R]", "Last output omega generator 2 [2nd order filter]", "rad/s"
   "TORQF_INLAST1", "[R]", "Last input torque generator 1 [2nd order filter]", "Nm"
   "TORQF_INLAST2", "[R]", "Last input torque generator 2 [2nd order filter]", "Nm"
   "TORQF_OUTLAST1", "[R]", "Last output torque generator 1 [2nd order filter]", "Nm"
   "TORQF_OUTLAST2", "[R]", "Last output torque generator 2 [2nd order filter]", "Nm"
   "GENARTQ_PII", "[R]", "Integral term PI omega generator Above rated", "Nm"
   "GENBRTQ_PII", "[R]", "Integral term PI omega generator Below rated", "Nm"
   "PITCH_PII", "[R]", "Integral term PI pitch", "rad"


Time-dependent variables
------------------------------------------------------------------------------
These variables are available in the diachronic file under the subgroup 'Wind_turbines', which itself contains one subgroup per wind turbine. 
These outputs can be activated with variable :code:`LDIA_EOL` in :ref:`NAM_EOL`.

.. csv-table::
   :header: "Name", "Dimension", "Meaning", "Units"
   :widths: 20, 15, 60, 5
 
   "THRUST", "[t]", "Thrust (wind$\rightarrow$rotor) in hub frame", "N"
   "TORQUE", "[t]", "Torque (wind$\rightarrow$rotor) in hub frame", "Nm"
   "POWER", "[t]", "Power (wind$\rightarrow$rotor)", "W"
   "OMEGA", "[t]", "Angular velocity", "rad/s"
   "PITCH", "[t]", "Blade pitch", "rad"
   "AZIMUTH", "[t]", "Angular position of the hub frame", "rad"    

Controller
**********************************************************************

:code:`LMAIN_EOL=T`, :code:`LCONTROL_EOL=T`, :code:`CMETH_OPS='ROSCO'` or :code:`'JONKM'`, :code:`'CMETH_EOL='ALM'` or :code:`'ADR'`

.. csv-table::
   :header: "Name", "Dimension", "Meaning", "Units"
   :widths: 20, 15, 60, 5
   
   "REGION", "[t]", "Which of the 5-region is currently used for angular speed control", "-"
   "GEN_TORQUE", "[t]", "Current generator torque", "Nm"
   "GEN_SPEED", "[t]", "Current generator rotational velocity", "rad/s"  


Floating wind turbine
**********************************************************************

Additionally, if :code:`LFLOAT_EOL=T` , the 6-DOF velocities and positions of the floater are available:

.. csv-table::
   :header: "Name", "Dimension", "Meaning", "Units"
   :widths: 20, 15, 60, 5
 
   "FLOAT_SURGE_POS", "[t]", "Floater relative surge position speed", "m"
   "FLOAT_SWAY_POS", "[t]", "Floater relative sway position", "m"
   "FLOAT_HEAVE_POS", "[t]", "Floater relative heave position", "m"
   "FLOAT_ROLL_POS", "[t]", "Floater relative roll position", "rad"
   "FLOAT_PITCH_POS", "[t]", "Floater relative pitch position", "rad"
   "FLOAT_YAW_POS", "[t]", "Floater relative yaw position", "rad"
   "FLOAT_SURGE_VEL", "[t]", "Floater surge velocity", "m/s"
   "FLOAT_SWAY_VEL", "[t]", "Floater sway velocity", "m/s"
   "FLOAT_HEAVE_VEL", "[t]", "Floater heave velocity", "m/s"
   "FLOAT_ROLL_VEL", "[t]", "Floater roll velocity", "rad/s"
   "FLOAT_PITCH_VEL", "[t]", "Floater pitch velocity", "rad/s"
   "FLOAT_YAW_VEL", "[t]", "Floater yaw velocity", "rad/s"   


High-frequency outputs
**********************************************************************

If at least one field is requested in :ref:`NAM_OUTPUT` (for instance, UT) and if :code:`LMAIN_EOL=T`, 
then the high-frequency output files will automatically contain:

.. csv-table::
   :header: "Name", "Dimension", "Meaning", "Units"
   :widths: 20, 15, 60, 5
 
   "THRUT", "[t]", "Thrust (wind$\rightarrow$rotor) in hub frame", "N"
   "TORQT", "[t]", "Torque (wind$\rightarrow$rotor) in hub frame", "Nm"
   "POWT", "[t]", "Power (wind$\rightarrow$rotor)", "W"
   "OMEGAT", "[t]", "Angular velocity", "rad/s"
   "PITCHT", "[t]", "Blade pitch", "rad"
   "AZIMUTHT", "[t]", "Angular position of the hub frame", "rad"

Additionally, with :code:`LMAIN_EOL=T`, :code:`LCONTROL_EOL=T`, :code:`CMETH_OPS='ROSCO'` or :code:`'JONKM'`

it also contains:

.. csv-table::
   :header: "Name", "Dimension", "Meaning", "Units"
   :widths: 20, 15, 60, 5
 
   "REGION", "[R]", "Which of the 5-region is currently used for angular speed control", "m"
   "TORQUE_GEN", "[R]", "Current generator torque", "Nm"
   "OMEGA_GEN", "[R]", "Current filtered generator rotational velocity", "rad/s"


Finally, if :code:`LMAIN_TRACER=T`, it also contains:

.. csv-table::
   :header: "Name", "Dimension", "Meaning", "Units"
   :widths: 20, 15, 60, 5

   "SVEOLT_001", "[x,y,z]", "Current concentration of turbine passive scalar number NEMITTING_ROT(1)  ", ""     
   "SVEOLT_{...}", "[x,y,z]", "Current concentration of turbine passive scalar number NEMITTING_ROT(...)  ", ""     
   "SVEOLT_00N", "[x,y,z]", "Current concentration of turbine passive scalar number NEMITTING_ROT(N) where N = NNB_EMITTING_ROT  ", ""
