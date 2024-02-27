import os

from shape import ShapeData
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    FILE = os.getenv('shape')
    s = ShapeData(FILE)
    print(s.total_bbox)