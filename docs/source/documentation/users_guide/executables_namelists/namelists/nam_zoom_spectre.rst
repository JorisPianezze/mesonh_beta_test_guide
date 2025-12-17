.. _nam_zoom_spectre:

NAM_ZOOM_SPECTRE
-----------------------------------------------------------------------------

.. csv-table:: NAM_ZOOM_SPECTRE content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LZOOM","LOGICAL",".FALSE."
   "NXDEB","INTEGER",""
   "NYDEB","INTEGER",""
   "NITOT","INTEGER",""
   "NJTOT","INTEGER",""

* :code:`LZOOM` : flag to make a zoom on the file domain

* :code:`NXDEB` : first point I index, left to and out of the wanted domain

* :code:`NYDEB` : first point J index, under and out of the wanted domain

* :code:`NITOT` : number of grid points in I direction. It must be equal to :math:`2^m \times 3^n \times 5^p` with :math:`(m,n,p) \ge 0`.

* :code:`NJTOT` : number of grid points in J direction. It must be equal to :math:`2^m \times 3^n \times 5^p` with :math:`(m,n,p) \ge 0`.   
