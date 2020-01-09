from skimage import io
import matplotlib.pyplot as plt
import numpy as np
def conv(img,kernel): #function to perform convoultion
        kernel = np.flipud(np.fliplr(kernel))   #flipping the kernel   
        output = np.zeros_like(img)             #Creating an output matrix with same dimensions as the image
        for i in range(3): #One time for each channel
                for x in range(img.shape[1]-2):  
                        for y in range(img.shape[0]-2):
                                #Performing the convolution and storing the result in the output 
                                output[y,x,i]=(kernel*img[y:y+3,x:x+3,i]).sum()
        return output

img = io.imread('proj.jpg') #Importing the image as a 3D matrix
plt.imshow(img)             #Plotting the image matrix     
plt.title("Original Image")
plt.show()                  #Outputting the original image

output = np.zeros_like(img) #Creating the matrix that stores the convoluted image

kernel = np.array([[1,1,1],[1,1,1],[1,1,1]])/9.0 #Assigning kernel value for box blur
output = conv(img,kernel)       #Calling the function for the convolution

plt.imshow(output)
plt.title("Box Blur")
plt.show()


kernel = np.array([[1,0,-1],[0,0,0],[-1,0,1]]) #Assigning kernel value for edge detection 
output = conv(img,kernel)

plt.imshow(output)
plt.title("Edge Detection")
plt.show()


kernel = np.array([[0,0,0],[0,1,0],[0,0,0]]) #Assigning kernel value for identity
output = conv(img,kernel)

plt.imshow(output)
plt.title("Identity")
plt.show()
