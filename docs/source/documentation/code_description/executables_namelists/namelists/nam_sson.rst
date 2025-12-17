.. _nam_sson:

NAM_SSOn
----------------------------------------------------------------------------- 

.. csv-table:: NAM_SSOn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "CROUGH", "CHARACTER(LEN=4)", "'BE04'"
   "XFRACZ0", "REAL", "2.0"
   "LDSV", "LOGICAL", ".FALSE."
   "LDSH", "LOGICAL", ".FALSE."
   "LDSL", "LOGICAL", ".FALSE."

* :code:`CROUGH` : type of orographic roughness length. The following options are currently available:

  * "Z01D": orographic roughness length does not depend on wind direction
  * "Z04D": orographic roughness length depends on wind direction 
  * "BE04": :cite:t:`beljaars_new_2004` orographic drag
  * "NONE": no orographic treatment

* :code:`XFRACZ0` : Z0=min(Z0, Href/XFRACZ0)

* :code:`XCOEFBE` : coefficient for Beljaars calculation of SSO drag.

* :code:`LDSV` : orographic shadowing, sky view factor (only if LORORAD = T in PGD field)

* :code:`LDSH` : orographic shadowing, shadow factor (only if LORORAD = T in PGD field)

* :code:`LDSL` : orographic shadowing, slope factor (only if LORORAD = T in PGD field)
