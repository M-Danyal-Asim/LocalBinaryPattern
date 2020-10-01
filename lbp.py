import numpy as np  #importing libraries
import cv2 as cv
import matplotlib.pyplot as plt
import matplotlib.pylab as pl
image_read = cv.imread('huamn.png', 1)   #reading image
image_gray = cv.cvtColor(image_read, cv.COLOR_BGR2GRAY)
row, col= image_gray.shape
image = np.pad(image_gray, pad_width=[(1, 1), (1, 1)], mode='constant', constant_values=0)  #padding image
output_image = np.zeros((row, col), np.uint8)
histogram = [0]*256
def threshold(image,centre,i,j):     #function to calculate binary pattern
        binary =[]
        if (image[i - 1][j - 1]) <centre:
             binary.append(0)
        else:
             binary.append(1)

        if (image[i - 1][j]) <centre:
             binary.append(0)
        else:
             binary.append(1)

        if (image[i - 1][j+1]) <centre:
             binary.append(0)
        else:
             binary.append(1)

        if (image[i][j + 1]) < centre:
            binary.append(0)
        else:
            binary.append(1)

        if (image[i + 1][j + 1]) < centre:
            binary.append(0)
        else:
            binary.append(1)

        if (image[i + 1][j]) < centre:
            binary.append(0)
        else:
            binary.append(1)

        if (image[i + 1][j - 1]) < centre:
            binary.append(0)
        else:
            binary.append(1)

        if (image[i ][j - 1]) < centre:
            binary.append(0)
        else:
            binary.append(1)

        return binary

def calculate_value (binary_array):                   #function to calculate value of centre pixel on basis of LSB pattern
    final_value =0
    weights = [1, 2, 4, 8, 16, 32, 64, 128]
    value = [weights[k]*binary[k] for k in range(len(weights))]
    for m in range (len(value)):
        final_value = final_value +value[m]

    return final_value



for i in range(row):
    for j in range(col):
        centre = image[i][j]
        binary = threshold(image, centre, i, j)
        final_output = calculate_value(binary)
        output_image[i][j] = final_output

cv.imshow('Local Binary Patterned Image',output_image)
cv.waitKey(0)
