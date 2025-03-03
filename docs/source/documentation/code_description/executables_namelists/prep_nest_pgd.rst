PREP_NEST_PGD
*****************************************************************************

In order to run models with the gridnesting technique, a condition on the orography must be satisfied. In the following, if file #2 is completely included in (and therefore in interaction during the run with) file #1, file #2 will be called the SON file, and file #1 the DAD file. In the following, the DAD file number must be smaller than any of its SON number. The condition on the orography is: "the mean of orography for a SON file in the domain corresponding to the grid mesh of its DAD file, must be equal to the orography of the DAD file in this mesh". Such a condition is not automatically satisfied when using enhanced orographies. The program PREP_NEST_PGD performs post-treatments on the orographies of up to 8 PGD files that will be used to create initialization files for a gridnested run. It modifies the orography of a DAD from the mean of the orography of its (several) SON(s).

.. csv-table:: PREP_NEST_PGD program and its corresponding namelist and function
   :header: "Executable", "Namelist", "Function"
   :widths: 30, 30, 30

   "PREP_NEST_PGD", "PRE_NEST_PGD1.nam", "Prepare surface file when grid nesting is used"

