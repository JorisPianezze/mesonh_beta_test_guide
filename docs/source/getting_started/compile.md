# Compile {#compilation}

## Principle

During the first Meso-NH compilation, almost all the numerical schemes
and all the physical parameterizations are compiled. The numerical
scheme and physical parameterizations are then chosen in
`namelists <executables_and_namelists>`{.interpreted-text role="ref"}
files during program executions. In the Meso-NH language, we say that we
compile the **MASTER**. This compilation is quite long, typically more
than 20 minutes on one core.

When you want to modify the Meso-NH code, you need to create a directory
containing the modified code and then compile it. In the Meso-NH
language, we say that we compile a **VER_USER**. This compilation is
shorter than the **MASTER** one, it depends on how many sources are
modified but you need to compile the **MASTER** before a **VER_USER**.

:::: note
::: title
Note
:::

If you are in a hurry to compile Meso-NH please go to
`compilation <compilation_on_different_systems>`{.interpreted-text
role="ref"} section.
::::

The following lines are just for your information, especially if you are
interested in understanding how Meso-NH compilation works. For the
**MASTER** compilation, you will use following commands:

``` bash
cd ~/MNH-VX-Y-Z/src
./configure
export MAKEFLAGS='-j 8' # optional, to speed up the compilation on up to 8 processes/cores
. ../conf/profile_mesonh
make
make installmaster
```

For the **VER_USER** compilation, you will use following commands:

``` bash
cd ~/MNH-VX-Y-Z/src
export VER_USER=NAME_OF_THE_DIRECTORY_CONTAINING_THE_MODIFIED_CODE
./configure
export MAKEFLAGS='-j 8' # optional, to speed up the compilation on up to 8 processes/cores
. ../conf/profile_mesonh
make user
make installuser
```

:::: note
::: title
Note
:::

- `configure`{.interpreted-text role="file"}, script that creates a
  `configuration`{.interpreted-text role="ref"} file
  `profile_mesonh`{.interpreted-text role="file"} in the
  `conf/ <what_do_you_download>`{.interpreted-text role="ref"} directory
  with an extension reflecting the different choices made.
- `export MAKEFLAGS='-j 8'`, optional command to speed up the
  compilation on up to 8 parallel processes. You can change the number
  of processes according to the number of cores available for the
  compilation. If you do not set this variable, the default value is 1
  process.
- `make`{.interpreted-text role="file"}, command that compiles the code
- `make installmaster`{.interpreted-text role="file"}, command that
  links the compiled executables in the
  `exe/ <what_do_you_download>`{.interpreted-text role="ref"} directory
  (cf
  `List of compiled executables <executables_and_namelists>`{.interpreted-text
  role="ref"}). Need to be done only one time by \"version\".
::::

:::: note
::: title
Note
:::

- The object files `*.o`{.interpreted-text role="file"} and main
  executables of the Meso-NH package are compiled in one step and
  created in the directory src/dir_obj-your_configuration/
- the `lib.*.a`{.interpreted-text role="file"} is only created and
  removed at the link phase. This allows a parallel compilation of the
  sources.
- The name \"dir obj\...\" depends on the different environment
  variables set by the `profile_mesonh`{.interpreted-text role="file"}
  that you have loaded before the compilation. This allows to compile in
  the same source/installation directory different versions of Meso-NH
  with different compilers, versions of MPI, \...
::::

:::: note
::: title
Note
:::

To get information about the compiled executables, go to
`executables_and_namelists`{.interpreted-text role="ref"}.
::::

## Compile on different systems {#compilation_on_different_systems}

On `Jean-Zay (IDRIS) <compilation_jeanzay_idris>`{.interpreted-text
role="ref"},
`Adastra (CINES) <compilation_adastra_cines>`{.interpreted-text
role="ref"}, `Irene (TGCC) <compilation_irene_tgcc>`{.interpreted-text
role="ref"}, `ECMWF <compilation_hpc_ecmwf>`{.interpreted-text
role="ref"},
`belenos (Meteo-France) <compilation_belenos_meteofrance>`{.interpreted-text
role="ref"} and some other machines, the compiler, libraries and
optimisation settings are automatically chosen during the compilation
procedure.

