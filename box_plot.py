import matplotlib.pyplot as plt
from data import df

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.boxplot(df['Age'])
plt.show()
