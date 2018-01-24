import datetime
import time
import picamera
import delete_old_pictures

def during_school_day(t):
  return (t.month <= 5 or t.month >= 9) and t.hour >= 8 and t.hour <= 14 and t.weekday() <= 4

def interval_test(t1,t0):
  return t1.minute != t0.minute and t1.minute % 10 == 1

print 'Starting Cleanliness Camera!'
camera = picamera.PiCamera()
camera.vflip = True
camera.hflip = True
now = datetime.datetime.now()
while True:
  before = now
  now = datetime.datetime.now()
  if during_school_day(now) and interval_test(now,before):
    camera.capture('/home/pi/Pictures/cleanliness/' + str(now).replace(' ','-').replace(':','-').split('.')[0] + '_cleanliness.jpg')
    print 'Captured photo at ' + str(now)
  
# testing
if True:
  i = 1
  print i, during_school_day(datetime.datetime(2018, 1, 24, 9, 51, 0)) == True; i += 1
  print i, during_school_day(datetime.datetime(2018, 7, 24, 9, 51, 0)) == False; i += 1
  print i, during_school_day(datetime.datetime(2018, 12, 24, 9, 51, 0)) == True; i += 1
  print i, during_school_day(datetime.datetime(2018, 1, 24, 19, 51, 0)) == False; i += 1
  print i, during_school_day(datetime.datetime(2018, 1, 24, 1, 51, 0)) == False; i += 1
  print i, during_school_day(datetime.datetime(2018, 1, 27, 9, 51, 0)) == False; i += 1

  print i, interval_test(datetime.datetime(2018, 1, 27, 9, 50, 0),datetime.datetime(2018, 1, 27, 9, 49, 59)) == True; i += 1
  print i, interval_test(datetime.datetime(2018, 1, 27, 9, 50, 10),datetime.datetime(2018, 1, 27, 9, 50, 9)) == False; i += 1
  print i, interval_test(datetime.datetime(2018, 1, 27, 9, 52, 0),datetime.datetime(2018, 1, 27, 9, 51, 59)) == False; i += 1
