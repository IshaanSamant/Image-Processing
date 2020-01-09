from skimage import io, color
import matplotlib.pyplot as plt
import numpy as np
def conv(img,kernel):
        kernel = np.flipud(np.fliplr(kernel))     
        output = np.zeros_like(img)
        
        for x in range(img.shape[1]-2): #Iterate two times lesser because the matrix size is 3 
                for y in range(img.shape[0]-2):
                        #Performing the convolution and storing the result in the output 
                        output[y,x]=(kernel*img[y:y+3,x:x+3]).sum()
        return output

img = io.imread('proj.jpg')#Importing the image as a 3D matrix
img = color.rgb2gray(img) #Reducing the image to one channel

plt.imshow(img, cmap=plt.cm.gray)#Plotting the image as a grey image
plt.title("Original Image")
plt.show()                      #Outputting the grey version of the original image

output = np.zeros_like(img) #Creating the matrix that stores the convoluted image

kernel = np.array([[1,1,1],[1,1,1],[1,1,1]])/9.0 #Assigning kernel value for box blur
output = conv(img,kernel)         #Calling the function for the convolution

plt.imshow(output, cmap=plt.cm.gray )
plt.title("Box Blur")
plt.show()


kernel = np.array([[1,0,-1],[0,0,0],[-1,0,1]]) #Assigning kernel value for edge detection
output = conv(img,kernel)

plt.imshow(output, cmap=plt.cm.gray)
plt.title("Edge Detection")
plt.show()


kernel = np.array([[0,0,0],[0,1,0],[0,0,0]])  #Assigning kernel value for identity
output = conv(img,kernel)

plt.imshow(output, cmap=plt.cm.gray)  
plt.title("Identity")
plt.show()
