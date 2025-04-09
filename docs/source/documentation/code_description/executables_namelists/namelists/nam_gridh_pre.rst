.. _nam_gridh_pre:

NAM_GRIDH_PRE
-----------------------------------------------------------------------------

.. csv-table:: NAM_GRIDH_PRE content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "XLATCEN","REAL","XUNDEF"
   "XLONCEN","REAL","XUNDEF"
   "XDELTAX","REAL","5000.0"
   "XDELTAY","REAL","5000.0"
   "XHMAX","REAL","300.0 / 0.0"
   "NEXPX","INTEGER","3"
   "NEXPY","INTEGER","1"
   "XAX","REAL","10000.0"
   "XAY","REAL","10000.0"
   "NIZS","INTEGER","5"
   "NJZS","INTEGER","5"

* :code:`XLATCEN` : latitude  of the center of the domain for initialization. This point is vertical vorticity point (:ref:`grids`)

* :code:`XLONCEN` :  longitude of the center of the domain for initialization. This  point is vertical vorticity point (:ref:`grids`)

* :code:`XDELTAX` : mesh length (in meters) in x-direction on the conformal or cartesian plane. It is  not used if you read information in a Meso-NH constant file (PGD_FILE). 

* :code:`XDELTAY` : mesh length (in meters) in y-direction on the conformal or cartesian plane. It is  not used if you read information in a Meso-NH constant file (PGD_FILE).

* :code:`XHMAX` : Maximum height (in meters) :math:`h_{max}` for orography (case CZS :math:`\neq` 'FLAT') or ground level for flat orography. Default is 0.0 for 'FLAT' and 300.0 elsewhere.

* :code:`NEXPX` : Exponent :math:`exp_{x}` for orography in case of CZS='SINE'

* :code:`NEXPY` : Exponent :math:`exp_{y}` for orography in case of CZS='SINE'

* :code:`XAX` :  Widths (in meters) :math:`a_{x}` along x  for orography in case CZS='BELL'

* :code:`XAY` : Width  (in meters) :math:`a_{y}` along y  for orography in case CZS='BELL'

* :code:`NIZS` :  Localization in x-direction in the physical domain of the mountain center in the  case CZS ='BELL'. (:math:`x_{s} = NIZS * XDELTAX`) It refers to a vertical velocity point at the ground ( NIZS, NJZS )(:ref:`grids`)

* :code:`NJZS` : Localization in y-direction in the physical domain of the mountain center in the case CZS ='BELL'. (:math:`y_{s} = NJZS * XDELTAY`)

.. note::

   In case of CZS = 'BELL' :

   * in the three-dimensional case :
   
   .. math::

      z_s \left( \hat{x} , \hat{y} \right) = { h_{max} \over  \left(
      1 +
      \left(  { \hat{x} - NIZS * XDELTAX \over XAX } \right) ^2 + 
      \left(  { \hat{y} - NJZS * XDELTAX \over XAY } \right) ^2 
                                                      \right) ^{1.5 } }

   * in the two-dimensional case :

   .. math::

      z_s \left( \hat{x}  \right) = {  h_{max} \over  1 + \left(  { \hat{x} - NIZS * XDELTAX \over XAX } \right) ^2 }

