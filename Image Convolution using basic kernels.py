from skimage import io
import matplotlib.pyplot as plt
import numpy as np
def conv(img,kernel):
        kernel = np.flipud(np.fliplr(kernel))     
        output = np.zeros_like(img)
        for i in range(3):
                for x in range(img.shape[1]-2):    
                        for y in range(img.shape[0]-2):
                                output[y,x,i]=(kernel*img[y:y+3,x:x+3,i]).sum()
        return output

img = io.imread('proj.jpg')
plt.imshow(img)
plt.title("Original Image")
plt.show()

output = np.zeros_like(img)

kernel = np.array([[1,1,1],[1,1,1],[1,1,1]])/9.0
output = conv(img,kernel)        

plt.imshow(output)
plt.title("Box Blur")
plt.show()


kernel = np.array([[1,0,-1],[0,0,0],[-1,0,1]])
output = conv(img,kernel)

plt.imshow(output)
plt.title("Edge Detection")
plt.show()


kernel = np.array([[0,0,0],[0,1,0],[0,0,0]])
output = conv(img,kernel)

plt.imshow(output)
plt.title("Identity")
plt.show()
