#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install opencv-python')

 

 

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
import cv2


# In[2]:



def LiveCamEdgeDetection_canny(image_color):
            
    threshold_1 = 100
    threshold_2 = 40
    image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(image_gray, threshold_1, threshold_2)
    
    return canny

 

 

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read() # Cap.read() returns a ret bool to indicate success.
    # cv2.imshow('Live Edge Detection', Cartoon(frame))
    
    cv2.imshow('Live Edge Detection', LiveCamEdgeDetection_canny(frame))
    cv2.imshow('Webcam Video', frame)
    if cv2.waitKey(1) == 13: #13 Enter Key
        break
        
cap.release() # camera release 
cv2.destroyAllWindows()  


# In[ ]:




