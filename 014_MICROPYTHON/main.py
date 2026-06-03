# 작성자 : 김동현
# 소속 : (주)위츠 기술연구소
# 사용환경 : G1 Coil + Sensing Module(3rd) + Pyboard(1.1) + PC
# 수정일자 : 2021년 6월14일

import time
import array
import ujson
from pyb import LED, Pin, ADC, Timer

def theREF_vs_Check():
     ADC.read_timed_multi((theCH1, theCH2, theCH3), (ADCoCH1, ADCoCH2, ADCoCH3), ADC_Timer)
     DataLength = len(ADCoCH1)

     CH1_value_tmp = 0
     CH2_value_tmp = 0
     CH3_value_tmp = 0
     Delta_CH1mCH2_tmp = 0
     Delta_CH1mCH3_tmp = 0
     Delta_CH2mCH3_tmp = 0

     for nn in range(DataLength):
          CH1_value_tmp = CH1_value_tmp + ADCoCH1[nn] * theVoltageScale * 3.3 / 4906
          CH2_value_tmp = CH2_value_tmp + ADCoCH2[nn] * theVoltageScale * 3.3 / 4906
          CH3_value_tmp = CH3_value_tmp + ADCoCH3[nn] * theVoltageScale * 3.3 / 4906

          Delta_CH1mCH2_tmp = Delta_CH1mCH2_tmp + abs(ADCoCH1[nn] - ADCoCH2[nn]) * theVoltageScale * 3.3 / 4906
          Delta_CH1mCH3_tmp = Delta_CH1mCH3_tmp + abs(ADCoCH1[nn] - ADCoCH3[nn]) * theVoltageScale * 3.3 / 4906
          Delta_CH2mCH3_tmp = Delta_CH2mCH3_tmp + abs(ADCoCH2[nn] - ADCoCH3[nn]) * theVoltageScale * 3.3 / 4906

     CH1_value = CH1_value_tmp / DataLength * 1000  # [mV]
     CH2_value = CH2_value_tmp / DataLength * 1000  # [mV]
     CH3_value = CH3_value_tmp / DataLength * 1000  # [mV]

     Delta_CH1mCH2 = Delta_CH1mCH2_tmp / DataLength * 1000  # [mV]
     Delta_CH1mCH3 = Delta_CH1mCH3_tmp / DataLength * 1000  # [mV]
     Delta_CH2mCH3 = Delta_CH2mCH3_tmp / DataLength * 1000  # [mV]

     return CH1_value, CH2_value, CH3_value, Delta_CH1mCH2, Delta_CH1mCH3, Delta_CH2mCH3

def theREF_ps_Check():
     ADC.read_timed_multi((theCH4, theCH5, theCH6), (ADCoCH1, ADCoCH2, ADCoCH3), ADC_Timer)
     DataLength = len(ADCoCH4)

     CH1_value_tmp = 0
     CH2_value_tmp = 0
     CH3_value_tmp = 0
     Delta_CH1mCH2_tmp = 0
     Delta_CH1mCH3_tmp = 0
     Delta_CH2mCH3_tmp = 0

     for nn in range(DataLength):
          CH1_value_tmp = CH1_value_tmp + ADCoCH1[nn] * theVoltageScale * 3.3 / 4906
          CH2_value_tmp = CH2_value_tmp + ADCoCH2[nn] * theVoltageScale * 3.3 / 4906
          CH3_value_tmp = CH3_value_tmp + ADCoCH3[nn] * theVoltageScale * 3.3 / 4906

          Delta_CH1mCH2_tmp = Delta_CH1mCH2_tmp + abs(ADCoCH1[nn] - ADCoCH2[nn]) * theVoltageScale * 3.3 / 4906
          Delta_CH1mCH3_tmp = Delta_CH1mCH3_tmp + abs(ADCoCH1[nn] - ADCoCH3[nn]) * theVoltageScale * 3.3 / 4906
          Delta_CH2mCH3_tmp = Delta_CH2mCH3_tmp + abs(ADCoCH2[nn] - ADCoCH3[nn]) * theVoltageScale * 3.3 / 4906

     CH1_value = CH1_value_tmp / DataLength * 1000  # [mV]
     CH2_value = CH2_value_tmp / DataLength * 1000  # [mV]
     CH3_value = CH3_value_tmp / DataLength * 1000  # [mV]

     Delta_CH1mCH2 = Delta_CH1mCH2_tmp / DataLength * 1000  # [mV]
     Delta_CH1mCH3 = Delta_CH1mCH3_tmp / DataLength * 1000  # [mV]
     Delta_CH2mCH3 = Delta_CH2mCH3_tmp / DataLength * 1000  # [mV]

     return CH1_value, CH2_value, CH3_value, Delta_CH1mCH2, Delta_CH1mCH3, Delta_CH2mCH3

def snr():
     t1 = time.ticks_us()
     ADC.read_timed_multi((theCH1, theCH2, theCH3), (ADCoCH1, ADCoCH2, ADCoCH3), ADC_Timer)
     t2 = time.ticks_us()
     theDT = (t2-t1) / len(ADCoCH1)

     print('Time[us], R_CH1[V], R_CH2[V], R_CH3[V]\n\r')
     for nn in range(len(ADCoCH1)):
          print('%f, %f, %f, %f' % (
               theDT * (nn + 1),
               ADCoCH1[nn] * theVoltageScale * 3.3 / 4906,
               ADCoCH2[nn] * theVoltageScale * 3.3 / 4906,
               ADCoCH3[nn] * theVoltageScale * 3.3 / 4906))

