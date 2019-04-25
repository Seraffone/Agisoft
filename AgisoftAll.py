#Aligns cameras on High Accuracy
#The syntax is for Agisoft Photoscan, but will work in Metashape with
#nonfatal errors

import PhotoScan

doc = PhotoScan.app.document
chunk = doc.chunk
#Align photos (sparse cloud)
chunk.matchPhotos(accuracy=PhotoScan.HighestAccuracy, generic_preselection=True,
reference_preselection=False)
chunk.alignCameras()
#Build dense cloud
chunk.buildDepthMaps(quality=PhotoScan.UltraQuality, filter=PhotoScan.AggressiveFiltering)
chunk.buildDenseCloud()
#Build model
chunk.buildModel(surface=PhotoScan.Arbitrary, interpolation=PhotoScan.EnabledInterpolation)
chunk.buildUV(mapping=PhotoScan.GenericMapping)
chunk.buildTexture(blending=PhotoScan.MosaicBlending, size=4096)
#Save work so far
doc.save()
