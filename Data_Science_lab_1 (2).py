#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import math
plt.rcParams["figure.figsize"] = (14,7)


# In[ ]:


# angle = np.arange( 0 , 2 * np.pi , 0.01 ) 
# radius = 5
# x = np.multiply(radius , np.cos( angle ))
# y = np.multiply(radius , np.sin( angle ))
# figure, axes = plt.subplots( 1) 
# axes.plot( x, y ) 
# axes.set_aspect( 1 ) 
# plt.title( 'Parametric Equation Circle' ) 
# plt.show() 


# In[13]:


X1 = np.arange(0,3, 0.1)
Y1  = np.arange(0,2, 0.1)
X2 = np.arange(3, 0, -0.1)
Y2 = np.arange(2,-0.1, -0.1)
x = []
y = []
for ele in X1:
    x.append(ele)
    y.append(0)
for ele in Y1:
    x.append(3)
    y.append(ele)
for ele in X2:
    x.append(ele)
    y.append(2)
for ele in Y2:
    x.append(0)
    y.append(ele)
x = [i for i in range(0,101)]
y = [1 for i in range(0,101)]
figure, axes = plt.subplots( 1) 
axes.plot( x, y ) 
axes.set_aspect( 1 ) 
plt.title( 'A rectangle' ) 
plt.show() 

data =[]
for i in range(0,len(x)):
    data.append(x[i]+ complex(0,1)*y[i])
print(len(data))

def translate(our_data, translate_x, translate_y):
    new_data=[]
    for element in our_data:
        new_data.append([element+ translate_x+ complex(0,1)*translate_y])
    return new_data 

def rotate(our_data, theta):
    new_data= np.multiply(our_data, np.exp(complex(0,1)*theta))
    return new_data    


def scaling(our_data, scale_factor):
    new_data=np.multiply(our_data, scale_factor)
    return new_data    

data_translate = translate(data, 50,100)

data_rotate  = rotate(data, math.pi/2)

data_scale = scaling(data, 2)


# In[4]:



def create_complex_matrix( length ):
    arr2D = []
    c =complex(0,1)
    for i in range(0,length):
        arr2D.append([])
        for j in range(0,length):
            arr2D[i].append(np.round(np.exp(c*2*3.14*i*j/length)))
    return arr2D

def projection_on_complex(our_data):
    A_u = np.dot(create_complex_matrix(len(our_data)), our_data)
    X = [x.real for x in A_u]
    Y = [x.imag for x in A_u]
    plt.plot(X, Y)
    plt.title("complex")
    return A_u

def back_to_normal(new_basis_data, percent):
    sigma = int(percent*(len(new_basis_data))/100)
    a_k = np.dot(np.linalg.inv(create_complex_matrix(len(new_basis_data[:sigma]))), new_basis_data[:sigma])
    return a_k


# In[14]:


def overall(data):
    error = []
    for i in [100,90,80,70,60,50,40,30,20,10]:
        changed_data = projection_on_complex(data)
        normal_data = back_to_normal(changed_data, i)
        error.append(np.sum(np.absolute(normal_data - data[:len(normal_data)])))
    plt.figure()    
    plt.plot(range(1, len(error)+1), error)
    
overall(data)


# In[15]:


rev_data = np.flipud(data)
overall(rev_data)


# In[16]:


beginning_changed_data = np.concatenate((data[20:], data[:20]))
overall(beginning_changed_data)


# In[17]:


overall(data_translate)


# In[18]:


overall(data_rotate)


# In[26]:


overall(data_scale)


# In[8]:


arr1 = [1,2,3,4,5, 6]
arr2 = [4,5,6,1,2,3]
print(projection_on_complex(arr1) - projection_on_complex(arr2))


# In[ ]:




