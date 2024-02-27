import shapefile
import tkinter.filedialog as fd
import pandas as pd
import numpy as np

from pandas import DataFrame
from shapefile import Shapes, Reader


class ShapeData():
    def __init__(self, file: str) -> None:
        self.shape_file: Reader = shapefile.Reader(file)
        self.fields: list = self.shape_file.fields
        self.records: list = self.shape_file.records()
        self.shapes: Shapes = self.shape_file.shapes()
        self.data: DataFrame = self.__convert()
        self.bound_boxes = np.empty((len(self.shapes), 4))
        self.__fill_bounding_boxes()

    def __convert(self) -> DataFrame:
        field_columns = [x[0] for x in self.fields if x[0] != "DeletionFlag"]
        data = np.array(self.records)
        df = pd.DataFrame(data, columns=field_columns)
        return df
    
    def __fill_bounding_boxes(self) -> None:
        for key, shape in enumerate(self.shapes):
            box = ['%.3f' % coord for coord in shape.bbox]
            self.bound_boxes[key] = box
        
          
    
    




if __name__ == "__main__":
    pass