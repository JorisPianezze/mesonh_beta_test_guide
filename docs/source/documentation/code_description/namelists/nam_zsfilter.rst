.. _nam_zsfilter:

NAM_ZSFILTER
-----------------------------------------------------------------------------

.. csv-table:: NAM_ZSFILTER content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "NZSFILTER", "INTEGER", "1"
   "LHSLOP", "LOGICAL", ".FALSE."
   "XHSLOP", "REAL", "1.2"
   "NLOCZSFILTER", "INTEGER", "3"

* NZSFILTER : number of iterations of the spatial filter applied to smooth the orography over the whole domain (integer, 1 iteration removes the :math:`2\Delta x` signal, 50 % of the :math:`4\Delta x` signal, 25 % of the :math:`6\Delta x` signal, etc...).

.. note::

   The amplitude of the filtered signal for each wavelength :math:`\lambda\Delta x` is :
   
   .. math::
        
      \frac{1}{2}\left(\cos\left(\frac{2\pi}{\lambda}\right) + 1\right)

* LHSLOP : flag to use a spatial filter applied to smooth the orography locally over the slopes (along the horizontal directions) higher than XHSLOP.

* XHSLOP : slope threshold (:math:`\Delta z/\Delta x` and :math:`\Delta z/\Delta y`) where the local spatial filter is applied.

* NLOCZSFILTER : number of iterations of the local spatial filter applied to smooth the large slopes. If LHSLOP is TRUE, 3 new variables are written in the output files : ZS_FILTR ([2D] height variations of the orography by local filtering), ZSLOPEX and ZSLOPEY ([2D] orography slopes along i and j indexes respectively after local filtering).
