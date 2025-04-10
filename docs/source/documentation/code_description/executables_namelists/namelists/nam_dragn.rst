.. _nam_dragn:

NAM_DRAGn
-----------------------------------------------------------------------------

.. csv-table:: NAM_DRAGn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LDRAG","LOGICAL",".FALSE."
   "LMOUNT","LOGICAL",".FALSE."
   "NSTART","INTEGER","1"
   "XHSTART","REAL","0.0"

* :code:`LDRAG` : Surface no-slip condition activation (instead of free-slip) - Only used with LVISC=T

* :code:`LMOUNT` : Surface no-slip condition activation only over a mountain

* :code:`NHSTART` : Grid point number (in the X-direction) from which the no-slip condition is applied, when LMOUNT = .FALSE.

* :code:`XHSTART` : Height above  which the no-slip condition is applied, when LMOUNT = .TRUE..     
