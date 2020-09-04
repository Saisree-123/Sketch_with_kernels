#!/usr/bin/env python
# coding: utf-8

# In[1]:


#import few libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


# In[2]:


def sketching_image(path,image_name):
    image_path=os.path.join(path+image_name)
    split_name=os.path.splitext(image_name)[0] #removing extension .jpg
    image=cv2.imread(image_path)    
    kernel=np.array([[5,5,5], 
                [5, -40,5],
                [5,5,5]])   
    #neighbors - same colour -> pixel in mind obtains a value of 0(dark) , else pixel in mind gets a high value 
    sketched_image = cv2.filter2D(image,-1,kernel) 
    #Plotting images
    plt.subplot(121),plt.imshow(image),plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122),plt.imshow(sketched_image),plt.title('Sketched')
    plt.xticks([]), plt.yticks([])
    plt.show()
    cv2.imwrite(split_name+"_sketch.jpg",sketched_image) 
    #return sketched_image,image


# In[3]:


sketching_image('./','lighthouse.jpg')


# In[ ]:




