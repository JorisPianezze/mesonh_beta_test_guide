.. _nam_dimn_pre:

NAM_DIMn_PRE
-----------------------------------------------------------------------------

.. csv-table:: NAM_DIMn_PRE content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "NIMAX","INTEGER","10"
   "NJMAX","INTEGER","10"

* :code:`NIMAX` : number of mass points in x-direction of the initial file is NIMAX+2*JPHEXT (JPHEXT corresponds to the number of marginal points in the horizontal directions and is fixed to 1 for the present Meso-NH version ). NIMAX must be equal to :math:`2^m \times 3^n \times 5^p` with :math:`(m,n,p) \ge 0`.

* :code:`NJMAX` : number of mass points in y-direction of the physical domain. The total size of the array written in the initial file is NJMAX+2*JPHEXT. NJMAX must be equal to :math:`2^m \times 3^n \times 5^p` with :math:`(m,n,p) \ge 0`.