:::: note
::: title
Note
:::

If necessary, these settings can be modified (see
`Compilation on other systems <compilation_unknown_computer>`{.interpreted-text
role="ref"}).
::::

:::: tip
::: title
Tip
:::

To check if the machine you are using is supported by Meso-NH look at
the `case`{.interpreted-text role="command"} condition in the
`configure`{.interpreted-text role="file"} script and search your
configuration. If your configuration is not referenced you have to go to
`compile on other systems <compilation_unknown_computer>`{.interpreted-text
role="ref"} section and adapt the `configure`{.interpreted-text
role="file"} script.
::::

The various steps for compiling Meso-NH on the machines used by main
Meso-NH\'s users are referenced in the following sections.

### On Jean-Zay (IDRIS) {#compilation_jeanzay_idris}

The compilation can be done interactively using the following commands:

``` {.bash substitutions=""}
cd |MNH_directory_extract_current|/src
./configure
. ../conf/profile_mesonh-LXifort-R8I4-MNH-V|MNH_xyz_version_hyphen_current|-MPIINTEL-O2
make -j16 |& tee error$XYZ
make installmaster
```

You can also use the \'compil\' partition:

``` {.bash substitutions=""}
cd |MNH_directory_extract_current|/src
./configure
sbatch job_make_mesonh_HPE_jeanzay
```

To run the test case examples, do:

``` {.bash substitutions=""}
cd |MNH_directory_extract_current|/src
sbatch -A your_projet.at.cpu job_make_examples_BullX_jeanzay
```

### On Adastra (CINES) {#compilation_adastra_cines}

Install the Meso-NH package in your \$HOME (default 50GB of quota) and
compile in interactive mode:

``` {.bash substitutions=""}
cd |MNH_directory_extract_current|/src
./configure
. ../conf/profile_mesonh-LXifort-R8I4-MNH-V|MNH_xyz_version_hyphen_current|-MPIINTEL-O2
make -j16 |& tee error$XYZ
make installmaster
```

To run the test case examples, do:

``` bash
sbatch job_make_examples_BullX_occigen
```

### On Irene (TGCC) {#compilation_irene_tgcc}

:::: warning
::: title
Warning
:::

Before compiling you need to go to your project data space :

``` bash
module switch dfldatadir/your_project_name
```
::::

+-------------+-------------+--------------+-----------------+---------------+
|             | Homedir     | Workdir      | Scratchdir      | Storedir      |
+=============+=============+==============+=================+===============+
| Location    | \$CCCHOME   | \$CCCWORKDIR | \$CCCSCRATCHDIR | \$CCCSTOREDIR |
+-------------+-------------+--------------+-----------------+---------------+
| Disk space  | 20 Go /     | 5 To         | > 100 To        | Unlimited     |
|             | user        |              |                 |               |
+-------------+-------------+--------------+-----------------+---------------+
| Data        | Saved       | Not saved    | Purged (60      | Saved on      |
| lifetime    |             |              | days)           | disk/band     |
+-------------+-------------+--------------+-----------------+---------------+

: Filesystem of Irene (project data space)

:::: tip
::: title
Tip
:::

We recommend to install Meso-NH on your Homedir, run the simulation on
the Workdir and store the files in Storedir.
::::

On Irene you can compile in interactive mode using:

``` {.bash substitutions=""}
cd |MNH_directory_extract_current|/src
./configure
. ../conf/profile_mesonh-LXifort-R8I4-MNH-V|MNH_xyz_version_hyphen_current|-AMD-MPIAUTO-O2
make -j16 |& tee error$XYZ
make installmaster
```

