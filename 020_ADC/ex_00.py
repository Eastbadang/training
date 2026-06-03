# error, pyboard ?
import streams
import dac # for digital to analog -> write
import adc # for analog to digital -> read
import math # mathematical function

# create a serial port stream with default parameters
streams.serial()

# create list of angles and calculate the cosine
angles = range(0,360,10)
val = []
for ang in angles:
    val.append(int(math.cos(math.radians(ang))*100)+100)

def read_and_print():
   #  add physical link pin D25 with pin A4 and read value
    while True:
        value = adc.read(A4)
        conv = (value-1500)*80//4095

        if conv>=0:
            print(" "*40,"#"*conv)
        else:
            print(" "*(40+conv),"#"*(-conv))
        sleep(10)

# read input in a separate thread
thread(read_and_print)

# write cos on pin D25
my_dac = dac.DAC(D25.DAC)
my_dac.start()
# circular mode: continuously repeat the input buffer
my_dac.write(val,50,MILLIS,circular=True) 