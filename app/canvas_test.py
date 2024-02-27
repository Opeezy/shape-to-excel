import os

from shape import ShapeData
from canvas import CanvasHandler
from dotenv import load_dotenv
from controls import App

load_dotenv()

if __name__ == '__main__':
    FILE = os.getenv('shape')
    s = ShapeData(FILE)
    ch = CanvasHandler()
    ch.draw_shape()