:::: note
::: title
Note
:::

To verify your compilation you can run test case examples with:

``` bash
ccc msub job_make_examples_BullX_irene_AMD
```
::::

### On hpc-login (ECMWF) {#compilation_hpc_ecmwf}

To compile Meso-NH package, go to the \$HPCPERM directory, connect to an
interactive compute node and compile the code:

``` bash
ecinteractive -c16 -m 16G -t 12:00:00
./configure
. ../profile_mesonh
make
make installmaster
```

To run test case examples, do :

``` bash
sbatch job_make_examples_Atos_HPCF
```

### On Belenos (Meteo-France) {#compilation_belenos_meteofrance}

  --------------------------------------------------------------------------
                 Homedir        Workdir        Scratchdir     Storedir
  -------------- -------------- -------------- -------------- --------------
  Location       \$HOME         \$WORKDIR      $\emptyset$    ftp/telnet
                                                              hendrix

  Disk space     50 Go / user   Unlimited      $\emptyset$    Unlimited

  Data lifetime  Saved          Few days       $\emptyset$    Saved on
                                                              disk/band
  --------------------------------------------------------------------------

  : Filesystem of Belenos

:::: tip
::: title
Tip
:::

We recommend to install Meso-NH on your Homedir, run the simulation on
the Workdir and store the files in hendrix at the end of your
simulation. **A robot cleans the workdir very regularly**.
::::

Due to limitation in time and memory in interactive shell, Meso-NH has
to be compiled in batch mode:

``` {.bash substitutions=""}
cd |MNH_directory_extract_current|/src
./configure
sbatch job_make_mesonh_BullX_belenos
```

:::: note
::: title
Note
:::

To verify your compilation you can run test case examples with:

``` bash
sbatch job_make_examples_BullX_belenos
```
::::

### On Datarmor (IFREMER) {#compilation_datarmor_ifremer}

:::: note
::: title
Note
:::

