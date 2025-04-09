.. _ibm_gene:

ibm_gene.obj
-----------------------------------------------------------------------------

The ibm_gene.obj file contains the information of the triangles constituting the faces of the obstacles. The .obj file must have a particular organization:

* A line with ’usemtl’ indicates the two materials of each side of the interface. Only the faces with their external face in contact with the outside air are read (mat2=air).

* A line starting with ’v’ indicates the location (x,y,z coordinates) of a triangle vertex.

* A line starting with ’f’ indicates the vertex constituting one triangle.

.. code-block::

   usemtl mat1:mat2
   v xv1 yv1 zv1
   v xv2 yv2 zv2
   v xv3 yv3 zv3
   v xv4 yv4 zv4
   f 1 2 3
   f 1 3 4
   usemtl mat3:mat2
   v xv5 yv5 zv5
   v xv6 yv6 zv6
   v xv7 yv7 zv7
   v xv8 yv8 zv8
   f 5 6 7
   f 5 7 8
  
In the above example, the first triangle is formed by vertex numbers 1, 2, 3 and the second by vertex numbers 1, 3, 4. The two triangles form the interface mat1:mat2. The interface mat3:mat2 is defined by two other triangles. The vertex number increment starts at the first vertex defined in the file. 
There are numerous other ways to write an .obj file. For instance, the normal or the texture of the faces can be defined. For the sake of simplicity only material (’usemtl’), vertex coordinates (’v’) and face definition (’f’) are considered in Meso-NH. The face normal is computed directly in the code and the face texture is irrelevant in the present version of the code.
