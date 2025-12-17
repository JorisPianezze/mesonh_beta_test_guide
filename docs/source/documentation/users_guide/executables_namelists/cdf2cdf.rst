CDF2CDF
***************************************************************************** 

.. warning::
   
   A adapter avec la 6.0.0
   
This executable is used to manipulate netcdf output files of Meso-NH. It allows to extract variables or concatenate files when they are split vertically (cf :ref:`nam_confz`).

.. code-block:: fortran

   Usage : lfi2cdf [-h --help] [-l] [-v --var var1[,...]] [-r --reduce-precision]
                   [-m --merge number_of_z_levels] [-s --split] [-o --output output-file.nc]
                   [-R --runmode mode] [-V --verbose] [-f --fallback-file fallback-file]
                   [-c --compress compression_level] input-file.lfi
           cdf2cdf [-h --help] [-v --var var1[,...]] [-r --reduce-precision]
                   [-m --merge number_of_split_files] [-s --split] [-o --output output-file.nc]
                   [-R --runmode mode] [-V --verbose] [-f --fallback-file fallback-file]
                   [-c --compress compression_level] input-file.nc
           cdf2lfi [-o --output output-file.lfi] [-R --runmode mode]  [-V --verbose]
                   [-f --fallback-file fallback-file] input-file.nc
 
   Options:
     --compress, -c compression_level
        Compress data. The compression level should be in the 1 to 9 interval.
        Only supported with the netCDF format (cdf2cdf and lfi2cdf only)
     -f --fallback-file fallback-file
        File to use to read some grid information if not found in input-file
     --help, -h
        Print this text
     --list, -l
        List all the fields of the LFI file and returns (lfi2cdf only)
     --merge, -m number_of_split_files
        Merge files which are split by vertical level (cdf2cdf and lfi2cdf only)
     --output, -o
        Name of file for the output
     --reduce-precision, -r
        Reduce the precision of the floating point variables to single precision (cdf2cdf and lfi2cdf only)
     --runmode, -R
        Force runmode (lfi2cdf, cdf2cdf or cdf2lfi)
     --split, -s
        Split variables specified with the -v option (one per file) (cdf2cdf and lfi2cdf only)
     --var, -v var1[,...]
        List of the variable to write in the output file. Variables names have to be separated by commas (,).
        A variable can be computed from the sum of existing variables (format: new_var=var1+var2[+...])
        (cdf2cdf and lfi2cdf only)
     --verbose, -V
        Be verbose (for debugging purpose)
