.. _nam_paspol:

NAM_PASPOL
-----------------------------------------------------------------------------

It contains the parameters to activate passive pollutants, by specifying the position and the kinetic of the release. 

.. csv-table:: NAM_PASPOL content
   :header: "Fortran name", "Fortran type", "Default value"
   :widths: 30, 30, 30

   "LPASPOL","LOGICAL","FALSE"
   "NRELEASE","INTEGER","0"
   "CPPINIT","ARRAY(100*CHARACTER(LEN=3))","100*'1PT'"
   "XPPLAT","ARRAY(100*REAL)","100*0.0"
   "XPPLON","ARRAY(100*REAL)","100*0.0"
   "XPPMASS","ARRAY(100*REAL)","100*0.0"
   "XPPBOT","ARRAY(100*REAL)","100*0.0"
   "XPPTOP","ARRAY(100*REAL)","100*0.0"
   "CPPT1","ARRAY(100*CHARACTER(LEN=14))","100*'20010921090000'"
   "CPPT2","ARRAY(100*CHARACTER(LEN=14))","100*'20010921090000'"
   "CPPT3","ARRAY(100*CHARACTER(LEN=14))","100*'20010921091500'"
   "CPPT4","ARRAY(100*CHARACTER(LEN=14))","100*'20010921091500'"

* :code:`LPASPOL` : Flag to activate passive pollutants                                            

* :code:`NRELEASE` : Number of releases (up to 100).                                                                                                    

* :code:`CPPINIT` : Type of initialization of the source ('1PT' or '9PT')          

* :code:`XPPLAT` : Latitude of the release
                    
* :code:`XPPLON` : Longitude of the release                      

* :code:`XPPMASS` : Released mass (in g)                         

* :code:`XPPBOT` : Height of the bottom of the release (in m)          

* :code:`XPPTOP` : Height of the top of the release (in m)        

* :code:`CPPT1` : Starting date of the release (in YYYYMMDDHHMMSS)        

* :code:`CPPT2` : Starting date of the constant rate (in YYYYMMDDHHMMSS)        

* :code:`CPPT3` : Ending date of the constant rate (in YYYYMMDDHHMMSS)        

* :code:`CPPT4` : Ending date of the release (in YYYYMMDDHHMMSS)        

