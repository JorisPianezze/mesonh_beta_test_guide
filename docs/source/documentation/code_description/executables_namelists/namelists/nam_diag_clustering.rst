.. _nam_diag_clustering:

NAM_DIAG - Clustering
-----------------------------------------------------------------------------

.. csv-table::
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LCLSTR", "LOGICAL", ".FALSE."
   "LBOTUP", "LOGICAL", ".TRUE."
   "CFIELD", "CHARACTER(LEN=8)", "'CLOUD'"
   "XTHRES", "REAL", "0.00001"
   
* :code:`LCLSTR` : flag for 3D clustering

* :code:`LBOTUP` : to propagate clustering from bottom to top (when TRUE); otherwise from top to bottom

* :code:`CFIELD` : field on which clustering is applied, could be 'W' or 'CLOUD'

* :code:`XTHRES` : threshold value to detect the 3D structures

Following variables will be stored :

.. csv-table::
   :header: "Name", "Meaning [Unit]", "Dimension"
   :widths: 30, 30, 30
   
   "CLUSTERID", "identity number", "3D"
   "CLUSTERLV", "level where the object has been identified for the first time (at its bottom if LBOTUP is true, at its top otherwise)", "3D"
   "CLDSIZE", "horizontal section of the object at the current level", "3D"
 
.. note::
   
   Together, CLUSTERID and CLUSTERLV refers univoqually to a unique 3D object. Their value is homogeneous inside each identified object. CLOUDSIZE is homogeneous at each level inside each object.
  
