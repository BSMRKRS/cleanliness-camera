import os

folder = '/home/pi/Pictures/cleanliness/'
contents = os.listdir(folder)

f = open('/home/pi/cleanliness/action/observe.html', 'w')
for c in list(reversed(sorted(contents))):
  f.write("<p>"+c+"</p>\n")
f.write("<script src='action/load_images.js'></script>")
f.close