You can find Datarmor documentation
[here](https://w3z.ifremer.fr/intraric/Mon-IntraRIC/Calcul-scientifique/Datarmor),
only available on IFREMER intranet.
::::

  --------------------------------------------------------------------------
                 Homedir        Workdir        Scratchdir     Storedir
  -------------- -------------- -------------- -------------- --------------
  Location       \$HOME         \$DATAWORK     \$SCRATCH      

  Disk space     50 Go / user   1 To / group   10 To / group  

  Data lifetime  Saved          Unsaved        15 days        
  --------------------------------------------------------------------------

  : Filesystem of Datarmor

:::: tip
::: title
Tip
:::

We recommend to install Meso-NH on your Homedir, run the simulation on
the Workdir or the Scratchdir.
::::

On Datarmor you can compile in interactive mode using:

``` {.bash substitutions=""}
cd |MNH_directory_extract_current|/src
./configure
. ../conf/profile_mesonh
make
make installmaster
```

:::: note
::: title
Note
:::

To verify your compilation you can run test case examples with:

``` bash
cd MY_RUN/KTEST
./run_all_KTESTPACK
```
::::

### On Olympe (CALMIP) {#compilation_olympe_calmip}

:::: note
::: title
Note
:::

You can find Olympe documentation
[here](https://www.calmip.univ-toulouse.fr/espace-utilisateurs/doc-technique-olympe).
::::

  -----------------------------------------------------------------------------------------------
                 Homedir                  Workdir         Scratchdir     Storedir
  -------------- ------------------------ --------------- -------------- ------------------------
  Location       /users/\$GROUPE/\$USER   /tmdir/\$USER   $\emptyset$    /store/\$GROUPE/\$USER

  Disk space     5 Go / user              Unlimited       $\emptyset$    1 To / group

  Data lifetime  Saved                    100 days        $\emptyset$    Saved
  -----------------------------------------------------------------------------------------------

  : Filesystem of Olympe

:::: tip
::: title
Tip
:::

We recommend to install Meso-NH on your Homedir, run the simulation on
the Workdir and store the files in storedir.
::::

On Olympe you can compile in interactive mode using:

``` {.bash substitutions=""}
cd |MNH_directory_extract_current|/src
./configure
. ../conf/profile_mesonh
make
make installmaster
```

:::: note
::: title
Note
:::

To verify your compilation you can run test case examples with:

``` bash
sbatch job_make_examples_BullX_olympe
```
::::

### On Nuwa (OMP) {#compilation_nuwa_omp}

:::: note
::: title
Note
:::

You can find nuwa documentation [here](http://nuwa.aero.obs-mip.fr/).
::::

  ----------------------------------------------------------------------------
                 Homedir        Workdir          Scratchdir     Storedir
  -------------- -------------- ---------------- -------------- --------------
  Location       /home/\$USER   /mesonh/\$USER   $\emptyset$    $\emptyset$

  Disk space     Unlimited      Unlimited        $\emptyset$    $\emptyset$

  Data lifetime  Unsaved        Unsaved          $\emptyset$    $\emptyset$
  ----------------------------------------------------------------------------

  : Filesystem of Nuwa

:::: tip
::: title
Tip
:::

We recommend to install Meso-NH on your Homedir and run the simulation
on the Workdir.
::::

On Nuwa you can compile in interactive mode using:

``` {.bash substitutions=""}
cd |MNH_directory_extract_current|/src
./configure
. ../conf/profile_mesonh
make
make installmaster
```

:::: note
::: title
Note
:::

To verify your compilation you can run test case examples with:

``` bash
cd MY_RUN/KTEST
./run_all_KTESTPACK
```
::::

### On other systems {#compilation_unknown_computer}

If you are installing Meso-NH on an unknown computer (not predefined in
the `configure`{.interpreted-text role="file"} script), there are 3 main
environment variables that can be set to configure the Meso-NH package:

- \`ARCH\`: the architecture to use (OS + compiler, default is
  [LXgfortran]{.title-ref} for Linux with gfortran compiler)
- \`VER_MPI\`: the version of MPI to use (default is
  [MPIVIDE]{.title-ref} for no parallel run)
- \`OPTLEVEL\`: the level of optimization for the compiler (default is
  [DEBUG]{.title-ref} for development purpose, debugging and fast
  compilation)

If needed, you can change the default values of these environment
variables. For example, if you want to use the Intel compiler
[ifx]{.title-ref} with the Intel MPI library and an optimisation level
of [-O2]{.title-ref}, you can run the following commands:

``` bash
export ARCH=LXifx
export VER_MPI=MPIAUTO
export OPTLEVEL=O2
./configure
```

:::: note
::: title
Note
:::

- The options specific to the architecture and compiler such as
  [OPTLEVEL]{.title-ref} are defined inside the
  `Rules.${ARCH}.mk`{.interpreted-text role="file"} files.
- The options specific to the MPI library ([VER_MPI]{.title-ref}) are
  defined inside [Makefile.MESONH.mk]{.title-ref}
- There are also options for the netCDF library (see the
  [VER_CDF]{.title-ref} variable). [CDFAUTO]{.title-ref}, the
  recommended and default option, compiles and uses the netCDF library
  included in the Meso-NH package.
- If needed, for adaptation to your requirements, look inside the files
  and changes options.
::::

Compile the code :

``` bash
. ../conf/profile_mesonh-your_configuration
export MAKEFLAGS='-j 8' # optional, to speed up the compilation on up to 8 processes/cores
make
make installmaster
```

:::: tip
::: title
Tip
:::

- The compilation takes about 20 minutes on one core. To speedup the
  compilation, set the environment variable [MAKEFLAGS]{.title-ref} to
  the number of cores you want to use.

- If you do not have sufficient space in your \$HOME directory, install
  the whole package directly on the \$WORKDIR. The name of the \$WORKDIR
  differs in the differents computer centers.

  :::: warning
  ::: title
  Warning
  :::

  Consider backing up your installation. The \$WORKDIR space is not
  typically backed up, and on some systems, it may be purged after a
  while. File system failures with file loss can occur.
  ::::

- Due to limitation in time and memory on the interactive shell of some
  systems, you could have to compile the Meso-NH package in batch mode.
  Jobs are provided for some computers in the different
  `src/job_make_mesonh*`{.interpreted-text role="file"} files.
::::

## Clean previous compiled version

If you have already compiled the same version of Meso-NH on this
computer (same \$XYZ value), you first have to clean it with:

``` bash
make cleanmaster
```

:::: note
::: title
Note
:::

This will delete the dir-obj\$XYZ directory content with all the
preprocessed sources contained in it.
::::

## Compile with additional libraries

It\'s possible to compile Meso-NH with additionnal libraries like
FOREFIRE, RTTOV, ECRAD, MEGAN, OASIS\... In the following subsections
you will find information to compile Meso-NH with these libraries.

### ForeFire runs (external package needed)

ForeFire is an open-source code for wildland fire spread models. The
interface to this tool is already compiled in Méso-NH (from version
6.0.0).

The
`<a href="https://github.com/forefireAPI/firefront.git" target="_blank">FOREFIRE API</a>`{=html}
package must be compiled independently of Méso-NH. It can be cloned
with:

``` bash
git clone https://github.com/forefireAPI/firefront.git
```

It depends on netCDF and scons for its compilation. The
`libForeFIre.so`{.interpreted-text role="file"} that has been generated
must be referenced either by adding its path to the LD_LIBRARY_PATH
environment variable or by moving or linking it to the
`exe/`{.interpreted-text role="file"} directory of Meso-NH.

### MNH_RTTOV for optional radiative computation {#compile_mesonh_with_rttov}

The RTTOV 13.2 package was not included into the open source version of
Meso-NH because it needs a licence agrement. Run the \"configure\"
script preceded with the setting of the MNH_RTTOV variable:

``` bash
cd MNH/src/
export MNH_RTTOV=1
export VER_RTTOV=13.2
```

Download the RTTOV package `rttov132.tar.xz`{.interpreted-text
role="file"} by following the instructions given on the RTTOV website.
Install the RTTOV package `rttov132.tar.xz`{.interpreted-text
role="file"}:

``` bash
cd MNH/src/LIB
mkdir RTTOV-13.2
cd RTTOV-13.2
tar xJf rttov132.tar.xz
cd build
```

edit `Makefile.local`{.interpreted-text role="file"} and set
HDF5_PREFIX, FFLAGS_HDF5 and LDFLAGS_HDF5 as shown below:

``` bash
HDF5_PREFIX = $(SRC_MESONH)/src/dir_obj${XYZ}/MASTER/NETCDF-${VERSION_CDFF}
FFLAGS_HDF5 = -D_RTTOV_HDF $(FFLAG_MOD)$(HDF5_PREFIX)/include
LDFLAGS_HDF5 = -L$(HDF5_PREFIX)/lib64 -lhdf5hl_fortran -lhdf5_hl -lhdf5_fortran -lhdf5 -lsz -laec -lz -ldl
```

and build RTTOV:

``` bash
cd src
../build/Makefile.PL RTTOV_HDF=1
make ARCH=ifort
```

:::: note
::: title
Note
:::

Other available options are gfortran, NAG, pgf90 and IBM.
::::

Then, you can follow the steps described in the section dedicated to
your computer (interactive or batch mode).

### MNH_ECRAD for optional compilation of new ECRAD radiative library from ECMWF

The default version of ECRAD is 1.4.0 (open-source) and is provided in
the Meso-NH package. To use ECRAD, do:

``` bash
export MNH_ECRAD=1
./configure
```

The version of ECRAD is set by (by default):

``` bash
export VER_ECRAD=140
```

If you want to use a different version of ECRAD, you can set the
environment variable [VER_ECRAD]{.title-ref} to the desired version
number. But you must have the corresponding ECRAD package installed in
the Meso-NH source directory.

:::: note
::: title
Note
:::

ECRAD has been tailored to Meso-NH. The modified files are included in
the directory
`${SRC_MESONH}/src/LIB/RAD/ecrad-1.4.0_mnh`{.interpreted-text
role="file"}.
::::

To compile Meso-NH with ECRAD, you can follow the steps described in the
section dedicated to your computer (interactive or batch mode). To use
ECRAD during a simulation, replace RAD='ECMW' by RAD='ECRA' in
EXSEG1.nam and add link to all "ecrad-1.X.X/data" files in your Meso-NH
run directory:

``` bash
ln -sf ${SRC_MESONH}/src/LIB/RAD/ecrad-1.X.X/data/* .
```

:::: tip
::: title
Tip
:::

You can replace CDATADIR = "." by CDATADIR = "data" of ini radiations
ecrad.f90 to link only the data folder instead of all the files one by
one. See `MY_RUN/KTEST/007_16janvier/008_run2`{.interpreted-text
role="file"} test case for example.
::::

### MNH_MEGAN for optional compilation of MEGAN code

To use MEGAN, do:

``` bash
export MNH_MEGAN=1
./configure
```

To compile Meso-NH with MEGAN, you can follow the steps described in the
section dedicated to your computer (interactive or batch mode).

## Compile with modified and/or new sources

Once the MASTER is compiled, you can can compile your own sources.

### Prepare your source directory

Suppose you want to create a MY_MODIF version of Meso-NH. First, put
your own sources in a subdirectory `src/MY_MODIF`{.interpreted-text
role="file"}. All subdirectories in MY_MODIF will be scanned during the
compilation process. So if you want, you could make a subdirectory for
each component of the Meso-NH package, for example:

``` bash
cd MY_MODIF
mkdir MNH
mkdir SURFEX
cp ../MNH/mesonh.f90 MNH/
cp ../SURFEX/isba.f90 SURFEX/
```

:::: caution
::: title
Caution
:::

In this subdirectory, put only fortran source you want to compile.
Don\'t use it as a trash with old sources file like
`mysource.f90.old`{.interpreted-text role="file"} or
`tar`{.interpreted-text role="file"} files. All unexpected file types
could confuse the `make`{.interpreted-text role="file"} command.
::::

### Configure with modified sources

Logout of the current session to be sure to unset all the environment
variables loaded with the your MASTER `profile_mesonh`{.interpreted-text
role="file"}. Login again and:

- set the environment variable VER USER to the name of your user
  directory (MY_MODIF, for example),
- set also the optional environment variable ARCH, VER MPI\... you want
  to use (they need to be the same as the MASTER)

and run again the `configure`{.interpreted-text role="file"} command:

``` bash
export VER_USER=MY_MODIF
./configure
```

This generates a `profile_mesonh`{.interpreted-text role="file"} file
with the VER_USER information.

### Compile with modified sources

Now, you can compile with the `make user`{.interpreted-text role="file"}
command in interactive with:

``` bash
. ../conf/profile_mesonh...${VER_USER}...
make user
make installuser
```

or in batch mode using a script located in src/ directory with user in
its name.

:::: note
::: title
Note
:::

- This will compile only your sources and the files depending on your
  sources and generate the new executables in the directory
  `dir_obj-your_configuration/${VER_USER}`{.interpreted-text
  role="file"}

- The \"make installuser\" needs to be done only one time by version.
  When you run the examples, your version should appear in the name of
  the used executables.

- Before compiling your own sources be sure that these ones are younger
  than the \"\*.o\" files of the MASTER directory. If any doubt, at any
  time use the command on your sources ,and only on yours:

  ``` bash
  touch your_files
  ```
::::
