.. _nam_mesonh_dom:

NAM_MESONH_DOM
-----------------------------------------------------------------------------

.. csv-table:: NAM_MESONH_DOM content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "NIMAX","INTEGER","input PGD domain"
   "NJMAX","INTEGER","input PGD domain"
   "NXOR","INTEGER","NUNDEF"
   "NYOR","INTEGER","NUNDEF"

* :code:`NIMAX` : number of grid points in I direction, according to input file grid, recovered by the new domain. NIMAX must be equal to :math:`2^m \times 3^n \times 5^p` with :math:`(m,n,p) \in [0,+\infty[\

* :code:`NJMAX` : number of grid points in J direction, according to input file  grid, recovered by the new domain. NJMAX must be equal to :math:`2^m \times 3^n \times 5^p` with :math:`(m,n,p) \in [0,+\infty[`

* :code:`NXOR` : first point I index, left to and out of the new physical domain.

* :code:`NYOR` : first point J index, under and out of the new physical domain.
