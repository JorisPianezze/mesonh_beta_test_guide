How to add surfex variables in outputs ?
==========================================

First, you need to know which kind of variable you want to save in output files. It can be :

* Global SURFEX variable on atmospheric grid 

* Global SURFEX variable on tile grid
 
* Local SURFEX variable on atmospheric grid

* Local SURFEX variable on tile grid

Example of global SURFEX variable
---------------------------------------

.. code-block:: fortran

   SUBROUTINE IO_Field_user_write( TPOUTPUT, KTCOUNT )
   !
   USE MODD_BLANK_n
   USE MODD_DYN_n,        ONLY: XTSTEP
   USE MODD_FIELD_n,      ONLY: XUT, XVT, XRT, XTHT, XSVT
   USE MODD_NSV,          ONLY: NSV
   USE MODD_PARAMETERS,   ONLY: JPVEXT
   USE MODD_PRECIP_n,     ONLY: XINPRR
   USE MODD_MNH_SURFEX_n, ONLY: YSURF_CUR
   USE MODD_IO_SURF_MNH
   !
   USE MODI_DIAG_SURF_ATM_N
   !
   IMPLICIT NONE
   !
   TYPE(TOUTBAK),    INTENT(IN)  :: TPOUTPUT !Output structure
   INTEGER, INTENT(IN)           :: KTCOUNT
   !
   TYPE(TFIELDMETADATA) :: TZFIELD
   !
   INTEGER                :: IKB
   REAL, DIMENSION(:,:), ALLOCATABLE :: ZWORK

   IF ( (KTCOUNT .GT. 1) .AND. (YSURF_CUR%DUO%N2M .GE. 1) ) THEN

     CALL DIAG_SURF_ATM_n(YSURF_CUR,'MESONH')

     ALLOCATE(ZWORK(NIU,NJU)) 
     ZWORK(:,:) = 0.0

     ZWORK(NIB:NIE+2*NHALO,NJB:NJE+2*NHALO) = RESHAPE( YSURF_CUR%DU%XT2M(:),(/NIE+2*NHALO-NIB+1,NJE+2*NHALO-NJB+1/) )

     TZFIELD = TFIELDMETADATA(  &
       CMNHNAME   = 'T2M',      &
       CLONGNAME  = 'Near surface Air Temperature', &
       CSTDNAME   = '',         &
       CUNITS     = 'K',        &
       CDIR       = 'XY',       &
       CCOMMENT   = 'X_Y_air temperature at 2m', &
       NGRID      = 1,          &
       NTYPE      = TYPEREAL,   &
       NDIMS      = 2,          &
       LTIMEDEP   = .TRUE.      )
     CALL IO_Field_write( TPOUTPUT%TFILE, TZFIELD, ZWORK(:,:) )

     DEALLOCATE(ZWORK)
   ENDIF

   END SUBROUTINE IO_Field_user_write

Example of local SURFEX variable on sea grid
-----------------------------------------------

.. code-block:: fortran

   SUBROUTINE IO_Field_user_write( TPOUTPUT )
   !
   USE MODD_BLANK_n
   !
   IMPLICIT NONE
   !
   TYPE(TOUTBAK),    INTENT(IN)  :: TPOUTPUT !Output structure
   !
   TYPE(TFIELDMETADATA) :: TZFIELD

   TZFIELD = TFIELDMETADATA(  &
     CMNHNAME   = 'DUMMY2D1',      &
     CLONGNAME  = '...', &
     CSTDNAME   = '',         &
     CUNITS     = '.',        &
     CDIR       = 'XY',       &
     CCOMMENT   = 'X_Y_...', &
     NGRID      = 1,          &
     NTYPE      = TYPEREAL,   &
     NDIMS      = 2,          &
     LTIMEDEP   = .TRUE.      )
   CALL IO_Field_write( TPOUTPUT%TFILE, TZFIELD, XDUMMY2D1 )

   END SUBROUTINE IO_Field_user_write
