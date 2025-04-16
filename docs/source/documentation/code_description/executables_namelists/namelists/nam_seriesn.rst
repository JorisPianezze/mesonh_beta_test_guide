.. _nam_seriesn:

NAM_SERIESn
-----------------------------------------------------------------------------

.. csv-table:: NAM_SERIESn content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30
   
   "NIBOXL","INTEGER","1"
   "NIBOXH","INTEGER","1"
   "NJBOXL","INTEGER","1"
   "NJBOXH","INTEGER","1"
   "NKCLS","INTEGER","1"
   "NKCLA","INTEGER","1"
   "NKLOW","INTEGER","1"
   "NKMID","INTEGER","1"
   "NKUP","INTEGER","1"
   "NBJSLICE","INTEGER","1"
   "NJSLICEL","ARRAY (20*INTEGER)","20*1"
   "NJSLICEH","ARRAY (20*INTEGER)","20*1"
   "NFREQSERIES","INTEGER","43200/(100*60)=7"

* :code:`NIBOXL`, :code:`NIBOXH`, :code:`NJBOXL`, :code:`NJBOXH` : lower and upper indexes along x and y axes, respectively, of the horizontal box used to average the series (t) and (z,t) in physical domain

* :code:`NKCLS`, :code:`NKCLA` : K level in physical domain respectively in the CLS and CLA ((x,t) series of U, Rv, Rr at KCLS and W at KCLA are stored).

* :code:`NKLOW`, :code:`NKUP` : two K levels in physical domain ((x,t) series of mean W between KLOW and KUP and mean Rc between the ground and KUP are stored).

* :code:`NKMID` : a K level in physical domain ((x,t) serie of Rv at KMID is stored).

* :code:`NBJSLICE` : number of y-slices for (x,t) serie.

* :code:`NJSLICEL`, :code:`NJSLICEH` : lower and higher index along y axe for the y-slices in physical domain.

* :code:`NFREQSERIES` : Temporal frequency of diagnostic writing (in time step unit).                    

