.. _nam_nudgingn:

NAM_NUDGINGn
-----------------------------------------------------------------------------

It contains the parameters needed for nudging of U, V, W, TH and Rv fields of model n towards large scale values. They are included in the declarative module MODD_NUDGINGn.

.. csv-table:: NAM_NUDGINGn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LNUDGING","LOGICAL",".FALSE."
   "XTNUDGING","REAL","21600.0"

* :code:`LNUDGING` : flag to activate nudging for model n.

* :code:`XTNUDGING` : time scale for nudging towards Large Scale values.
