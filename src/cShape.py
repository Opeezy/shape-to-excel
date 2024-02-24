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

    def __convert(self) -> pd.DataFrame:
        field_columns = [x[0] for x in self.fields if x[0] != "DeletionFlag"]
        data = np.array(self.records)
        df = pd.DataFrame(data, columns=field_columns)
        
    def clear(self):
        self.data = DataFrame

    




if __name__ == "__main__":
    pass