.. _nam_salt:

NAM_SALT
-----------------------------------------------------------------------------

This namelist is used to active explicit sea salt aerosols. It is not necessary to use chemistry to activate sea salt but it is recommended to activate on-line sea salt emissions.

.. csv-table:: NAM_SALT content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LSALT","LOGICAL",".FALSE."
   "LVARSIG_SLT","LOGICAL",".FALSE."
   "LSEDIMSALT","LOGICAL",".FALSE."
   "NMODE_SLT","INTEGER","8"
   "LRGFIX_SLT","LOGICAL",".FALSE."
   "LDEPOS_SLT","LOGICAL",".FALSE."

* :code:`LSALT` : flag to activate passive salt aerosol.

* :code:`LVARSIG_SLT` : flag to activate variable standard deviation for each salt modes.

* :code:`LSEDIMSALT` : flag to activate salt sedimentation.

* :code:`NMODE_SLT` : number of lognormal salt modes (a maximum of 8 modes is allowed).

* :code:`LRGFIX_SLT` : flag to use only 1 moment by salt mode (LRGFIX_SLT='TRUE' associated to LVARSIG_SLT='FALSE)

* :code:`LDEPOS_SLT` : flag to activate salt wet deposition  

