from matplotlib import pyplot as plt
from data import df

var = df.groupby(['Gender']).sum().stack()
temp = var.unstack()
print(type(temp))
x_list = temp['Sales']
label_list = temp.index
plt.axis("equal")
plt.pie(x_list, labels=label_list, autopct="%1.1f%%")
plt.title("Pastafarianism expenses")
plt.show()
