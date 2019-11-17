# Script to write select exif info from within PhotoScan
# Run from Tools->Run Script
# Christine Kranenburg
# 2018-03-22

import PhotoScan
doc = PhotoScan.app.document
chunk = doc.chunk
path = PhotoScan.app.getSaveFileName()
file = open(path, "w")

for i in range(0, len(chunk.cameras)):
	camera = chunk.cameras[i]
	dt = camera.photo.meta["Exif/DateTime"]
	ss = "1/" + str(int(1/float(camera.photo.meta["Exif/ExposureTime"])))
	iso = camera.photo.meta["Exif/ISOSpeedRatings"]
	bits = [camera.label, dt, iso, ss]
	print("Bits:",bits)
#	strout = ",".join(bits)
	print(camera.label,',',dt,',',iso,',',ss)
	my_str = camera.label+','+dt+','+iso+','+ss+"\n"
#	file.write(strout + "\n")
	file.write(my_str)
	print(camera.label, dt, iso, ss)
	
file.close()
print("all done");
