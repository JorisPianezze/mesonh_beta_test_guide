Cold bubble
============================================

Case description
*******************
This case tests the dynamics of the model in 2D on an idealized cold bubble falling with no initial wind.

Numerical setup
*****************

Steps
********
001_prep_ideal_case
002_mesonh

Options
********
The initial perturbation is set with


Physics 
- rayonnement
- LIMA...
(Cas réel : tracer la topo avec echelle commune à tous)

Output intéressants

Figures
***********
:download:`BOMEX.pdf <BOMEX.pdf>`.

Numerical ressources
***********************
.. csv-table:: Numerical ressources
   :header: "Node", "Core", "Timestep", "N° timestep", "Machine", "Compilation", "Version", "Elapsed time"
   :widths: 1, 1, 1, 1, 1, 1 , 1,1
   
      "1", "1","0.5s","1800","Ubuntu 24","gfortran O2", "5.7.1", ""