def theFO_vs_Check(theMethods, theCounts, theCalDuty, FO_CH1, FO_CH2, FO_CH3, FO_CH1mCH2, FO_CH1mCH3, FO_CH2mCH3,
                R_CH1, R_CH2, R_CH3, R_CH1mCH2, R_CH1mCH3, R_CH2mCH3):
     NO_FO_Flag = 0
     if theMethods == 1:
          Flag1_max = 0
          Flag2_max = 0
          Flag3_max = 0
          Flag4_max = 0
          Flag5_max = 0
          Flag6_max = 0
     for theRun in range(theCounts):
          FO_Counts = 0

          if NO_FO_Flag > 10:
               led_vs_error.off()
          if theRun % theCalDuty == 0:
               if theRun == 0:
                    continue

               print('\n\r')
               print('\033[91m' + 'Ref. Value 초기화 준비\n\r' + '\033[0m')
               time.sleep(6)
               led_ready.on()

               print('\033[91m' + 'Ref. Value 초기화 시작' + '\033[0m')
               print('\n\r')
               led_ready.off()
               led_calibration.on()

               R_CH1, R_CH2, R_CH3, R_CH1mCH2, R_CH1mCH3, R_CH2mCH3 = theREF_vs_Check()
               ADC.read_timed_multi((theCH1, theCH2, theCH3), (ADCoCH1, ADCoCH2, ADCoCH3), ADC_Timer)

               for check in range(8):
                    CH1_value_tmp = 0
                    CH2_value_tmp = 0
                    CH3_value_tmp = 0

                    Delta_CH1mCH2_tmp = 0
                    Delta_CH1mCH3_tmp = 0
                    Delta_CH2mCH3_tmp = 0

                    for nn in range(120 * check, 120 * (check + 1)):
                         CH1_value_tmp = CH1_value_tmp + ADCoCH1[nn] * theVoltageScale * 3.3 / 4906
                         CH2_value_tmp = CH2_value_tmp + ADCoCH2[nn] * theVoltageScale * 3.3 / 4906
                         CH3_value_tmp = CH3_value_tmp + ADCoCH3[nn] * theVoltageScale * 3.3 / 4906

                         Delta_CH1mCH2_tmp = Delta_CH1mCH2_tmp + abs(
                              ADCoCH1[nn] - ADCoCH2[nn]) * theVoltageScale * 3.3 / 4906
                         Delta_CH1mCH3_tmp = Delta_CH1mCH3_tmp + abs(
                              ADCoCH1[nn] - ADCoCH3[nn]) * theVoltageScale * 3.3 / 4906
                         Delta_CH2mCH3_tmp = Delta_CH2mCH3_tmp + abs(
                              ADCoCH2[nn] - ADCoCH3[nn]) * theVoltageScale * 3.3 / 4906

                    CH1_value = CH1_value_tmp / 120 * 1000  # [mV]
                    CH2_value = CH2_value_tmp / 120 * 1000  # [mV]
                    CH3_value = CH3_value_tmp / 120 * 1000  # [mV]

                    Delta_CH1mCH2 = Delta_CH1mCH2_tmp / 120 * 1000  # [mV]
                    Delta_CH1mCH3 = Delta_CH1mCH3_tmp / 120 * 1000  # [mV]
                    Delta_CH2mCH3 = Delta_CH2mCH3_tmp / 120 * 1000  # [mV]

                    Flag1 = abs(CH1_value - R_CH1)
                    Flag2 = abs(CH2_value - R_CH2)
                    Flag3 = abs(CH3_value - R_CH3)
                    Flag4 = abs(Delta_CH1mCH2 - R_CH1mCH2)
                    Flag5 = abs(Delta_CH1mCH3 - R_CH1mCH3)
                    Flag6 = abs(Delta_CH2mCH3 - R_CH2mCH3)

                    if Flag1 > FO_CH1 and Flag4 > FO_CH1mCH2:
                         FO_Counts = FO_Counts + 1
                    elif Flag1 > FO_CH1 and Flag5 > FO_CH1mCH3:
                         FO_Counts = FO_Counts + 1
                    elif Flag1 > FO_CH1 and Flag6 > FO_CH2mCH3:
                         FO_Counts = FO_Counts + 1

                    if Flag2 > FO_CH2 and Flag4 > FO_CH1mCH2:
                         FO_Counts = FO_Counts + 1
                    elif Flag2 > FO_CH2 and Flag5 > FO_CH1mCH3:
                         FO_Counts = FO_Counts + 1
                    elif Flag2 > FO_CH2 and Flag6 > FO_CH2mCH3:
                         FO_Counts = FO_Counts + 1

                    if Flag3 > FO_CH3 and Flag4 > FO_CH1mCH2:
                         FO_Counts = FO_Counts + 1
                    elif Flag3 > FO_CH3 and Flag5 > FO_CH1mCH3:
                         FO_Counts = FO_Counts + 1
                    elif Flag3 > FO_CH3 and Flag6 > FO_CH2mCH3:
                         FO_Counts = FO_Counts + 1

                    if FO_Counts >= 2:
                         theRun = theRun - 1
                         continue

               print('\n\r')
               print('\033[91m' + 'Ref. Value 초기화 끝' + '\033[0m')
               print('\n\r')
               led_calibration.off()
               FO_Counts = 0

          ADC.read_timed_multi((theCH1, theCH2, theCH3), (ADCoCH1, ADCoCH2, ADCoCH3), ADC_Timer)
          DataLength = len(ADCoCH1)

          for check in range(8):
               CH1_value_tmp = 0
               CH2_value_tmp = 0
               CH3_value_tmp = 0
               Delta_CH1mCH2_tmp = 0
               Delta_CH1mCH3_tmp = 0
               Delta_CH2mCH3_tmp = 0

               for nn in range(120 * check, 120 * (check + 1)):
                    CH1_value_tmp = CH1_value_tmp + ADCoCH1[nn] * theVoltageScale * 3.3 / 4906
                    CH2_value_tmp = CH2_value_tmp + ADCoCH2[nn] * theVoltageScale * 3.3 / 4906
                    CH3_value_tmp = CH3_value_tmp + ADCoCH3[nn] * theVoltageScale * 3.3 / 4906
                    Delta_CH1mCH2_tmp = Delta_CH1mCH2_tmp + abs(
                         ADCoCH1[nn] - ADCoCH2[nn]) * theVoltageScale * 3.3 / 4906
                    Delta_CH1mCH3_tmp = Delta_CH1mCH3_tmp + abs(
                         ADCoCH1[nn] - ADCoCH3[nn]) * theVoltageScale * 3.3 / 4906
                    Delta_CH2mCH3_tmp = Delta_CH2mCH3_tmp + abs(
                         ADCoCH2[nn] - ADCoCH3[nn]) * theVoltageScale * 3.3 / 4906

               CH1_value = CH1_value_tmp / 120 * 1000  # [mV]
               CH2_value = CH2_value_tmp / 120 * 1000  # [mV]
               CH3_value = CH3_value_tmp / 120 * 1000  # [mV]

               Delta_CH1mCH2 = Delta_CH1mCH2_tmp / 120 * 1000  # [mV]
               Delta_CH1mCH3 = Delta_CH1mCH3_tmp / 120 * 1000  # [mV]
               Delta_CH2mCH3 = Delta_CH2mCH3_tmp / 120 * 1000  # [mV]

               Flag1 = abs(CH1_value - R_CH1)
               Flag2 = abs(CH2_value - R_CH2)
               Flag3 = abs(CH3_value - R_CH3)
               Flag4 = abs(Delta_CH1mCH2 - R_CH1mCH2)
               Flag5 = abs(Delta_CH1mCH3 - R_CH1mCH3)
               Flag6 = abs(Delta_CH2mCH3 - R_CH2mCH3)

               if Flag1 > FO_CH1 and Flag4 > FO_CH1mCH2:
                    FO_Counts = FO_Counts + 1
               elif Flag1 > FO_CH1 and Flag5 > FO_CH1mCH3:
                    FO_Counts = FO_Counts + 1
               elif Flag1 > FO_CH1 and Flag6 > FO_CH2mCH3:
                    FO_Counts = FO_Counts + 1

               if Flag2 > FO_CH2 and Flag4 > FO_CH1mCH2:
                    FO_Counts = FO_Counts + 1
               elif Flag2 > FO_CH2 and Flag5 > FO_CH1mCH3:
                    FO_Counts = FO_Counts + 1
               elif Flag2 > FO_CH2 and Flag6 > FO_CH2mCH3:
                    FO_Counts = FO_Counts + 1

               if Flag3 > FO_CH3 and Flag3 > FO_CH1mCH2:
                    FO_Counts = FO_Counts + 1
               elif Flag3 > FO_CH3 and Flag5 > FO_CH1mCH3:
                    FO_Counts = FO_Counts + 1
               elif Flag3 > FO_CH3 and Flag6 > FO_CH2mCH3:
                    FO_Counts = FO_Counts + 1

               if theMethods == 0:
                    print(CH1_value, CH2_value, CH3_value)

               elif theMethods == 1:
                    if Flag1 > Flag1_max:
                         Flag1_max = Flag1
                    if Flag2 > Flag2_max:
                         Flag2_max = Flag2
                    if Flag3 > Flag3_max:
                         Flag3_max = Flag3
                    if Flag4 > Flag4_max:
                         Flag4_max = Flag4
                    if Flag5 > Flag5_max:
                         Flag5_max = Flag5
                    if Flag6 > Flag6_max:
                         Flag6_max = Flag6
               else:
                    if FO_Counts >= 3:
                         led_vs_error.on()
                         print(Flag1, Flag2, Flag3, Flag4, Flag5, Flag6)
                         NO_FO_Flag = 0

                    if FO_Counts == 0:
                         NO_FO_Flag = NO_FO_Flag + 1

     if theMethods == 1:
          return Flag1_max, Flag2_max, Flag3_max, Flag4_max, Flag5_max, Flag6_max

