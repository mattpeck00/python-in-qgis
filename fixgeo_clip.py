
import processing

infeature = 'C:/MappingProjects/infeature.shp'
outputfixed= 'C:/Documents/MappingProjects/outputfixed.shp'
clipfile= 'C:/Documents/MappingProjects/clipfile.shp'
outputclip = 'C:/Documents/MappingProjects/outputclip.shp'

processing.run("native:fixgeometries",\
{'INPUT':infeature,\
'OUTPUT': outputfixed})
print("Fix Geometries Done")

processing.run("native:clip", {'INPUT':outputfixed,\
'OVERLAY':driftlessregion,\
'OUTPUT':outputclip})
print("Clip Done")