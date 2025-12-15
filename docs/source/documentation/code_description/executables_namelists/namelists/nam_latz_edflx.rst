.. _nam_latz_edflx:

NAM_LATZ_EDFLX
-----------------------------------------------------------------------------

.. csv-table:: NAM_LATZ_EDFLX content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LUV_FLX","LOGICAL",".FALSE."
   "XUV_FLX1","REAL","3.E+14"
   "XUV_FLX2","REAL","0"
   "LTH_FLX","LOGICAL",".FALSE."
   "XTH_FLX","REAL","0.75"

* :code:`LUV_FLX` : to activate eddy flux for the UV flux

* :code:`XUV_FLX1` : Coefficient in the formulation of the UV flux (m3). It gives the magnitude of u'v' the eddy flux. If 0, there is no UV flux The UV flux mimics the meridional transports of momentum associated with eddies  not taken into account in a 2D  meridional vertical model.

* :code:`XUV_FLX2` : Coefficient in the formulation of the UV flux. Add a miminum constant value to the u'v' flux. 

* :code:`LTH_FLX` : to activate eddy flux for the theta flux

* :code:`XTH_FLX` : Coefficient in the formulation of the theta flux. It gives the magnitude of the v'T' and W'T' eddy flux. If 0, there is no theta flux The theta flux mimics the meridional transports of potential temperature associated with eddies not taken into account in a 2D model.