def theFO_ps_Check(theMethods, theCounts, theCalDuty, FO_CH1, FO_CH2, FO_CH3, FO_CH1mCH2, FO_CH1mCH3, FO_CH2mCH3,
                R_CH1, R_CH2, R_CH3, R_CH1mCH2, R_CH1mCH3, R_CH2mCH3):
     NO_FO_Flag = 0
     if theMethods == 1:
          Flag1_max = 0
          Flag2_max = 0
          Flag3_max = 0
          Flag4_max = 0
          Flag5_max = 0
          Flag6_max = 0
     for theRun in range(theCounts):
          FO_Counts = 0
          if NO_FO_Flag > 10:
               led_ps_error.off()
          if theRun % theCalDuty == 0:
               if theRun == 0:
                    continue

               print('\n\r')
               print('\033[91m' + 'Ref. Value 초기화 준비\n\r' + '\033[0m')
               time.sleep(6)
               led_ready.on()

               print('\033[91m' + 'Ref. Value 초기화 시작' + '\033[0m')
               print('\n\r')
               led_ready.off()
               led_calibration.on()

               R_CH1, R_CH2, R_CH3, R_CH1mCH2, R_CH1mCH3, R_CH2mCH3 = theREF_ps_Check()
               ADC.read_timed_multi((theCH4, theCH5, theCH6), (ADCoCH1, ADCoCH2, ADCoCH3), ADC_Timer)

               for check in range(8):
                    CH1_value_tmp = 0
                    CH2_value_tmp = 0
                    CH3_value_tmp = 0

                    Delta_CH1mCH2_tmp = 0
                    Delta_CH1mCH3_tmp = 0
                    Delta_CH2mCH3_tmp = 0

                    for nn in range(120 * check, 120 * (check + 1)):
                         CH1_value_tmp = CH1_value_tmp + ADCoCH1[nn] * theVoltageScale * 3.3 / 4906
                         CH2_value_tmp = CH2_value_tmp + ADCoCH2[nn] * theVoltageScale * 3.3 / 4906
                         CH3_value_tmp = CH3_value_tmp + ADCoCH3[nn] * theVoltageScale * 3.3 / 4906

                         Delta_CH1mCH2_tmp = Delta_CH1mCH2_tmp + abs(
                              ADCoCH1[nn] - ADCoCH2[nn]) * theVoltageScale * 3.3 / 4906
                         Delta_CH1mCH3_tmp = Delta_CH1mCH3_tmp + abs(
                              ADCoCH1[nn] - ADCoCH3[nn]) * theVoltageScale * 3.3 / 4906
                         Delta_CH2mCH3_tmp = Delta_CH2mCH3_tmp + abs(
                              ADCoCH2[nn] - ADCoCH3[nn]) * theVoltageScale * 3.3 / 4906

                    CH1_value = CH1_value_tmp / 120 * 1000  # [mV]
                    CH2_value = CH2_value_tmp / 120 * 1000  # [mV]
                    CH3_value = CH3_value_tmp / 120 * 1000  # [mV]

                    Delta_CH1mCH2 = Delta_CH1mCH2_tmp / 120 * 1000  # [mV]
                    Delta_CH1mCH3 = Delta_CH1mCH3_tmp / 120 * 1000  # [mV]
                    Delta_CH2mCH3 = Delta_CH2mCH3_tmp / 120 * 1000  # [mV]

                    Flag1 = abs(CH1_value - R_CH1)
                    Flag2 = abs(CH2_value - R_CH2)
                    Flag3 = abs(CH3_value - R_CH3)
                    Flag4 = abs(Delta_CH1mCH2 - R_CH1mCH2)
                    Flag5 = abs(Delta_CH1mCH3 - R_CH1mCH3)
                    Flag6 = abs(Delta_CH2mCH3 - R_CH2mCH3)

                    if Flag1 > FO_CH1 and Flag4 > FO_CH1mCH2:
                         FO_Counts = FO_Counts + 1
                    elif Flag1 > FO_CH1 and Flag5 > FO_CH1mCH3:
                         FO_Counts = FO_Counts + 1
                    elif Flag1 > FO_CH1 and Flag6 > FO_CH2mCH3:
                         FO_Counts = FO_Counts + 1

                    if Flag2 > FO_CH2 and Flag4 > FO_CH1mCH2:
                         FO_Counts = FO_Counts + 1
                    elif Flag2 > FO_CH2 and Flag5 > FO_CH1mCH3:
                         FO_Counts = FO_Counts + 1
                    elif Flag2 > FO_CH2 and Flag6 > FO_CH2mCH3:
                         FO_Counts = FO_Counts + 1

                    if Flag3 > FO_CH3 and Flag4 > FO_CH1mCH2:
                         FO_Counts = FO_Counts + 1
                    elif Flag3 > FO_CH3 and Flag5 > FO_CH1mCH3:
                         FO_Counts = FO_Counts + 1
                    elif Flag3 > FO_CH3 and Flag6 > FO_CH2mCH3:
                         FO_Counts = FO_Counts + 1

                    if FO_Counts >= 2:
                         theRun = theRun - 1
                         continue

               print('\n\r')
               print('\033[91m' + 'Ref. Value 초기화 끝' + '\033[0m')
               print('\n\r')
               led_calibration.off()
               FO_Counts = 0

          ADC.read_timed_multi((theCH4, theCH5, theCH6), (ADCoCH1, ADCoCH2, ADCoCH3), ADC_Timer)
          DataLength = len(ADCoCH4)

          for check in range(8):
               CH1_value_tmp = 0
               CH2_value_tmp = 0
               CH3_value_tmp = 0
               Delta_CH1mCH2_tmp = 0
               Delta_CH1mCH3_tmp = 0
               Delta_CH2mCH3_tmp = 0

               for nn in range(120 * check, 120 * (check + 1)):
                    CH1_value_tmp = CH1_value_tmp + ADCoCH1[nn] * theVoltageScale * 3.3 / 4906
                    CH2_value_tmp = CH2_value_tmp + ADCoCH2[nn] * theVoltageScale * 3.3 / 4906
                    CH3_value_tmp = CH3_value_tmp + ADCoCH3[nn] * theVoltageScale * 3.3 / 4906
                    Delta_CH1mCH2_tmp = Delta_CH1mCH2_tmp + abs(
                         ADCoCH1[nn] - ADCoCH2[nn]) * theVoltageScale * 3.3 / 4906
                    Delta_CH1mCH3_tmp = Delta_CH1mCH3_tmp + abs(
                         ADCoCH1[nn] - ADCoCH3[nn]) * theVoltageScale * 3.3 / 4906
                    Delta_CH2mCH3_tmp = Delta_CH2mCH3_tmp + abs(
                         ADCoCH2[nn] - ADCoCH3[nn]) * theVoltageScale * 3.3 / 4906

               CH1_value = CH1_value_tmp / 120 * 1000  # [mV]
               CH2_value = CH2_value_tmp / 120 * 1000  # [mV]
               CH3_value = CH3_value_tmp / 120 * 1000  # [mV]

               Delta_CH1mCH2 = Delta_CH1mCH2_tmp / 120 * 1000  # [mV]
               Delta_CH1mCH3 = Delta_CH1mCH3_tmp / 120 * 1000  # [mV]
               Delta_CH2mCH3 = Delta_CH2mCH3_tmp / 120 * 1000  # [mV]

               Flag1 = abs(CH1_value - R_CH1)
               Flag2 = abs(CH2_value - R_CH2)
               Flag3 = abs(CH3_value - R_CH3)
               Flag4 = abs(Delta_CH1mCH2 - R_CH1mCH2)
               Flag5 = abs(Delta_CH1mCH3 - R_CH1mCH3)
               Flag6 = abs(Delta_CH2mCH3 - R_CH2mCH3)

               if Flag1 > FO_CH1 and Flag4 > FO_CH1mCH2:
                    FO_Counts = FO_Counts + 1
               elif Flag1 > FO_CH1 and Flag5 > FO_CH1mCH3:
                    FO_Counts = FO_Counts + 1
               elif Flag1 > FO_CH1 and Flag6 > FO_CH2mCH3:
                    FO_Counts = FO_Counts + 1

               if Flag2 > FO_CH2 and Flag4 > FO_CH1mCH2:
                    FO_Counts = FO_Counts + 1
               elif Flag2 > FO_CH2 and Flag5 > FO_CH1mCH3:
                    FO_Counts = FO_Counts + 1
               elif Flag2 > FO_CH2 and Flag6 > FO_CH2mCH3:
                    FO_Counts = FO_Counts + 1

               if Flag3 > FO_CH3 and Flag3 > FO_CH1mCH2:
                    FO_Counts = FO_Counts + 1
               elif Flag3 > FO_CH3 and Flag5 > FO_CH1mCH3:
                    FO_Counts = FO_Counts + 1
               elif Flag3 > FO_CH3 and Flag6 > FO_CH2mCH3:
                    FO_Counts = FO_Counts + 1

               if theMethods == 0:
                    print(CH1_value, CH2_value, CH3_value)

               elif theMethods == 1:
                    if Flag1 > Flag1_max:
                         Flag1_max = Flag1
                    if Flag2 > Flag2_max:
                         Flag2_max = Flag2
                    if Flag3 > Flag3_max:
                         Flag3_max = Flag3
                    if Flag4 > Flag4_max:
                         Flag4_max = Flag4
                    if Flag5 > Flag5_max:
                         Flag5_max = Flag5
                    if Flag6 > Flag6_max:
                         Flag6_max = Flag6
               else:
                    if FO_Counts >= 3:
                         led_ps_error.on()
                         print(Flag1, Flag2, Flag3, Flag4, Flag5, Flag6)
                         NO_FO_Flag = 0

                    if FO_Counts == 0:
                         NO_FO_Flag = NO_FO_Flag + 1

     if theMethods == 1:
          return Flag1_max, Flag2_max, Flag3_max, Flag4_max, Flag5_max, Flag6_max

