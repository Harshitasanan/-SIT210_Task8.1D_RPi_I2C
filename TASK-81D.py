import smbus # library to access I2C devices
from time import sleep # import sleep(delay) function from time library 

Address = 0x23 # variable to store the address of the I2C device. This is the default address
bus = smbus.SMBus(1) # create object of SMBus class to access I2C based Python function


try:
    while True:
        data = bus.read_i2c_block_data(Address, 0x23, 2)
        intensity = int.from_bytes(data, "big", signed=False)
        
        if intensity < 9:
            status = 'TOO DARK'
        elif intensity < 20 and intensity >= 9:
            status ='DARK'
        elif intensity < 130 and intensity >=20:
            status = 'MEDIUM'
        elif intensity < 600 and intensity >=130:
            status ='BRIGHT'
        else:
            status ='TOO BRIGHT'
        print('Light is', status, ':', intensity, 'lx') # print the light brightness with the intesity
        sleep(0.5)

            
except KeyboardInterrupt: #code stops id ctrl+c is pressed on keyboard
 GPIO.cleanup()
