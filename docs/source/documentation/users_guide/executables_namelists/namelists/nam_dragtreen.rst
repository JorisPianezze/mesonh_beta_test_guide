.. _nam_dragtreen:

NAM_DRAGTREEn
-----------------------------------------------------------------------------

.. warning::

   This namelist comes from SURFEX 9.0.0 user guide https://www.umr-cnrm.fr/surfex/IMG/pdf/surfex_tecdoc.pdf.

This namelist allows to take into account drag of trees in the atmospheric model instead of SURFEX according to Aumond et al. (2011) in the case of very fine vertical resolution. The Z0 vegetation is therefore reduced to the roughness of grassland in SURFEX (:file:`z0v_from_lai.F90`). LTREEDRAG in NAM_TREEDRAG of SURFEX must also be activated.
   
.. csv-table:: NAM_DRAGTREEn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LDRAGTREE","LOGICAL",".FALSE."
   "LDEPOTREE","LOGICAL",".FALSE."
   "XVDEPOTREE","REAL","0.02"

* :code:`LDRAGTREE` : flag to activate drag of trees

* :code:`LDEPOTREE` : flag for droplet deposition on trees

* :code:`XVDEPOTREE` : Droplet deposition velocity on trees
