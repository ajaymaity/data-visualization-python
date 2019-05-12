from matplotlib import pyplot as plt
from data import df
import numpy as np

data = np.random.rand(4, 2)
rows = list('1234')
columns = list('MF')
fig, ax = plt.subplots()
ax.pcolor(data, cmap=plt.cm.Reds, edgecolors='k')
ax.set_xticks(np.arange(0, 2)+0.5)
ax.set_yticks(np.arange(0, 4)+0.5)
ax.xaxis.tick_bottom()
ax.yaxis.tick_left()
ax.set_xticklabels(columns, minor=False, fontsize=20)
ax.set_yticklabels(rows, minor=False, fontsize=20)
plt.show()