def theFO2_Check(theCounts, theCalDuty, FO_CH1v, FO_CH2v, FO_CH3v, FO_CH1mCH2v, FO_CH1mCH3v, FO_CH2mCH3v,
               FO_CH1p, FO_CH2p, FO_CH3p, FO_CH1mCH2p, FO_CH1mCH3p, FO_CH2mCH3p,
               R_CH1v, R_CH2v, R_CH3v, R_CH1mCH2v, R_CH1mCH3v, R_CH2mCH3v,
               R_CH1p, R_CH2p, R_CH3p, R_CH1mCH2p, R_CH1mCH3p, R_CH2mCH3p):
     NO_FO_Flag = 0
     Calibration_token = 0
     for theRun in range(theCounts):
          FO_Counts = 0
          if NO_FO_Flag > 10:
               led_vs_error.off()
               led_ps_error.off()
          if theRun % theCalDuty == 0:
               if theRun == 0:
                    continue

               print('\n\r')
               print('\033[91m' + 'Ref. Value 초기화 준비\n\r' + '\033[0m')
               time.sleep(6)
               led_ready.on()

               print('\033[91m' + 'Ref. Value 초기화 시작' + '\033[0m')
               print('\n\r')
               led_ready.off()
               led_calibration.on()

               if Calibration_token == 0:
                    R_CH1v, R_CH2v, R_CH3v, R_CH1mCH2v, R_CH1mCH3v, R_CH2mCH3v = theREF_vs_Check()
                    FO_CH1v, FO_CH2v, FO_CH3v, FO_CH1mCH2v, FO_CH1mCH3v, FO_CH2mCH3v =\
                         theFO_vs_Check(1, 500, 1000, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
                                        R_CH1v, R_CH2v, R_CH3v, R_CH1mCH2v, R_CH1mCH3v, R_CH2mCH3v)
                    R_CH1v, R_CH2v, R_CH3v, R_CH1mCH2v, R_CH1mCH3v, R_CH2mCH3v = theREF_vs_Check()

                    ADC.read_timed_multi((theCH1, theCH2, theCH3), (ADCoCH1, ADCoCH2, ADCoCH3), ADC_Timer)
                    for check in range(8):
                         CH1_value_tmp = 0
                         CH2_value_tmp = 0
                         CH3_value_tmp = 0

                         Delta_CH1mCH2_tmp = 0
                         Delta_CH1mCH3_tmp = 0
                         Delta_CH2mCH3_tmp = 0

                         for nn in range(120 * check, 120 * (check + 1)):
                              CH1_value_tmp = CH1_value_tmp + ADCoCH1[nn] * theVoltageScale * 3.3 / 4906
                              CH2_value_tmp = CH2_value_tmp + ADCoCH2[nn] * theVoltageScale * 3.3 / 4906
                              CH3_value_tmp = CH3_value_tmp + ADCoCH3[nn] * theVoltageScale * 3.3 / 4906

                              Delta_CH1mCH2_tmp = Delta_CH1mCH2_tmp + abs(
                                   ADCoCH1[nn] - ADCoCH2[nn]) * theVoltageScale * 3.3 / 4906
                              Delta_CH1mCH3_tmp = Delta_CH1mCH3_tmp + abs(
                                   ADCoCH1[nn] - ADCoCH3[nn]) * theVoltageScale * 3.3 / 4906
                              Delta_CH2mCH3_tmp = Delta_CH2mCH3_tmp + abs(
                                   ADCoCH2[nn] - ADCoCH3[nn]) * theVoltageScale * 3.3 / 4906

                         CH1_value = CH1_value_tmp / 120 * 1000  # [mV]
                         CH2_value = CH2_value_tmp / 120 * 1000  # [mV]
                         CH3_value = CH3_value_tmp / 120 * 1000  # [mV]

                         Delta_CH1mCH2 = Delta_CH1mCH2_tmp / 120 * 1000  # [mV]
                         Delta_CH1mCH3 = Delta_CH1mCH3_tmp / 120 * 1000  # [mV]
                         Delta_CH2mCH3 = Delta_CH2mCH3_tmp / 120 * 1000  # [mV]

                         Flag1 = abs(CH1_value - R_CH1v)
                         Flag2 = abs(CH2_value - R_CH2v)
                         Flag3 = abs(CH3_value - R_CH3v)
                         Flag4 = abs(Delta_CH1mCH2 - R_CH1mCH2v)
                         Flag5 = abs(Delta_CH1mCH3 - R_CH1mCH3v)
                         Flag6 = abs(Delta_CH2mCH3 - R_CH2mCH3v)

                         if Flag1 > FO_CH1v and Flag4 > FO_CH1mCH2v:
                              FO_Counts = FO_Counts + 1
                         elif Flag1 > FO_CH1v and Flag5 > FO_CH1mCH3v:
                              FO_Counts = FO_Counts + 1
                         elif Flag1 > FO_CH1v and Flag6 > FO_CH2mCH3v:
                              FO_Counts = FO_Counts + 1

                         if Flag2 > FO_CH2v and Flag4 > FO_CH1mCH2v:
                              FO_Counts = FO_Counts + 1
                         elif Flag2 > FO_CH2v and Flag5 > FO_CH1mCH3v:
                              FO_Counts = FO_Counts + 1
                         elif Flag2 > FO_CH2v and Flag6 > Max6:
                              FO_Counts = FO_Counts + 1

                         if Flag3 > FO_CH3v and Flag4 > FO_CH1mCH2v:
                              FO_Counts = FO_Counts + 1
                         elif Flag3 > FO_CH3v and Flag5 > FO_CH1mCH3v:
                              FO_Counts = FO_Counts + 1
                         elif Flag3 > FO_CH3v and Flag6 > FO_CH2mCH3v:
                              FO_Counts = FO_Counts + 1

                         if FO_Counts >= 2:
                              theRun = theRun - 1
                         else:
                             Calibration_token = 1

               elif Calibration_token == 1:
                    R_CH1p, R_CH2p, R_CH3p, R_CH1mCH2p, R_CH1mCH3p, R_CH2mCH3p = theREF_ps_Check()
                    FO_CH1p, FO_CH2p, FO_CH3p, FO_CH1mCH2p, FO_CH1mCH3p, FO_CH2mCH3p =\
                         theFO_ps_Check(1, 500, 1000, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
                                        R_CH1p, R_CH2p, R_CH3p, R_CH1mCH2p, R_CH1mCH3p, R_CH2mCH3p)
                    R_CH1p, R_CH2p, R_CH3p, R_CH1mCH2p, R_CH1mCH3p, R_CH2mCH3p = theREF_ps_Check()

                    ADC.read_timed_multi((theCH4, theCH5, theCH6), (ADCoCH1, ADCoCH2, ADCoCH3), ADC_Timer)
                    for check in range(7):
                         CH1_value_tmp = 0
                         CH2_value_tmp = 0
                         CH3_value_tmp = 0

                         Delta_CH1mCH2_tmp = 0
                         Delta_CH1mCH3_tmp = 0
                         Delta_CH2mCH3_tmp = 0

                         for nn in range(120 * check, 120 * (check + 1)):
                              CH1_value_tmp = CH1_value_tmp + ADCoCH1[nn] * theVoltageScale * 3.3 / 4906
                              CH2_value_tmp = CH2_value_tmp + ADCoCH2[nn] * theVoltageScale * 3.3 / 4906
                              CH3_value_tmp = CH3_value_tmp + ADCoCH3[nn] * theVoltageScale * 3.3 / 4906

                              Delta_CH1mCH2_tmp = Delta_CH1mCH2_tmp + abs(
                                   ADCoCH1[nn] - ADCoCH2[nn]) * theVoltageScale * 3.3 / 4906
                              Delta_CH1mCH3_tmp = Delta_CH1mCH3_tmp + abs(
                                   ADCoCH1[nn] - ADCoCH3[nn]) * theVoltageScale * 3.3 / 4906
                              Delta_CH2mCH3_tmp = Delta_CH2mCH3_tmp + abs(
                                   ADCoCH2[nn] - ADCoCH3[nn]) * theVoltageScale * 3.3 / 4906

                         CH1_value = CH1_value_tmp / 120 * 1000  # [mV]
                         CH2_value = CH2_value_tmp / 120 * 1000  # [mV]
                         CH3_value = CH3_value_tmp / 120 * 1000  # [mV]

                         Delta_CH1mCH2 = Delta_CH1mCH2_tmp / 120 * 1000  # [mV]
                         Delta_CH1mCH3 = Delta_CH1mCH3_tmp / 120 * 1000  # [mV]
                         Delta_CH2mCH3 = Delta_CH2mCH3_tmp / 120 * 1000  # [mV]

                         Flag1 = abs(CH1_value - R_CH1p)
                         Flag2 = abs(CH2_value - R_CH2p)
                         Flag3 = abs(CH3_value - R_CH3p)
                         Flag4 = abs(Delta_CH1mCH2 - R_CH1mCH2p)
                         Flag5 = abs(Delta_CH1mCH3 - R_CH1mCH3p)
                         Flag6 = abs(Delta_CH2mCH3 - R_CH2mCH3p)

                         if Flag1 > FO_CH1p and Flag4 > FO_CH1mCH2p:
                              FO_Counts = FO_Counts + 1
                         elif Flag1 > FO_CH1p and Flag5 > FO_CH1mCH3p:
                              FO_Counts = FO_Counts + 1
                         elif Flag1 > FO_CH1p and Flag6 > FO_CH2mCH3p:
                              FO_Counts = FO_Counts + 1

                         if Flag2 > FO_CH2p and Flag4 > FO_CH1mCH2p:
                              FO_Counts = FO_Counts + 1
                         elif Flag2 > FO_CH2p and Flag5 > FO_CH1mCH3p:
                              FO_Counts = FO_Counts + 1
                         elif Flag2 > FO_CH2p and Flag6 > FO_CH2mCH3p:
                              FO_Counts = FO_Counts + 1

                         if Flag3 > FO_CH3p and Flag4 > FO_CH1mCH2p:
                              FO_Counts = FO_Counts + 1
                         elif Flag3 > FO_CH3p and Flag5 > FO_CH1mCH3p:
                              FO_Counts = FO_Counts + 1
                         elif Flag3 > FO_CH3p and Flag6 > FO_CH2mCH3p:
                              FO_Counts = FO_Counts + 1

                         if FO_Counts >= 2:
                              theRun = theRun - 1
                              continue
                         else:
                             Calibration_token = 0

               print('\n\r')
               print('\033[91m' + 'Ref. Value 초기화 끝' + '\033[0m')
               print('\n\r')
               led_calibration.off()
               FO_Counts = 0

          if theRun % 10 <= 5:  # Voltage Sensing
               ADC.read_timed_multi((theCH1, theCH2, theCH3), (ADCoCH1, ADCoCH2, ADCoCH3), ADC_Timer)
               for check in range(8):
                    CH1_value_tmp = 0
                    CH2_value_tmp = 0
                    CH3_value_tmp = 0
                    Delta_CH1mCH2_tmp = 0
                    Delta_CH1mCH3_tmp = 0
                    Delta_CH2mCH3_tmp = 0

                    for nn in range(120 * check, 120 * (check + 1)):
                         CH1_value_tmp = CH1_value_tmp + ADCoCH1[nn] * theVoltageScale * 3.3 / 4906
                         CH2_value_tmp = CH2_value_tmp + ADCoCH2[nn] * theVoltageScale * 3.3 / 4906
                         CH3_value_tmp = CH3_value_tmp + ADCoCH3[nn] * theVoltageScale * 3.3 / 4906
                         Delta_CH1mCH2_tmp = Delta_CH1mCH2_tmp + abs(
                              ADCoCH1[nn] - ADCoCH2[nn]) * theVoltageScale * 3.3 / 4906
                         Delta_CH1mCH3_tmp = Delta_CH1mCH3_tmp + abs(
                              ADCoCH1[nn] - ADCoCH3[nn]) * theVoltageScale * 3.3 / 4906
                         Delta_CH2mCH3_tmp = Delta_CH2mCH3_tmp + abs(
                              ADCoCH2[nn] - ADCoCH3[nn]) * theVoltageScale * 3.3 / 4906

                    CH1_value = CH1_value_tmp / 120 * 1000  # [mV]
                    CH2_value = CH2_value_tmp / 120 * 1000  # [mV]
                    CH3_value = CH3_value_tmp / 120 * 1000  # [mV]

                    Delta_CH1mCH2 = Delta_CH1mCH2_tmp / 120 * 1000  # [mV]
                    Delta_CH1mCH3 = Delta_CH1mCH3_tmp / 120 * 1000  # [mV]
                    Delta_CH2mCH3 = Delta_CH2mCH3_tmp / 120 * 1000  # [mV]

                    Flag1 = abs(CH1_value - R_CH1v)
                    Flag2 = abs(CH2_value - R_CH2v)
                    Flag3 = abs(CH3_value - R_CH3v)
                    Flag4 = abs(Delta_CH1mCH2 - R_CH1mCH2v)
                    Flag5 = abs(Delta_CH1mCH3 - R_CH1mCH3v)
                    Flag6 = abs(Delta_CH2mCH3 - R_CH2mCH3v)

                    if Flag1 > FO_CH1v and Flag4 > FO_CH1mCH2v:
                         FO_Counts = FO_Counts + 1
                    elif Flag1 > FO_CH1v and Flag5 > FO_CH1mCH3v:
                         FO_Counts = FO_Counts + 1
                    elif Flag1 > FO_CH1v and Flag6 > FO_CH2mCH3v:
                         FO_Counts = FO_Counts + 1

                    if Flag2 > FO_CH2v and Flag4 > FO_CH1mCH2v:
                         FO_Counts = FO_Counts + 1
                    elif Flag2 > FO_CH2v and Flag5 > FO_CH1mCH3v:
                         FO_Counts = FO_Counts + 1
                    elif Flag2 > FO_CH2v and Flag6 > FO_CH2mCH3v:
                         FO_Counts = FO_Counts + 1

                    if Flag3 > FO_CH3v and Flag3 > FO_CH1mCH2v:
                         FO_Counts = FO_Counts + 1
                    elif Flag3 > FO_CH3v and Flag5 > FO_CH1mCH3v:
                         FO_Counts = FO_Counts + 1
                    elif Flag3 > FO_CH3v and Flag6 > FO_CH2mCH3v:
                         FO_Counts = FO_Counts + 1

                    if FO_Counts >= 3:
                         led_vs_error.on()
                         print(Flag1, Flag2, Flag3, Flag4, Flag5, Flag6)
                         NO_FO_Flag = 0
                    if FO_Counts == 0:
                         NO_FO_Flag = NO_FO_Flag + 1
          else:  # Phase Sensing
               ADC.read_timed_multi((theCH4, theCH5, theCH6), (ADCoCH1, ADCoCH2, ADCoCH3), ADC_Timer)
               for check in range(8):
                    CH1_value_tmp = 0
                    CH2_value_tmp = 0
                    CH3_value_tmp = 0
                    Delta_CH1mCH2_tmp = 0
                    Delta_CH1mCH3_tmp = 0
                    Delta_CH2mCH3_tmp = 0

                    for nn in range(120 * check, 120 * (check + 1)):
                         CH1_value_tmp = CH1_value_tmp + ADCoCH1[nn] * theVoltageScale * 3.3 / 4906
                         CH2_value_tmp = CH2_value_tmp + ADCoCH2[nn] * theVoltageScale * 3.3 / 4906
                         CH3_value_tmp = CH3_value_tmp + ADCoCH3[nn] * theVoltageScale * 3.3 / 4906
                         Delta_CH1mCH2_tmp = Delta_CH1mCH2_tmp + abs(
                              ADCoCH1[nn] - ADCoCH2[nn]) * theVoltageScale * 3.3 / 4906
                         Delta_CH1mCH3_tmp = Delta_CH1mCH3_tmp + abs(
                              ADCoCH1[nn] - ADCoCH3[nn]) * theVoltageScale * 3.3 / 4906
                         Delta_CH2mCH3_tmp = Delta_CH2mCH3_tmp + abs(
                              ADCoCH2[nn] - ADCoCH3[nn]) * theVoltageScale * 3.3 / 4906

                    CH1_value = CH1_value_tmp / 120 * 1000  # [mV]
                    CH2_value = CH2_value_tmp / 120 * 1000  # [mV]
                    CH3_value = CH3_value_tmp / 120 * 1000  # [mV]

                    Delta_CH1mCH2 = Delta_CH1mCH2_tmp / 120 * 1000  # [mV]
                    Delta_CH1mCH3 = Delta_CH1mCH3_tmp / 120 * 1000  # [mV]
                    Delta_CH2mCH3 = Delta_CH2mCH3_tmp / 120 * 1000  # [mV]

                    Flag1 = abs(CH1_value - R_CH1p)
                    Flag2 = abs(CH2_value - R_CH2p)
                    Flag3 = abs(CH3_value - R_CH3p)
                    Flag4 = abs(Delta_CH1mCH2 - R_CH1mCH2p)
                    Flag5 = abs(Delta_CH1mCH3 - R_CH1mCH3p)
                    Flag6 = abs(Delta_CH2mCH3 - R_CH2mCH3p)

                    if Flag1 > FO_CH1p and Flag4 > FO_CH1mCH2p:
                         FO_Counts = FO_Counts + 1
                    elif Flag1 > FO_CH1p and Flag5 > FO_CH1mCH3p:
                         FO_Counts = FO_Counts + 1
                    elif Flag1 > FO_CH1p and Flag6 > FO_CH2mCH3p:
                         FO_Counts = FO_Counts + 1

                    if Flag2 > FO_CH2p and Flag4 > FO_CH1mCH2p:
                         FO_Counts = FO_Counts + 1
                    elif Flag2 > FO_CH2p and Flag5 > FO_CH1mCH3p:
                         FO_Counts = FO_Counts + 1
                    elif Flag2 > FO_CH2p and Flag6 > FO_CH2mCH3p:
                         FO_Counts = FO_Counts + 1

                    if Flag3 > FO_CH3p and Flag3 > FO_CH1mCH2p:
                         FO_Counts = FO_Counts + 1
                    elif Flag3 > FO_CH3p and Flag5 > FO_CH1mCH3p:
                         FO_Counts = FO_Counts + 1
                    elif Flag3 > FO_CH3p and Flag6 > FO_CH2mCH3p:
                         FO_Counts = FO_Counts + 1

                    if FO_Counts >= 3:
                         led_ps_error.on()
                         print(Flag1, Flag2, Flag3, Flag4, Flag5, Flag6)
                         NO_FO_Flag = 0
                    if FO_Counts == 0:
                         NO_FO_Flag = NO_FO_Flag + 1

