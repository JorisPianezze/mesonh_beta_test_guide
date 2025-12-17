.. _nam_dust:

NAM_DUST
-----------------------------------------------------------------------------

This namelist is use to activate explicit aerosol dusts. It is not necessary to use chemistry to activate dusts but it is recommended to activate on-line dust emissions (see SURFEX namelists). Radiative direct effects are automatically deduced from an interpolation table of SHDOM radiative code (Mie). 

.. csv-table:: NAM_DUST content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LDUST","LOGICAL",".FALSE."
   "LVARSIG","LOGICAL",".FALSE."
   "LSEDIMDUST","LOGICAL",".FALSE."
   "NMODE_DST","INTEGER","3"
   "LRGFIX_DST","LOGICAL",".FALSE."
   "LDEPOS_DST","LOGICAL",".FALSE."

* :code:`LDUST` : flag to activate passive dust aerosol.

* :code:`LVARSIG` : flag to activate variable standard deviation for each dust mode.

* :code:`LSEDIMDUST` : flag to activate dust sedimentation.

* :code:`NMODE_DST` : number of lognormal dust modes (maximum of 3 modes).

* :code:`LRGFIX_DST` : flag to use only 1 moment for each dust mode (LRGFIX_DST='TRUE' associated to LVARSIG='FALSE)

* :code:`LDEPOS_DST` : flag to activate wet dust deposition  

