from matplotlib import pyplot as plt
from data import df

var = df.groupby(['BMI', 'Gender']).Sales.sum()
var.unstack().plot(kind='bar',
                   color=['red', 'blue'],
                   grid=False)
plt.show()
