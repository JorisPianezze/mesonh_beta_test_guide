.. _nam_confn:

NAM_CONFn
-----------------------------------------------------------------------------

.. csv-table:: NAM_CONFn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LUSERV","LOGICAL",".TRUE."
   "LUSECI","LOGICAL",".FALSE."
   "LUSERC","LOGICAL",".FALSE."
   "LUSERR","LOGICAL",".FALSE."
   "LUSERI","LOGICAL",".FALSE."
   "LUSERS","LOGICAL",".FALSE."
   "LUSERG","LOGICAL",".FALSE."
   "LUSERH","LOGICAL",".FALSE."
   "NSV_USER","INTEGER","0"

* :code:`LUSERV` : Flag to use vapor mixing ratio (:math:`r_v`)

* :code:`LUSECI` : Flag to use pristine ice (:math:`C_i`)

* :code:`LUSERC` : Flag to use cloud mixing ratio (:math:`r_c`)

* :code:`LUSERR` : Flag to use rain mixing ratio (:math:`r_r`

* :code:`LUSERI` : Flag to use ice mixing ratio (:math:`r_i`)

* :code:`LUSERS` : Flag to use snow mixing ratio (:math:`r_s`)

* :code:`LUSERG` : Flag to use graupel mixing ratio (:math:`r_g`)

* :code:`LUSERH` : Flag to use hail mixing ratio (:math:`r_h`)

.. note::

   You don't need to fill this records : they are directly managed by CCLOUD.

* NSV_USER  : Number of user passive scalar variables

.. warning::

  Scalar variables needed for the 2-moment microphysical schemes, lagrangian trajectory, passive pollutants or the chemistry options are treated automatically by the model and should not be counted here.
