.. _nam_diag_coarse_graining:

NAM_DIAG - Coarse graining
-----------------------------------------------------------------------------
  
.. csv-table::
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LCOARSE", "logical", ".FALSE."
   "NDXCOARSE", "integer", "1"
 
* LCOARSE: flag to compute TKE (summation of the gridscale and the subgridscale parts) using coarse graining by both block and moving average

* NDXCOARSE: number of gridpoints over which the averaging is done

Following variables will be stored :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30

   "TKE_BLOCKAVGxx", "TKE averaged block by block", "3D"
   "TKE_MOVINGAVGxx", "TKE averaged over a moving block", "3D"
   
.. note::

   The suffix xx stands for the number NDXCOARSE.
