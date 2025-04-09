.. _nam_grid2_spa:

NAM_GRID2_SPA
-----------------------------------------------------------------------------

.. csv-table:: NAM_GRID2_SPA content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "IXOR","INTEGER","1"
   "IYOR","INTEGER","1"
   "IXSIZE","INTEGER","file 1 domain"
   "IYSIZE","INTEGER","file 1 domain"
   "IDXRATIO","INTEGER","1"
   "IDYRATIO","INTEGER","1"
   "GBAL_ONLY","INTEGER",".FALSE."


* :code:`IXOR` : first point I index, according to the file 1 grid, left to and out of the new physical domain.

* :code:`IYOR` : first point J index, according to the file 1 grid, under and out of the new physical domain.

* :code:`IXSIZE` : number of grid points in I direction, according to file 1 grid, recovered by the new domain. It must be equal to :math:`2^m \times 3^n \times 5^p` with :math:`(m,n,p) \ge 0`

* :code:`IYSIZE` : number of grid points in J direction, according to file 1 grid, recovered by the new domain. It must be equal to :math:`2^m \times 3^n \times 5^p` with :math:`(m,n,p) \ge 0`

* :code:`IDXRATIO` : resolution factor in I direction between the file 1 grid and the new grid. It must be  equal to :math:`2^m \times 3^n \times 5^p` with :math:`(m,n,p) \ge 0`

* :code:`IDYRATIO` : resolution factor in J direction between the file 1 grid and the new grid. It must be equal to :math:`2^m \times 3^n \times 5^p` with :math:`(m,n,p) \ge 0`

* :code:`GBAL_ONLY` : flag to enforce anelastic constraint only. The spawned file have the same characteristics as the CINIFILE one.
