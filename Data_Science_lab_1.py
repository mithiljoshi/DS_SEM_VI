#!/usr/bin/env python
# coding: utf-8

# In[67]:


import numpy as np
import matplotlib.pyplot as plt



import cv2
img = cv2.imread("pyramid.jpg")
canny_img = cv2.Canny(img, 255, 0)
plt.imshow(canny_img)
plt.show()

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
    plt.scatter(X,Y, color='red')
    plt.show()

    return A_u

def back_to_normal(new_basis_data):
    a_k = np.dot(np.linalg.inv(create_complex_matrix(len(new_basis_data))), new_basis_data)

    return a_k
    
changed_data = projection_on_complex(canny_img)
normal_data = back_to_normal(changed_data)

plt.imshow(normal_data.real)
plt.show()



# In[ ]:




