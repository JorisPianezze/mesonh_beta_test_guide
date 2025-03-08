.. _nam_zoom_spectre:

NAM_ZOOM_SPECTRE
-----------------------------------------------------------------------------

.. csv-table:: NAM_ZOOM_SPECTRE content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LZOOM","logical",".FALSE."
   "NXDEB","integer",""
   "NYDEB","integer",""
   "NITOT","integer",""
   "NJTOT","integer",""

* LZOOM : flag to make a zoom on the file domain

* NXDEB : first point I index, left to and out of the wanted domain

* NYDEB : first point J index, under and out of the wanted domain

* NITOT : number of grid points in I direction. It must be equal to :math:`2^m \times 3^n \times 5^p` with :math:`(m,n,p) \ge 0`.

* NJTOT : number of grid points in J direction. It must be equal to :math:`2^m \times 3^n \times 5^p` with :math:`(m,n,p) \ge 0`.   
