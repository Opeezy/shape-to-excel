import os

from cShape import ShapeData
from shapefile import Shape

if __name__ == "__main__":
    shape_dir = os.path.join(os.getcwd(), 'shapes\\Test2')
    shp = ShapeData(shape_dir)
    print(len(shp.records))
    print(len(shp.shapes))
    print(shp.shape_file)
    print(len(shp.fields))
    


    
