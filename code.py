
import cv2
import numpy as np

def main():

   img = np.zeros((512, 512, 3), np.uint8) 
   cv2.line(img, (100, 100), (100, 200), (255, 0, 0), 2)
   cv2.line(img, (100, 200), (200, 200), (0, 255, 0), 2)
   cv2.line(img, (100, 200), (40, 250), (0, 0, 255), 2)
  
  
   
   cv2.imshow('Adobe', img)
  
   cv2.waitKey(0)
   cv2.destroyAllWindows()
    
if(__name__=="__main__"):
    main()    
