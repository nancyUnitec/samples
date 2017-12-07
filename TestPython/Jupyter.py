
#############pie chart######################

"""
import matplotlib.pyplot as plt
labels='frogs','hogs','dogs','logs'
sizes=15,20,45,10
colors='yellowgreen','gold','lightskyblue','lightcoral'
explode=0,0.1,0,0
plt.pie(sizes,explode=explode,labels=labels,colors=colors,autopct='%1.1f%%',shadow=True,startangle=50)
plt.axis('equal')
plt.show()
"""
##################################################

%matplotlib inline
import numpy as np
import matplotlib.pyplot as plt
from pylab import *


income = [3.2 4.1 5.0 5.6];
outgo = [2.5 4.0 3.35 4.9];

subplot(2,1,1); plot(income)
subplot(2,1,2); plot(outgo)



x = np.arange(-5.0, 5.0, 0.02)
y1 = np.sin(x)

plt.figure(1)
plt.subplot(211)
plt.plot(x, y1)

plt.subplot(212)
#设置x轴范围
xlim(-2.5, 2.5)
#设置y轴范围
ylim(-1, 1)
plt.plot(x, y1)






# coding: utf-8

# In[1]:


print("Hello World")


#import numpy as np
ls1 = range(10)
list(ls1)

print("why why")
#print(list)

# In[2]:





# In[3]:





# In[4]:



