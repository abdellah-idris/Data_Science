import numpy as np
data = np.array([150000, 125000, 320000, 540000, 200000, 120000, 160000, 230000, 280000, 290000, 300000, 500000, 420000, 100000, 150000, 280000])
initialLength = len(data)
var = np.std(data)
mean = np.mean(data)
datafiltred = data[ (data >= mean-var) & (data <= mean+var) ]
lenth = len(datafiltred)
per= (lenth/initialLength)*100
print((per))
