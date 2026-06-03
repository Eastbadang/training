* mkssm generated this combined library (all.lib) from cm018typ.orig.kf.lib
* v 1 chosen from "typical" model file publically available from MOSIS /TL
* v 2 added KF parameters /TL
*
*                           MOSIS PARAMETRIC TEST RESULTS
*                                          
*          RUN: T16X (MM_NON-EPI)                            VENDOR: TSMC
*   TECHNOLOGY: SCN018                                FEATURE SIZE: 0.18 microns
*
*
*INTRODUCTION: This report contains the lot average results obtained by MOSIS
*              from measurements of MOSIS test structures on each wafer of
*              this fabrication lot. SPICE parameters obtained from similar
*              measurements on a selected wafer are also attached.
*
*COMMENTS: DSCN6M018_TSMC
*
*
*TRANSISTOR PARAMETERS     W/L       N-CHANNEL P-CHANNEL  UNITS
*                                                        
* MINIMUM                  0.27/0.18                     
*  Vth                                    0.51     -0.55  volts
*                                                        
* SHORT                    20.0/0.18                     
*  Idss                                 577      -278     uA/um
*  Vth                                    0.52     -0.55  volts
*  Vpt                                    4.8      -5.4   volts
*                                                        
* WIDE                     20.0/0.18                     
*  Ids0                                  21.1      -9.2   pA/um
*                                                        
* LARGE                    50/50                         
*  Vth                                    0.43     -0.43  volts
*  Vjbkd                                  3.9      -5.1   volts
*  Ijlk                                 &lt;50.0     &lt;50.0   pA
*  Gamma                                  0.54      0.62  V^0.5
*                                                        
* K' (Uo*Cox/2)                         166.5     -35.3   uA/V^2
* Low-field Mobility                    395.39     83.83  cm^2/V*s
*                                                        
*COMMENTS: Poly bias varies with design technology. To account for mask and
*           etch bias use the appropriate value for the parameters XL and XW
*           in your SPICE model card.
*                       Design Technology                   XL        XW
*                       -----------------                   -------  ------
*                       SCN6M_DEEP (lambda=0.09)            -0.02    -0.01
*                                     thick oxide           -0.03    -0.01
*                       TSMC18                              -0.02     0.00
*                                     thick oxide           -0.02     0.00
*                       SCN6M_SUBM (lambda=0.10)            -0.04     0.00
*                                     thick oxide           -0.07     0.00
*
*
*FOX TRANSISTORS           GATE      N+ACTIVE  P+ACTIVE  UNITS
* Vth                      Poly         &gt;6.6     &lt;-6.6   volts
*
*
*
*PROCESS PARAMETERS    N+ACTV P+ACTV  POLY  N+BLK  PLY+BLK  MTL1  MTL2  UNITS
* Sheet Resistance       6.5    7.3   7.6    60.2   330.6   0.08  0.08  ohms/sq
* Contact Resistance    10.9   11.3   9.8                         5.94  ohms
* Gate Oxide Thickness  41                                              angstrom
*
*&#12;
*PROCESS PARAMETERS        MTL3      MTL4      MTL5      MTL6   N_WELL   UNITS
* Sheet Resistance         0.08      0.07      0.07      0.03    951     ohms/sq
* Contact Resistance      11.60     17.40     22.58     25.41            ohms
*
*COMMENTS: BLK is silicide block.
*
*
*CAPACITANCE PARAMETERS N+ACTV  P+ACTV  POLY M1 M2 M3 M4 M5 M6 M5P N_WELL UNITS
* Area (substrate)      996    1172     100  37 18 12  8  8  3       65   aF/um^2
* Area (N+active)                      8409  52 19 13 10  9  8            aF/um^2
* Area (P+active)                      8127                               aF/um^2
* Area (poly)                                63 16  9  7  5  4            aF/um^2
* Area (metal1)                                 34 13  9  6  5            aF/um^2
* Area (metal2)                                    35 14  9  6            aF/um^2
* Area (metal3)                                       36 14  8            aF/um^2
* Area (metal4)                                          34 13            aF/um^2
* Area (metal5)                                             33 996        aF/um^2
* Area (no well)        129                                               aF/um^2
* Fringe (substrate)    259     218          23 58 53 39 23 --            aF/um
* Fringe (poly)                              65 37 28 23 19 17            aF/um
* Fringe (metal1)                               55 33    21 18            aF/um
* Fringe (metal2)                                  50 34 26 22            aF/um
* Fringe (metal3)                                     53 34 27            aF/um
* Fringe (metal4)                                        56 34            aF/um
* Fringe (metal5)                                           53            aF/um
* Overlap (N+active)                    723                               aF/um
* Overlap (P+active)                    683                               aF/um
*                                                                 
*
*
*CIRCUIT PARAMETERS                            UNITS      
* Inverters                     K                         
*  Vinv                        1.0       0.75  volts      
*  Vinv                        1.5       0.80  volts      
*  Vol (100 uA)                2.0       0.08  volts      
*  Voh (100 uA)                2.0       1.63  volts      
*  Vinv                        2.0       0.83  volts      
*  Gain                        2.0     -23.45             
* Ring Oscillator Freq.                                   
*  D1024_THK (31-stg,3.3V)             322.22  MHz        
*  DIV1024 (31-stg,1.8V)               385.64  MHz        
* Ring Oscillator Power                                   
*  D1024_THK (31-stg,3.3V)               0.07  uW/MHz/gate
*  DIV1024 (31-stg,1.8V)                 0.02  uW/MHz/gate
*                                                         
*COMMENTS: DEEP_SUBMICRON
*
*
*
*
*&#12; T16X SPICE BSIM3 VERSION 3.1 PARAMETERS
*
*SPICE 3f5 Level 8, Star-HSPICE Level 49, UTMOST Level 8
*
* DATE: Sep  5/01
* LOT: T16X                  WAF: 0001
* Temperature_parameters=Default
.MODEL NMOS NMOS (                                LEVEL   = 8
+VERSION = 3.1            TNOM    = 27             TOX     = 4.1E-9
+XJ      = 1E-7           NCH     = 2.3549E17      VTH0    = 0.3581698
+K1      = 0.574024       K2      = 2.751715E-3    K3      = 1.959368E-3
+K3B     = 2.2040222      W0      = 7.371562E-7    NLX     = 1.768395E-7
+DVT0W   = 0              DVT1W   = 0              DVT2W   = 0
+DVT0    = 1.4705192      DVT1    = 0.4151006      DVT2    = 0.0343357
+U0      = 296.2894586    UA      = -6.93439E-10   UB      = 1.32165E-18
+UC      = -1.35144E-11   VSAT    = 9.146457E4     A0      = 1.7920403
+AGS     = 0.3415021      B0      = -1.763016E-8   B1      = -1E-7
+KETA    = 6.109641E-3    A1      = 2.006795E-4    A2      = 0.9923701
+RDSW    = 127.7755888    PRWG    = 0.5            PRWB    = -0.2
+WR      = 1              WINT    = 0              LINT    = 9.512723E-9
+XL      = -2E-8          XW      = -1E-8          DWG     = -1.647691E-9
+DWB     = -7.387757E-9   VOFF    = -0.0720847     NFACTOR = 2.4126738
+CIT     = 0              CDSC    = 2.4E-4         CDSCD   = 0
+CDSCB   = 0              ETA0    = 0.0603469      ETAB    = -0.0640255
+DSUB    = 1              PCLM    = 0.8413441      PDIBLC1 = 0.0737257
+PDIBLC2 = 0.01           PDIBLCB = -0.0946392     DROUT   = 0.5318923
+PSCBE1  = 7.990582E10    PSCBE2  = 2.575736E-8    PVAG    = 4.297626E-3
+DELTA   = 0.01           RSH     = 6.5            MOBMOD  = 1
+PRT     = 0              UTE     = -1.5           KT1     = -0.11
+KT1L    = 0              KT2     = 0.022          UA1     = 4.31E-9
+UB1     = -7.61E-18      UC1     = -5.6E-11       AT      = 3.3E4
+WL      = 0              WLN     = 1              WW      = 0
+WWN     = 1              WWL     = 0              LL      = 0
+LLN     = 1              LW      = 0              LWN     = 1
+LWL     = 0              CAPMOD  = 2              XPART   = 0.5
+CGDO    = 7.23E-10       CGSO    = 7.23E-10       CGBO    = 1E-12
+CJ      = 9.92536E-4     PB      = 0.7270294      MJ      = 0.3574892
+CJSW    = 2.47496E-10    PBSW    = 0.5750347      MJSW    = 0.1322155
+CJSWG   = 3.3E-10        PBSWG   = 0.5750347      MJSWG   = 0.1322155
+CF      = 0              PVTH0   = -3.36027E-4    PRDSW   = -5
+PK2     = -9.513629E-4   WKETA   = 2.169006E-3    LKETA   = -9.246664E-3
+PU0     = 22.0242664     PUA     = 8.96812E-11    PUB     = 1.210283E-24
+PVSAT   = 1.648121E3     PETA0   = 1E-4           PKETA   = 2.23841E-3
+KF      = 1.62e-28       AF      = 1       )
*
.MODEL PMOS PMOS (                                LEVEL   = 8
+VERSION = 3.1            TNOM    = 27             TOX     = 4.1E-9
+XJ      = 1E-7           NCH     = 4.1589E17      VTH0    = -0.4110712
+K1      = 0.5592556      K2      = 0.0361476      K3      = 0
+K3B     = 8.9370813      W0      = 1E-6           NLX     = 1.066206E-7
+DVT0W   = 0              DVT1W   = 0              DVT2W   = 0
+DVT0    = 0.3917505      DVT1    = 0.2264932      DVT2    = 0.1
+U0      = 118.8985733    UA      = 1.593783E-9    UB      = 1.006669E-21
+UC      = -1E-10         VSAT    = 1.881479E5     A0      = 1.7197621
+AGS     = 0.3947587      B0      = 1.76795E-6     B1      = 4.757164E-6
+KETA    = 0.0160237      A1      = 0.0270792      A2      = 0.7327539
+RDSW    = 246.9856489    PRWG    = 0.5            PRWB    = -0.4411786
+WR      = 1              WINT    = 0              LINT    = 2.109171E-8
+XL      = -2E-8          XW      = -1E-8          DWG     = -2.45406E-8
+DWB     = 1.043995E-9    VOFF    = -0.0975832     NFACTOR = 1.9757896
+CIT     = 0              CDSC    = 2.4E-4         CDSCD   = 0
+CDSCB   = 0              ETA0    = 0.209929       ETAB    = -0.1915604
+DSUB    = 1.2874821      PCLM    = 2.5428497      PDIBLC1 = 6.318378E-3
+PDIBLC2 = 0.050851       PDIBLCB = -1E-3          DROUT   = 1.00051E-3
+PSCBE1  = 1.733719E9     PSCBE2  = 5.002385E-10   PVAG    = 14.9921084
+DELTA   = 0.01           RSH     = 7.3            MOBMOD  = 1
+PRT     = 0              UTE     = -1.5           KT1     = -0.11
+KT1L    = 0              KT2     = 0.022          UA1     = 4.31E-9
+UB1     = -7.61E-18      UC1     = -5.6E-11       AT      = 3.3E4
+WL      = 0              WLN     = 1              WW      = 0
+WWN     = 1              WWL     = 0              LL      = 0
+LLN     = 1              LW      = 0              LWN     = 1
+LWL     = 0              CAPMOD  = 2              XPART   = 0.5
+CGDO    = 6.83E-10       CGSO    = 6.83E-10       CGBO    = 1E-12
+CJ      = 1.179299E-3    PB      = 0.8432276      MJ      = 0.4100642
+CJSW    = 1.984295E-10   PBSW    = 0.6418798      MJSW    = 0.3010116
+CJSWG   = 4.22E-10       PBSWG   = 0.6418798      MJSWG   = 0.3010116
+CF      = 0              PVTH0   = 3.030104E-3    PRDSW   = 6.1983509
+PK2     = 3.028394E-3    WKETA   = 0.0269438      LKETA   = -4.108436E-3
+PU0     = -2.1162137     PUA     = -7.6853E-11    PUB     = 1E-21
+PVSAT   = -50            PETA0   = 9.996562E-5    PKETA   = -2.459504E-3
+KF      = 3.24e-29       AF      = 1    )
*
