.. _nam_vprof_pre:

NAM_VPROF_PRE
-----------------------------------------------------------------------------

.. csv-table:: NAM_VPROF_PRE content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LGEOSBAL","LOGICAL","FALSE"
   "CFUNU","CHARACTER(LEN=3)","ZZZ"
   "CFUNV","CHARACTER(LEN=3)","ZZZ"
   "CTYPELOC","CHARACTER(LEN=6)","IJGRID"
   "XLATLOC","REAL","45.0"
   "XLONLOC","REAL","0.0"
   "XXHATLOC","REAL","20000.0"
   "XYHATLOC","REAL","20000.0"
   "NILOC","INTEGER","4"
   "NJLOC","INTEGER","4"

* :code:`LGEOSBAL` : Flag to fulfill the geostrophic balance or not

  * .TRUE. the geostrophic balance is satisfied by the initial fields
  * .FALSE. the geostrophic balance is not satisfied by the initial fields

* :code:`CFUNU` : String of 3 characters, describing the type of function, which gives the  x component of the wind. Possible configurations are listed below :

  * 'ZZZ' :  U = U(z). The U(z) values are taken from the Radio-Sounding or analitycal profile given in the free-formatted part of the  PRE_IDEA1.nam file.

  * 'Y*Z' : U= F(Y)*U(Z). The U(z) values are build in the same way as the 'ZZZ' case and the function F(Y) is a simple function of Y, which must be adapted by modifying its definition directly in the routine FUNUY. The default  function is :
  
  .. math::  
  
     FUNUY(\hat{y}) = {1 \over \cosh \left({ \hat{y} - \hat{y_0} \over zwidth } \right)}

  * 'Y,Z' : U= G(Y,Z). The function  G must also be adapted  by modifying its definition directly in the routine FUNUYZ. The default function is :
  
  .. math::   
     
     FUNUYZ(\hat{y},z) = { 1 \over \cosh \left(\left( { \hat{y} - \hat{y_0} \over zwidthy } \right) ^2 +  \left( { z - z_0 \over zwidthz } \right) ^2 \right) }

  .. note::
  
     Notice that in this case the U(z) values given by the profile are not used. 

* :code:`CFUNV` : String of 3 characters, describing the type of function, which gives the  y component of the wind. Possible configurations are listed below

  * 'ZZZ' :  V = V(z). The  V(z) values are taken from the Radio-Sounding or analitycal profile given in the free-formatted part of the PRE_IDEA1.nam file.

  * 'X*Z' : V= F(X)*V(Z). The V(z) values are build in the same way as the 'ZZZ' case and the function F(X) is a simple function of X, which must be adapted by modifying its definition directly in the routine FUNVX. The default function is :

  .. math::  
  
     FUNVX(\hat{x}) = { 1 \over \cosh \left({ \hat{x} - \hat{x_0} \over zwidth } \right) }

  * 'X,Z' : V= G(X,Z). The function  G must also be adapted  by modifying its definition directly in the routine FUNVXZ. The default function is :
  
  .. math::   

     FUNVXZ(\hat{x},z) = { 1 \over \cosh \left(\left( { \hat{x} - \hat{x_0} \over zwidthx } \right) ^2 +  \left( { z - z_0 \over zwidthz } \right) ^2 \right) }
     
  .. note::     

     Notice that in this case the V(z) values given by the profile are not used.


* :code:`CTYPELOC` : Type of information used to give the localization of vertical profile :

  * 'IJGRID' for (i,j) point  on index space

  * 'XYHATM' for (x,y) coordinates on conformal plane or cartesian plane

  * 'LATLON' for (latitude,longitude) on spherical earth

* :code:`XLATLOC` : Latitude (in degrees) of the vertical profile localization (used in case CTYPELOC='LATLON') 

* :code:`XLONLOC` : Longitude (in degrees) of the vertical profile localization (used in case CTYPELOC='LATLON') 

* :code:`XXHATLOC` : position (in meters) x of the vertical profile localization (used in cases CTYPELOC='XYHATM') 

* :code:`XYHATLOC` :  position (in meters) y of the vertical profile localization (used in cases CTYPELOC='XYHATM') 

* :code:`NILOC` : position i in the physical domain  of the vertical profile localization (used in cases CTYPELOC='IJGRID'). If you use a 1D model, then NILOC is reset to 1 by the program.
                                         
* :code:`NJLOC` : position j in the physical domain of the vertical profile localization (used in cases CTYPELOC='IJGRID')  If you use a 1D or a 2D  model, then NJLOC is reset to 1 by the program.