def main():
     global theVoltageScale                        # ADC 조정 값
     global theCH1, theCH2, theCH3, theCH4, theCH5, theCH6                 # ADC Pin 정의 변수
     global ADC_Timer                              # ADC Timer 정의 변수
     global ADCoCH1, ADCoCH2, ADCoCH3, theDT       # 채널 Data 및 센싱 소요 시간
     global led_ready, led_calibration, led_error  # LED 정의

     led_ready = LED(3)  # Yellow led, no FO condition
     led_vs_error = LED(2)  # Green led, FO Voltage Sensing
     led_ps_error = LED(4)  # Blue led, FO Phase Sensing
     led_calibration = LED(1)  # Red led, calibration

     theVoltageScale = 1.19  # 실측값
     theMemory = 4096  # 11152  # 20ms 동안 센싱

     # ADC 입력 Pin 정의, 3.3/4096 => 0.8mV step
     theCH1 = ADC(Pin('X19'))  # Voltage Sensing CH1 Vout
     theCH2 = ADC(Pin('X20'))  # Voltage Sensing CH2 Vout
     theCH3 = ADC(Pin('X21'))  # Voltage Sensing CH3 Vout
     theCH4 = ADC(Pin('X1'))  # Phase Sensing CH4 Vout
     theCH5 = ADC(Pin('X2'))  # Phase Sensing CH5 Vout
     theCH6 = ADC(Pin('X3'))  # Phase Sensing CH6 Vout

     # 채널 간 동기 ADC
     ADC_Timer = Timer(6, freq=140000)
     ADCoCH1 = array.array('I', bytearray(theMemory))  # I : unsigned int, theMemory의 1/4 용량
     ADCoCH2 = array.array('I', bytearray(theMemory))
     ADCoCH3 = array.array('I', bytearray(theMemory))

     n = 8

     while n != 0:
          print('테스트 모드를 선택해 주세요\n\r')
          print('0 : 테스트 종료 \n\r')
          print('1 : Voltage Sensing Test at Pre-Power Mode\n\r')
          print('2 : Voltage Sensing Test at During Power Mode\n\r')
          print('3 : Phase Sensing Test at Pre-Power Mode\n\r')
          print('4 : Phase Sensing Test at During Power Mode\n\r')
          print('5 : Voltage Sensing & Phase Sensing Test at Pre-Power Mode\n\r')
          print('6 : Voltage Sensing & Phase Sensing Test at During Power Mode\n\r')
          print('7 : SNR Test')
          print('\n\r')

          n = int(input("테스트 모드 선택 :  "))

          if n == 0:
               print('\n\r')
               print('테스트 종료를 합니다.')
               led_ready.off()
               led_calibration.off()
               led_vs_error.off()
               break

          elif n == 1:
               print('\n\r')
               print('테스트 준비 중.....\n\r')
               print('테스트 판넬 위에 FO를 치워주세요.\n\r')
               print('\n\r')

               theCounts = 0
               theCounts = int(input("반복 측정 회수 :  "))
               print('\n\r')

               print('\n\r')
               print('\033[91m' + 'Calibration 준비\n\r' + '\033[0m')
               time.sleep(6)
               led_ready.on()

               print('\033[91m' + 'Calibration  시작' + '\033[0m')
               print('\n\r')
               led_ready.off()
               led_calibration.on()

               R_CH1, R_CH2, R_CH3, R_CH1mCH2, R_CH1mCH3, R_CH2mCH3 = theREF_vs_Check()

               # t1 = time.ticks_ms()

               Max1, Max2, Max3, Max4, Max5, Max6 = theFO_vs_Check(1, 500, 1000, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
                                                               R_CH1, R_CH2, R_CH3, R_CH1mCH2, R_CH1mCH3, R_CH2mCH3)
               # t2 = time.ticks_ms()

               # print(t2-t1)  # 약 3분40초 소요

               print('\n\r')

               R_CH1, R_CH2, R_CH3, R_CH1mCH2, R_CH1mCH3, R_CH2mCH3 = theREF_vs_Check()

               led_calibration.off()
               print('\033[91m' + 'Calibration 끝' + '\033[0m')
               print('\n\r')
               print('테스트 시작\n\r')

               CalDuty = 10000
               theFO_vs_Check(2, theCounts, CalDuty, Max1, Max2, Max3, Max4, Max5, Max6,
                           R_CH1, R_CH2, R_CH3, R_CH1mCH2, R_CH1mCH3, R_CH2mCH3)

               print('\n\r')
               print('테스트 끝\n\r')
               print('\n\r')

          elif n == 2:
               print('\n\r')
               print('테스트 준비 중.....\n\r')
               print('테스트 판넬 위에 FO를 치워주세요.\n\r')
               print('\n\r')

               theCounts = 0
               theCounts = int(input("반복 측정 회수 :  "))
               print('\n\r')

               print('\n\r')
               print('\033[91m' + 'Calibration 준비\n\r' + '\033[0m')
               time.sleep(6)
               led_ready.on()

               print('\033[91m' + 'Calibration 시작' + '\033[0m')
               print('\n\r')
               led_ready.off()
               led_calibration.on()

               R_CH1, R_CH2, R_CH3, R_CH1mCH2, R_CH1mCH3, R_CH2mCH3 = theREF_vs_Check()

               # t1 = time.ticks_ms()

               Max1, Max2, Max3, Max4, Max5, Max6 = theFO_vs_Check(1, 500, 1000, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
                                                                R_CH1, R_CH2, R_CH3, R_CH1mCH2, R_CH1mCH3, R_CH2mCH3)
               # t2 = time.ticks_ms()

               # print(t2-t1)  # 약 3분40초 소요

               print('\n\r')

               R_CH1, R_CH2, R_CH3, R_CH1mCH2, R_CH1mCH3, R_CH2mCH3 = theREF_vs_Check()

               led_calibration.off()
               print('\033[91m' + 'Calibration 끝' + '\033[0m')
               print('\n\r')
               print('테스트 시작\n\r')

               CalDuty = 10000
               theFO_vs_Check(2, theCounts, CalDuty, Max1, Max2, Max3, Max4, Max5, Max6,
                           R_CH1, R_CH2, R_CH3, R_CH1mCH2, R_CH1mCH3, R_CH2mCH3)

               print('\n\r')
               print('테스트 끝\n\r')
               print('\n\r')

          elif n == 3:
               print('\n\r')
               print('테스트 준비 중.....\n\r')
               print('테스트 판넬 위에 FO를 치워주세요.\n\r')
               print('\n\r')

               theCounts = 0
               theCounts = int(input("반복 측정 회수 :  "))
               print('\n\r')

               print('\n\r')
               print('\033[91m' + 'Calibration 준비\n\r' + '\033[0m')
               time.sleep(6)
               led_ready.on()

               print('\033[91m' + 'Calibration 시작' + '\033[0m')
               print('\n\r')
               led_ready.off()
               led_calibration.on()

               R_CH1, R_CH2, R_CH3, R_CH1mCH2, R_CH1mCH3, R_CH2mCH3 = theREF_ps_Check()

               # t1 = time.ticks_ms()

               Max1, Max2, Max3, Max4, Max5, Max6 = theFO_ps_Check(1, 500, 1000, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
                                                                R_CH1, R_CH2, R_CH3, R_CH1mCH2, R_CH1mCH3, R_CH2mCH3)
               # t2 = time.ticks_ms()

               # print(t2-t1)  # 약 3분40초 소요

               print('\n\r')

               R_CH1, R_CH2, R_CH3, R_CH1mCH2, R_CH1mCH3, R_CH2mCH3 = theREF_ps_Check()

               led_calibration.off()
               print('\033[91m' + 'Calibration 끝' + '\033[0m')
               print('\n\r')
               print('테스트 시작\n\r')

               CalDuty = 10000
               theFO_ps_Check(2, theCounts, CalDuty, Max1, Max2, Max3, Max4, Max5, Max6,
                           R_CH1, R_CH2, R_CH3, R_CH1mCH2, R_CH1mCH3, R_CH2mCH3)

               print('\n\r')
               print('테스트 끝\n\r')
               print('\n\r')

          elif n == 4:
               print('\n\r')
               print('테스트 준비 중.....\n\r')
               print('테스트 판넬 위에 FO를 치워주세요.\n\r')
               print('\n\r')

               theCounts = 0
               theCounts = int(input("반복 측정 회수 :  "))
               print('\n\r')

               print('\n\r')
               print('\033[91m' + 'Calibration 준비\n\r' + '\033[0m')
               time.sleep(6)
               led_ready.on()

               print('\033[91m' + 'Calibration 시작' + '\033[0m')
               print('\n\r')
               led_ready.off()
               led_calibration.on()

               R_CH1, R_CH2, R_CH3, R_CH1mCH2, R_CH1mCH3, R_CH2mCH3 = theREF_ps_Check()

               # t1 = time.ticks_ms()

               Max1, Max2, Max3, Max4, Max5, Max6 = theFO_ps_Check(1, 500, 1000, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
                                                                R_CH1, R_CH2, R_CH3, R_CH1mCH2, R_CH1mCH3, R_CH2mCH3)
               # t2 = time.ticks_ms()

               # print(t2-t1)  # 약 3분40초 소요

               print('\n\r')

               R_CH1, R_CH2, R_CH3, R_CH1mCH2, R_CH1mCH3, R_CH2mCH3 = theREF_ps_Check()

               led_calibration.off()
               print('\033[91m' + 'Calibration 끝' + '\033[0m')
               print('\n\r')
               print('테스트 시작\n\r')

               CalDuty = 10000
               theFO_ps_Check(2, theCounts, CalDuty, Max1, Max2, Max3, Max4, Max5, Max6,
                           R_CH1, R_CH2, R_CH3, R_CH1mCH2, R_CH1mCH3, R_CH2mCH3)

               print('\n\r')
               print('테스트 끝\n\r')
               print('\n\r')

          elif n == 5:
               print('\n\r')
               print('테스트 준비 중.....\n\r')
               print('테스트 판넬 위에 FO를 치워주세요.\n\r')
               print('\n\r')

               theCounts = 0
               theCounts = int(input("반복 측정 회수 :  "))
               print('\n\r')

               print('\n\r')
               print('\033[91m' + 'Calibration 준비\n\r' + '\033[0m')
               time.sleep(6)
               led_ready.on()

               print('\033[91m' + 'Calibration 시작' + '\033[0m')
               print('\n\r')
               led_ready.off()
               led_calibration.on()

               R_CH1v, R_CH2v, R_CH3v, R_CH1mCH2v, R_CH1mCH3v, R_CH2mCH3v = theREF_vs_Check()
               R_CH1p, R_CH2p, R_CH3p, R_CH1mCH2p, R_CH1mCH3p, R_CH2mCH3p = theREF_ps_Check()

               # t1 = time.ticks_ms()
               Max1, Max2, Max3, Max4, Max5, Max6 = \
                    theFO_vs_Check(1, 500, 1000, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
                                   R_CH1v, R_CH2v, R_CH3v, R_CH1mCH2v, R_CH1mCH3v, R_CH2mCH3v)
               Max7, Max8, Max9, Max10, Max11, Max12 = \
                    theFO_ps_Check(1, 500, 1000, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
                                   R_CH1p, R_CH2p, R_CH3p, R_CH1mCH2p, R_CH1mCH3p, R_CH2mCH3p)
               # t2 = time.ticks_ms()

               # print(t2-t1)  # 약 7분20초 소요

               print('\n\r')
               
               R_CH1v, R_CH2v, R_CH3v, R_CH1mCH2v, R_CH1mCH3v, R_CH2mCH3v = theREF_vs_Check()
               R_CH1p, R_CH2p, R_CH3p, R_CH1mCH2p, R_CH1mCH3p, R_CH2mCH3p = theREF_ps_Check()

               led_calibration.off()
               print('\033[91m' + 'Calibration 끝' + '\033[0m')
               print('\n\r')
               print('테스트 시작\n\r')

               CalDuty = 10000
               theFO2_Check(theCounts, CalDuty, Max1, Max2, Max3, Max4, Max5, Max6, Max7, Max8, Max9, Max10,
                            Max11, Max12, R_CH1v, R_CH2v, R_CH3v, R_CH1mCH2v, R_CH1mCH3v, R_CH2mCH3v,
                            R_CH1p, R_CH2p, R_CH3p, R_CH1mCH2p, R_CH1mCH3p, R_CH2mCH3p)

               print('\n\r')
               print('테스트 끝\n\r')
               print('\n\r')

          elif n == 6:
               print('\n\r')
               print('테스트 준비 중.....\n\r')
               print('테스트 판넬 위에 FO를 치워주세요.\n\r')
               print('\n\r')

               theCounts = 0
               theCounts = int(input("반복 측정 회수 :  "))
               print('\n\r')

               print('\n\r')
               print('\033[91m' + 'Calibration 준비\n\r' + '\033[0m')
               time.sleep(6)
               led_ready.on()

               print('\033[91m' + 'Calibration 시작' + '\033[0m')
               print('\n\r')
               led_ready.off()
               led_calibration.on()

               R_CH1v, R_CH2v, R_CH3v, R_CH1mCH2v, R_CH1mCH3v, R_CH2mCH3v = theREF_vs_Check()
               R_CH1p, R_CH2p, R_CH3p, R_CH1mCH2p, R_CH1mCH3p, R_CH2mCH3p = theREF_ps_Check()

               # t1 = time.ticks_ms()

               Max1, Max2, Max3, Max4, Max5, Max6 = \
                    theFO_vs_Check(1, 500, 1000, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
                                   R_CH1v, R_CH2v, R_CH3v, R_CH1mCH2v, R_CH1mCH3v, R_CH2mCH3v)
               Max7, Max8, Max9, Max10, Max11, Max12 = \
                    theFO_ps_Check(1, 500, 1000, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1,
                                   R_CH1p, R_CH2p, R_CH3p, R_CH1mCH2p, R_CH1mCH3p, R_CH2mCH3p)
               # t2 = time.ticks_ms()

               # print(t2-t1)  # 약 7분20초 소요

               print('\n\r')
               
               R_CH1v, R_CH2v, R_CH3v, R_CH1mCH2v, R_CH1mCH3v, R_CH2mCH3v = theREF_vs_Check()
               R_CH1p, R_CH2p, R_CH3p, R_CH1mCH2p, R_CH1mCH3p, R_CH2mCH3p = theREF_ps_Check()

               led_calibration.off()
               print('\033[91m' + 'Calibration 끝' + '\033[0m')
               print('\n\r')
               print('테스트 시작\n\r')

               CalDuty = 10000
               theFO2_Check(theCounts, CalDuty, Max1, Max2, Max3, Max4, Max5, Max6, Max7, Max8, Max9, Max10,
                            Max11, Max12, R_CH1v, R_CH2v, R_CH3v, R_CH1mCH2v, R_CH1mCH3v, R_CH2mCH3v,
                            R_CH1p, R_CH2p, R_CH3p, R_CH1mCH2p, R_CH1mCH3p, R_CH2mCH3p)

               print('\n\r')
               print('테스트 끝\n\r')
               print('\n\r')

          elif n == 7:

               print('\n\r')
               print('SNR 테스트 시작\n\r')
               print('\n\r')

               print(snr())

               print('\n\r')
               print('SNR 테스트 끝\n\r')
               print('\n\r')

          else:
               print('잘못된 메뉴를 선택했습니다.\n\r')
               print('프로그램을 종료합니다.')
               led_ready.off()
               led_calibration.off()
               led_vs_error.off()
               led_ps_error.off()
               break

          led_ready.off()
          led_calibration.off()
          led_vs_error.off()
          led_ps_error.off()

# Main 함수 실행
main()