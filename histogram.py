from data import df
from matplotlib import pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.hist(df['Age'], bins=7)
plt.title('Age distribution')
plt.xlabel('Age')
plt.ylabel('#Employee')
plt.show()
