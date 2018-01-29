import os

folder = '/home/pi/Pictures/cleanliness/'
contents = os.listdir(folder)

f = open('/home/pi/cleanliness/action/observe.html', 'w')
f.write("<link rel='stylesheet' type='text/css' href='format_page.css'>")
f.write("<div class='image-container'>")
f.write("<div id='current-image-title'></div>")
f.write("<div id='current-image'></div>")
f.write("</div>")
f.write("<div class='list-container'>")
i = 0
for c in list(reversed(sorted(contents))):
  i += 1
  f.write("<p style='cursor:pointer;color:#f30;' class='btn' id='id"+str(i)+"' onclick='show_image(event);'>"+c+"</p>\n")
f.write("</div>")
f.write("<script src='load_images.js'></script>")
f.write("<script src='format_page.css'></script>")
f.close
