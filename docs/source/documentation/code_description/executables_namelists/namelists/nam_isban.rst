.. _nam_isban:

NAM_ISBAn
----------------------------------------------------------------------------- 

.. csv-table:: NAM_ISBAn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CC1DRY", "CHARACTER(LEN=4)", "'DEF'"
   "CSCOND", "CHARACTER(LEN=4)", "'PL98'"
   "CSOILFRZ", "CHARACTER(LEN=3)", "'DEF'"
   "CDIFSFCOND", "CHARACTER(LEN=4)", "'DEF'"
   "CSNOWRES", "CHARACTER(LEN=3)", "'DEF'"
   "CCPSURF", "CHARACTER(LEN=3)", "'DRY'"
   "XTSTEP", "REAL", "none"
   "XCVHEATF", "REAL", "0.20"
   "XCGMAX", "REAL", "2.E-5"
   "XCDRAG", "REAL", "0.15"
   "LGLACIER", "LOGICAL", ".FALSE."
   "LCANOPY_DRAG", "LOGICAL", ".FALSE."
   "LVEGUPD", "LOGICAL", ".TRUE."
   "LPERTSURF", "LOGICAL", ".TRUE."

* :code:`CC1DRY` : type of C1 formulation for dry soils. The following options are currently available:

  * 'DEF' : Giard-Bazile formulation
  * 'GB93' : Giordani 1993, Braud 1993

* :code:`CSCOND` : type of thermal conductivity. The following options are currently available:

  * 'NP89' : Noilhan and Planton (1989) formula
  * 'PL98' : Peters-Lidard et al. (1998) formula

* :code:`CSOILFRZ` : type of soil freezing-physics option. The following options are currently available:

  * 'DEF' : Boone et al. 2000; Giard and Bazile 2000
  * 'LWT' : Phase changes as above, but relation between unfrozen water and temperature considered

* :code:`CDIFSFCOND` : type of Mulch effects. The following options are currently available:

  * 'DEF' : no mulch effect
  * 'MLCH' : include the insulating effect of leaf litter/mulch on the surf. thermal cond.
  
* :code:`CSNOWRES` : type of turbulent exchanges over snow. The following options are currently available:

  * 'DEF' : Louis
  * 'RIL' : Maximum Richardson number limit for stable conditions ISBA-SNOW3L turbulent exchange option
  * 'M98' : Martin et Lejeune 1998: older computation for turbulent fluxes coefficents in Crocus
  
* :code:`CCPSURF` : type of specific heat at surface. The following options are currently available:

  * 'DRY' : specific heat does not depend on humidity at surface
  * 'HUM' : specific heat depends on humidity at surface.
  
* :code:`XTSTEP` : time step for ISBA. Default is to use the time-step given by the atmospheric coupling (seconds).

* :code:`XCVHEATF` : Modify Cv to compensate biases in ground temperature

* :code:`XCGMAX` : maximum value for soil heat capacity.

* :code:`XCDRAG` : drag coefficient in canopy.

* :code:`LGLACIER` : If activated, specific treatment (as in Arpege) over permanent snow/ice regions. Snow depth initialised to 10m and soil ice to porosity. During the run, snow albedo ranges from 0.8 to 0.85

* :code:`LCANOPY_DRAG` : drag activated in SBL scheme within the canopy

* :code:`LVEGUPD` : True = update vegetation parameters every decade

* :code:`LPERTSURF` : if T modification of surface fluxes for ensemble forecasting
