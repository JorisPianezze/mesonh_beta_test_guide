.. _nam_mean:

NAM_MEAN
-----------------------------------------------------------------------------

.. csv-table:: NAM_MEAN content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "LMEAN_FIELD","LOGICAL",".FALSE."
   "LCOV_FIELD","LOGICAL",".FALSE."
   "LUH_MAX","LOGICAL",".FALSE."
   "LMINMAX_MSLP","LOGICAL",".FALSE."
   "LMINMAX_VORT","LOGICAL",".FALSE."
   "LMINMAX_WINDFFTKE","LOGICAL",".FALSE."

* :code:`LMEAN_FIELD` : flag for computation of the mean and maximum values of variables between two backup outputs. The list of variables available can be modified in :file:`mean_field.f90`.

* :code:`LCOV_FIELD` : flag for computation of covariances values of variables between two backup outputs. The list of variables available can be modified in :file:`mean_field.f90`.

* :code:`LUH_MAX` : flag for computation of the maximum values between two backup outputs of the updraft helicity.

* :code:`LMINMAX_MSLP` : flag for computation of the minimum and maximum values between two backup outputs of the mean sea-level pressure.

* :code:`LMINMAX_VORT` : flag for computation of the minimum and maximum values between two backup outputs of the vorticities.

* :code:`LMINMAX_WINDFFTKE` : flag for computation of the minimum and maximum values between two backup outputs of the TKE at first level, 10 and 20 meters height; the wind gust (FF) at 10 and 20 meters and an AROME-like wind gust diagnostic.
