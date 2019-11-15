import serial 
import time   
 
arduino = serial.Serial('com11',9600) 
time.sleep(2) 


print ("Fan ON or OFF")
n=input();

 
while 1:      

    var = n 
    b = bytes(var, 'utf-8')
   
    
    if (var == '1'): 
        arduino.write(b) 
        print ("Fan ON")
        time.sleep(1)
    
    if (var == '0'): 
        arduino.write(b) 
        print ("Fan OFF")
        time.sleep(1)
