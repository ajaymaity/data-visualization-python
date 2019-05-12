from matplotlib import pyplot as plt
from data import df

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.scatter(df['Age'], df['Sales'])
plt.show()
