import os
import datetime

folder = '/home/pi/Pictures/cleanliness/'
contents = os.listdir(folder)

current_date_string = datetime.datetime.now()
if current_date_string.month == 1:
  one_month_ago = current_date_string.replace(month=12).replace(year=current_date_string.year - 1)
else:
  one_month_ago = current_date_string.replace(month=current_date_string.month - 1)
one_month_ago = str(one_month_ago)

contents_to_remove = [e for e in contents if e < one_month_ago]
for f in contents_to_remove:
  print "removing", f
  os.remove(folder + f)
