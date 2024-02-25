import geopandas as gp
import matplotlib.pyplot as plt


df = gp.read_file("C:\\Users\\copen\\Documents\\github\\repos\\shape-to-excel\\shapes")  
df.plot()
plt.show()

