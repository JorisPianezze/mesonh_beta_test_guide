.. _nam_condsamp:

NAM_CONDSAMP
-----------------------------------------------------------------------------


It contains the parameters to activate conditional sampling (Couvreux et al., 2010). The first tracer is released at the surface, the second one is released XHEIGHT_BASE below the cloud base on XDEPTH_BASE depth the third one is released XHEIGHT_TOP above the cloud top on XDEPTH_TOP depth.

.. csv-table:: NAM_CONDSAMP content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LCONDSAMP","LOGICAL",".FALSE."
   "NCONDSAMP","INTEGER","3"
   "XRADIO","ARRAY(REAL)","3*900.0"
   "XSCAL","ARRAY(REAL)","3*1.0"
   "XHEIGHT_BASE","REAL","100.0"
   "XDEPTH_BASE","REAL","100.0"
   "XHEIGHT_TOP","REAL","100.0"
   "XDEPTH_TOP","REAL","100.0"
   "NFINDTOP","INTEGER","0"
   "XTHVP","REAL","0.25"
   "LTPLUS","LOGICAL",".TRUE."

* :code:`LCONDSAMP` : Flag to activate conditional sampling

* :code:`NCONDSAMP` : Number of conditional samplings

* :code:`XRADIO` : Period of radioactive decay                                    

* :code:`XSCAL` : Scaling factor                               

* :code:`XHEIGHT_BASE` : Height below the cloud base where the 2nd tracer is released

* :code:`XDEPTH_BASE` : Depth  on which the 2nd tracer is released

* :code:`XHEIGHT_TOP` : Height above the cloud top where the 3rd tracer is released

* :code:`XDEPTH_TOP` : Depth on which the 3rd tracer is released

* :code:`NFINDTOP` : Method for identifying the altitude where the 3rd tracer is released :

  * 0 (by default) : the top tracer is released above the cloud top
  * 1 : the top tracer is released above the layer with the maximum gradient of potential temperature (by default if no clouds)
  * 2 : the top tracer is released at the first layer from the surface where the virtual potential temperature exceeds its bottom-up integration plus a threshold XTHVP (by default 0.25K)

* :code:`XTHVP` : Threshold (in Kelvin) to identify the boundary-layer top based on virtual potential temperature (if NFINDTOP = 2)

* :code:`LTPLUS` : Flag to allow the release of 2nd and 3rd tracers one layer below the cloud base and one level above the PBL top (when the layers of emission are not detected)
