import PhotoScan

doc = PhotoScan.app.document
chunk = doc.chunk

#Build dense cloud
chunk.buildDepthMaps(quality=PhotoScan.HighQuality, filter=PhotoScan.ModerateFiltering)
chunk.buildDenseCloud()
#Build model
chunk.buildModel(surface=PhotoScan.Arbitrary, interpolation=PhotoScan.EnabledInterpolation)
chunk.buildUV(mapping=PhotoScan.GenericMapping)
chunk.buildTexture(blending=PhotoScan.MosaicBlending, size=8192)
#Save work so far
doc.save()
