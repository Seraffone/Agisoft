#Aligns cameras on High Accuracy
#The syntax is for Agisoft Photoscan, but will work in Metashape with
#nonfatal errors

import PhotoScan

doc = PhotoScan.app.document
chunk = doc.chunk
chunk.matchPhotos(accuracy=PhotoScan.HighAccuracy, generic_preselection=True,
reference_preselection=False)
chunk.alignCameras()
doc.save()
