from shape import ShapeData
from tkinter import Canvas
from gui import Gui

class CanvasHandler:
    def __init__(self, canvas: Canvas) -> None:
        self.canvas = canvas
        self.width = self.canvas.winfo_width()
        self.height = self.canvas.winfo_height()
        self.bmin = (0, 0)
        self.bmax = (self.width, self.height)
        self.canvas_bbox = (self.bmin, self.bmax)

    def draw_shape(self, shape: ShapeData):
        shape_total_bbox = ((shape.total_bbox[0], shape.total_bbox[1]), (shape.total_bbox[2], shape.total_bbox[3]))
        ratio = self.calculate_ratio(self.canvas_bbox, shape_total_bbox)
        for box in shape.bound_boxes:
            new_box = []
            new_min = self.transform(ratio, self.canvas_bbox, shape_total_bbox, box[0], box[1])
            new_max = self.transform(ratio, self.canvas_bbox, shape_total_bbox, box[2], box[3])
            new_box.append(new_min)
            new_box.append(new_max)
            self.canvas.create_rectangle(new_min[0], new_min[1], new_max[0], new_max[1])

    def calculate_ratio(self, bbox1: tuple, bbox2: tuple):
        width = lambda box: box[1][0] - box[0][0]
        length = lambda box: box[1][1] - box[0][1]
        ratio = (width(bbox1)/width(bbox2), length(bbox1)/length(bbox2))
        return ratio

    def transform(self, ratio, bbox1, bbox2, x, y):
        transform_axis = lambda axis, units: bbox1[0][axis]+(units - bbox2[0][axis])*ratio[axis]
        transform = lambda x, y: (transform_axis(0, x), transform_axis(1, y))
        return transform(x, y)
        # transform_axis = lambda axis, units: bigBox[0][axis]+(units - smallBox[0][axis])*ratio[axis]
        # transform = lambda x, y: (transform_axis(0, x), transform_axis(1, y))

