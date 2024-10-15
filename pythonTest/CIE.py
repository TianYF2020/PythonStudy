import colour
import matplotlib.pyplot as plt

[x,y]=[0.3,0.6]
colour.plotting.plot_chromaticity_diagram_CIE1931(standalone=False)
plt.plot(x,y,'o',markersize=8,color=(0,0.5,0))  # 绘图
plt.axis([-0.1, 1, -0.1, 1])    #改变坐标轴范围
plt.show()