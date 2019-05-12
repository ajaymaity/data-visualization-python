import seaborn as sns
from matplotlib import pyplot as plt
from data import df

sns.violinplot(df['Gender'], df['Age'])
sns.despine()
plt.show()
