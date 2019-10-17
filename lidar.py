import Pylidar as lidar
import time

#to find port in linux type "ls /dev/tty*"

port = "/dev/ttyUSB0" 

x2 = lidar.YdLidarX4(port)
x = 0

#print x2.Connect()
#print x2.GetHealthStatus()

if(x2.Connect()):
  print(x2.GetDeviceInfo())
  gen = x2.StartScanning()
  t = time.time()
  while (time.time() - t) < 30:
    #for x in 360:
     # if(gen.distdict[x] == [])
      #  pass
      #else:
       # print(gen.distdict[x])
    print (gen.next())
    time.sleep(.5)
    print ("\n")
  x2.StopScanning()
  x2.Disconnect()
else:
  print("No Connection found")

